#!/usr/bin/env python3
"""Render YouTube playlists as courses through the batch processing pipeline.

Enumerates playlists from a YouTube channel, scaffolds course directory
structures with transcript-based module.md files, and renders each module
through process_module_by_type() -> PDF, HTML, DOCX, TXT, MD, MP3.

Usage:
    uv run python scripts/render_youtube_courses.py [OPTIONS]

Options:
    --channel URL         Channel URL (default: @ActiveInference)
    --course SLUG         Only render this playlist-course
    --formats FORMATS     Comma-separated: pdf,html,docx,txt,md,mp3 (default: all)
    --skip-scaffold       Render existing courses only (no enumeration/scaffolding)
    --skip-render         Scaffold only (no format rendering)
    --skip-whisper        Captions only for missing transcripts
    --no-resume           Re-render everything
    --list-playlists      Enumerate playlists only, save manifest
    --dry-run             Preview without writing
    --limit N             Max playlists to process

Examples:
    uv run python scripts/render_youtube_courses.py --list-playlists
    uv run python scripts/render_youtube_courses.py --formats txt,md --limit 1
    uv run python scripts/render_youtube_courses.py --course active-inference-textbook-group
    uv run python scripts/render_youtube_courses.py --skip-scaffold --formats pdf,html
    uv run python scripts/render_youtube_courses.py --dry-run
"""

import argparse
import json
import logging
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.youtube_transcript.config import DEFAULT_CHANNEL_URL, OUTPUT_DIR_NAME
from src.youtube_transcript.render import (
    enumerate_and_map_playlists,
    load_youtube_manifest,
    render_all_youtube_courses,
    save_youtube_manifest,
    scaffold_course_directory,
)

YOUTUBE_COURSES_SUBDIR = "youtube"
MANIFEST_FILENAME = "youtube_courses.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def parse_args(argv=None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Render YouTube playlists as courses.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--channel",
        type=str,
        default=DEFAULT_CHANNEL_URL,
        help=f"YouTube channel URL (default: {DEFAULT_CHANNEL_URL})",
    )
    parser.add_argument(
        "--course",
        type=str,
        default=None,
        help="Only render this playlist-course slug",
    )
    parser.add_argument(
        "--formats",
        type=str,
        default="all",
        help="Comma-separated formats: pdf,html,docx,txt,md,mp3 (default: all)",
    )
    parser.add_argument(
        "--skip-scaffold",
        action="store_true",
        help="Render existing courses only (no enumeration/scaffolding)",
    )
    parser.add_argument(
        "--skip-render",
        action="store_true",
        help="Scaffold only (no format rendering)",
    )
    parser.add_argument(
        "--skip-whisper",
        action="store_true",
        help="Captions only for missing transcripts (no Whisper fallback)",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Re-render everything (ignore existing outputs)",
    )
    parser.add_argument(
        "--list-playlists",
        action="store_true",
        help="Enumerate playlists only, save manifest, and exit",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without writing any files",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Max playlists to process",
    )
    return parser.parse_args(argv)


def get_formats(formats_str: str) -> list[str] | None:
    """Parse formats argument into list or None for all.

    Args:
        formats_str: Comma-separated format string or 'all'

    Returns:
        List of format strings, or None for all formats
    """
    if formats_str == "all":
        return None
    return [f.strip() for f in formats_str.split(",") if f.strip()]


