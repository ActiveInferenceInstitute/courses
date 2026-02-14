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

from src.batch_processing.config import COURSE_REGISTRY

from src.validation import (
    generate_validation_report,
    get_output_summary,
    validate_outputs,
    validate_published,
)
from src.validation.config import DEFAULT_REQUIRED_FORMATS, ALL_SUPPORTED_FORMATS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def parse_formats(formats_str: Optional[str]) -> Optional[List[str]]:
    """Parse comma-separated formats string into list."""
    if not formats_str:
        return None
    formats = [f.strip().lower() for f in formats_str.split(',')]
    
    # Validate formats
    invalid = [f for f in formats if f not in ALL_SUPPORTED_FORMATS]
    if invalid:
        logger.warning(f"Ignoring unsupported formats: {invalid}")
        return [f for f in formats if f in ALL_SUPPORTED_FORMATS]
    
    return formats


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate course outputs.")
    parser.add_argument(
        "--course",
        type=str,
        choices=list(COURSE_REGISTRY.keys()) + ["all"],
        required=True,
        help="Course to validate"
    )
    parser.add_argument(
        "--formats",
        type=str,
        help=f"Comma-separated list of formats (default: {','.join(DEFAULT_REQUIRED_FORMATS)})"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed module-level results"
    )
    
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    
    repo_root = software_dir.parent
    
    # Determine courses to validate
    courses_to_validate = []
    if args.course == "all":
        courses_to_validate = list(COURSE_REGISTRY.keys())
    else:
        courses_to_validate = [args.course]
        
    # Parse output formats
    required_formats = parse_formats(args.formats)
    if not required_formats:
        required_formats = DEFAULT_REQUIRED_FORMATS
        
    logger.info(f"Validating courses: {courses_to_validate}")
    logger.info(f"Checking formats: {required_formats}")
    
    # Run validation for each course
    all_results = []
    any_failed = False
    
    for course_name in courses_to_validate:
        course_path = repo_root / "course_development" / course_name
        if not course_path.exists():
            logger.error(f"Course path not found: {course_path}")
            any_failed = True
            continue
            
        results = validate_outputs(
            str(course_path),
            formats=required_formats
        )
        all_results.append(results)
        
        if not results["valid"]:
            any_failed = True
            
        # Check if labs have issues
        if results.get("issues"):
            any_failed = True
    
    # Generate report/summary
    if args.json:
        print(json.dumps(all_results, indent=2))
    else:
        for results in all_results:
            print(f"\nValidation for {results['course']}:")
            print(f"  Valid: {results['valid']}")
            print(f"  Modules Checked: {results['modules_checked']}")
            print(f"  Modules Valid: {results['modules_valid']}")
            if results.get("issues"):
                print("  Issues:")
                for issue in results["issues"]:
                    print(f"    - {issue}")
    
    # Exit with error if any validation failed
    if any_failed:
        return 1
        
    return 0


if __name__ == "__main__":
    main()
