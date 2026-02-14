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


def write_template_file(file_path: Path, template: str, **kwargs) -> None:
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
    """Extract module number from module directory path.

    Handles both naming conventions:
    - BIOL-1 style: module-1, module-2, module-10
    - BIOL-8 style: module-01-topic-name, module-02-chemistry-of-life

    Args:
        module_path: Path to module directory

    Returns:
        Module number

    Raises:
        ValueError: If module number cannot be extracted
    """
    module_name = module_path.name
    if not module_name.startswith("module-"):
        raise ValueError(f"Invalid module directory name: {module_name}")

    try:
        # Extract the number part after "module-"
        # Works for both "module-1" and "module-01-topic-name"
        module_number = int(module_name.split("-")[1])
        return module_number
    except (IndexError, ValueError) as e:
        raise ValueError(f"Could not extract module number from: {module_name}") from e


def matches_module_number(dirname: str, target: int) -> bool:
    """Check if a directory name matches a target module number.

    Handles both naming conventions:
    - BIOL-1 style: module-1, module-2, module-10
    - BIOL-8 style: module-01-topic-name, module-02-chemistry-of-life

    Args:
        dirname: Directory name (e.g., "module-1" or "module-01-topic-name")
        target: Target module number to match

    Returns:
        True if the directory matches the target module number
    """
    # Pattern matches "module-" followed by the number (with optional leading zeros)
    # and then either end of string or a hyphen (for topic suffix)
    pattern = rf"^module-0*{target}(?:-|$)"
    return bool(re.match(pattern, dirname))


def find_module_path(course_path: Path, module_number: int) -> Optional[Path]:
    """Find the module directory for a given module number.

    Searches for module directories matching the module number,
    supporting both naming conventions (module-N and module-NN-topic-name).

    Args:
        course_path: Path to course directory
        module_number: Module number to find

    Returns:
        Path to module directory if found, None otherwise
    """
    course_dir = course_path / "course"
    if not course_dir.exists():
        return None

    for item in course_dir.iterdir():
        if item.is_dir() and item.name.startswith("module-"):
            if matches_module_number(item.name, module_number):
                return item

    return None


def list_all_modules(course_path: Path) -> List[Path]:
    """List all module directories in a course.

    Args:
        course_path: Path to course directory

    Returns:
        List of module directory paths, sorted by module number
    """
    course_dir = course_path / "course"
    if not course_dir.exists():
        return []

    modules = []
    for item in course_dir.iterdir():
        if item.is_dir() and item.name.startswith("module-"):
            try:
                get_module_number_from_path(item)
                modules.append(item)
            except ValueError:
                # Skip invalid module directories
                continue

    # Sort by module number
    modules.sort(key=lambda p: get_module_number_from_path(p))
    return modules


def get_next_module_number(course_path: Path) -> int:
    """Get the next available module number for a course.

    Args:
        course_path: Path to course directory

    Returns:
        Next available module number (1 if no modules exist)
    """
    modules = list_all_modules(course_path)
    if not modules:
        return 1

    # Get the highest module number and add 1
    max_number = max(get_module_number_from_path(m) for m in modules)
    return max_number + 1
