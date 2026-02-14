"""Main functions for module organization."""

from pathlib import Path
from typing import Any, Dict, List

from . import config
from .utils import (
    check_directory_exists,
    check_file_exists,
    ensure_directory_exists,
    get_module_path,
    get_next_module_number,
    list_all_modules,
    list_missing_directories,
    list_missing_files,
    write_template_file,
)


def create_module_structure(course_path: str, module_number: int) -> str:
    """Create standard module folder structure.

    Args:
        course_path: Path to course directory
        module_number: Module number

    Returns:
        Path to created module directory

    Raises:
        ValueError: If course_path doesn't exist or module already exists
        OSError: If directory creation fails
    """
    course_dir = Path(course_path)
    if not course_dir.exists():
        raise ValueError(f"Course path does not exist: {course_path}")

    module_path = get_module_path(course_dir, module_number)

    if module_path.exists():
        raise ValueError(f"Module already exists: {module_path}")

    # Create module directory
    ensure_directory_exists(module_path)

    # Create assignments directory
    assignments_dir = module_path / "assignments"
    ensure_directory_exists(assignments_dir)

    # Create README.md
    readme_path = module_path / "README.md"
    write_template_file(
        readme_path, config.README_TEMPLATE, module_number=module_number
    )

    # Create AGENTS.md
    agents_path = module_path / "AGENTS.md"
    write_template_file(
        agents_path, config.AGENTS_TEMPLATE, module_number=module_number
    )

    # Create assignments/README.md
    assignments_readme_path = assignments_dir / "README.md"
    write_template_file(
        assignments_readme_path,
        config.ASSIGNMENTS_README_TEMPLATE,
        module_number=module_number,
    )

    # Create assignments/AGENTS.md
    assignments_agents_path = assignments_dir / "AGENTS.md"
    write_template_file(
        assignments_agents_path,
        config.ASSIGNMENTS_AGENTS_TEMPLATE,
        module_number=module_number,
    )

    return str(module_path)


def validate_module_structure(module_path: str) -> bool:
    """Validate that module structure matches requirements.

    Args:
        module_path: Path to module directory

    Returns:
        True if structure is valid, False otherwise
    """
    module_dir = Path(module_path)

    if not module_dir.exists():
        return False

    # Check required files
    missing_files = list_missing_files(module_dir, config.REQUIRED_FILES)
    if missing_files:
        return False

    # Check required directories
    missing_dirs = list_missing_directories(module_dir, config.REQUIRED_DIRECTORIES)
    if missing_dirs:
        return False

    return True


def initialize_module_files(module_path: str, template: str) -> None:
    """Initialize module with template files.

    Args:
        module_path: Path to module directory
        template: Template identifier (currently only "default" is supported)

    Raises:
        ValueError: If module_path doesn't exist or template is invalid
    """
    module_dir = Path(module_path)

    if not module_dir.exists():
        raise ValueError(f"Module path does not exist: {module_path}")

    if template != "default":
        raise ValueError(f"Unknown template: {template}")

    # Extract module number from path
    from .utils import get_module_number_from_path

    try:
        module_number = get_module_number_from_path(module_dir)
    except ValueError as e:
        raise ValueError(f"Could not extract module number: {e}") from e

    # Create README.md if it doesn't exist
    readme_path = module_dir / "README.md"
    if not check_file_exists(readme_path):
        write_template_file(
            readme_path, config.README_TEMPLATE, module_number=module_number
        )

    # Create AGENTS.md if it doesn't exist
    agents_path = module_dir / "AGENTS.md"
    if not check_file_exists(agents_path):
        write_template_file(
            agents_path, config.AGENTS_TEMPLATE, module_number=module_number
        )

    # Ensure assignments directory exists
    assignments_dir = module_dir / "assignments"
    ensure_directory_exists(assignments_dir)

    # Create assignments/README.md if it doesn't exist
    assignments_readme_path = assignments_dir / "README.md"
    if not check_file_exists(assignments_readme_path):
        write_template_file(
            assignments_readme_path,
            config.ASSIGNMENTS_README_TEMPLATE,
            module_number=module_number,
        )

    # Create assignments/AGENTS.md if it doesn't exist
    assignments_agents_path = assignments_dir / "AGENTS.md"
    if not check_file_exists(assignments_agents_path):
        write_template_file(
            assignments_agents_path,
            config.ASSIGNMENTS_AGENTS_TEMPLATE,
            module_number=module_number,
        )


def create_next_module(course_path: str) -> str:
    """Create the next module in sequence for a course.

    Args:
        course_path: Path to course directory

    Returns:
        Path to created module directory

    Raises:
        ValueError: If course_path doesn't exist
        OSError: If directory creation fails
    """
    course_dir = Path(course_path)
    if not course_dir.exists():
        raise ValueError(f"Course path does not exist: {course_path}")

    next_number = get_next_module_number(course_dir)
    return create_module_structure(course_path, next_number)


def list_course_modules(course_path: str) -> List[str]:
    """List all modules in a course.

    Args:
        course_path: Path to course directory

    Returns:
        List of module directory paths as strings, sorted by module number

    Raises:
        ValueError: If course_path doesn't exist
    """
    course_dir = Path(course_path)
    if not course_dir.exists():
        raise ValueError(f"Course path does not exist: {course_path}")

    modules = list_all_modules(course_dir)
    return [str(m) for m in modules]


def get_module_statistics(module_path: str) -> Dict[str, Any]:
    """Get statistics about a module.

    Args:
        module_path: Path to module directory

    Returns:
        Dictionary with module statistics including:
        - module_number: Module number
        - total_files: Total number of files
        - total_directories: Total number of directories
        - assignment_count: Number of assignment files
        - has_readme: Whether README.md exists
        - has_agents: Whether AGENTS.md exists
        - is_valid: Whether module structure is valid

    Raises:
        ValueError: If module_path doesn't exist
    """
    module_dir = Path(module_path)
    if not module_dir.exists():
        raise ValueError(f"Module path does not exist: {module_path}")

    from .utils import get_module_number_from_path

    try:
        module_number = get_module_number_from_path(module_dir)
    except ValueError:
        module_number = None

    # Count files and directories
    total_files = sum(1 for _ in module_dir.rglob("*") if _.is_file())
    total_directories = sum(1 for _ in module_dir.rglob("*") if _.is_dir())

    # Count assignments (exclude README.md and AGENTS.md)
    assignments_dir = module_dir / "assignments"
    assignment_count = 0
    if assignments_dir.exists():
        from ..file_validation.utils import validate_assignment_name
        assignment_count = sum(
            1
            for f in assignments_dir.iterdir()
            if f.is_file()
            and f.name not in ["README.md", "AGENTS.md"]
            and validate_assignment_name(f.name)
        )

    # Check required files
    has_readme = check_file_exists(module_dir / "README.md")
    has_agents = check_file_exists(module_dir / "AGENTS.md")

    # Check validity
    is_valid = validate_module_structure(module_path)

    return {
        "module_number": module_number,
        "total_files": total_files,
        "total_directories": total_directories,
        "assignment_count": assignment_count,
        "has_readme": has_readme,
        "has_agents": has_agents,
        "is_valid": is_valid,
    }
