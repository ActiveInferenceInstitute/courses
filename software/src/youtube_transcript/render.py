"""Course scaffolding and rendering orchestration for YouTube playlists.

Transforms YouTube channel playlists into course directory structures
with transcript-based module.md files, then renders them through the
existing batch processing pipeline.
"""

import json
import logging
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from .config import TRANSCRIPTS_SUBDIR

logger = logging.getLogger(__name__)


def slugify(title: str, max_length: int = 60) -> str:
    """Convert a title to a filesystem-safe slug.

    Lowercases, replaces non-alphanumeric characters with hyphens,
    collapses multiple hyphens, strips leading/trailing hyphens,
    and truncates to max_length (on a word boundary when possible).

    Args:
        title: Input title string
        max_length: Maximum slug length (default 60)

    Returns:
        Filesystem-safe slug string
    """
    slug = title.lower()
    # Replace non-alphanumeric (keeping hyphens) with hyphens
    slug = re.sub(r"[^a-z0-9-]", "-", slug)
    # Collapse multiple hyphens
    slug = re.sub(r"-{2,}", "-", slug)
    # Strip leading/trailing hyphens
    slug = slug.strip("-")

    if len(slug) > max_length:
        # Truncate on word boundary
        truncated = slug[:max_length]
        last_hyphen = truncated.rfind("-")
        if last_hyphen > max_length // 2:
            truncated = truncated[:last_hyphen]
        slug = truncated.rstrip("-")

    return slug


def load_youtube_manifest(path: Path) -> Dict[str, Any]:
    """Load youtube_courses.json manifest from disk.

    Args:
        path: Path to manifest file

    Returns:
        Manifest dict, or empty structure if file doesn't exist
    """
    if path.exists():
        data: Dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
        return data
    return {
        "channel_url": "",
        "last_updated": "",
        "total_playlists": 0,
        "playlists": {},
    }


