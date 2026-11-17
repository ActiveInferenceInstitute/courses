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
import logging
import sys
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
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--transcript-dir", type=Path)
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
        "--force-scaffold",
        action="store_true",
        help="Overwrite existing module.md files during scaffolding",
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


def get_formats(formats_str: str) -> list[str]:
    from src.batch_processing.utils import get_formats_to_process

    return get_formats_to_process(formats_str)


def main(argv=None) -> int:
    args = parse_args(argv)
    root = args.repo_root
    transcript_dir = args.transcript_dir or root / "software" / OUTPUT_DIR_NAME
    courses_dir = root / "course_development" / YOUTUBE_COURSES_SUBDIR
    manifest_path = courses_dir / MANIFEST_FILENAME
    errors = []
    selected = None
    try:
        formats = get_formats(args.formats)
        if args.limit is not None and args.limit < 1:
            raise ValueError("--limit must be positive")
        if args.skip_scaffold and args.skip_render and not args.list_playlists:
            raise ValueError("Both phases are disabled")
        # Dry-run is local-only, including --list-playlists.
        if args.dry_run or not args.skip_scaffold or args.list_playlists:
            manifest = load_youtube_manifest(manifest_path)
            if (args.list_playlists or not manifest["playlists"]) and not args.dry_run:
                manifest = enumerate_and_map_playlists(args.channel, transcript_dir)
            playlists = list(manifest["playlists"].items())
            if args.course is not None:
                playlists = [(slug, value) for slug, value in playlists if slug == args.course]
            if args.limit is not None:
                playlists = playlists[: args.limit]
            if not playlists:
                raise ValueError(
                    "No playlists match selection; local dry-run requires an existing manifest"
                )
            selected = [slug for slug, _ in playlists]
            if args.dry_run:
                for slug, playlist in playlists:
                    print(f"{slug}: {len(playlist['videos'])} videos; formats={','.join(formats)}")
                return 0
            if args.list_playlists:
                save_youtube_manifest(manifest, manifest_path)
                return 0
            save_youtube_manifest(manifest, manifest_path)
            for slug, playlist in playlists:
                try:
                    outcome = scaffold_course_directory(
                        slug,
                        playlist["videos"],
                        transcript_dir,
                        courses_dir,
                        playlist,
                        skip_whisper=args.skip_whisper,
                        force=args.force_scaffold,
                    )
                    errors.extend(outcome["errors"])
                except (OSError, ValueError, KeyError, TypeError) as error:
                    errors.append(f"{slug}: {error}")
        if not args.skip_render:
            rendered = render_all_youtube_courses(
                courses_dir,
                formats,
                args.course,
                not args.no_resume,
                course_slugs=selected,
                limit=args.limit,
            )
            errors.extend(rendered["total_errors"])
    except Exception as error:
        errors.append(str(error))
    for error in errors:
        logger.error(error)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
