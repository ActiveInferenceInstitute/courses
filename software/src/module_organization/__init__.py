"""Module organization utilities for creating and managing course module structures."""

from .main import (
    create_module_structure,
    create_next_module,
    get_module_statistics,
    initialize_module_files,
    list_course_modules,
    validate_module_structure,
)

__all__ = [
    "create_module_structure",
    "create_next_module",
    "get_module_statistics",
    "initialize_module_files",
    "list_course_modules",
    "validate_module_structure",
]
