#!/usr/bin/env python3
"""Script to publish course materials."""

import argparse
import sys
import logging
from pathlib import Path

# Add software directory to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(software_dir))

from src.batch_processing.config import COURSE_REGISTRY  # noqa: E402
from src.publish.main import publish_course  # noqa: E402
from src.batch_processing.utils import (  # noqa: E402
    get_courses_to_process, get_formats_to_process, parse_limits, plan_generation,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish course materials.")
    parser.add_argument(
        "--course",
        type=str,
        choices=list(COURSE_REGISTRY.keys()) + ["all"],
        required=True,
        help="Course to publish",
    )
    parser.add_argument("--repo-root", type=Path, default=software_dir.parent)
    parser.add_argument("--module", type=int)
    parser.add_argument("--unit")
    parser.add_argument("--formats", default="all")
    parser.add_argument("--no-website", action="store_true")
    parser.add_argument("--skip-labs", action="store_true")
    parser.add_argument("--max-module", action="append", default=[])
    parser.add_argument("--max-lab", action="append", default=[])
    parser.add_argument("--clean", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        plans = plan_generation(
            args.repo_root, get_courses_to_process(args.course), get_formats_to_process(args.formats),
            module_filter=args.module, unit_filter=args.unit,
            generate_website=not args.no_website, skip_labs=args.skip_labs,
            max_modules=parse_limits(args.max_module), max_labs=parse_limits(args.max_lab),
        )
        if args.dry_run:
            for plan in plans:
                print(f"Would publish {plan['course_id']}: {len(plan['artifacts'])} artifacts")
            return 0
        errors = []
        for plan in plans:
            result = publish_course(
                str(plan["path"]), str(args.repo_root / "published"),
                course_id=plan["course_id"], plan=plan, clean=args.clean,
            )
            errors.extend(result["errors"])
        for error in errors:
            logger.error(error)
        return 1 if errors else 0
    except (ValueError, OSError) as error:
        logger.error("Publication rejected: %s", error)
        return 1


if __name__ == "__main__":
    sys.exit(main())
