"""Main logic for the publish module."""

from pathlib import Path
from typing import Dict, Any, List
import logging

from . import config
from .utils import get_course_config, clean_directory, copy_directory_contents

logger = logging.getLogger(__name__)


def publish_course(course_path: str, publish_root: str = None) -> Dict[str, Any]:
    """Publish course materials to the published directory.

    Args:
        course_path: Path to the course directory (e.g., 'biol-1')
        publish_root: Root directory for publishing (default: PUBLISHED in repo root)

    Returns:
        Dictionary with publishing results
    """
    course_dir = Path(course_path).resolve()
    course_name = course_dir.name
    
    if publish_root:
        out_root = Path(publish_root)
    else:
        # Default to repo root / PUBLISHED
        # Assuming software/src/publish/main.py -> repo_root is ../../../
        # BUT if course_path is under course_development, we need to go up appropriately
        # Safer way: get repo root relative to this file
        repo_root = Path(__file__).resolve().parent.parent.parent.parent
        out_root = repo_root / config.PUBLISH_ROOT_NAME

    published_course_dir = out_root / course_name
    
    logger.info(f"Publishing {course_name} to {published_course_dir}")
    
    # Get configuration
    course_conf = get_course_config(course_name)
    module_src_name = course_conf["module_source_dir"]
    syllabus_src_name = course_conf["syllabus_source_dir"]
    
    results = {
        "course": course_name,
        "modules_published": 0,
        "syllabus_files": 0,
        "total_files": 0,
        "modules": [],
        "errors": []
    }
    
    # Clean/Create destination
    if not published_course_dir.exists():
        published_course_dir.mkdir(parents=True)
    
    # 1. Publish Modules
    modules_dir = course_dir / "course"
    if modules_dir.exists():
        for module_path in sorted(modules_dir.glob("module-*")):
            if not module_path.is_dir():
                continue
                
            module_name = module_path.name
            source_path = module_path / module_src_name
            
            if not source_path.exists():
                logger.warning(f"Source directory not found for {module_name}: {source_path}")
                continue
                
            dest_path = published_course_dir / module_name
            
            # Clean destination module dir before copying to ensure fresh state
            clean_directory(dest_path)
            
            # Primary Source
            files_copied = 0
            if source_path.exists():
                files_copied += copy_directory_contents(source_path, dest_path)
            else:
                logger.warning(f"Source directory not found for {module_name}: {source_path}")

            # Additional Sources (e.g., slides)
            for extra_src in course_conf.get("additional_module_dirs", []):
                 extra_path = module_path / extra_src
                 if extra_path.exists():
                     logger.info(f"Publishing additional content from {extra_src} for {module_name}")
                     files_copied += copy_directory_contents(extra_path, dest_path / extra_src)
            
            if files_copied > 0:
                results["modules_published"] += 1
                results["total_files"] += files_copied
                results["modules"].append({
                    "name": module_name,
                    "files": files_copied
                })
                logger.info(f"Published {module_name}: {files_copied} files")
            else:
                logger.warning(f"No files found to publish in {module_name}")

    # 2. Publish Syllabus
    if course_conf.get("include_syllabus"):
        syllabus_path = course_dir / "syllabus"
        if syllabus_path.exists():
            source_path = syllabus_path / syllabus_src_name
            
            if source_path.exists():
                dest_path = published_course_dir / "syllabus"
                clean_directory(dest_path)
                
                files_copied = copy_directory_contents(source_path, dest_path)
                
                results["syllabus_files"] = files_copied
                results["total_files"] += files_copied
                logger.info(f"Published syllabus: {files_copied} files")
            else:
                logger.warning(f"Syllabus output directory not found: {source_path}")
        else:
            logger.warning(f"Syllabus directory not found: {syllabus_path}")

    return results
