#!/usr/bin/env python3
"""
Publish All Courses - Complete Pipeline

Thin orchestrator - delegates to src.publish and src.batch_processing modules.

This script orchestrates the full course publishing workflow:
1. Generate all outputs (PDF, DOCX, HTML, TXT, MP3) for all courses
2. Publish outputs to PUBLISHED/ directory
3. Copy labs and dashboards
4. Flatten module structure (remove subfolders)
5. Run validation

Usage:
    uv run python scripts/publish_all.py [--clean] [--skip-generation] [--verbose]
"""

import argparse
import logging
import sys
from pathlib import Path

# Add software directory to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(software_dir))

from src.batch_processing.config import COURSE_REGISTRY  # noqa: E402
from src.batch_processing.main import clear_all_outputs, generate_selected_outputs  # noqa: E402
from src.batch_processing.utils import (  # noqa: E402
    describe_generation, get_courses_to_process, get_formats_to_process,
    parse_limits, plan_generation,
)
from src.publish.main import publish_course  # noqa: E402
from src.publish.config import PUBLISH_ROOT_NAME  # noqa: E402
from src.validation.main import validate_plan  # noqa: E402
from src.publish.utils import (  # noqa: E402
    copy_labs_and_dashboards,
    copy_practice_tests,
    copy_slides,
    copy_slides_to_modules,
    flatten_published,
    reorganize_to_categories,
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)






def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish all courses - Complete pipeline")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--course", choices=[*COURSE_REGISTRY, "all"], default="all")
    parser.add_argument("--module", type=int)
    parser.add_argument("--unit")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-website", action="store_true")
    parser.add_argument("--skip-clear", action="store_true")
    parser.add_argument(
        "--clean", action="store_true", help="Clean PUBLISHED directory before starting"
    )
    parser.add_argument(
        "--skip-generation",
        action="store_true",
        help="Skip output generation (use existing outputs)",
    )
    parser.add_argument(
        "--skip-mp3", action="store_true", help="Skip MP3 audio generation (faster iteration)"
    )
    parser.add_argument(
        "--formats",
        type=str,
        default="all",
        help="Comma-separated formats: pdf,mp3,docx,html,txt (default: all)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show detailed output from subscripts"
    )
    parser.add_argument(
        "--skip-publish", action="store_true", help="Skip publishing to PUBLISHED/ directory"
    )
    parser.add_argument(
        "--skip-copy-extras", action="store_true", help="Skip copying labs and dashboards"
    )
    parser.add_argument(
        "--skip-flatten", action="store_true", help="Skip flattening module structure"
    )
    parser.add_argument("--skip-validate", action="store_true", help="Skip output validation")
    parser.add_argument(
        "--skip-labs", action="store_true", help="Skip lab manual rendering during generation"
    )
    parser.add_argument(
        "--clean-source-outputs",
        action="store_true",
        help="Clean source output/ directories before generation",
    )
    parser.add_argument(
        "--max-module",
        type=str,
        action="append",
        default=[],
        help="Max module per course (format: course:number, e.g., biol-8:6)",
    )
    parser.add_argument(
        "--max-lab",
        type=str,
        action="append",
        default=[],
        help="Max lab per course (format: course:number, e.g., biol-8:5)",
    )

    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    root = args.repo_root
    published = root / PUBLISH_ROOT_NAME
    try:
        formats = get_formats_to_process(args.formats)
        if args.skip_mp3:
            formats = [fmt for fmt in formats if fmt != "mp3"]
        plans = plan_generation(
            root, get_courses_to_process(args.course), formats,
            module_filter=args.module, unit_filter=args.unit,
            max_modules=parse_limits(args.max_module), max_labs=parse_limits(args.max_lab),
            skip_labs=args.skip_labs, generate_website=not args.no_website,
        )
        if args.skip_generation and args.clean_source_outputs:
            raise ValueError("--clean-source-outputs requires generation")
        if args.dry_run:
            print(describe_generation(plans))
            return 0
        if not args.skip_generation:
            if not args.skip_clear:
                clearing = clear_all_outputs(root, plans=plans)
                if clearing["errors"]:
                    raise OSError("\n".join(clearing["errors"]))
            generated = generate_selected_outputs(plans)
            if generated["errors"]:
                raise OSError("\n".join(generated["errors"]))
        if not args.skip_validate:
            issues = [issue for plan in plans for issue in validate_plan(plan)["issues"]]
            if issues:
                raise ValueError("\n".join(issues))
        if not args.skip_publish:
            for plan in plans:
                result = publish_course(
                    str(plan["path"]), str(published), course_id=plan["course_id"],
                    plan=plan, clean=args.clean and not args.skip_clear,
                )
                if result["errors"]:
                    raise OSError("\n".join(result["errors"]))
            courses = [plan["course_id"] for plan in plans]
            selected = {plan["course_id"]: plan["modules"] for plan in plans}
            if not args.skip_copy_extras:
                copy_labs_and_dashboards(root, courses, args.verbose, plans=plans,
                                         skip_labs=args.skip_labs)
                if "pdf" in formats:
                    copy_slides_to_modules(root, courses, args.verbose, selected_modules=selected)
                if args.module is None and args.unit is None and not args.max_module and not args.max_lab:
                    if "pdf" in formats:
                        copy_slides(root, courses, args.verbose)
                    copy_practice_tests(root, courses, args.verbose, formats=formats)
            if not args.skip_flatten:
                modules = [
                    published / plan["course_id"] / module.relative_to(plan["path"])
                    for plan in plans for module in plan["modules"]
                ]
                flatten_published(published, modules=modules)
                reorganize_to_categories(published, courses, modules=modules)
        return 0
    except (OSError, ValueError) as error:
        logger.error("Publication failed: %s", error)
        return 1


if __name__ == "__main__":
    sys.exit(main())
