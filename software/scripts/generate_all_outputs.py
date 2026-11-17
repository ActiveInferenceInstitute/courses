#!/usr/bin/env python3
"""Generate only admitted course/unit/module artifacts; preview never mutates."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.main import clear_all_outputs, generate_selected_outputs
from src.batch_processing.utils import (
    describe_generation,
    get_courses_to_process,
    get_formats_to_process,
    parse_limits,
    plan_generation,
)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course", choices=[*COURSE_REGISTRY, "all"], default="all")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument(
        "--unit", help="Exact unit directory name; required for ambiguous numeric module selectors"
    )
    parser.add_argument("--module", type=int)
    parser.add_argument("--formats", default="all")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-clear", action="store_true")
    parser.add_argument("--no-website", action="store_true")
    parser.add_argument("--skip-labs", action="store_true")
    parser.add_argument("--max-module", action="append", default=[])
    parser.add_argument("--max-lab", action="append", default=[])
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        plans = plan_generation(
            args.repo_root,
            get_courses_to_process(args.course),
            get_formats_to_process(args.formats),
            module_filter=args.module,
            unit_filter=args.unit,
            generate_website=not args.no_website,
            skip_labs=args.skip_labs,
            max_modules=parse_limits(args.max_module),
            max_labs=parse_limits(args.max_lab),
        )
        if args.dry_run:
            print(describe_generation(plans))
            return 0
        if not args.skip_clear:
            cleared = clear_all_outputs(args.repo_root, plans=plans)
            if cleared["errors"]:
                for error in cleared["errors"]:
                    print(error, file=sys.stderr)
                return 1
        result = generate_selected_outputs(plans)
        for error in result["errors"]:
            print(error, file=sys.stderr)
        return 1 if result["errors"] else 0
    except (ValueError, OSError) as error:
        print(f"Generation rejected: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
