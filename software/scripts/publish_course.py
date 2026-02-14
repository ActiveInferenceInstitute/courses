#!/usr/bin/env python3
"""Script to publish course materials."""

import argparse
import sys
import logging
from pathlib import Path

# Add software directory to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(software_dir))

from src.batch_processing.config import COURSE_REGISTRY
from src.publish.main import publish_course

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish course materials.")
    parser.add_argument(
        "--course", 
        type=str, 
        choices=list(COURSE_REGISTRY.keys()) + ["all"],
        required=True, 
        help="Course to publish"
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    
    repo_root = software_dir.parent
    
    courses_to_process = []
    if args.course == "all":
        courses_to_process = list(COURSE_REGISTRY.keys())
    else:
        courses_to_process = [args.course]
        
    for course_name in courses_to_process:
        if course_name not in COURSE_REGISTRY:
            logger.error(f"Course not found in registry: {course_name}")
            continue

        rel_path = COURSE_REGISTRY[course_name]["rel_path"]
        course_path = repo_root / rel_path
            
        if not course_path.exists():
            logger.error(f"Course directory not found: {course_path}")
            continue
            
        try:
            results = publish_course(str(course_path))
            
            logger.info("=" * 60)
            logger.info(f"Publishing Results for {results['course']}")
            logger.info("=" * 60)
            logger.info(f"Modules processed: {results['modules_published']}")
            logger.info(f"Syllabus files: {results['syllabus_files']}")
            logger.info(f"Total files published: {results['total_files']}")
            
            if results["modules"]:
                logger.info("\nModule Details:")
                for mod in results["modules"]:
                    logger.info(f"  - {mod['name']}: {mod['files']} files")
            
        except Exception as e:
            logger.error(f"Failed to publish {course_name}: {e}")
            return 1
            
    return 0


if __name__ == "__main__":
    main()
