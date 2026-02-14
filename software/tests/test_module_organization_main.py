"""Tests for module_organization main functions."""

from pathlib import Path

import pytest

from src.module_organization.main import (
    create_module_structure,
    create_next_module,
    initialize_module_files,
    list_course_modules,
    validate_module_structure,
)


def test_create_module_structure(temp_dir):
    """Test creating a new module structure."""
    course_path = str(temp_dir)
    module_number = 1

    module_path = create_module_structure(course_path, module_number)

    # Verify module directory was created
    assert Path(module_path).exists()
    assert Path(module_path).name == "module-1"

    # Verify required files exist
    assert (Path(module_path) / "README.md").exists()
    assert (Path(module_path) / "AGENTS.md").exists()

    # Verify assignments directory exists
    assert (Path(module_path) / "assignments").exists()
    assert (Path(module_path) / "assignments" / "README.md").exists()
    assert (Path(module_path) / "assignments" / "AGENTS.md").exists()


def test_create_module_structure_existing_module(temp_dir):
    """Test creating a module that already exists raises error."""
    course_path = str(temp_dir)
    module_number = 1

    # Create module first time
    create_module_structure(course_path, module_number)

    # Try to create again
    with pytest.raises(ValueError, match="Module already exists"):
        create_module_structure(course_path, module_number)


def test_create_module_structure_invalid_course_path():
    """Test creating module with invalid course path raises error."""
    with pytest.raises(ValueError, match="Course path does not exist"):
        create_module_structure("/nonexistent/path", 1)


def test_validate_module_structure_valid(sample_module_structure):
    """Test validating a valid module structure."""
    result = validate_module_structure(str(sample_module_structure))
    assert result is True


def test_validate_module_structure_missing_files(temp_dir):
    """Test validating module with missing files."""
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()

    # Create assignments directory but no README.md
    (module_dir / "assignments").mkdir()

    result = validate_module_structure(str(module_dir))
    assert result is False


def test_validate_module_structure_nonexistent():
    """Test validating nonexistent module."""
    result = validate_module_structure("/nonexistent/module")
    assert result is False


def test_initialize_module_files(sample_module_structure):
    """Test initializing module files with default template."""
    # Remove README.md to test initialization
    (sample_module_structure / "README.md").unlink()

    initialize_module_files(str(sample_module_structure), "default")

    # Verify README.md was created
    assert (sample_module_structure / "README.md").exists()


def test_initialize_module_files_invalid_template(sample_module_structure):
    """Test initializing with invalid template raises error."""
    with pytest.raises(ValueError, match="Unknown template"):
        initialize_module_files(str(sample_module_structure), "invalid")


def test_initialize_module_files_nonexistent_path():
    """Test initializing nonexistent module raises error."""
    with pytest.raises(ValueError, match="Module path does not exist"):
        initialize_module_files("/nonexistent/module", "default")


def test_create_next_module(temp_dir):
    """Test creating the next module in sequence."""
    course_path = str(temp_dir)

    # Create first module
    module1_path = create_module_structure(course_path, 1)
    assert Path(module1_path).exists()

    # Create next module
    module2_path = create_next_module(course_path)
    assert Path(module2_path).exists()
    assert Path(module2_path).name == "module-2"


def test_create_next_module_no_existing_modules(temp_dir):
    """Test create_next_module when no modules exist."""
    course_path = str(temp_dir)

    # Should create module-1
    module_path = create_next_module(course_path)
    assert Path(module_path).exists()
    assert Path(module_path).name == "module-1"


def test_create_next_module_nonexistent_course():
    """Test create_next_module with nonexistent course raises error."""
    with pytest.raises(ValueError, match="Course path does not exist"):
        create_next_module("/nonexistent/course")


def test_list_course_modules(temp_dir):
    """Test listing all modules in a course."""
    course_path = str(temp_dir)

    # Create multiple modules
    create_module_structure(course_path, 1)
    create_module_structure(course_path, 2)
    create_module_structure(course_path, 3)

    modules = list_course_modules(course_path)
    assert len(modules) == 3
    assert all("module-" in m for m in modules)
    # Should be sorted by module number
    assert "module-1" in modules[0] or "module-1" in modules[0].lower()


def test_list_course_modules_empty(temp_dir):
    """Test listing modules when no modules exist."""
    course_path = str(temp_dir)

    modules = list_course_modules(course_path)
    assert isinstance(modules, list)
    assert len(modules) == 0


def test_list_course_modules_nonexistent():
    """Test listing modules for nonexistent course raises error."""
    with pytest.raises(ValueError, match="Course path does not exist"):
        list_course_modules("/nonexistent/course")


def test_initialize_module_files_module_number_error(temp_dir):
    """Test initialize_module_files with path that can't extract module number."""
    # Create a directory that doesn't follow module naming convention
    invalid_module = temp_dir / "invalid-module"
    invalid_module.mkdir()

    # Should still work, but module_number will be None
    try:
        initialize_module_files(str(invalid_module), "default")
        # Should succeed even if module number can't be extracted
        assert (invalid_module / "README.md").exists()
    except ValueError as e:
        # If it raises an error about module number, that's also valid
        assert "module number" in str(e).lower() or "extract" in str(e).lower()
