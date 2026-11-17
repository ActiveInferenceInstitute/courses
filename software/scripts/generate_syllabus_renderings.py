#!/usr/bin/env python3
"""Script to generate all renderings for syllabus files.

Usage:
    uv run python scripts/generate_syllabus_renderings.py [OPTIONS]

Options:
    --course COURSE    Course to process (e.g., ai-philosophy)
    --help             Show this help message

Examples:
    # Generate syllabus renderings for ai-philosophy (default)
    uv run python scripts/generate_syllabus_renderings.py

    # Generate syllabus renderings for ai-math
    uv run python scripts/generate_syllabus_renderings.py --course ai-math
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.main import process_course_syllabus
from src.batch_processing.utils import get_formats_to_process, require_contained


def parse_args(argv=None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate all renderings for syllabus files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                         Generate for ai-philosophy syllabus (default)
  %(prog)s --course ai-math        Generate for ai-math syllabus
        """,
    )

    parser.add_argument(
        "--course",
        choices=list(COURSE_REGISTRY.keys()),
        default="ai-philosophy",
        help="Course to process (default: ai-philosophy)",
    )
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--formats", default="all")
    parser.add_argument("--dry-run", action="store_true")

    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        formats = get_formats_to_process(args.formats)
        metadata = COURSE_REGISTRY[args.course]
        course = args.repo_root / metadata["rel_path"]
        syllabus = course / metadata.get("syllabus_location", "syllabus")
        require_contained(syllabus, args.repo_root)
        if not syllabus.exists():
            raise FileNotFoundError(syllabus)
        if syllabus.is_file():
            print(f"File-style syllabus is copied during publication, not rendered: {syllabus}")
            return 0
        if args.dry_run:
            from src.batch_processing.utils import syllabus_artifacts

            for artifact in syllabus_artifacts(course, formats, args.course):
                print(artifact["destination"])
            return 0
        result = process_course_syllabus(course, metadata["display_name"], formats, args.course)
        for error in result["errors"]:
            print(error, file=sys.stderr)
        return 1 if result["errors"] else 0
    except (OSError, ValueError) as error:
        print(f"Syllabus generation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
