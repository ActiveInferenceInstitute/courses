#!/usr/bin/env python3
"""Regenerate stub questions.md files from module.md content.

Detects template questions (generic 'and why does it matter' pattern)
and replaces them with substantive, module-specific study questions
that follow Bloom's taxonomy progression.

Refactored to be a thin orchestrator using src.content_processing.
"""

import argparse
import sys
from pathlib import Path

# Add software directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.utils import extract_course_info_from_path as extract_course_info
from src.content_processing import find_stub_questions, generate_questions_content
from src.content_processing.utils import parse_module


DEFAULT_BASE = Path(__file__).resolve().parent.parent.parent / "course_development"


def parse_args(argv=None):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Regenerate stub questions.md files")
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
    stubs = find_stub_questions(base)
    print(f"Found {len(stubs)} stub questions files to fix\\n")

    fixed = 0
    skipped = 0
    errors = 0

    for qf_path in stubs:
        module_dir = qf_path.parent
        course_info = extract_course_info(qf_path, base)

        # Filter by --course if given
        if args.course and course_info["course"] != args.course:
            continue

        try:
            module_data = parse_module(module_dir)
            if not module_data:
                print(f"  SKIP (no module.md): {qf_path.relative_to(base)}")
                skipped += 1
                continue

            concepts = module_data.get("key_concepts", [])
            objectives = module_data.get("objectives", [])

            if not concepts and not objectives:
                print(f"  SKIP (no concepts/objectives): {qf_path.relative_to(base)}")
                skipped += 1
                continue

            q_text = generate_questions_content(module_data, course_info)

            if args.dry_run:
                print(
                    f"  Would fix: {qf_path.relative_to(base)} ({len(concepts)} concepts, {len(objectives)} objectives)"
                )
            else:
                qf_path.write_text(q_text, encoding="utf-8")
                print(
                    f"  Fixed: {qf_path.relative_to(base)} ({len(concepts)} concepts, {len(objectives)} objectives)"
                )
            fixed += 1

        except Exception as e:
            print(f"  ERROR: {qf_path.relative_to(base)}: {e}")
            errors += 1

    print(f"\\nDone: {fixed} fixed, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
