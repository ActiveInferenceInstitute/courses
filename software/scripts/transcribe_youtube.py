#!/usr/bin/env python3
"""Download and transcribe YouTube channel videos.

Usage:
    uv run python scripts/transcribe_youtube.py [OPTIONS]

Options:
    --channel URL        Channel URL (default: @ActiveInference)
    --output DIR         Output directory (default: transcription/)
    --video-id ID        Single video mode
    --whisper-model M    Whisper model: tiny/base/small/medium/large (default: base)
    --skip-whisper       Skip Whisper fallback (captions only)
    --limit N            Max videos to process
    --no-resume          Re-process all videos
    --list-only          Enumerate videos only, save manifest
    --dry-run            Preview without transcribing

Examples:
    uv run python scripts/transcribe_youtube.py --list-only
    uv run python scripts/transcribe_youtube.py --limit 5
    uv run python scripts/transcribe_youtube.py --skip-whisper
    uv run python scripts/transcribe_youtube.py --video-id dQw4w9WgXcQ
"""

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.youtube_transcript.config import DEFAULT_CHANNEL_URL, DEFAULT_WHISPER_MODEL, OUTPUT_DIR_NAME
from src.youtube_transcript.main import get_channel_video_list, transcribe_channel, transcribe_video
from src.youtube_transcript.utils import ensure_output_directory, load_manifest, save_manifest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def parse_args(argv=None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Download and transcribe YouTube channel videos.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--channel",
        type=str,
        default=DEFAULT_CHANNEL_URL,
        help=f"Channel URL (default: {DEFAULT_CHANNEL_URL})",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help=f"Output directory (default: {OUTPUT_DIR_NAME}/)",
    )
    parser.add_argument(
        "--video-id",
        type=str,
        default=None,
        help="Transcribe a single video by ID",
    )
    parser.add_argument(
        "--whisper-model",
        type=str,
        default=DEFAULT_WHISPER_MODEL,
        choices=["tiny", "base", "small", "medium", "large"],
        help=f"Whisper model size (default: {DEFAULT_WHISPER_MODEL})",
    )
    parser.add_argument(
        "--skip-whisper",
        action="store_true",
        help="Skip Whisper fallback, use captions only",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Max number of videos to process",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Re-process all videos (ignore existing manifest)",
    )
    parser.add_argument(
        "--list-only",
        action="store_true",
        help="Enumerate videos only, save to manifest",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be done without transcribing",
    )
    return parser.parse_args(argv)


def main(argv=None) -> int:
    """Run YouTube transcription pipeline."""
    args = parse_args(argv)

    # Resolve output directory
    if args.output:
        output_dir = Path(args.output)
    else:
        output_dir = Path(__file__).parent.parent / OUTPUT_DIR_NAME

    ensure_output_directory(output_dir)

    # Single video mode
    if args.video_id:
        logger.info(f"Transcribing single video: {args.video_id}")
        result = transcribe_video(
            args.video_id,
            output_dir,
            whisper_model=args.whisper_model,
            skip_whisper=args.skip_whisper,
        )
        logger.info(f"Result: {result['status']} (method: {result['method']})")
        if result["transcript_path"]:
            logger.info(f"Transcript: {output_dir / result['transcript_path']}")
        return 0 if result["status"] == "completed" else 1

    # List-only mode
    if args.list_only:
        logger.info(f"Enumerating videos from {args.channel}...")
        videos = get_channel_video_list(args.channel)
        logger.info(f"Found {len(videos)} videos")

        from datetime import datetime, timezone

        manifest = load_manifest(output_dir / "manifest.json")
        manifest["channel_url"] = args.channel
        manifest["total_videos"] = len(videos)
        manifest["last_updated"] = datetime.now(timezone.utc).isoformat()
        for v in videos:
            if v["id"] not in manifest.get("videos", {}):
                if "videos" not in manifest:
                    manifest["videos"] = {}
                manifest["videos"][v["id"]] = {
                    "title": v.get("title", ""),
                    "duration": v.get("duration"),
                    "upload_date": v.get("upload_date"),
                    "method": None,
                    "status": "pending",
                    "transcript_path": None,
                    "error": None,
                }
        save_manifest(manifest, output_dir / "manifest.json")
        logger.info(f"Manifest saved to {output_dir / 'manifest.json'}")

        for i, v in enumerate(videos):
            dur = f"{v['duration']}s" if v.get("duration") else "?"
            logger.info(f"  {i + 1:3d}. [{v['id']}] ({dur}) {v.get('title', '?')}")
        return 0

    # Dry-run mode
    if args.dry_run:
        logger.info(f"DRY RUN: Would transcribe from {args.channel}")
        videos = get_channel_video_list(args.channel)
        manifest = load_manifest(output_dir / "manifest.json")
        existing = manifest.get("videos", {})
        completed = sum(1 for v in existing.values() if v.get("status") == "completed")

        logger.info(f"  Total videos: {len(videos)}")
        logger.info(f"  Already completed: {completed}")
        logger.info(f"  Remaining: {len(videos) - completed}")
        if args.limit:
            logger.info(f"  Limit: {args.limit}")
        logger.info(f"  Whisper fallback: {'off' if args.skip_whisper else 'on'}")
        logger.info(f"  Output: {output_dir}")
        return 0

    # Full transcription
    logger.info(f"Starting transcription from {args.channel}")
    summary = transcribe_channel(
        channel_url=args.channel,
        output_dir=output_dir,
        whisper_model=args.whisper_model,
        skip_whisper=args.skip_whisper,
        limit=args.limit,
        resume=not args.no_resume,
    )

    logger.info("=" * 60)
    logger.info(f"Total videos found: {summary['total_enumerated']}")
    logger.info(f"Processed: {summary['processed']}")
    logger.info(f"Completed: {summary['completed']}")
    logger.info(f"Failed: {summary['failed']}")
    logger.info(f"Manifest: {summary['manifest_path']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
