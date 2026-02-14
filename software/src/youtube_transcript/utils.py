"""Internal helpers for YouTube transcript processing."""

import json
import os
import re
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from .config import (
    CAPTIONS_SUBDIR,
    RATE_LIMIT_BATCH_DELAY,
    RATE_LIMIT_BATCH_SIZE,
    RATE_LIMIT_DELAY,
    SUBTITLE_FORMAT,
    SUBTITLE_LANGUAGE,
)


def enumerate_channel_videos(channel_url: str) -> List[Dict[str, Any]]:
    """List all video IDs and metadata from a YouTube channel.

    Uses yt-dlp extract_flat to get video list without downloading.

    Args:
        channel_url: YouTube channel URL (e.g. https://www.youtube.com/@ActiveInference)

    Returns:
        List of dicts with keys: id, title, duration, upload_date, url
    """
    import yt_dlp  # type: ignore[import-untyped]

    videos_url = channel_url.rstrip("/") + "/videos"

    ydl_opts = {
        "extract_flat": True,
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(videos_url, download=False)

    if not info or "entries" not in info:
        return []

    results = []
    for entry in info["entries"]:
        if entry is None:
            continue
        results.append(
            {
                "id": entry.get("id", ""),
                "title": entry.get("title", ""),
                "duration": entry.get("duration"),
                "upload_date": entry.get("upload_date"),
                "url": entry.get("url", f"https://www.youtube.com/watch?v={entry.get('id', '')}"),
            }
        )

    return results


def download_auto_captions(video_id: str, output_dir: Path) -> Optional[Path]:
    """Download auto-generated captions for a YouTube video.

    Args:
        video_id: YouTube video ID
        output_dir: Directory to save VTT file

    Returns:
        Path to downloaded VTT file, or None if no captions available
    """
    import yt_dlp  # type: ignore[import-untyped]

    captions_dir = output_dir / CAPTIONS_SUBDIR
    captions_dir.mkdir(parents=True, exist_ok=True)

    outtmpl = str(captions_dir / f"{video_id}")

    ydl_opts = {
        "writeautomaticsub": True,
        "writesubtitles": True,
        "subtitleslangs": [SUBTITLE_LANGUAGE],
        "subtitlesformat": SUBTITLE_FORMAT,
        "skip_download": True,
        "outtmpl": outtmpl,
        "quiet": True,
        "no_warnings": True,
    }

    url = f"https://www.youtube.com/watch?v={video_id}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # yt-dlp names subtitle files as: {id}.{lang}.{format}
    expected_path = captions_dir / f"{video_id}.{SUBTITLE_LANGUAGE}.{SUBTITLE_FORMAT}"
    if expected_path.exists():
        return expected_path

    # Check for auto-generated variant naming
    for suffix in [
        f".{SUBTITLE_LANGUAGE}.{SUBTITLE_FORMAT}",
        f".{SUBTITLE_LANGUAGE}-orig.{SUBTITLE_FORMAT}",
    ]:
        candidate = captions_dir / f"{video_id}{suffix}"
        if candidate.exists():
            return candidate

    return None


def clean_vtt_text(raw_text: str) -> str:
    """Clean VTT subtitle text into plain readable text.

    Strips WEBVTT header, timestamps, HTML tags, position metadata,
    and deduplicates overlapping caption segments.

    Args:
        raw_text: Raw VTT file content

    Returns:
        Clean plain text transcript
    """
    lines = raw_text.split("\n")

    # Skip WEBVTT header and metadata
    content_start = 0
    for i, line in enumerate(lines):
        if line.strip() == "" and i > 0:
            content_start = i + 1
            break
    if content_start == 0:
        content_start = 1  # Skip at least the WEBVTT line

    text_lines = []
    seen_lines: set[str] = set()

    for line in lines[content_start:]:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Skip timestamp lines (00:00:00.000 --> 00:00:00.000)
        if re.match(r"\d{2}:\d{2}[:\.]?\d{0,2}[\.,]?\d{0,3}\s*-->", line):
            continue

        # Skip numeric cue identifiers
        if re.match(r"^\d+$", line):
            continue

        # Skip position/alignment metadata
        if re.match(r"^(position|align|size|line):", line, re.IGNORECASE):
            continue

        # Remove HTML tags
        line = re.sub(r"<[^>]+>", "", line)

        # Remove VTT position metadata inline (e.g., align:start position:0%)
        line = re.sub(r"\b(align|position|size|line):[^\s]+", "", line).strip()

        if not line:
            continue

        # Deduplicate overlapping segments
        if line not in seen_lines:
            seen_lines.add(line)
            text_lines.append(line)

    return " ".join(text_lines)


def parse_vtt_to_text(vtt_path: Path) -> str:
    """Read a VTT file and return clean plain text.

    Args:
        vtt_path: Path to VTT subtitle file

    Returns:
        Clean plain text transcript
    """
    raw_text = vtt_path.read_text(encoding="utf-8")
    return clean_vtt_text(raw_text)


def download_audio_for_whisper(video_id: str, output_dir: Path) -> Path:
    """Download audio-only from YouTube for Whisper transcription.

    Args:
        video_id: YouTube video ID
        output_dir: Directory for temporary audio file

    Returns:
        Path to downloaded audio file

    Raises:
        RuntimeError: If download fails
    """
    import yt_dlp  # type: ignore[import-untyped]

    output_dir.mkdir(parents=True, exist_ok=True)
    outtmpl = str(output_dir / f"{video_id}_audio.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "128",
            }
        ],
        "quiet": True,
        "no_warnings": True,
    }

    url = f"https://www.youtube.com/watch?v={video_id}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    audio_path = output_dir / f"{video_id}_audio.mp3"
    if not audio_path.exists():
        # Check for other extensions
        for ext in ["mp3", "m4a", "wav", "opus", "webm"]:
            candidate = output_dir / f"{video_id}_audio.{ext}"
            if candidate.exists():
                return candidate
        raise RuntimeError(f"Audio download failed for {video_id}")

    return audio_path


