#!/usr/bin/env python3
"""Regenerate stub lab.md files from module.md content.

Detects template labs (generic 'explore X through hands-on engagement' pattern)
and replaces them with substantive, module-specific lab activities.

Thin orchestrator: delegates to src.content_processing.labs.
"""

import argparse
import sys
from pathlib import Path

# Add software/ to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(software_dir))

from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.utils import extract_course_info_from_path as extract_course_info
from src.content_processing.labs import find_stub_labs, generate_lab_content, parse_module

DEFAULT_BASE = Path(__file__).resolve().parent.parent.parent / "course_development"


def parse_args(argv=None):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Regenerate stub lab.md files")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--base", type=Path, default=DEFAULT_BASE,
                        help="Base course_development directory")
    parser.add_argument("--course", choices=list(COURSE_REGISTRY.keys()),
                        help="Process only this course")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    base = args.base
    stubs = find_stub_labs(base)
    print(f"Found {len(stubs)} stub labs to fix\n")

    fixed = 0
    skipped = 0
    errors = 0

    for lab_path in stubs:
        module_dir = lab_path.parent
        course_info = extract_course_info(lab_path, base)

        # Filter by --course if given
        if args.course and course_info["course"] != args.course:
            continue

        try:
            module_data = parse_module(module_dir)
            if not module_data:
                print(f"  SKIP (no module.md): {lab_path.relative_to(base)}")
                skipped += 1
                continue

            concepts = module_data.get("key_concepts", [])
            objectives = module_data.get("objectives", [])

            if not concepts and not objectives:
                print(f"  SKIP (no concepts/objectives): {lab_path.relative_to(base)}")
                skipped += 1
                continue

            lab_text = generate_lab_content(module_data, course_info)

            if args.dry_run:
                n_concepts = len(concepts)
                n_obj = len(objectives)
                print(f"  Would fix: {lab_path.relative_to(base)} ({n_concepts} concepts, {n_obj} objectives)")
            else:
                lab_path.write_text(lab_text, encoding="utf-8")
                print(f"  Fixed: {lab_path.relative_to(base)} ({len(concepts)} concepts, {len(objectives)} objectives)")
            fixed += 1

        except Exception as e:
            print(f"  ERROR: {lab_path.relative_to(base)}: {e}")
            errors += 1

    print(f"\nDone: {fixed} fixed, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
