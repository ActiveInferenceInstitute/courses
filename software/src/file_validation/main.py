"""Main functions for file validation."""

from pathlib import Path
from typing import Any, Dict, List

from . import config
from .utils import (
    check_required_directories_exist,
    check_required_files_exist,
    get_file_extension,
    has_module_prefix,
    is_kebab_case,
    is_valid_extension,
    validate_assignment_name,
    validate_lab_name,
    validate_lecture_name,
    validate_quiz_name,
    validate_study_guide_name,
)


def validate_module_files(module_path: str) -> Dict[str, Any]:
    """Validate files in a module directory.

    Args:
        module_path: Path to module directory

    Returns:
        Dictionary with validation results including:
        - valid: bool indicating if module is valid
        - missing_files: List of missing required files
        - missing_directories: List of missing required directories
        - naming_violations: List of files with naming violations
        - invalid_extensions: List of files with invalid extensions
    """
    module_dir = Path(module_path)

    if not module_dir.exists():
        return {
            "valid": False,
            "missing_files": [],
            "missing_directories": [],
            "naming_violations": [],
            "invalid_extensions": [],
            "error": f"Module path does not exist: {module_path}",
        }

    missing_files = check_required_files_exist(module_dir)
    missing_directories = check_required_directories_exist(module_dir)

    naming_violations = []
    invalid_extensions = []

    # Check all files in module directory
    for file_path in module_dir.rglob("*"):
        if file_path.is_file():
            file_name = file_path.name

            # Skip required files (README.md, AGENTS.md) from naming checks
            if file_name in config.REQUIRED_FILES:
                continue

            # Check extension
            if not is_valid_extension(file_path):
                invalid_extensions.append(str(file_path.relative_to(module_dir)))

            # Check naming conventions for course material files
            if file_name.endswith((".md", ".pdf", ".pptx", ".docx")):
                # Check if it's in assignments directory
                if "assignments" in file_path.parts:
                    if not validate_assignment_name(file_name):
                        naming_violations.append(str(file_path.relative_to(module_dir)))
                # Check other file types
                elif not (
                    validate_lecture_name(file_name)
                    or validate_lab_name(file_name)
                    or validate_study_guide_name(file_name)
                    or validate_quiz_name(file_name)
                    or file_name in config.REQUIRED_FILES
                ):
                    # Allow files that don't match specific patterns if they're in subdirectories
                    if len(file_path.parts) - len(module_dir.parts) > 1:
                        # File is in a subdirectory, check basic kebab-case
                        if not is_kebab_case(file_path.stem):
                            naming_violations.append(
                                str(file_path.relative_to(module_dir))
                            )
                    else:
                        # File is directly in module, should match a pattern
                        naming_violations.append(str(file_path.relative_to(module_dir)))

    valid = (
        len(missing_files) == 0
        and len(missing_directories) == 0
        and len(naming_violations) == 0
        and len(invalid_extensions) == 0
    )

    return {
        "valid": valid,
        "missing_files": missing_files,
        "missing_directories": missing_directories,
        "naming_violations": naming_violations,
        "invalid_extensions": invalid_extensions,
    }


def check_naming_conventions(directory: str) -> List[str]:
    """Check file naming convention compliance.

    Args:
        directory: Directory to check

    Returns:
        List of files with naming convention violations
    """
    dir_path = Path(directory)

    if not dir_path.exists():
        return []

    violations = []

    for file_path in dir_path.rglob("*"):
        if file_path.is_file():
            file_name = file_path.name

            # Skip required files
            if file_name in config.REQUIRED_FILES:
                continue

            # Check if file name is kebab-case (without extension)
            stem = file_path.stem
            if not is_kebab_case(stem):
                violations.append(str(file_path.relative_to(dir_path)))
                continue

            # For files in assignments directory, check assignment pattern
            if "assignments" in file_path.parts:
                if not validate_assignment_name(file_name):
                    violations.append(str(file_path.relative_to(dir_path)))

    return violations


def verify_required_structure(module_path: str) -> bool:
    """Verify module has required folder structure.

    Args:
        module_path: Path to module directory

    Returns:
        True if structure is complete, False otherwise
    """
    module_dir = Path(module_path)

    if not module_dir.exists():
        return False

    missing_files = check_required_files_exist(module_dir)
    missing_directories = check_required_directories_exist(module_dir)

    return len(missing_files) == 0 and len(missing_directories) == 0