def transcribe_with_whisper(audio_path: Path, model: str = "base") -> str:
    """Transcribe audio file using OpenAI Whisper.

    Args:
        audio_path: Path to audio file
        model: Whisper model size (tiny, base, small, medium, large)

    Returns:
        Transcribed text

    Raises:
        ImportError: If whisper is not installed
        RuntimeError: If transcription fails
    """
    try:
        import whisper  # type: ignore[import-not-found]
    except ImportError:
        raise ImportError(
            "openai-whisper is not installed. Install with: uv sync --extra whisper"
        )

    whisper_model = whisper.load_model(model)
    result = whisper_model.transcribe(str(audio_path))
    text = str(result.get("text", ""))
    return text.strip()


def load_manifest(path: Path) -> Dict[str, Any]:
    """Load manifest JSON from disk.

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
        "total_videos": 0,
        "videos": {},
    }


def save_manifest(manifest: Dict[str, Any], path: Path) -> None:
    """Save manifest JSON to disk with atomic write.

    Uses a temp file + os.replace for crash safety.

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


def ensure_output_directory(path: Path) -> None:
    """Create directory and parents if they don't exist.

    Args:
        path: Directory path to create
    """
    path.mkdir(parents=True, exist_ok=True)


def rate_limit_sleep(index: int) -> None:
    """Sleep for rate limiting between video downloads.

    Args:
        index: Zero-based index of current video in batch
    """
    time.sleep(RATE_LIMIT_DELAY)
    if (index + 1) % RATE_LIMIT_BATCH_SIZE == 0:
        time.sleep(RATE_LIMIT_BATCH_DELAY)


def enumerate_channel_playlists(channel_url: str) -> List[Dict[str, Any]]:
    """List all playlists from a YouTube channel's /playlists tab.

    Uses yt-dlp extract_flat to get playlist list without downloading.

    Args:
        channel_url: YouTube channel URL (e.g. https://www.youtube.com/@ActiveInference)

    Returns:
        List of dicts with keys: id, title, url, playlist_count
    """
    import yt_dlp  # type: ignore[import-untyped]

    playlists_url = channel_url.rstrip("/") + "/playlists"

    ydl_opts = {
        "extract_flat": True,
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlists_url, download=False)

    if not info or "entries" not in info:
        return []

    results = []
    for entry in info["entries"]:
        if entry is None:
            continue
        playlist_id = entry.get("id", "")
        results.append(
            {
                "id": playlist_id,
                "title": entry.get("title", ""),
                "url": entry.get(
                    "url",
                    f"https://www.youtube.com/playlist?list={playlist_id}",
                ),
                "playlist_count": entry.get("playlist_count", 0),
            }
        )

    return results


def enumerate_playlist_videos(playlist_url: str) -> List[Dict[str, Any]]:
    """List all videos in a playlist, ordered by position.

    Uses yt-dlp extract_flat to get video list without downloading.

    Args:
        playlist_url: YouTube playlist URL

    Returns:
        List of dicts with keys: id, title, duration, upload_date, playlist_index
    """
    import yt_dlp  # type: ignore[import-untyped]

    ydl_opts = {
        "extract_flat": True,
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)

    if not info or "entries" not in info:
        return []

    results = []
    for i, entry in enumerate(info["entries"]):
        if entry is None:
            continue
        results.append(
            {
                "id": entry.get("id", ""),
                "title": entry.get("title", ""),
                "duration": entry.get("duration"),
                "upload_date": entry.get("upload_date"),
                "playlist_index": i,
            }
        )

    return results
