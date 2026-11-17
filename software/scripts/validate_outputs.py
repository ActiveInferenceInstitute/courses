#!/usr/bin/env python3
"""Script to validate course outputs.

Usage:
    uv run python scripts/validate_outputs.py --course {ai-philosophy|ai-math|all}
    uv run python scripts/validate_outputs.py --course all --formats pdf,docx,md

Options:
    --course    Course to validate (ai-philosophy, ai-math, or all)
    --formats   Comma-separated list of formats to validate (default: pdf,docx)
                Only validates that these formats exist, ignoring others.
    --json      Output results as JSON
    --verbose   Show detailed module-level results
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import List, Optional

# Add software directory to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(software_dir))

from src.batch_processing.config import COURSE_REGISTRY  # noqa: E402

from src.batch_processing.utils import (  # noqa: E402
    get_courses_to_process, get_formats_to_process, parse_limits, plan_generation,
)
from src.validation.main import validate_plan  # noqa: E402
from src.validation.config import DEFAULT_REQUIRED_FORMATS  # noqa: E402

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def parse_formats(formats_str: Optional[str]) -> Optional[List[str]]:
    return None if formats_str is None else get_formats_to_process(formats_str)


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate course outputs.")
    parser.add_argument(
        "--course",
        type=str,
        choices=list(COURSE_REGISTRY.keys()) + ["all"],
        required=True,
        help="Course to validate",
    )
    parser.add_argument(
        "--formats",
        type=str,
        help=f"Comma-separated list of formats (default: {','.join(DEFAULT_REQUIRED_FORMATS)})",
    )
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--verbose", action="store_true", help="Show detailed module-level results")
    parser.add_argument("--repo-root", type=Path, default=software_dir.parent)
    parser.add_argument("--module", type=int)
    parser.add_argument("--unit")
    parser.add_argument("--max-module", action="append", default=[])
    parser.add_argument("--max-lab", action="append", default=[])
    parser.add_argument("--no-website", action="store_true")
    parser.add_argument("--skip-labs", action="store_true")

    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        active = parse_formats(args.formats)
        plans = plan_generation(
            args.repo_root, get_courses_to_process(args.course),
            DEFAULT_REQUIRED_FORMATS if active is None else active,
            module_filter=args.module, unit_filter=args.unit,
            max_modules=parse_limits(args.max_module), max_labs=parse_limits(args.max_lab),
            generate_website=not args.no_website, skip_labs=args.skip_labs,
        )
        results = [validate_plan(plan) for plan in plans]
    except (ValueError, OSError) as error:
        results = [{"course": args.course, "valid": False, "issues": [str(error)]}]
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for result in results:
            print(f"{result['course']}: {'valid' if result['valid'] else 'FAILED'}")
            for issue in result["issues"]:
                print(f"  {issue}")
    return 0 if all(result["valid"] for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())
