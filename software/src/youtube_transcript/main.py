"""Public API for YouTube transcript processing."""

import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from .config import (
    DEFAULT_CHANNEL_URL,
    DEFAULT_WHISPER_MODEL,
    MANIFEST_FILENAME,
    OUTPUT_DIR_NAME,
    TRANSCRIPTS_SUBDIR,
)
from .utils import (
    download_audio_for_whisper,
    download_auto_captions,
    ensure_output_directory,
    enumerate_channel_videos,
    load_manifest,
    parse_vtt_to_text,
    rate_limit_sleep,
    save_manifest,
    transcribe_with_whisper,
)

logger = logging.getLogger(__name__)


def transcribe_video(
    video_id: str,
    output_dir: Path,
    whisper_model: str = DEFAULT_WHISPER_MODEL,
    skip_whisper: bool = False,
) -> Dict[str, Any]:
    """Transcribe a single YouTube video.

    Tries auto-captions first, then Whisper fallback if available.

    Args:
        video_id: YouTube video ID
        output_dir: Base output directory
        whisper_model: Whisper model size for fallback
        skip_whisper: If True, skip Whisper fallback

    Returns:
        Dict with keys: video_id, method, status, transcript_path, error
    """
    result: Dict[str, Any] = {
        "video_id": video_id,
        "method": "no_transcript",
        "status": "failed",
        "transcript_path": None,
        "error": None,
    }

    transcripts_dir = output_dir / TRANSCRIPTS_SUBDIR
    ensure_output_directory(transcripts_dir)

    transcript_path = transcripts_dir / f"{video_id}.txt"

    # Try auto-captions first
    try:
        vtt_path = download_auto_captions(video_id, output_dir)
        if vtt_path is not None:
            text = parse_vtt_to_text(vtt_path)
            if text.strip():
                transcript_path.write_text(text, encoding="utf-8")
                result["method"] = "auto_caption"
                result["status"] = "completed"
                result["transcript_path"] = str(transcript_path.relative_to(output_dir))
                logger.info(f"[caption] {video_id}: {len(text)} chars")
                return result
    except Exception as e:
        logger.warning(f"Caption download failed for {video_id}: {e}")

    # Whisper fallback
    if not skip_whisper:
        try:
            audio_path = download_audio_for_whisper(video_id, output_dir)
            try:
                text = transcribe_with_whisper(audio_path, whisper_model)
                if text.strip():
                    transcript_path.write_text(text, encoding="utf-8")
                    result["method"] = "whisper"
                    result["status"] = "completed"
                    result["transcript_path"] = str(transcript_path.relative_to(output_dir))
                    logger.info(f"[whisper] {video_id}: {len(text)} chars")
                    return result
            finally:
                # Clean up audio file
                if audio_path.exists():
                    audio_path.unlink()
        except ImportError:
            logger.info(f"Whisper not installed, skipping fallback for {video_id}")
            result["error"] = "whisper_not_installed"
        except Exception as e:
            logger.warning(f"Whisper transcription failed for {video_id}: {e}")
            result["error"] = str(e)

    if result["status"] != "completed":
        result["status"] = "skipped" if skip_whisper else "failed"
        if not result["error"]:
            result["error"] = "no_captions_available"

    return result


def transcribe_channel(
    channel_url: str = DEFAULT_CHANNEL_URL,
    output_dir: Optional[Path] = None,
    whisper_model: str = DEFAULT_WHISPER_MODEL,
    skip_whisper: bool = False,
    limit: Optional[int] = None,
    resume: bool = True,
) -> Dict[str, Any]:
    """Transcribe all videos from a YouTube channel.

    Enumerates channel videos, skips completed ones if resuming,
    processes remaining, and saves manifest after each video.

    Args:
        channel_url: YouTube channel URL
        output_dir: Base output directory (default: software/transcription/)
        whisper_model: Whisper model size
        skip_whisper: Skip Whisper fallback
        limit: Max videos to process (None for all)
        resume: Skip videos already in manifest

    Returns:
        Summary dict with counts and manifest path
    """
    if output_dir is None:
        output_dir = Path(__file__).parent.parent.parent / OUTPUT_DIR_NAME

    ensure_output_directory(output_dir)
    manifest_path = output_dir / MANIFEST_FILENAME
    manifest = load_manifest(manifest_path)

    # Enumerate channel
    logger.info(f"Enumerating videos from {channel_url}...")
    videos = enumerate_channel_videos(channel_url)
    logger.info(f"Found {len(videos)} videos")

    manifest["channel_url"] = channel_url
    manifest["total_videos"] = len(videos)

    if "videos" not in manifest:
        manifest["videos"] = {}

    # Filter to unprocessed videos if resuming
    to_process = []
    for video in videos:
        vid = video["id"]
        if resume and vid in manifest["videos"]:
            existing = manifest["videos"][vid]
            if existing.get("status") == "completed":
                continue
        to_process.append(video)

    if limit is not None:
        to_process = to_process[:limit]

    logger.info(f"Processing {len(to_process)} videos (skipped {len(videos) - len(to_process)})")

    completed = 0
    failed = 0

    for i, video in enumerate(to_process):
        vid = video["id"]
        logger.info(f"[{i + 1}/{len(to_process)}] {video.get('title', vid)}")

        result = transcribe_video(vid, output_dir, whisper_model, skip_whisper)

        manifest["videos"][vid] = {
            "title": video.get("title", ""),
            "duration": video.get("duration"),
            "upload_date": video.get("upload_date"),
            "method": result["method"],
            "status": result["status"],
            "transcript_path": result["transcript_path"],
            "error": result["error"],
        }
        manifest["last_updated"] = datetime.now(timezone.utc).isoformat()

        # Save manifest after each video for crash recovery
        save_manifest(manifest, manifest_path)

        if result["status"] == "completed":
            completed += 1
        else:
            failed += 1

        # Rate limiting
        if i < len(to_process) - 1:
            rate_limit_sleep(i)

    return {
        "total_enumerated": len(videos),
        "processed": len(to_process),
        "completed": completed,
        "failed": failed,
        "manifest_path": str(manifest_path),
    }


def get_channel_video_list(channel_url: str = DEFAULT_CHANNEL_URL) -> List[Dict[str, Any]]:
    """Enumerate videos from a YouTube channel without transcribing.

    Args:
        channel_url: YouTube channel URL

    Returns:
        List of video metadata dicts
    """
    return enumerate_channel_videos(channel_url)
