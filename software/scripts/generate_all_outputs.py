#!/usr/bin/env python3
"""Comprehensive script to generate all outputs for all modules and courses.

Usage:
    uv run python scripts/generate_all_outputs.py [OPTIONS]

Options:
    --course COURSE    Course to process (e.g., ai-philosophy, ai-math, or all)
    --module MODULE    Specific module number to process (default: all)
    --formats FORMATS  Comma-separated list of formats: pdf,mp3,docx,html,txt,md (default: all)
    --dry-run          Show what would be generated without actually generating
    --skip-clear       Skip clearing existing outputs before generation
    --no-website       Skip website generation
    --skip-labs        Skip lab manual rendering
    --help             Show this help message

Examples:
    uv run python scripts/generate_all_outputs.py
    uv run python scripts/generate_all_outputs.py --course ai-philosophy
    uv run python scripts/generate_all_outputs.py --course ai-math --formats txt,md
    uv run python scripts/generate_all_outputs.py --course ai-philosophy --module 1
    uv run python scripts/generate_all_outputs.py --dry-run
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.batch_processing.config import COURSE_REGISTRY, AVAILABLE_FORMATS
from src.batch_processing.logging_config import setup_logging
from src.batch_processing.main import (
    clear_all_outputs,
    process_course_labs,
    process_course_modules,
    process_course_practice_tests,
    process_course_syllabus,
)
from src.batch_processing.utils import (
    generate_dry_run_report,
    get_courses_to_process,
    get_formats_to_process,
)

logger = setup_logging()


def parse_args(argv=None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate all outputs for course modules and syllabi.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--course", choices=list(COURSE_REGISTRY.keys()) + ["all"], default="all")
    parser.add_argument("--module", type=int)
    parser.add_argument("--formats", type=str, default="all")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-clear", action="store_true")
    parser.add_argument("--no-website", action="store_true")
    parser.add_argument("--skip-labs", action="store_true")
    parser.add_argument("--max-module", type=str, action="append", default=[],
                        help="Max module per course (course:number, e.g., ai-math:6)")
    parser.add_argument("--max-lab", type=str, action="append", default=[],
                        help="Max lab per course (course:number, e.g., ai-math:5)")
    return parser.parse_args(argv)


def parse_limits(limit_args: list) -> dict:
    """Parse course:number limits into {course: number} dict."""
    limits = {}
    for limit in limit_args:
        if ":" in limit:
            course, num = limit.split(":", 1)
            try:
                limits[course] = int(num)
            except ValueError:
                logger.warning(f"Invalid limit format: {limit}")
    return limits


def main(argv=None) -> int:
    """Generate all outputs for all courses."""
    args = parse_args(argv)
    start_time = time.time()
    repo_root = Path(__file__).parent.parent.parent

    courses = get_courses_to_process(args.course)
    formats = get_formats_to_process(args.formats)

    logger.info("=" * 60)
    logger.info("Starting comprehensive output generation")
    logger.info(f"Courses: {', '.join(c[1] for c in courses)} | Formats: {', '.join(formats)}")
    # Parse module/lab limits
    max_module_limits = parse_limits(args.max_module)
    max_lab_limits = parse_limits(args.max_lab)

    if args.module:
        logger.info(f"Module filter: module-{args.module}")

    if args.dry_run:
        logger.info("DRY RUN MODE - Checking what would be generated")
        changes = generate_dry_run_report(
            repo_root,
            courses,
            formats,
            module_filter=args.module,
            generate_website=not args.no_website,
            skip_labs=args.skip_labs
        )
        print(changes)
        return 0

    # Execute generation
    if not args.skip_clear:
        clear_all_outputs(repo_root)

    # Track overall success
    success = True

    for course_rel_path, course_name, course_id in courses:
        course_path = repo_root / course_rel_path
        logger.info(f"\n=== Processing Course: {course_name} ===")

        try:
            # Process Modules
            logger.info(f"--- Processing Modules for {course_name} ---")
            process_course_modules(
                course_path,
                course_name,
                module_filter=args.module,
                generate_website=not args.no_website,
                formats=formats,
                max_module=max_module_limits.get(course_id) if course_id else None
            )

            # Process Labs
            if not args.skip_labs and not args.module:
                 logger.info(f"--- Processing Labs for {course_name} ---")
                 process_course_labs(
                     course_path,
                     course_name,
                     formats=formats,
                     max_lab=max_lab_limits.get(course_id) if course_id else None,
                     course_id=course_id
                 )

            # Process Syllabus (only if not filtering by module)
            if not args.module:
                logger.info(f"--- Processing Syllabus for {course_name} ---")
                process_course_syllabus(
                    course_path, 
                    course_name, 
                    formats=formats,
                    course_id=course_id
                )
                
            # Process Practice Tests
            if not args.module:
                logger.info(f"--- Processing Practice Tests for {course_name} ---")
                process_course_practice_tests(course_path, course_name, formats=formats)

        except Exception as e:
            logger.error(f"Failed to process course {course_name}: {e}", exc_info=True)
            success = False

    duration = time.time() - start_time
    logger.info("=" * 60)
    logger.info(f"Generation completed in {duration:.1f}s")
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
