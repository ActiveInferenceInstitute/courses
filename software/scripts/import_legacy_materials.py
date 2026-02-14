#!/usr/bin/env python3
"""Import legacy materials to course structure.

Usage:
    uv run python scripts/import_legacy_materials.py [OPTIONS]

Options:
    --course COURSE    Course to import into (e.g., ai-philosophy)
    --dry-run          Show what would be imported without importing
    --skip-questions   Skip importing chapter questions
    --skip-slides      Skip importing slides
    --help             Show this help message

Examples:
    # Import all materials for a specific course
    uv run python scripts/import_legacy_materials.py --course ai-philosophy

    # Dry run to preview what would be imported
    uv run python scripts/import_legacy_materials.py --dry-run

    # Import only slides, skip questions
    uv run python scripts/import_legacy_materials.py --skip-questions
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.batch_processing.logging_config import setup_logging
from src.batch_processing.config import COURSE_REGISTRY
from src.legacy_import import (
    process_chapter_questions,
    process_slides,
    process_for_upload_all_modules,
)

# Setup logging
logger = setup_logging()


def parse_args(argv=None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Import legacy materials to course structure.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --course ai-philosophy   Import for ai-philosophy
  %(prog)s --dry-run                Show what would be done
""",
    )

    parser.add_argument(
        "--course",
        choices=list(COURSE_REGISTRY.keys()),
        default="ai-philosophy",
        help="Course to import into (default: ai-philosophy)",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be imported without importing",
    )

    parser.add_argument(
        "--skip-questions",
        action="store_true",
        help="Skip importing chapter questions",
    )

    parser.add_argument(
        "--skip-slides",
        action="store_true",
        help="Skip importing slides",
    )

    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).parent.parent.parent

    # Log start
    logger.info("============================================================")
    logger.info(f"LEGACY IMPORT STARTED: {args.course}")
    logger.info("============================================================")

    if args.dry_run:
        logger.info("DRY RUN MODE - No files will be modified")
        logger.info("============================================================")

    # 1. Determine paths
    if args.course not in COURSE_REGISTRY:
        logger.error(f"Course {args.course} not found in registry")
        return 1

    course_root = repo_root / COURSE_REGISTRY[args.course]["rel_path"]  # Course root
    legacy_files_dir = repo_root / "bio_1_2025" / "files"  # Fixed source

    if not legacy_files_dir.exists():
        logger.error(f"Legacy files directory not found: {legacy_files_dir}")
        return 1
        
    if not course_root.exists():
        logger.error(f"Course directory not found: {course_root}")
        return 1

    success = True

    # 2. Process Chapter Questions
    if not args.skip_questions:
        logger.info("\n--- Importing Chapter Questions ---")
        qs_success = process_chapter_questions(
            legacy_files_dir, course_root, dry_run=args.dry_run
        )
        if not qs_success:
            success = False

    # 3. Process Slides
    if not args.skip_slides:
        logger.info("\n--- Importing Slides ---")
        slides_success = process_slides(
            legacy_files_dir, course_root, dry_run=args.dry_run
        )
        if not slides_success:
            success = False
            
    # 4. Process for Upload (renumbering)
    # This might be redundant if we are already renumbering, but legacy script does it
    # We can skip this if we trust renumber_questions.py, but keeping for compatibility
    if not args.dry_run:
         pass 

    logger.info("\n============================================================")
    if success:
        logger.info("IMPORT COMPLETED SUCCESSFULLY")
        return 0
    else:
        logger.error("IMPORT COMPLETED WITH ERRORS")
        return 1


if __name__ == "__main__":
    sys.exit(main())
