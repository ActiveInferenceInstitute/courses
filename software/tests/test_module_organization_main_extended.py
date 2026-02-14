"""Extended tests for module_organization main functions."""

from pathlib import Path

import pytest

from src.module_organization.main import (
    create_next_module,
    get_module_statistics,
    list_course_modules,
)


def test_create_next_module(temp_dir):
    """Test creating next module in sequence."""
    course_path = str(temp_dir)

    # Create first module
    module1 = create_next_module(course_path)
    assert Path(module1).name == "module-1"

    # Create second module
    module2 = create_next_module(course_path)
    assert Path(module2).name == "module-2"

    # Verify both exist
    assert Path(module1).exists()
    assert Path(module2).exists()


def test_create_next_module_nonexistent_course():
    """Test creating next module with nonexistent course raises error."""
    with pytest.raises(ValueError, match="Course path does not exist"):
        create_next_module("/nonexistent/course")


def test_list_course_modules(temp_dir):
    """Test listing all modules in a course."""
    course_path = str(temp_dir)

    # Create multiple modules
    from src.module_organization.main import create_module_structure

    create_module_structure(course_path, 1)
    create_module_structure(course_path, 2)
    create_module_structure(course_path, 3)

    modules = list_course_modules(course_path)
    assert len(modules) == 3
    assert all("module-" in m for m in modules)


def test_list_course_modules_empty(temp_dir):
    """Test listing modules when none exist."""
    course_path = str(temp_dir)
    modules = list_course_modules(course_path)
    assert len(modules) == 0


def test_list_course_modules_nonexistent():
    """Test listing modules from nonexistent course raises error."""
    with pytest.raises(ValueError, match="Course path does not exist"):
        list_course_modules("/nonexistent/course")


def test_get_module_statistics(sample_module_structure):
    """Test getting module statistics."""
    stats = get_module_statistics(str(sample_module_structure))

    assert stats["module_number"] == 1
    assert stats["total_files"] > 0
    assert stats["total_directories"] > 0
    assert stats["has_readme"] is True
    assert stats["has_agents"] is True
    assert stats["is_valid"] is True


def test_get_module_statistics_with_assignments(temp_dir):
    """Test getting statistics for module with assignments."""
    from src.module_organization.main import create_module_structure

    course_path = str(temp_dir)
    module_path = create_module_structure(course_path, 1)

    # Add an assignment
    assignments_dir = Path(module_path) / "assignments"
    assignment_file = assignments_dir / "module-1-assignment-1-test.md"
    assignment_file.write_text("# Assignment\n", encoding="utf-8")

    stats = get_module_statistics(module_path)
    assert stats["assignment_count"] == 1
    assert stats["total_files"] >= 5  # README, AGENTS, assignments README, AGENTS, assignment


def test_get_module_statistics_nonexistent():
    """Test getting statistics for nonexistent module raises error."""
    with pytest.raises(ValueError, match="Module path does not exist"):
        get_module_statistics("/nonexistent/module")