def main(argv=None) -> int:
    """Main entry point for YouTube course rendering."""
    args = parse_args(argv)
    start_time = time.time()

    # Resolve paths
    repo_root = Path(__file__).parent.parent.parent
    transcript_dir = Path(__file__).parent.parent / OUTPUT_DIR_NAME
    youtube_courses_dir = repo_root / "course_development" / YOUTUBE_COURSES_SUBDIR
    manifest_path = youtube_courses_dir / MANIFEST_FILENAME

    logger.info("=" * 60)
    logger.info("YouTube Course Renderer")
    logger.info(f"Channel: {args.channel}")
    logger.info(f"Courses dir: {youtube_courses_dir}")
    logger.info(f"Transcript dir: {transcript_dir}")

    formats = get_formats(args.formats)
    resume = not args.no_resume

    # --list-playlists: enumerate + save manifest + exit
    if args.list_playlists:
        manifest = enumerate_and_map_playlists(args.channel, transcript_dir)
        if not args.dry_run:
            youtube_courses_dir.mkdir(parents=True, exist_ok=True)
            save_youtube_manifest(manifest, manifest_path)
            logger.info(f"Manifest saved: {manifest_path}")

        logger.info(f"\nPlaylists ({manifest['total_playlists']}):")
        for slug, playlist in manifest["playlists"].items():
            logger.info(f"  {slug}: {playlist['title']} ({playlist['video_count']} videos)")

        elapsed = time.time() - start_time
        logger.info(f"\nCompleted in {elapsed:.1f}s")
        return 0

    # --dry-run: load manifest, print summary + exit
    if args.dry_run:
        manifest = load_youtube_manifest(manifest_path)
        if not manifest["playlists"]:
            logger.info("No manifest found. Run --list-playlists first.")
            return 1

        logger.info(f"\nDry run - {manifest['total_playlists']} playlists:")
        for slug, playlist in manifest["playlists"].items():
            logger.info(f"  {slug}: {playlist['title']} ({playlist['video_count']} videos)")

        # Check existing scaffolded courses
        if youtube_courses_dir.exists():
            existing = [
                d.name
                for d in youtube_courses_dir.iterdir()
                if d.is_dir() and d.name != "__pycache__"
            ]
            logger.info(f"\nExisting course directories: {len(existing)}")
            for name in sorted(existing):
                module_count = sum(
                    1
                    for d in (youtube_courses_dir / name).iterdir()
                    if d.is_dir() and (d / "module.md").exists()
                )
                logger.info(f"  {name}: {module_count} modules")

        formats_desc = ", ".join(formats) if formats else "all"
        logger.info(f"\nFormats: {formats_desc}")
        logger.info(f"Resume: {resume}")
        return 0

    # Scaffold phase (unless --skip-scaffold)
    if not args.skip_scaffold:
        logger.info("\n--- Scaffold Phase ---")

        # Load or enumerate playlists
        manifest = load_youtube_manifest(manifest_path)
        if not manifest["playlists"]:
            logger.info("No manifest found, enumerating playlists...")
            manifest = enumerate_and_map_playlists(args.channel, transcript_dir)
            youtube_courses_dir.mkdir(parents=True, exist_ok=True)
            save_youtube_manifest(manifest, manifest_path)

        playlists = list(manifest["playlists"].items())
        if args.course:
            playlists = [(s, p) for s, p in playlists if s == args.course]
            if not playlists:
                logger.error(f"Course not found: {args.course}")
                return 1

        if args.limit:
            playlists = playlists[: args.limit]

        total_created = 0
        total_skipped = 0
        total_failed = 0

        for slug, playlist in playlists:
            logger.info(f"\nScaffolding: {playlist['title']} ({len(playlist['videos'])} videos)")
            scaffold_results = scaffold_course_directory(
                course_slug=slug,
                videos=playlist["videos"],
                transcript_dir=transcript_dir,
                youtube_courses_dir=youtube_courses_dir,
                course_metadata=playlist,
                skip_whisper=args.skip_whisper,
            )
            total_created += scaffold_results["created"]
            total_skipped += scaffold_results["skipped"]
            total_failed += scaffold_results["failed"]

        logger.info(
            f"\nScaffold summary: {total_created} created, "
            f"{total_skipped} skipped, {total_failed} failed"
        )

    # Render phase (unless --skip-render)
    if not args.skip_render:
        logger.info("\n--- Render Phase ---")
        render_results = render_all_youtube_courses(
            youtube_courses_dir=youtube_courses_dir,
            formats=formats,
            course_filter=args.course,
            resume=resume,
        )

        logger.info(
            f"\nRender summary: {render_results['total_rendered']} modules rendered"
        )
        if render_results["total_errors"]:
            logger.warning(f"Errors: {len(render_results['total_errors'])}")
            for err in render_results["total_errors"][:10]:
                logger.error(f"  {err}")

    elapsed = time.time() - start_time
    logger.info(f"\nCompleted in {elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
