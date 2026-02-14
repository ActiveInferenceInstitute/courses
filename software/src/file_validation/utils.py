"""Utility functions for file validation."""

import re
from pathlib import Path
from typing import Any, Dict, List, Pattern

from . import config


def is_kebab_case(name: str) -> bool:
    """Check if a name follows kebab-case convention.

    Args:
        name: Name to check

    Returns:
        True if name is kebab-case, False otherwise
    """
    return bool(config.KEBAB_CASE_PATTERN.match(name))


def has_module_prefix(name: str) -> bool:
    """Check if a name has module prefix (e.g., "module-1-").

    Args:
        name: Name to check

    Returns:
        True if name has module prefix, False otherwise
    """
    return bool(config.MODULE_PREFIX_PATTERN.match(name))


def matches_pattern(name: str, pattern: Pattern[str]) -> bool:
    """Check if a name matches a pattern.

    Args:
        name: Name to check
        pattern: Pattern to match against

    Returns:
        True if name matches pattern, False otherwise
    """
    return bool(pattern.match(name))


def get_file_extension(file_path: Path) -> str:
    """Get file extension (lowercase).

    Args:
        file_path: Path to file

    Returns:
        File extension (including dot) or empty string
    """
    return file_path.suffix.lower()


def is_valid_extension(file_path: Path) -> bool:
    """Check if file has valid extension.

    Args:
        file_path: Path to file

    Returns:
        True if extension is valid, False otherwise
    """
    ext = get_file_extension(file_path)
    return ext in config.VALID_EXTENSIONS


def validate_assignment_name(file_name: str) -> bool:
    """Validate assignment file name.

    Args:
        file_name: File name to validate

    Returns:
        True if name is valid, False otherwise
    """
    return matches_pattern(file_name, config.ASSIGNMENT_PATTERN)


def validate_lecture_name(file_name: str) -> bool:
    """Validate lecture file name.

    Args:
        file_name: File name to validate

    Returns:
        True if name is valid, False otherwise
    """
    return matches_pattern(file_name, config.LECTURE_PATTERN)


def validate_lab_name(file_name: str) -> bool:
    """Validate lab protocol file name.

    Args:
        file_name: File name to validate

    Returns:
        True if name is valid, False otherwise
    """
    return matches_pattern(file_name, config.LAB_PATTERN)


def validate_study_guide_name(file_name: str) -> bool:
    """Validate study guide file name.

    Args:
        file_name: File name to validate

    Returns:
        True if name is valid, False otherwise
    """
    return matches_pattern(file_name, config.STUDY_GUIDE_PATTERN)


def validate_quiz_name(file_name: str) -> bool:
    """Validate quiz file name.

    Args:
        file_name: File name to validate

    Returns:
        True if name is valid, False otherwise
    """
    return matches_pattern(file_name, config.QUIZ_PATTERN)


def check_required_files_exist(module_path: Path) -> List[str]:
    """Check which required files are missing.

    Args:
        module_path: Path to module directory

    Returns:
        List of missing required file names
    """
    missing = []
    for file_name in config.REQUIRED_FILES:
        file_path = module_path / file_name
        if not file_path.exists() or not file_path.is_file():
            missing.append(file_name)
    return missing


def check_required_directories_exist(module_path: Path) -> List[str]:
    """Check which required directories are missing.

    Args:
        module_path: Path to module directory

    Returns:
        List of missing required directory names
    """
    missing = []
    for dir_name in config.REQUIRED_DIRECTORIES:
        dir_path = module_path / dir_name
        if not dir_path.exists() or not dir_path.is_dir():
            missing.append(dir_name)
    return missing


def get_file_type(file_name: str) -> str:
    """Determine the type of course material file based on name.

    Args:
        file_name: File name to analyze

    Returns:
        File type: "assignment", "lecture", "lab", "study_guide", "quiz", or "unknown"
    """
    if validate_assignment_name(file_name):
        return "assignment"
    elif validate_lecture_name(file_name):
        return "lecture"
    elif validate_lab_name(file_name):
        return "lab"
    elif validate_study_guide_name(file_name):
        return "study_guide"
    elif validate_quiz_name(file_name):
        return "quiz"
    else:
        return "unknown"


def extract_module_number_from_filename(file_name: str) -> int:
    """Extract module number from a file name.

    Args:
        file_name: File name (e.g., "module-1-assignment-1.md")

    Returns:
        Module number

    Raises:
        ValueError: If module number cannot be extracted
    """
    match = config.MODULE_PREFIX_PATTERN.match(file_name)
    if not match:
        raise ValueError(f"File name does not have module prefix: {file_name}")

    # Extract number from "module-N-"
    parts = file_name.split("-")
    if len(parts) < 2:
        raise ValueError(f"Cannot extract module number from: {file_name}")

    try:
        module_num = int(parts[1])
        return module_num
    except (ValueError, IndexError) as e:
        raise ValueError(f"Cannot extract module number from: {file_name}") from e


def validate_file_name_structure(file_name: str) -> Dict[str, Any]:
    """Validate and analyze file name structure.

    Args:
        file_name: File name to validate

    Returns:
        Dictionary with validation results:
        - valid: bool indicating if name is valid
        - file_type: Type of file (assignment, lecture, etc.)
        - module_number: Extracted module number (if available)
        - issues: List of validation issues
    """
    result = {
        "valid": True,
        "file_type": "unknown",
        "module_number": None,
        "issues": [],
    }

    # Check if it's a required file first (README.md, AGENTS.md)
    # These don't need module prefix
    if file_name in config.REQUIRED_FILES:
        result["file_type"] = "required_file"
        result["valid"] = True
        result["issues"] = []
        return result

    # Check if it has module prefix
    if not has_module_prefix(file_name):
        result["valid"] = False
        result["issues"].append("Missing module prefix (module-N-)")
        return result

    # Try to extract module number
    try:
        result["module_number"] = extract_module_number_from_filename(file_name)
    except ValueError:
        result["valid"] = False
        result["issues"].append("Cannot extract module number")

    # Determine file type
    result["file_type"] = get_file_type(file_name)

    # Check if file type is unknown
    if result["file_type"] == "unknown":
        result["valid"] = False
        result["issues"].append("Unknown file type - does not match any pattern")

    # Check kebab-case for stem
    stem = Path(file_name).stem
    if not is_kebab_case(stem):
        result["valid"] = False
        result["issues"].append("File name is not kebab-case")

    return result
