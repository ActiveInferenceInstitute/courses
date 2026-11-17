"""Main validation functions for course outputs.

This module provides comprehensive validation and logging for course output
generation and publishing.
"""

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import config
from .config import DEFAULT_REQUIRED_FORMATS
from .utils import (
    count_files_by_extension,
    format_file_counts,
    get_module_directories,
    get_timestamp,
)
from ..batch_processing.config import COURSE_REGISTRY
from ..batch_processing.utils import (
    get_courses_to_process,
    get_formats_to_process,
    plan_course,
)

logger = logging.getLogger(__name__)




def validate_outputs(
    course_path: str,
    formats: Optional[List[str]] = None,
    max_module: Optional[int] = None,
    max_lab: Optional[int] = None,
    *,
    course_id: Optional[str] = None,
    module_filter: Optional[int] = None,
    unit_filter: Optional[str] = None,
    generate_website: Optional[bool] = None,
    skip_labs: bool = False,
) -> Dict[str, Any]:
    """Validate exactly the artifacts admitted by the generation producer."""
    course_dir = Path(course_path)
    active = DEFAULT_REQUIRED_FORMATS if formats is None else formats
    try:
        active = get_formats_to_process(",".join(active))
        plan = plan_course(
            course_dir, course_id or course_dir.name, active, course_id=course_id,
            module_filter=module_filter, unit_filter=unit_filter,
            max_module=max_module, max_lab=max_lab, skip_labs=skip_labs,
            generate_website=("html" in active if generate_website is None else generate_website),
        )
        return validate_plan(plan)
    except (ValueError, OSError) as error:
        return {
            "valid": False, "course": course_id or course_dir.name,
            "formats_validated": active, "timestamp": get_timestamp(),
            "modules_checked": 0, "modules_valid": 0, "modules": [],
            "syllabus_valid": False, "issues": [str(error)],
        }


def _missing_artifacts(artifacts: List[dict]) -> List[str]:
    missing = []
    for artifact in artifacts:
        path = artifact["destination"]
        if not path.is_file() or path.stat().st_size == 0:
            missing.append(str(path))
    return missing


def validate_plan(plan: dict) -> Dict[str, Any]:
    """Consume an already admitted generation manifest without inventing inputs."""
    artifacts = plan["artifacts"]
    missing = _missing_artifacts(artifacts)
    modules = []
    for module in plan["modules"]:
        expected = [a for a in artifacts if a.get("module") == module]
        absent = _missing_artifacts(expected)
        modules.append({
            "name": module.relative_to(plan["path"]).as_posix(),
            "valid": not absent, "missing_files": absent,
        })
    syllabus = [a for a in artifacts if a["kind"] == "syllabus"]
    labs = [a for a in artifacts if a["kind"] == "lab"]
    return {
        "valid": not missing, "course": plan["course_id"] or plan["course"],
        "formats_validated": plan["formats"], "timestamp": get_timestamp(),
        "modules_checked": len(modules), "modules_valid": sum(m["valid"] for m in modules),
        "modules": modules, "syllabus_valid": not _missing_artifacts(syllabus),
        "labs": {"source_labs": len({a["source"] for a in labs}),
                 "missing_outputs": _missing_artifacts(labs), "issues": []},
        "issues": [f"Missing or empty required artifact: {path}" for path in missing],
    }