def validate_course_structure(course_path: str) -> Dict[str, Any]:
    """Validate entire course structure.

    Args:
        course_path: Path to course directory

    Returns:
        Dictionary with validation results:
        - valid: bool indicating if course is valid
        - modules: List of module validation results
        - total_modules: Total number of modules
        - valid_modules: Number of valid modules
        - issues: List of course-level issues
    """
    course_dir = Path(course_path)

    if not course_dir.exists():
        return {
            "valid": False,
            "modules": [],
            "total_modules": 0,
            "valid_modules": 0,
            "issues": [f"Course path does not exist: {course_path}"],
        }

    course_dir_path = course_dir / "course"
    if not course_dir_path.exists():
        return {
            "valid": False,
            "modules": [],
            "total_modules": 0,
            "valid_modules": 0,
            "issues": ["Course directory does not contain 'course' subdirectory"],
        }

    modules = []
    issues = []

    # Find all module directories
    module_dirs = [d for d in course_dir_path.iterdir() if d.is_dir() and d.name.startswith("module-")]

    for module_dir in sorted(module_dirs):
        module_validation = validate_module_files(str(module_dir))
        modules.append({
            "module_path": str(module_dir),
            "module_name": module_dir.name,
            "validation": module_validation,
        })

        if not module_validation["valid"]:
            issues.append(f"Module {module_dir.name} has validation issues")

    valid_modules = sum(1 for m in modules if m["validation"]["valid"])

    return {
        "valid": len(issues) == 0,
        "modules": modules,
        "total_modules": len(modules),
        "valid_modules": valid_modules,
        "issues": issues,
    }


def get_validation_report(module_path: str) -> Dict[str, Any]:
    """Get detailed validation report for a module.

    Args:
        module_path: Path to module directory

    Returns:
        Dictionary with detailed validation report:
        - module_path: Path to module
        - is_valid: Overall validity
        - structure_valid: Structure validity
        - files_valid: Files validity
        - naming_valid: Naming conventions validity
        - details: Detailed breakdown
        - recommendations: List of recommendations
    """
    module_dir = Path(module_path)

    if not module_dir.exists():
        return {
            "module_path": module_path,
            "is_valid": False,
            "structure_valid": False,
            "files_valid": False,
            "naming_valid": False,
            "details": {"error": "Module path does not exist"},
            "recommendations": ["Create module directory"],
        }

    validation = validate_module_files(module_path)
    structure_valid = verify_required_structure(module_path)
    naming_violations = check_naming_conventions(module_path)

    details = {
        "missing_files": validation.get("missing_files", []),
        "missing_directories": validation.get("missing_directories", []),
        "naming_violations": validation.get("naming_violations", []),
        "invalid_extensions": validation.get("invalid_extensions", []),
        "naming_check_violations": naming_violations,
    }

    recommendations = []
    if validation.get("missing_files"):
        recommendations.append(f"Add missing files: {', '.join(validation['missing_files'])}")
    if validation.get("missing_directories"):
        recommendations.append(f"Create missing directories: {', '.join(validation['missing_directories'])}")
    if naming_violations:
        recommendations.append(f"Fix naming violations: {len(naming_violations)} files")
    if not recommendations:
        recommendations.append("Module structure is valid")

    return {
        "module_path": module_path,
        "is_valid": validation["valid"] and structure_valid and len(naming_violations) == 0,
        "structure_valid": structure_valid,
        "files_valid": len(validation.get("missing_files", [])) == 0,
        "naming_valid": len(naming_violations) == 0,
        "details": details,
        "recommendations": recommendations,
    }


def find_missing_materials(module_path: str) -> Dict[str, Any]:
    """Find missing required materials in a module.

    Args:
        module_path: Path to module directory

    Returns:
        Dictionary with missing materials:
        - missing_required: List of missing required files/directories
        - missing_optional: List of missing optional materials
        - suggestions: Suggestions for completing module
    """
    module_dir = Path(module_path)

    if not module_dir.exists():
        return {
            "missing_required": [],
            "missing_optional": [],
            "suggestions": ["Module does not exist"],
        }

    validation = validate_module_files(module_path)

    missing_required = []
    missing_required.extend(validation.get("missing_files", []))
    missing_required.extend(validation.get("missing_directories", []))

    # Check for optional materials
    missing_optional = []
    optional_patterns = {
        "lectures": ["*lecture*.pdf", "*lecture*.pptx"],
        "lab_protocols": ["*lab*.md", "*lab*.pdf"],
        "study_guides": ["*study-guide*.md", "*study-guide*.pdf"],
        "quizzes": ["*quiz*.md", "*quiz*.pdf"],
    }

    for material_type, patterns in optional_patterns.items():
        found = False
        for pattern in patterns:
            if list(module_dir.glob(pattern)):
                found = True
                break
        if not found:
            missing_optional.append(material_type)

    suggestions = []
    if missing_required:
        suggestions.append("Add required files and directories")
    if missing_optional:
        suggestions.append(f"Consider adding: {', '.join(missing_optional)}")

    return {
        "missing_required": missing_required,
        "missing_optional": missing_optional,
        "suggestions": suggestions,
    }


def check_file_sizes(module_path: str, max_size: int = 50 * 1024 * 1024) -> List[str]:
    """Check for files that exceed maximum size.

    Args:
        module_path: Path to module directory
        max_size: Maximum file size in bytes (default: 50MB)

    Returns:
        List of files that exceed maximum size
    """
    module_dir = Path(module_path)

    if not module_dir.exists():
        return []

    oversized_files = []

    for file_path in module_dir.rglob("*"):
        if file_path.is_file():
            try:
                file_size = file_path.stat().st_size
                if file_size > max_size:
                    oversized_files.append(str(file_path.relative_to(module_dir)))
            except OSError:
                # Skip files that can't be accessed
                continue

    return oversized_files
