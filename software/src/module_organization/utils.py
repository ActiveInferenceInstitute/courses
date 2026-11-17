"""Utility functions for module organization."""

import re
from pathlib import Path
from typing import List, Optional


def ensure_directory_exists(directory: Path) -> None:
    """Create directory if it doesn't exist.

    Args:
        directory: Path to directory to create
    """
    directory.mkdir(parents=True, exist_ok=True)


def write_template_file(file_path: Path, template: str, **kwargs: object) -> None:
    """Write a template file with substitutions.

    Args:
        file_path: Path where file should be written
        template: Template string with placeholders
        **kwargs: Values to substitute in template
    """
    content = template.format(**kwargs)
    file_path.write_text(content, encoding="utf-8")


def get_module_path(course_path: Path, module_number: int) -> Path:
    """Get path to module directory.

    Args:
        course_path: Path to course directory
        module_number: Module number

    Returns:
        Path to module directory
    """
    return course_path / "course" / f"module-{module_number}"


def check_file_exists(file_path: Path) -> bool:
    """Check if a file exists.

    Args:
        file_path: Path to file to check

    Returns:
        True if file exists, False otherwise
    """
    return file_path.exists() and file_path.is_file()


def check_directory_exists(directory_path: Path) -> bool:
    """Check if a directory exists.

    Args:
        directory_path: Path to directory to check

    Returns:
        True if directory exists, False otherwise
    """
    return directory_path.exists() and directory_path.is_dir()


def list_missing_files(module_path: Path, required_files: List[str]) -> List[str]:
    """List required files that are missing.

    Args:
        module_path: Path to module directory
        required_files: List of required file names

    Returns:
        List of missing file names
    """
    missing = []
    for file_name in required_files:
        file_path = module_path / file_name
        if not check_file_exists(file_path):
            missing.append(file_name)
    return missing


def list_missing_directories(module_path: Path, required_dirs: List[str]) -> List[str]:
    """List required directories that are missing.

    Args:
        module_path: Path to module directory
        required_dirs: List of required directory names

    Returns:
        List of missing directory names
    """
    missing = []
    for dir_name in required_dirs:
        dir_path = module_path / dir_name
        if not check_directory_exists(dir_path):
            missing.append(dir_name)
    return missing


def get_module_number_from_path(module_path: Path) -> int:
    """Read current NN_topic and legacy module-N[-topic] numeric identities."""
    match = re.match(r"^(?:module-(\d+)(?:-|$)|(\d+)_)", module_path.name)
    if match is None:
        raise ValueError(f"Invalid module directory name: {module_path.name}")
    return int(match.group(1) or match.group(2))


def matches_module_number(dirname: str, target: int) -> bool:
    try:
        return get_module_number_from_path(Path(dirname)) == target
    except ValueError:
        return False


def find_module_path(
    course_path: Path, module_number: int, unit: Optional[str] = None
) -> Optional[Path]:
    """Find a unique current/legacy module, rejecting ambiguous numeric selectors."""
    modules = list_all_modules(course_path)
    if unit is not None:
        if Path(unit).is_absolute() or len(Path(unit).parts) != 1 or unit in ("", ".", ".."):
            raise ValueError(f"Invalid unit: {unit}")
        modules = [m for m in modules if m.parent.relative_to(course_path).as_posix() == unit]
    matches = [m for m in modules if matches_module_number(m.name, module_number)]
    if len(matches) > 1:
        raise ValueError(f"Ambiguous module {module_number}; supply --unit")
    return matches[0] if matches else None


def list_all_modules(course_path: Path) -> List[Path]:
    from ..batch_processing.utils import find_modules_for_course

    return sorted(
        find_modules_for_course(course_path),
        key=lambda p: (p.parent.as_posix(), get_module_number_from_path(p)),
    )


def get_next_module_number(course_path: Path) -> int:
    modules = list_all_modules(course_path)
    return max((get_module_number_from_path(m) for m in modules), default=0) + 1
