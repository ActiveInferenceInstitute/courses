#!/usr/bin/env python3
"""Render one explicitly selected module, rejecting ambiguous numeric identities."""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.main import process_module_website
from src.batch_processing.utils import get_formats_to_process, select_modules


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course", choices=list(COURSE_REGISTRY), required=True)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--module", type=int, default=1)
    parser.add_argument("--unit")
    parser.add_argument("--formats", default="all")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        get_formats_to_process(args.formats)
        course = args.repo_root / COURSE_REGISTRY[args.course]["rel_path"]
        module = select_modules(course, args.course, args.module, args.unit)[0]
        process_module_website(str(module))
        return 0
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
