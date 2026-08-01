"""Main validation functions for course outputs.

This module provides comprehensive validation and logging for course output
generation and publishing.
"""

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import config
from .config import (
    get_syllabus_required_formats,
    DEFAULT_REQUIRED_FORMATS,
)
from .utils import (
    check_lab_files,
    check_output_directory,
    check_study_guide_files,
    check_website_files,
    count_files_by_extension,
    format_file_counts,
    get_module_directories,
    get_timestamp,
)

logger = logging.getLogger(__name__)


def _get_module_number(module_name: str) -> int:
    """Extract module number from module directory name.

    Args:
        module_name: Directory name like 'module-01-study-of-life'

    Returns:
        Module number as integer (e.g., 1 for module-01)
    """
    import re

    match = re.match(r"module-(\d+)", module_name)
    if match:
        return int(match.group(1))
    return 0


def validate_outputs(
    course_path: str,
    formats: List[str] = None,
    max_module: Optional[int] = None,
    max_lab: Optional[int] = None,
) -> Dict[str, Any]:
    """Validate that all expected outputs exist for a course.

    Args:
        course_path: Path to course directory (e.g., course_development/biol-8)
        formats: Optional list of formats to validate (e.g., ["pdf", "docx", "md"]).
                 If None, uses DEFAULT_REQUIRED_FORMATS from config.
        max_module: Optional max module number to validate (e.g., 6 means only validate 1-6)
        max_lab: Optional max lab number to validate (e.g., 4 means only validate labs 1-4)

    Returns:
        Dictionary with validation results:
        - valid: bool indicating overall validity
        - course: course name
        - formats_validated: list of formats being validated
        - modules_checked: number of modules checked
        - modules_valid: number of modules with complete outputs
        - modules: list of module validation details
        - syllabus_valid: bool for syllabus outputs
        - issues: list of issues found
    """
    course_dir = Path(course_path).resolve()
    course_name = course_dir.name

    # Determine formats to validate
    if formats is None:
        formats = DEFAULT_REQUIRED_FORMATS

    logger.info(f"Validating outputs for {course_name}")
    logger.info(f"  Formats: {', '.join(formats)}")
    if max_module:
        logger.info(f"  Max module: {max_module}")
    if max_lab:
        logger.info(f"  Max lab: {max_lab}")

    results = {
        "valid": True,
        "course": course_name,
        "formats_validated": formats,
        "timestamp": get_timestamp(),
        "modules_checked": 0,
        "modules_valid": 0,
        "modules": [],
        "syllabus_valid": False,
        "issues": [],
    }

    # Get expected module count - use max_module limit if provided
    full_expected = config.COURSE_CONFIG.get(course_name, {}).get("expected_modules", 0)
    expected_modules = max_module if max_module else full_expected

    # Validate modules - filter to max_module if specified
    all_modules = get_module_directories(course_dir)
    if max_module:
        # Filter to only modules 1 through max_module
        modules = [m for m in all_modules if _get_module_number(m.name) <= max_module]
    else:
        modules = all_modules
    results["modules_checked"] = len(modules)

    if expected_modules and len(modules) != expected_modules:
        results["issues"].append(f"Expected {expected_modules} modules, found {len(modules)}")

    for module_path in modules:
        module_result = _validate_module_outputs(module_path, formats)
        results["modules"].append(module_result)

        if module_result["valid"]:
            results["modules_valid"] += 1
        else:
            results["valid"] = False

    # Validate syllabus
    syllabus_result = _validate_syllabus_outputs(course_dir, formats)
    results["syllabus_valid"] = syllabus_result["valid"]

    if not syllabus_result["valid"]:
        results["issues"].extend(syllabus_result.get("issues", []))

    # Validate labs (with optional max_lab limit)
    lab_result = check_lab_files(course_dir, max_lab=max_lab)
    results["labs"] = lab_result

    if lab_result["missing_outputs"]:
        results["issues"].extend(
            [f"Lab missing rendered output: {lab}" for lab in lab_result["missing_outputs"]]
        )
    if lab_result["issues"]:
        results["issues"].extend(lab_result["issues"])

    # Log summary
    logger.info(
        f"Validation complete: {results['modules_valid']}/{results['modules_checked']} modules valid"
    )
    if lab_result["source_labs"] > 0:
        logger.info(
            f"Labs: {lab_result['source_labs']} source, outputs: {lab_result['output_files']}, dashboards: {lab_result['dashboards']}"
        )

    return results


