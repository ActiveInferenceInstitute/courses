"""Tests for module_organization utility functions."""

from pathlib import Path

import pytest

from src.module_organization.utils import (
    get_module_number_from_path,
    get_next_module_number,
    list_all_modules,
)


def test_get_module_number_from_path_valid(temp_dir):
    """Test extracting module number from valid path."""
    module_dir = temp_dir / "module-5"
    module_dir.mkdir()

    number = get_module_number_from_path(module_dir)
    assert number == 5


def test_get_module_number_from_path_invalid(temp_dir):
    """Test extracting module number from invalid path raises error."""
    module_dir = temp_dir / "invalid-name"
    module_dir.mkdir()

    with pytest.raises(ValueError, match="Invalid module directory name"):
        get_module_number_from_path(module_dir)


def test_list_all_modules(temp_dir):
    """Test listing all modules in a course."""
    course_dir = temp_dir / "course"
    course_dir.mkdir()

    # Create multiple modules
    (course_dir / "module-1").mkdir()
    (course_dir / "module-2").mkdir()
    (course_dir / "module-3").mkdir()
    (course_dir / "other-dir").mkdir()  # Should be ignored

    modules = list_all_modules(temp_dir)
    assert len(modules) == 3
    assert all("module-" in str(m) for m in modules)


def test_list_all_modules_empty(temp_dir):
    """Test listing modules when none exist."""
    modules = list_all_modules(temp_dir)
    assert len(modules) == 0


def test_get_next_module_number(temp_dir):
    """Test getting next module number."""
    course_dir = temp_dir / "course"
    course_dir.mkdir()

    # No modules exist
    next_num = get_next_module_number(temp_dir)
    assert next_num == 1

    # Create module 1
    (course_dir / "module-1").mkdir()
    next_num = get_next_module_number(temp_dir)
    assert next_num == 2

    # Create module 2
    (course_dir / "module-2").mkdir()
    next_num = get_next_module_number(temp_dir)
    assert next_num == 3


def test_get_next_module_number_with_gaps(temp_dir):
    """Test getting next module number when gaps exist."""
    course_dir = temp_dir / "course"
    course_dir.mkdir()

    # Create modules 1 and 3 (gap at 2)
    (course_dir / "module-1").mkdir()
    (course_dir / "module-3").mkdir()

    # Should return 4 (next after highest)
    next_num = get_next_module_number(temp_dir)
    assert next_num == 4
