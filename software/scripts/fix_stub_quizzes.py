#!/usr/bin/env python3
"""Regenerate stub practice quizzes from module.md content.

Reads module.md, extracts key concepts, objectives, and lesson content,
then generates a proper practice quiz with 7 multiple-choice questions,
3 free-response questions, and a complete answer key with explanations.

Refactored to be a thin orchestrator using src.content_processing.
"""

import argparse
import sys
from pathlib import Path

# Add software directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.utils import extract_course_info_from_path as extract_course_info
from src.content_processing import find_stub_quizzes, generate_quiz_content
from src.content_processing.utils import parse_module

DEFAULT_BASE = Path(__file__).resolve().parent.parent.parent / "course_development"


def parse_args(argv=None):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Regenerate stub practice quizzes")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument(
        "--base", type=Path, default=DEFAULT_BASE, help="Base course_development directory"
    )
    parser.add_argument(
        "--course", choices=list(COURSE_REGISTRY.keys()), help="Process only this course"
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    base = args.base
    stubs = find_stub_quizzes(base)
    print(f"Found {len(stubs)} stub quizzes to fix\\n")

    fixed = skipped = errors = 0
    for quiz_path in stubs:
        module_dir = quiz_path.parent
        course_info = extract_course_info(quiz_path, base)

        # Filter by --course if given
        if args.course and course_info["course"] != args.course:
            continue

        module_data = parse_module(module_dir)

        if not module_data.get("key_concepts"):
            print(f"  SKIP (no concepts): {quiz_path.relative_to(base)}")
            skipped += 1
            continue

        try:
            quiz_text = generate_quiz_content(module_data, course_info)
            action = "Would fix" if args.dry_run else "Fixed"
            if not args.dry_run:
                quiz_path.write_text(quiz_text, encoding="utf-8")
            print(
                f"  {action}: {quiz_path.relative_to(base)} ({len(module_data.get('key_concepts', []))} concepts, {len(module_data.get('objectives', []))} objectives)"
            )
            fixed += 1
        except Exception as e:
            print(f"  ERROR: {quiz_path.relative_to(base)}: {e}")
            errors += 1

    print(f"\\nDone: {fixed} fixed, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
