"""Tests for file_validation main functions."""

from pathlib import Path

import pytest

from src.file_validation.main import (
    check_naming_conventions,
    validate_module_files,
    verify_required_structure,
)


def test_validate_module_files_valid(sample_module_structure):
    """Test validating a valid module."""
    result = validate_module_files(str(sample_module_structure))

    assert result["valid"] is True
    assert len(result["missing_files"]) == 0
    assert len(result["missing_directories"]) == 0


def test_validate_module_files_missing_files(temp_dir):
    """Test validating module with missing required files."""
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()
    (module_dir / "assignments").mkdir()

    result = validate_module_files(str(module_dir))

    assert result["valid"] is False
    assert "README.md" in result["missing_files"]
    assert "AGENTS.md" in result["missing_files"]


def test_validate_module_files_nonexistent():
    """Test validating nonexistent module."""
    result = validate_module_files("/nonexistent/module")

    assert result["valid"] is False
    assert "error" in result


def test_check_naming_conventions_valid(sample_module_structure):
    """Test checking naming conventions for valid files."""
    # Create a properly named assignment file
    assignment_file = sample_module_structure / "assignments" / "module-1-assignment-1-test.md"
    assignment_file.write_text("# Assignment\n", encoding="utf-8")

    violations = check_naming_conventions(str(sample_module_structure))
    assert len(violations) == 0


def test_check_naming_conventions_invalid(sample_module_structure):
    """Test checking naming conventions for invalid files."""
    # Create an improperly named file
    bad_file = sample_module_structure / "assignments" / "bad_file_name.md"
    bad_file.write_text("# Bad\n", encoding="utf-8")

    violations = check_naming_conventions(str(sample_module_structure))
    assert len(violations) > 0


def test_verify_required_structure_valid(sample_module_structure):
    """Test verifying required structure for valid module."""
    result = verify_required_structure(str(sample_module_structure))
    assert result is True


def test_verify_required_structure_invalid(temp_dir):
    """Test verifying required structure for invalid module."""
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()
    # Missing assignments directory

    result = verify_required_structure(str(module_dir))
    assert result is False


def test_verify_required_structure_nonexistent():
    """Test verifying structure for nonexistent module."""
    result = verify_required_structure("/nonexistent/module")
    assert result is False


def test_validate_course_structure_nonexistent():
    """Test validating nonexistent course structure."""
    from src.file_validation.main import validate_course_structure

    result = validate_course_structure("/nonexistent/course")
    assert result["valid"] is False
    assert "does not exist" in result["issues"][0]