def save_youtube_manifest(manifest: Dict[str, Any], path: Path) -> None:
    """Save youtube_courses.json manifest to disk with atomic write.

    Args:
        manifest: Manifest dict
        path: Path to manifest file
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    fd, tmp_path = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(tmp_path, path)
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise


def format_duration(seconds: Optional[float]) -> str:
    """Format duration in seconds to H:MM:SS or M:SS string.

    Args:
        seconds: Duration in seconds, or None

    Returns:
        Formatted duration string, or "Unknown" if None
    """
    if seconds is None:
        return "Unknown"
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def format_upload_date(upload_date: Optional[str]) -> str:
    """Format yt-dlp upload_date (YYYYMMDD) to YYYY-MM-DD.

    Args:
        upload_date: Date string in YYYYMMDD format, or None

    Returns:
        Formatted date string, or "Unknown" if None/invalid
    """
    if not upload_date or len(upload_date) != 8:
        return "Unknown"
    try:
        return f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
    except (IndexError, ValueError):
        return "Unknown"


def render_module_md_template(
    video_title: str,
    video_id: str,
    transcript_text: str,
    duration: Optional[int] = None,
    upload_date: Optional[str] = None,
    playlist_title: str = "",
    transcript_method: str = "auto_caption",
) -> str:
    """Generate module.md content from a video transcript.

    Args:
        video_title: Title of the YouTube video
        video_id: YouTube video ID
        transcript_text: Plain text transcript content
        duration: Video duration in seconds
        upload_date: Upload date in YYYYMMDD format
        playlist_title: Title of the containing playlist
        transcript_method: How the transcript was obtained

    Returns:
        Formatted module.md content string
    """
    duration_str = format_duration(duration)
    date_str = format_upload_date(upload_date)

    lines = [
        f"# {video_title}",
        "",
        f"> **Source**: [YouTube](https://www.youtube.com/watch?v={video_id})",
    ]
    if playlist_title:
        lines.append(f"> **Playlist**: {playlist_title}")
    lines.extend(
        [
            f"> **Duration**: {duration_str} | **Uploaded**: {date_str}",
            f"> **Transcript method**: {transcript_method}",
            "",
            "---",
            "",
            transcript_text,
            "",
        ]
    )
    return "\n".join(lines)


def enumerate_and_map_playlists(
    channel_url: str,
    transcript_dir: Path,
) -> Dict[str, Any]:
    """Enumerate all playlists and videos, build course manifest.

    Cross-references with the full channel video list to identify
    uncategorized videos (not in any playlist).

    Args:
        channel_url: YouTube channel URL
        transcript_dir: Directory containing transcripts (for manifest reference)

    Returns:
        Manifest dict with playlists and uncategorized videos
    """
    from .utils import (
        enumerate_channel_playlists,
        enumerate_channel_videos,
        enumerate_playlist_videos,
    )

    logger.info(f"Enumerating playlists from {channel_url}...")
    playlists = enumerate_channel_playlists(channel_url)
    logger.info(f"Found {len(playlists)} playlists")

    manifest: Dict[str, Any] = {
        "channel_url": channel_url,
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_playlists": len(playlists),
        "playlists": {},
    }

    # Track all video IDs that appear in playlists
    playlist_video_ids: set[str] = set()

    for playlist in playlists:
        playlist_id = playlist["id"]
        playlist_url = playlist["url"]
        playlist_slug = slugify(playlist["title"])

        logger.info(f"  Enumerating playlist: {playlist['title']} ({playlist_id})")
        videos = enumerate_playlist_videos(playlist_url)

        for v in videos:
            playlist_video_ids.add(v["id"])

        manifest["playlists"][playlist_slug] = {
            "id": playlist_id,
            "title": playlist["title"],
            "url": playlist_url,
            "slug": playlist_slug,
            "video_count": len(videos),
            "videos": videos,
        }

    # Find uncategorized videos
    logger.info("Enumerating all channel videos for uncategorized detection...")
    all_videos = enumerate_channel_videos(channel_url)
    uncategorized = [v for v in all_videos if v["id"] not in playlist_video_ids]

    if uncategorized:
        logger.info(f"Found {len(uncategorized)} uncategorized videos")
        # Add playlist_index to uncategorized videos
        for i, v in enumerate(uncategorized):
            v["playlist_index"] = i
        manifest["playlists"]["uncategorized"] = {
            "id": "uncategorized",
            "title": "Uncategorized",
            "url": "",
            "slug": "uncategorized",
            "video_count": len(uncategorized),
            "videos": uncategorized,
        }

    manifest["total_playlists"] = len(manifest["playlists"])
    return manifest


def scaffold_course_directory(
    course_slug: str,
    videos: List[Dict[str, Any]],
    transcript_dir: Path,
    youtube_courses_dir: Path,
    course_metadata: Dict[str, Any],
    skip_whisper: bool = False,
) -> Dict[str, Any]:
    """Create course directory structure with module.md files.

    For each video, creates a numbered module directory containing module.md
    with the transcript text. Reads existing transcripts from
    transcript_dir/transcripts/{video_id}.txt; calls transcribe_video()
    on-demand for missing ones.

    Args:
        course_slug: Filesystem-safe course name
        videos: List of video metadata dicts (id, title, duration, etc.)
        transcript_dir: Base transcript directory (contains transcripts/ subdir)
        youtube_courses_dir: Base directory for YouTube courses
        course_metadata: Dict with playlist title, url, id
        skip_whisper: Skip Whisper fallback for missing transcripts

    Returns:
        Dict with scaffolding results: created, skipped, failed counts
    """
    course_dir = youtube_courses_dir / course_slug
    course_dir.mkdir(parents=True, exist_ok=True)

    # Write course.json metadata
    course_json = course_dir / "course.json"
    course_meta = {
        "title": course_metadata.get("title", ""),
        "playlist_url": course_metadata.get("url", ""),
        "playlist_id": course_metadata.get("id", ""),
        "slug": course_slug,
        "video_count": len(videos),
        "last_updated": datetime.now(timezone.utc).isoformat(),
    }
    course_json.write_text(
        json.dumps(course_meta, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    transcripts_path = transcript_dir / TRANSCRIPTS_SUBDIR

    created = 0
    skipped = 0
    failed = 0
    modules: List[Dict[str, str]] = []

    for video in videos:
        video_id = video["id"]
        video_title = video.get("title", video_id)
        idx = video.get("playlist_index", 0)
        video_slug = slugify(video_title)
        module_name = f"{idx + 1:02d}_{video_slug}"
        module_dir = course_dir / module_name
        module_md_path = module_dir / "module.md"

        # Skip if module.md already exists
        if module_md_path.exists():
            skipped += 1
            modules.append({"name": module_name, "status": "skipped"})
            continue

        # Find or fetch transcript
        transcript_file = transcripts_path / f"{video_id}.txt"
        transcript_text = ""
        transcript_method = "auto_caption"

        if transcript_file.exists():
            transcript_text = transcript_file.read_text(encoding="utf-8").strip()
        else:
            # Fetch transcript on demand
            logger.info(f"  Fetching transcript for {video_id}: {video_title}")
            try:
                from .main import transcribe_video

                result = transcribe_video(
                    video_id, transcript_dir, skip_whisper=skip_whisper
                )
                if result["status"] == "completed":
                    rel_path = result.get("transcript_path", "")
                    if rel_path:
                        full_path = transcript_dir / rel_path
                        if full_path.exists():
                            transcript_text = full_path.read_text(encoding="utf-8").strip()
                    transcript_method = result.get("method", "auto_caption")
                else:
                    logger.warning(
                        f"  Transcript failed for {video_id}: {result.get('error', 'unknown')}"
                    )
            except Exception as e:
                logger.warning(f"  Transcript fetch error for {video_id}: {e}")

        if not transcript_text:
            failed += 1
            modules.append({"name": module_name, "status": "no_transcript"})
            continue

        # Create module directory and write module.md
        module_dir.mkdir(parents=True, exist_ok=True)
        content = render_module_md_template(
            video_title=video_title,
            video_id=video_id,
            transcript_text=transcript_text,
            duration=video.get("duration"),
            upload_date=video.get("upload_date"),
            playlist_title=course_metadata.get("title", ""),
            transcript_method=transcript_method,
        )
        module_md_path.write_text(content, encoding="utf-8")
        created += 1
        modules.append({"name": module_name, "status": "created"})
        logger.info(f"  Created {module_name}/module.md ({len(transcript_text)} chars)")

    return {"created": created, "skipped": skipped, "failed": failed, "modules": modules}


def render_course_modules(
    course_dir: Path,
    formats: Optional[List[str]] = None,
    resume: bool = True,
) -> Dict[str, Any]:
    """Render all module.md files in a course through process_module_by_type.

    Args:
        course_dir: Path to course directory containing numbered module subdirs
        formats: List of output formats (default: all)
        resume: If True, skip modules that already have output files

    Returns:
        Dict with rendering results per module
    """
    from ..batch_processing.main import process_module_by_type

    rendered = 0
    skipped_count = 0
    errors: List[str] = []
    module_results_list: List[Dict[str, Any]] = []

    # Find module directories (numbered dirs containing module.md)
    module_dirs = sorted(
        [
            d
            for d in course_dir.iterdir()
            if d.is_dir() and (d / "module.md").exists()
        ]
    )

    if not module_dirs:
        logger.warning(f"No module directories found in {course_dir}")
        return {
            "rendered": rendered,
            "skipped": skipped_count,
            "errors": errors,
            "modules": module_results_list,
        }

    logger.info(f"Rendering {len(module_dirs)} modules in {course_dir.name}")

    for module_dir in module_dirs:
        output_dir = module_dir / "output"

        # Check if already rendered when resuming
        if resume and output_dir.exists():
            lecture_dir = output_dir / "lecture-content"
            if lecture_dir.exists() and any(lecture_dir.iterdir()):
                skipped_count += 1
                module_results_list.append(
                    {"name": module_dir.name, "status": "skipped"}
                )
                continue

        try:
            logger.info(f"  Rendering {module_dir.name}...")
            module_result = process_module_by_type(
                str(module_dir), str(output_dir), formats=formats
            )
            rendered += 1
            module_results_list.append(
                {
                    "name": module_dir.name,
                    "status": "rendered",
                    "summary": module_result.get("summary", {}),
                }
            )
            if module_result.get("errors"):
                errors.extend(module_result["errors"])
        except Exception as e:
            error_msg = f"Render failed for {module_dir.name}: {e}"
            logger.error(error_msg)
            errors.append(error_msg)
            module_results_list.append(
                {"name": module_dir.name, "status": "error", "error": str(e)}
            )

    return {
        "rendered": rendered,
        "skipped": skipped_count,
        "errors": errors,
        "modules": module_results_list,
    }


def render_all_youtube_courses(
    youtube_courses_dir: Path,
    formats: Optional[List[str]] = None,
    course_filter: Optional[str] = None,
    resume: bool = True,
) -> Dict[str, Any]:
    """Render all YouTube courses through the batch processing pipeline.

    Args:
        youtube_courses_dir: Base directory containing course subdirs
        formats: List of output formats (default: all)
        course_filter: If set, only render this course slug
        resume: If True, skip already-rendered modules

    Returns:
        Dict with rendering results per course
    """
    courses: Dict[str, Dict[str, Any]] = {}
    total_rendered = 0
    total_errors: List[str] = []

    if not youtube_courses_dir.exists():
        logger.warning(f"YouTube courses directory not found: {youtube_courses_dir}")
        return {"courses": courses, "total_rendered": total_rendered, "total_errors": total_errors}

    # Find course directories
    course_dirs = sorted(
        [
            d
            for d in youtube_courses_dir.iterdir()
            if d.is_dir() and d.name != "__pycache__"
        ]
    )

    if course_filter:
        course_dirs = [d for d in course_dirs if d.name == course_filter]
        if not course_dirs:
            logger.warning(f"Course not found: {course_filter}")
            return {
                "courses": courses,
                "total_rendered": total_rendered,
                "total_errors": total_errors,
            }

    for course_dir in course_dirs:
        # Skip if no module dirs
        has_modules = any(
            (d / "module.md").exists()
            for d in course_dir.iterdir()
            if d.is_dir()
        )
        if not has_modules:
            continue

        logger.info(f"Rendering course: {course_dir.name}")
        course_results = render_course_modules(course_dir, formats, resume)
        courses[course_dir.name] = course_results
        total_rendered += course_results["rendered"]
        total_errors.extend(course_results["errors"])

    return {"courses": courses, "total_rendered": total_rendered, "total_errors": total_errors}
