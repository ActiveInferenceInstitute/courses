"""Utility functions for validation module."""

import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from . import config

logger = logging.getLogger(__name__)


def count_files_by_extension(directory: Path) -> Dict[str, int]:
    """Count files in directory by extension.

    Args:
        directory: Path to directory to scan

    Returns:
        Dictionary mapping extension to count
    """
    counts: Dict[str, int] = {}

    if not directory.exists():
        return counts

    for file_path in directory.rglob("*"):
        if file_path.is_file() and not file_path.name.startswith("."):
            ext = file_path.suffix.lower().lstrip(".")
            if ext:
                counts[ext] = counts.get(ext, 0) + 1

    return counts


def get_module_directories(course_path: Path) -> List[Path]:
    """Use the same current and legacy identities as the generation producer."""
    from ..batch_processing.utils import find_modules_for_course

    return find_modules_for_course(course_path)


def check_output_directory(module_path: Path) -> Tuple[bool, Dict[str, bool]]:
    """Check if module has expected output directory structure.

    Args:
        module_path: Path to module directory

    Returns:
        Tuple of (has_output, dict of subdirectory existence)
    """
    output_path = module_path / "output"

    if not output_path.exists():
        return False, {}

    subdirs = {
        "study_guides": (output_path / config.OUTPUT_DIRS["study_guides"]).exists(),
        "website": (output_path / config.OUTPUT_DIRS["website"]).exists(),
    }

    return True, subdirs


def check_study_guide_files(
    module_path: Path, formats: Optional[List[str]] = None
) -> Dict[str, bool]:
    """Check outputs of authored study-guide sources, not a hardcoded curriculum."""
    from ..batch_processing.utils import module_artifacts

    artifacts = module_artifacts(
        module_path, config.DEFAULT_REQUIRED_FORMATS if formats is None else formats
    )
    return {
        artifact["destination"].name: (
            artifact["destination"].is_file() and artifact["destination"].stat().st_size > 0
        )
        for artifact in artifacts if artifact["category"] == "study-guides"
    }


def check_website_files(module_path: Path) -> Dict[str, bool]:
    """Check which website files exist for a module.

    Args:
        module_path: Path to module directory

    Returns:
        Dictionary mapping expected filename to existence
    """
    website_path = module_path / "output" / config.OUTPUT_DIRS["website"]

    if not website_path.exists():
        return {f: False for f in config.EXPECTED_WEBSITE_FILES}

    result = {}
    for expected_file in config.EXPECTED_WEBSITE_FILES:
        file_path = website_path / expected_file
        result[expected_file] = file_path.exists()

    return result


def format_file_counts(counts: Dict[str, int]) -> str:
    """Format file counts as readable string.

    Args:
        counts: Dictionary of extension to count

    Returns:
        Formatted string like "pdf:10, html:5, mp3:3"
    """
    if not counts:
        return "none"

    return ", ".join(f"{ext}:{count}" for ext, count in sorted(counts.items()))


def get_timestamp() -> str:
    """Get current timestamp for logging.

    Returns:
        Formatted timestamp string
    """
    return datetime.now().strftime(config.LOG_DATE_FORMAT)


def check_lab_files(
    course_path: Path, max_lab: Optional[int] = None,
    formats: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Require each requested lab artifact from the shared source manifest."""
    from ..batch_processing.utils import get_formats_to_process, lab_artifacts

    active = get_formats_to_process(
        ",".join(config.LAB_OUTPUT_FORMATS if formats is None else formats)
    )
    artifacts = lab_artifacts(course_path, active, max_lab=max_lab)
    missing = [
        str(a["destination"]) for a in artifacts
        if not a["destination"].is_file() or a["destination"].stat().st_size == 0
    ]
    dashboard_dirs = {artifact["source"].parent / "dashboards" for artifact in artifacts}
    return {
        "source_labs": len({a["source"] for a in artifacts}),
        "output_files": {
            fmt: sum(a["format"] == fmt and str(a["destination"]) not in missing
                     for a in artifacts)
            for fmt in active if fmt in config.LAB_OUTPUT_FORMATS
        },
        "dashboards": sum(path.is_file() for directory in dashboard_dirs for path in directory.glob("*.html")),
        "missing_outputs": missing,
        "issues": [f"Missing or empty required lab artifact: {path}" for path in missing],
    }