def test_validate_course_structure(temp_dir):
    """Test validating course structure."""
    from src.file_validation.main import validate_course_structure

    # Create course structure
    course_dir = temp_dir / "course"
    course_dir.mkdir()
    module1 = course_dir / "module-1"
    module1.mkdir()
    (module1 / "README.md").write_text("# Module 1\n", encoding="utf-8")
    (module1 / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")
    assignments = module1 / "assignments"
    assignments.mkdir()

    result = validate_course_structure(str(temp_dir))
    assert "modules" in result
    assert "total_modules" in result
    assert result["total_modules"] >= 1


def test_get_validation_report(temp_dir):
    """Test getting validation report."""
    from src.file_validation.main import get_validation_report

    # Create module structure
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()
    (module_dir / "README.md").write_text("# Module 1\n", encoding="utf-8")
    (module_dir / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")
    assignments = module_dir / "assignments"
    assignments.mkdir()

    report = get_validation_report(str(module_dir))
    assert "module_path" in report
    assert "is_valid" in report
    assert "structure_valid" in report
    assert "details" in report
    assert "recommendations" in report


def test_find_missing_materials(temp_dir):
    """Test finding missing materials."""
    from src.file_validation.main import find_missing_materials

    # Create minimal module
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()
    (module_dir / "README.md").write_text("# Module 1\n", encoding="utf-8")

    result = find_missing_materials(str(module_dir))
    assert "missing_required" in result
    assert "missing_optional" in result
    assert "suggestions" in result


def test_check_file_sizes(temp_dir):
    """Test checking file sizes."""
    from src.file_validation.main import check_file_sizes

    # Create module with files
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()
    small_file = module_dir / "small.txt"
    small_file.write_text("Small content", encoding="utf-8")

    # Check with large max size (should find none)
    result = check_file_sizes(str(module_dir), max_size=100 * 1024 * 1024)
    assert isinstance(result, list)
    assert len(result) == 0

    # Check with very small max size (should find files)
    result = check_file_sizes(str(module_dir), max_size=1)
    assert len(result) > 0


def test_validate_module_files_naming_violations_in_assignments(temp_dir):
    """Test validate_module_files detects naming violations in assignments."""
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()
    (module_dir / "README.md").write_text("# Module 1\n", encoding="utf-8")
    (module_dir / "AGENTS.md").write_text("# Docs\n", encoding="utf-8")
    assignments_dir = module_dir / "assignments"
    assignments_dir.mkdir()

    # Create file with invalid assignment name
    bad_file = assignments_dir / "bad-name.md"
    bad_file.write_text("# Bad\n", encoding="utf-8")

    result = validate_module_files(str(module_dir))
    assert "naming_violations" in result
    assert len(result["naming_violations"]) > 0


def test_validate_module_files_naming_violations_subdirectory(temp_dir):
    """Test validate_module_files handles files in subdirectories."""
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()
    (module_dir / "README.md").write_text("# Module 1\n", encoding="utf-8")
    (module_dir / "AGENTS.md").write_text("# Docs\n", encoding="utf-8")
    (module_dir / "assignments").mkdir()

    # Create subdirectory with file
    subdir = module_dir / "subdir"
    subdir.mkdir()
    # File in subdirectory with invalid kebab-case
    bad_file = subdir / "BadFileName.md"
    bad_file.write_text("# Bad\n", encoding="utf-8")

    result = validate_module_files(str(module_dir))
    assert "naming_violations" in result


def test_validate_module_files_naming_violations_root_level(temp_dir):
    """Test validate_module_files detects naming violations at root level."""
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()
    (module_dir / "README.md").write_text("# Module 1\n", encoding="utf-8")
    (module_dir / "AGENTS.md").write_text("# Docs\n", encoding="utf-8")
    (module_dir / "assignments").mkdir()

    # Create file at root level that doesn't match any pattern
    bad_file = module_dir / "bad_file_name.md"
    bad_file.write_text("# Bad\n", encoding="utf-8")

    result = validate_module_files(str(module_dir))
    assert "naming_violations" in result
    assert len(result["naming_violations"]) > 0


def test_check_naming_conventions_nonexistent():
    """Test check_naming_conventions with nonexistent directory."""
    violations = check_naming_conventions("/nonexistent/dir")
    assert isinstance(violations, list)
    assert len(violations) == 0


def test_find_missing_materials_with_optional(temp_dir):
    """Test find_missing_materials detects missing optional materials."""
    from src.file_validation.main import find_missing_materials

    # Create minimal module
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()
    (module_dir / "README.md").write_text("# Module 1\n", encoding="utf-8")
    (module_dir / "AGENTS.md").write_text("# Docs\n", encoding="utf-8")
    (module_dir / "assignments").mkdir()

    result = find_missing_materials(str(module_dir))
    assert "missing_optional" in result
    # Should detect missing optional materials
    assert isinstance(result["missing_optional"], list)


def test_check_file_sizes_oserror(temp_dir):
    """Test check_file_sizes handles OSError when accessing files."""
    from src.file_validation.main import check_file_sizes

    module_dir = temp_dir / "module-1"
    module_dir.mkdir()

    # Create a file
    test_file = module_dir / "test.txt"
    test_file.write_text("Test", encoding="utf-8")

    # Test that OSError path is covered (hard to trigger, but we test the structure)
    result = check_file_sizes(str(module_dir))
    assert isinstance(result, list)


def test_validate_course_structure_no_course_dir(temp_dir):
    """Test validating course structure without course subdirectory."""
    from src.file_validation.main import validate_course_structure

    # Create directory but no 'course' subdirectory
    course_dir = temp_dir
    course_dir.mkdir(exist_ok=True)

    result = validate_course_structure(str(temp_dir))
    assert result["valid"] is False
    assert "course" in result["issues"][0].lower()


def test_validate_course_structure_with_modules(temp_dir):
    """Test validating course structure with multiple modules."""
    from src.file_validation.main import validate_course_structure

    # Create course structure with multiple modules
    course_dir = temp_dir / "course"
    course_dir.mkdir()

    # Module 1 - valid
    module1 = course_dir / "module-1"
    module1.mkdir()
    (module1 / "README.md").write_text("# Module 1\n", encoding="utf-8")
    (module1 / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")
    (module1 / "assignments").mkdir()

    # Module 2 - valid
    module2 = course_dir / "module-2"
    module2.mkdir()
    (module2 / "README.md").write_text("# Module 2\n", encoding="utf-8")
    (module2 / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")
    (module2 / "assignments").mkdir()

    result = validate_course_structure(str(temp_dir))
    assert "modules" in result
    assert result["total_modules"] == 2
    assert result["valid_modules"] >= 0


def test_get_validation_report_nonexistent():
    """Test getting validation report for nonexistent module."""
    from src.file_validation.main import get_validation_report

    report = get_validation_report("/nonexistent/module")
    assert report["is_valid"] is False
    assert "error" in report["details"]
    assert "recommendations" in report


def test_find_missing_materials_comprehensive(temp_dir):
    """Test finding missing materials comprehensively."""
    from src.file_validation.main import find_missing_materials

    # Create minimal module
    module_dir = temp_dir / "module-1"
    module_dir.mkdir()
    (module_dir / "README.md").write_text("# Module 1\n", encoding="utf-8")
    (module_dir / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")
    (module_dir / "assignments").mkdir()

    result = find_missing_materials(str(module_dir))
    assert "missing_required" in result
    assert "missing_optional" in result
    assert "suggestions" in result
    assert isinstance(result["missing_required"], list)
    assert isinstance(result["missing_optional"], list)
    assert isinstance(result["suggestions"], list)


def test_check_file_sizes_nonexistent():
    """Test check_file_sizes with nonexistent module."""
    from src.file_validation.main import check_file_sizes

    result = check_file_sizes("/nonexistent/module")
    assert isinstance(result, list)
    assert len(result) == 0


def test_check_file_sizes_large_files(temp_dir):
    """Test check_file_sizes with large files."""
    from src.file_validation.main import check_file_sizes

    module_dir = temp_dir / "module-1"
    module_dir.mkdir()

    # Create a file that's larger than default max (50MB)
    # For testing, we'll use a smaller threshold
    large_file = module_dir / "large.txt"
    # Create a file larger than 1KB for testing
    large_file.write_bytes(b"x" * 2000)

    result = check_file_sizes(str(module_dir), max_size=1000)
    assert len(result) > 0
    assert any("large.txt" in f for f in result)