def _validate_module_outputs(module_path: Path, formats: List[str] = None) -> Dict[str, Any]:
    """Validate outputs for a single module.

    Args:
        module_path: Path to module directory
        formats: Optional list of formats to validate

    Returns:
        Dictionary with module validation results
    """
    module_name = module_path.name

    result = {
        "name": module_name,
        "valid": True,
        "has_output_dir": False,
        "formats_checked": formats or DEFAULT_REQUIRED_FORMATS,
        "study_guides": {},
        "website": {},
        "missing_files": [],
    }

    # Check output directory
    has_output, subdirs = check_output_directory(module_path)
    result["has_output_dir"] = has_output

    if not has_output:
        result["valid"] = False
        result["missing_files"].append("output/")
        return result

    # Check study guide files (format-aware)
    study_guide_files = check_study_guide_files(module_path, formats)
    result["study_guides"] = study_guide_files

    missing_sg = [f for f, exists in study_guide_files.items() if not exists]
    if missing_sg:
        result["missing_files"].extend([f"study-guides/{f}" for f in missing_sg])
        result["valid"] = False

    # Check website files (index.html is always required if html format requested)
    # Website is optional unless html is in the formats list
    if formats is None or "html" in formats:
        website_files = check_website_files(module_path)
        result["website"] = website_files

        missing_web = [f for f, exists in website_files.items() if not exists]
        if missing_web:
            result["missing_files"].extend([f"website/{f}" for f in missing_web])
            result["valid"] = False
    else:
        # Skip website validation if html not requested
        result["website"] = {"index.html": "skipped (html not in formats)"}

    return result


def _validate_syllabus_outputs(course_dir: Path, formats: List[str] = None) -> Dict[str, Any]:
    """Validate syllabus outputs for a course.

    Syllabus outputs are placed directly in the syllabus/output/ directory
    (flat structure), not in format subdirectories.

    Args:
        course_dir: Path to course directory
        formats: Optional list of formats to validate. If None, uses default.

    Returns:
        Dictionary with syllabus validation results
    """
    result = {
        "valid": True,
        "formats_checked": formats,
        "files": {},
        "issues": [],
    }

    syllabus_output = course_dir / "syllabus" / "output"

    if not syllabus_output.exists():
        result["valid"] = False
        result["issues"].append("Syllabus output directory not found")
        return result

    # Get required formats based on what was requested
    required_formats = get_syllabus_required_formats(formats)
    optional_formats = ["mp3", "md"]  # Always optional

    # Track what we're checking
    result["required_formats"] = required_formats

    for fmt in required_formats:
        files = list(syllabus_output.glob(f"*.{fmt}"))
        result["files"][fmt] = len(files)
        if len(files) == 0:
            result["issues"].append(f"No syllabus {fmt.upper()} files found")
            result["valid"] = False

    for fmt in optional_formats:
        files = list(syllabus_output.glob(f"*.{fmt}"))
        result["files"][fmt] = len(files)
        # No validity check for optional formats

    return result


def validate_published(published_path: str) -> Dict[str, Any]:
    """Validate that published directory has expected structure.

    Args:
        published_path: Path to PUBLISHED directory

    Returns:
        Dictionary with validation results
    """
    pub_dir = Path(published_path).resolve()

    logger.info(f"Validating published directory: {pub_dir}")

    results = {
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

    # Check each expected course
    for course_name in config.COURSE_CONFIG.keys():
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

        # Check module directories
        for module_dir in sorted(course_dir.glob("module-*")):
            if module_dir.is_dir():
                mod_counts = count_files_by_extension(module_dir)
                results["courses"][course_name]["modules"].append(
                    {
                        "name": module_dir.name,
                        "files": sum(mod_counts.values()),
                    }
                )

    logger.info(f"Published validation complete: {results['total_files']} total files")

    return results


def generate_validation_report(
    course_name: str,
    repo_root: Optional[str] = None,
    formats: List[str] = None,
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

    course_path = root / "course_development" / course_name
    published_path = root / config.PUBLISHED_DIR_NAME

    logger.info(f"Generating validation report for {course_name}")
    if formats:
        logger.info(f"  Validating formats: {', '.join(formats)}")

    report = {
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
            max_lab=max_lab,
        )
    else:
        report["source_validation"] = {
            "valid": False,
            "issues": [f"Course directory not found: {course_path}"],
        }

    # Validate published outputs
    if published_path.exists():
        report["published_validation"] = validate_published(str(published_path))
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

    summary = {
        "course": course_name,
        "timestamp": get_timestamp(),
        "modules": {},
        "totals": {},
        "by_format": {},
    }

    total_by_format: Dict[str, int] = {}

    for module_path in get_module_directories(course_dir):
        module_name = module_path.name
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
