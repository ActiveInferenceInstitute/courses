"""Main logic for the publish module.

Module discovery is driven by COURSE_REGISTRY metadata (batch_processing.config).
This eliminates the legacy hardcoded ``course/module-*`` glob pattern and supports
all three course layouts:

  - Legacy biology courses   : course/module-*/  (has_course_subdir=True, module-* glob)
  - Active Inference flat    : XX_topic/          (has_course_subdir=False, [0-9][0-9]_*)
  - Level-adapted / domain   : unit/XX_topic/     (unit_glob present, two-level discovery)
"""

from pathlib import Path
from typing import Dict, Any, List, Optional
import logging

from . import config
from .utils import get_course_config, clean_directory, copy_directory_contents
from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.utils import find_modules_for_course

logger = logging.getLogger(__name__)


def _get_registry_entry(course_name: str) -> Optional[Dict[str, Any]]:
    """Return COURSE_REGISTRY entry for *course_name*, or None if not found.

    Tries an exact key match first, then falls back to matching by path suffix
    so that callers can pass either a registry ID or a bare directory name.
    """
    if course_name in COURSE_REGISTRY:
        return COURSE_REGISTRY[course_name]
    # Fuzzy: match courses whose rel_path ends with the given name
    for reg in COURSE_REGISTRY.values():
        if reg["rel_path"].endswith(course_name):
            return reg
    return None


def publish_course(course_path: str, publish_root: str = None) -> Dict[str, Any]:
    """Publish course materials to the published directory.

    Uses COURSE_REGISTRY-aware module discovery via
    ``batch_processing.utils.find_modules_for_course`` instead of the legacy
    hardcoded ``course/module-*`` glob pattern.

    Args:
        course_path: Path to the course directory (e.g., 'biol-1' or an abs path).
        publish_root: Root directory for publishing (default: PUBLISHED in repo root).

    Returns:
        Dictionary with publishing results::

            {
                "course":             str,   # course directory name
                "modules_published":  int,
                "syllabus_files":     int,
                "total_files":        int,
                "modules":            list[{"name": str, "files": int}],
                "errors":             list[str],
            }
    """
    course_dir = Path(course_path).resolve()
    course_name = course_dir.name

    if publish_root:
        out_root = Path(publish_root)
    else:
        # Repo root is four levels up from software/src/publish/main.py
        repo_root = Path(__file__).resolve().parent.parent.parent.parent
        out_root = repo_root / config.PUBLISH_ROOT_NAME

    published_course_dir = out_root / course_name

    logger.info(f"Publishing {course_name} to {published_course_dir}")

    # ------------------------------------------------------------------
    # Resolve publish-time config (COURSE_CONFIGS → DEFAULT_CONFIG)
    # ------------------------------------------------------------------
    course_conf = get_course_config(course_name)
    module_src_name = course_conf["module_source_dir"]
    syllabus_src_name = course_conf["syllabus_source_dir"]

    results: Dict[str, Any] = {
        "course": course_name,
        "modules_published": 0,
        "syllabus_files": 0,
        "total_files": 0,
        "modules": [],
        "errors": [],
    }

    # Ensure destination root exists
    published_course_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # 1. Module discovery via COURSE_REGISTRY
    # ------------------------------------------------------------------
    # find_modules_for_course accepts either an abs path (preferred) or a
    # registry ID.  We pass the abs path; it will auto-match the registry.
    modules: List[Path] = find_modules_for_course(course_dir, course_name)

    if not modules:
        logger.warning(
            f"No modules discovered for {course_name} at {course_dir}. "
            "Check COURSE_REGISTRY or that the course directory exists."
        )

    for module_path in modules:
        module_name = module_path.name
        source_path = module_path / module_src_name

        if not source_path.exists():
            logger.warning(f"Rendered output directory not found for {module_name}: {source_path}")
            continue

        dest_path = published_course_dir / module_name

        # Clean destination to ensure fresh state
        clean_directory(dest_path)

        files_copied = copy_directory_contents(source_path, dest_path)

        # Additional sources (e.g. slides)
        for extra_src in course_conf.get("additional_module_dirs", []):
            extra_path = module_path / extra_src
            if extra_path.exists():
                logger.info(f"Publishing additional content from {extra_src} for {module_name}")
                files_copied += copy_directory_contents(extra_path, dest_path / extra_src)

        if files_copied > 0:
            results["modules_published"] += 1
            results["total_files"] += files_copied
            results["modules"].append({"name": module_name, "files": files_copied})
            logger.info(f"Published {module_name}: {files_copied} files")
        else:
            logger.warning(f"No files found to publish in {module_name}")

    # ------------------------------------------------------------------
    # 2. Syllabus publishing
    # ------------------------------------------------------------------
    if course_conf.get("include_syllabus"):
        # Prefer the registry's syllabus_location, fall back to "syllabus/"
        reg_entry = _get_registry_entry(course_name)
        syllabus_location = (
            reg_entry.get("syllabus_location", "syllabus") if reg_entry else "syllabus"
        )
        syllabus_path = course_dir / syllabus_location

        if syllabus_path.is_dir():
            # Directory-style syllabus (legacy biology: syllabus/output/)
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
        elif syllabus_path.is_file():
            # Single-file syllabus (Active Inference style: syllabus.md)
            dest_path = published_course_dir / syllabus_path.name
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            import shutil

            shutil.copy2(syllabus_path, dest_path)
            results["syllabus_files"] = 1
            results["total_files"] += 1
            logger.info(f"Published syllabus file: {syllabus_path.name}")
        else:
            logger.warning(f"Syllabus not found at expected location: {syllabus_path}")

    return results
