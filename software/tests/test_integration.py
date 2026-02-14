"""Integration tests for software modules."""

from pathlib import Path

import pytest

from src.file_validation.main import validate_module_files
from src.module_organization.main import create_module_structure


def test_module_creation_and_validation_workflow(temp_dir):
    """Test complete workflow of creating and validating a module."""
    course_path = str(temp_dir)

    # Create module
    module_path = create_module_structure(course_path, 1)

    # Validate module
    validation = validate_module_files(module_path)

    assert validation["valid"] is True
    assert len(validation["missing_files"]) == 0
    assert len(validation["missing_directories"]) == 0


def test_module_with_assignment_validation(temp_dir):
    """Test module validation with assignment files."""
    course_path = str(temp_dir)

    # Create module
    module_path = create_module_structure(course_path, 1)

    # Add a properly named assignment
    assignments_dir = Path(module_path) / "assignments"
    assignment_file = assignments_dir / "module-1-assignment-1-intro.md"
    assignment_file.write_text("# Assignment 1\n", encoding="utf-8")

    # Validate module
    validation = validate_module_files(module_path)

    assert validation["valid"] is True
    assert len(validation["naming_violations"]) == 0