def validate_published(
    published_path: str, courses: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Validate that published directory has expected structure.

    Args:
        published_path: Path to PUBLISHED directory

    Returns:
        Dictionary with validation results
    """
    pub_dir = Path(published_path).resolve()

    logger.info(f"Validating published directory: {pub_dir}")

    results: Dict[str, Any] = {
        "valid": True,
        "path": str(pub_dir),
        "timestamp": get_timestamp(),
        "courses": {},
        "total_files": 0,
        "issues": [],
    }

    if not pub_dir.exists():
        results["valid"] = False
        results["issues"].append("Published directory does not exist")
        return results

    selected = [entry[2] for entry in get_courses_to_process("all")] if courses is None else courses
    for course_name in selected:
        if course_name not in COURSE_REGISTRY:
            results["issues"].append(f"Unknown course: {course_name}")
            results["valid"] = False
            continue
        course_dir = pub_dir / course_name

        if not course_dir.exists():
            results["issues"].append(f"Course {course_name} not found in published")
            results["valid"] = False
            continue

        # Count files by type
        file_counts = count_files_by_extension(course_dir)
        total = sum(file_counts.values())

        results["courses"][course_name] = {
            "files_by_type": file_counts,
            "total_files": total,
            "modules": [],
        }
        results["total_files"] += total

        from ..batch_processing.utils import find_modules_for_course

        modules = find_modules_for_course(course_dir, course_name)
        if not modules:
            results["valid"] = False
            results["issues"].append(f"Course {course_name} has no published modules")
        for module_dir in modules:
            mod_counts = count_files_by_extension(module_dir)
            payloads = [
                path for path in module_dir.rglob("*")
                if path.is_file() and path.name not in ("README.md", "AGENTS.md")
                and not any(part.startswith(".") for part in path.relative_to(module_dir).parts)
            ]
            if not payloads or any(path.stat().st_size == 0 for path in payloads):
                results["valid"] = False
                results["issues"].append(
                    f"Missing or empty published payload: {course_name}/{module_dir.relative_to(course_dir)}"
                )
            results["courses"][course_name]["modules"].append({
                "name": module_dir.relative_to(course_dir).as_posix(),
                "files": sum(mod_counts.values()),
            })

    logger.info(f"Published validation complete: {results['total_files']} total files")

    return results


def generate_validation_report(
    course_name: str,
    repo_root: Optional[str] = None,
    formats: Optional[List[str]] = None,
    max_module: Optional[int] = None,
    max_lab: Optional[int] = None,
) -> Dict[str, Any]:
    """Generate comprehensive validation report for a course.

    Args:
        course_name: Name of course (biol-1 or biol-8)
        repo_root: Optional repo root path (auto-detected if not provided)
        formats: Optional list of formats to validate (e.g., ["pdf", "docx", "md"])
        max_module: Optional max module number to validate (e.g., 6 means only validate 1-6)
        max_lab: Optional max lab number to validate (e.g., 4 means only validate labs 1-4)

    Returns:
        Dictionary with complete validation report
    """
    if repo_root:
        root = Path(repo_root)
    else:
        # Auto-detect from this file's location
        root = Path(__file__).resolve().parent.parent.parent.parent

    if course_name not in COURSE_REGISTRY:
        raise ValueError(f"Unknown course: {course_name}")
    course_path = root / COURSE_REGISTRY[course_name]["rel_path"]
    published_path = root / config.PUBLISHED_DIR_NAME

    logger.info(f"Generating validation report for {course_name}")
    if formats:
        logger.info(f"  Validating formats: {', '.join(formats)}")

    report: Dict[str, Any] = {
        "course": course_name,
        "timestamp": get_timestamp(),
        "formats_validated": formats or DEFAULT_REQUIRED_FORMATS,
        "source_validation": {},
        "published_validation": {},
        "summary": {},
    }

    # Validate source outputs (format-aware, with optional limits)
    if course_path.exists():
        report["source_validation"] = validate_outputs(
            str(course_path),
            formats=formats,
            max_module=max_module,
            max_lab=max_lab, course_id=course_name,
        )
    else:
        report["source_validation"] = {
            "valid": False,
            "issues": [f"Course directory not found: {course_path}"],
        }

    # Validate published outputs
    if published_path.exists():
        report["published_validation"] = validate_published(str(published_path), [course_name])
    else:
        report["published_validation"] = {
            "valid": False,
            "issues": ["Published directory not found"],
        }

    # Generate summary
    src = report["source_validation"]
    pub = report["published_validation"]

    report["summary"] = {
        "source_valid": src.get("valid", False),
        "source_modules_valid": f"{src.get('modules_valid', 0)}/{src.get('modules_checked', 0)}",
        "published_valid": pub.get("valid", False),
        "published_files": pub.get("total_files", 0),
    }

    return report


def get_output_summary(course_path: str) -> Dict[str, Any]:
    """Get summary of outputs for a course.

    Args:
        course_path: Path to course directory

    Returns:
        Dictionary with output counts by format and module
    """
    course_dir = Path(course_path).resolve()
    course_name = course_dir.name

    summary: Dict[str, Any] = {
        "course": course_name,
        "timestamp": get_timestamp(),
        "modules": {},
        "totals": {},
        "by_format": {},
    }

    total_by_format: Dict[str, int] = {}

    for module_path in get_module_directories(course_dir):
        module_name = module_path.relative_to(course_dir).as_posix()
        output_dir = module_path / "output"

        if output_dir.exists():
            counts = count_files_by_extension(output_dir)
            summary["modules"][module_name] = counts

            for fmt, count in counts.items():
                total_by_format[fmt] = total_by_format.get(fmt, 0) + count

    summary["by_format"] = total_by_format
    summary["totals"]["modules"] = len(summary["modules"])
    summary["totals"]["files"] = sum(total_by_format.values())

    logger.info(f"Output summary for {course_name}: {format_file_counts(total_by_format)}")

    return summary
