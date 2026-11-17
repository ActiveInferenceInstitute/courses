"""Course scaffolding and rendering orchestration for YouTube playlists.

Transforms YouTube channel playlists into course directory structures
with transcript-based module.md files, then renders them through the
existing batch processing pipeline.
"""

import hashlib
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
    force: bool = False,
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
        force: Overwrite existing module.md files instead of skipping

    Returns:
        Dict with scaffolding results: created, skipped, failed counts
    """
    from ..batch_processing.utils import require_contained

    if not course_slug or Path(course_slug).name != course_slug or course_slug in (".", ".."):
        raise ValueError(f"Invalid course slug: {course_slug}")
    if not videos:
        return {"created": 0, "skipped": 0, "failed": 1, "modules": [],
                "errors": [f"No videos selected for {course_slug}"]}
    names = set()
    for video in videos:
        identity = video.get("id")
        index = video.get("playlist_index", 0)
        if not isinstance(identity, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", identity):
            raise ValueError(f"Invalid video identity: {identity}")
        if type(index) is not int or index < 0:
            raise ValueError(f"Invalid playlist index for {identity}: {index}")
        name = f"{index + 1:02d}_{slugify(video.get('title', identity))}"
        if name in names:
            raise ValueError(f"Duplicate module identity: {course_slug}/{name}")
        names.add(name)
        require_contained(youtube_courses_dir / course_slug / name / "module.md", youtube_courses_dir)
        require_contained(transcript_dir / TRANSCRIPTS_SUBDIR / f"{identity}.txt", transcript_dir)
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
    errors: List[str] = []

    for video in videos:
        video_id = video["id"]
        video_title = video.get("title", video_id)
        idx = video.get("playlist_index", 0)
        video_slug = slugify(video_title)
        module_name = f"{idx + 1:02d}_{video_slug}"
        module_dir = course_dir / module_name
        module_md_path = module_dir / "module.md"

        # Skip if module.md already exists (unless force=True)
        if module_md_path.exists() and not force:
            skipped += 1
            modules.append({"name": module_name, "status": "skipped"})
            continue
        elif module_md_path.exists() and force:
            logger.info(f"  Force-overwriting {module_name}/module.md")

        # Find or fetch transcript
        transcript_file = transcripts_path / f"{video_id}.txt"
        transcript_text = ""
        failure = "empty transcript"
        transcript_method = "auto_caption"

        if transcript_file.exists():
            transcript_text = transcript_file.read_text(encoding="utf-8").strip()
        else:
            # Fetch transcript on demand
            logger.info(f"  Fetching transcript for {video_id}: {video_title}")
            try:
                from .main import transcribe_video

                result = transcribe_video(video_id, transcript_dir, skip_whisper=skip_whisper)
                if result["status"] == "completed":
                    rel_path = result.get("transcript_path", "")
                    if rel_path:
                        full_path = transcript_dir / rel_path
                        require_contained(full_path, transcript_dir)
                        if full_path.exists():
                            transcript_text = full_path.read_text(encoding="utf-8").strip()
                    transcript_method = result.get("method", "auto_caption")
                else:
                    failure = str(result.get("error", "transcription failed"))
                    logger.warning("Transcript failed for %s: %s", video_id, failure)
            except Exception as e:
                failure = str(e)
                logger.warning(f"  Transcript fetch error for {video_id}: {e}")

        if not transcript_text:
            failed += 1
            modules.append({"name": module_name, "status": "no_transcript"})
            errors.append(f"{course_slug}/{module_name}: {failure}")
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

    return {"created": created, "skipped": skipped, "failed": failed, "modules": modules,
            "errors": errors}


def _render_binding(module_dir: Path, formats: List[str]) -> tuple[dict, List[dict]]:
    from ..batch_processing.utils import module_artifacts, require_contained

    artifacts = module_artifacts(module_dir, formats)
    if not artifacts:
        raise ValueError(f"No authored renderable sources in {module_dir}")
    sources = sorted({artifact["source"] for artifact in artifacts})
    for artifact in artifacts:
        require_contained(artifact["destination"], module_dir)
    producer = Path(__file__).parents[1] / "batch_processing"
    return {
        "schema": "courses-youtube-render/v1",
        "formats": sorted(formats),
        "sources": {str(path.relative_to(module_dir)): hashlib.sha256(path.read_bytes()).hexdigest()
                    for path in sources},
        "producer": {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                     for path in (producer / "main.py", producer / "utils.py", Path(__file__))},
    }, artifacts


def _output_binding(module_dir: Path, artifacts: List[dict]) -> dict:
    outputs = {}
    for artifact in artifacts:
        destination = artifact["destination"]
        if not destination.is_file() or destination.stat().st_size == 0:
            raise ValueError(f"Missing or empty render: {destination}")
        outputs[str(destination.relative_to(module_dir))] = hashlib.sha256(destination.read_bytes()).hexdigest()
    return outputs


def render_course_modules(
    course_dir: Path, formats: Optional[List[str]] = None, resume: bool = True,
) -> Dict[str, Any]:
    """Resume only an exact source/format/producer-bound set of complete outputs."""
    from ..batch_processing.main import process_module_by_type
    from ..batch_processing.utils import get_formats_to_process, require_contained

    result: Dict[str, Any] = {"rendered": 0, "skipped": 0, "errors": [], "modules": []}
    try:
        active = get_formats_to_process("all" if formats is None else ",".join(formats))
        modules = sorted(d for d in course_dir.iterdir()
                         if d.is_dir() and (d / "module.md").is_file())
        if not modules:
            raise ValueError(f"No modules selected in {course_dir}")
    except (OSError, ValueError) as error:
        result["errors"].append(str(error))
        return result
    for module in modules:
        try:
            require_contained(module, course_dir)
            receipt_path = module / "output/.render-receipt.json"
            require_contained(receipt_path, module)
            binding, artifacts = _render_binding(module, active)
            if resume and receipt_path.is_file():
                try:
                    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
                    complete = receipt == {**binding, "outputs": _output_binding(module, artifacts)}
                except (OSError, ValueError, TypeError):
                    complete = False
                if complete:
                    result["skipped"] += 1
                    result["modules"].append({"name": module.name, "status": "skipped"})
                    continue
            if receipt_path.exists():
                receipt_path.unlink()
            rendered = process_module_by_type(str(module), str(module / "output"), formats=active)
            if rendered["errors"]:
                raise RuntimeError("; ".join(rendered["errors"]))
            after, _ = _render_binding(module, active)
            if binding != after:
                raise RuntimeError("Authored source or producer changed during rendering")
            receipt = {**binding, "outputs": _output_binding(module, artifacts)}
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                                 dir=receipt_path.parent, delete=False) as stream:
                    temporary = Path(stream.name)
                    json.dump(receipt, stream, sort_keys=True)
                    stream.write("\n")
                os.replace(temporary, receipt_path)
            finally:
                if temporary is not None and temporary.exists():
                    temporary.unlink()
            result["rendered"] += 1
            result["modules"].append({"name": module.name, "status": "rendered",
                                      "summary": rendered["summary"]})
        except Exception as error:
            message = f"{course_dir.name}/{module.name}: {error}"
            result["errors"].append(message)
            result["modules"].append({"name": module.name, "status": "error", "error": message})
    return result


def render_all_youtube_courses(
    youtube_courses_dir: Path, formats: Optional[List[str]] = None,
    course_filter: Optional[str] = None, resume: bool = True, *,
    course_slugs: Optional[List[str]] = None, limit: Optional[int] = None,
) -> Dict[str, Any]:
    from ..batch_processing.utils import require_contained

    result: Dict[str, Any] = {"courses": {}, "total_rendered": 0, "total_errors": []}
    try:
        if limit is not None and (type(limit) is not int or limit < 1):
            raise ValueError("Playlist limit must be a positive integer")
        courses = sorted(d for d in youtube_courses_dir.iterdir()
                         if d.is_dir() and not d.name.startswith((".", "__")))
        if course_filter is not None:
            courses = [d for d in courses if d.name == course_filter]
        if course_slugs is not None:
            missing = set(course_slugs) - {course.name for course in courses}
            if missing:
                result["total_errors"].append(f"Missing selected courses: {sorted(missing)}")
            courses = [course for course in courses if course.name in course_slugs]
        if limit is not None:
            courses = courses[:limit]
        if not courses:
            raise ValueError(f"No courses match selection in {youtube_courses_dir}")
        for course in courses:
            require_contained(course, youtube_courses_dir)
    except (OSError, ValueError) as error:
        result["total_errors"].append(str(error))
        return result
    for course in courses:
        course_result = render_course_modules(course, formats, resume)
        result["courses"][course.name] = course_result
        result["total_rendered"] += course_result["rendered"]
        result["total_errors"].extend(course_result["errors"])
    return result
