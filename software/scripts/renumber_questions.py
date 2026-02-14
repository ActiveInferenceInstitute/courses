#!/usr/bin/env python3
"""Script to renumber questions.md files to use continuous numbering.

Thin orchestrator - delegates to src.content_processing.

Usage:
    uv run python scripts/renumber_questions.py --course all
    uv run python scripts/renumber_questions.py --course ai-philosophy
    uv run python scripts/renumber_questions.py --course ai-math --module module-03
    uv run python scripts/renumber_questions.py --course all --dry-run --verbose
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.batch_processing.config import COURSE_REGISTRY
from src.content_processing import process_questions_file, renumber_questions_in_course


def parse_args(argv=None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Renumber questions.md files to use continuous numbering."
    )
    parser.add_argument(
        "--course",
        type=str,
        choices=list(COURSE_REGISTRY.keys()) + ["all"],
        default="all",
        help="Course to process (default: all)"
    )
    parser.add_argument(
        "--module",
        type=str,
        default=None,
        help="Process a single module (e.g., module-03)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without writing files"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed processing information"
    )

    return parser.parse_args(argv)


def main(argv=None):
    """Process questions.md files in specified courses."""
    args = parse_args(argv)

    # Paths
    repo_root = Path(__file__).parent.parent.parent

    # Determine courses to process
    if args.course == "all":
        courses = list(COURSE_REGISTRY.keys())
    else:
        courses = [args.course]

    # Run renumbering
    results = renumber_questions_in_course(
        repo_root,
        courses=courses,
        module_filter=args.module,
        dry_run=args.dry_run,
        verbose=args.verbose
    )

    # Report results
    print(f"\nTotal files converted: {results['files_converted']}")
    print(f"Total questions: {results['total_questions']}")

    if results["errors"]:
        print(f"\nErrors ({len(results['errors'])}):")
        for error in results["errors"]:
            print(f"  - {error}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
