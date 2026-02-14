"""Tests for file_validation utility functions."""

import pytest

from src.file_validation.utils import (
    extract_module_number_from_filename,
    get_file_type,
    validate_file_name_structure,
)


def test_get_file_type_assignment():
    """Test identifying assignment file type."""
    assert get_file_type("module-1-assignment-1-intro.md") == "assignment"
    assert get_file_type("module-2-assignment-5-test.pdf") == "assignment"


def test_get_file_type_lecture():
    """Test identifying lecture file type."""
    assert get_file_type("module-1-lecture-introduction.pdf") == "lecture"
    assert get_file_type("module-2-lecture-cells.pptx") == "lecture"


def test_get_file_type_lab():
    """Test identifying lab file type."""
    assert get_file_type("module-1-lab-1-safety.md") == "lab"
    assert get_file_type("module-2-lab-3-microscopy.md") == "lab"


def test_get_file_type_study_guide():
    """Test identifying study guide file type."""
    assert get_file_type("module-1-study-guide.md") == "study_guide"
    assert get_file_type("module-2-study-guide.pdf") == "study_guide"


def test_get_file_type_quiz():
    """Test identifying quiz file type."""
    assert get_file_type("module-1-quiz.md") == "quiz"
    assert get_file_type("module-2-quiz.pdf") == "quiz"


def test_get_file_type_unknown():
    """Test identifying unknown file type."""
    assert get_file_type("random-file.txt") == "unknown"
    assert get_file_type("module-1-other-file.md") == "unknown"


def test_extract_module_number_from_filename_valid():
    """Test extracting module number from valid filename."""
    assert extract_module_number_from_filename("module-1-assignment-1.md") == 1
    assert extract_module_number_from_filename("module-5-lecture-intro.pdf") == 5
    assert extract_module_number_from_filename("module-10-quiz.md") == 10


def test_extract_module_number_from_filename_invalid():
    """Test extracting module number from invalid filename raises error."""
    with pytest.raises(ValueError, match="does not have module prefix"):
        extract_module_number_from_filename("assignment-1.md")

    with pytest.raises(ValueError):
        extract_module_number_from_filename("module-abc-assignment.md")


def test_validate_file_name_structure_valid():
    """Test validating valid file name structure."""
    result = validate_file_name_structure("module-1-assignment-1-intro.md")

    assert result["valid"] is True
    assert result["file_type"] == "assignment"
    assert result["module_number"] == 1
    assert len(result["issues"]) == 0


def test_validate_file_name_structure_invalid_missing_prefix():
    """Test validating file name without module prefix."""
    result = validate_file_name_structure("assignment-1.md")

    assert result["valid"] is False
    assert "Missing module prefix" in result["issues"][0]


def test_validate_file_name_structure_invalid_unknown_type():
    """Test validating file name with unknown type."""
    result = validate_file_name_structure("module-1-random-file.md")

    assert result["valid"] is False
    assert any("Unknown file type" in issue for issue in result["issues"])


def test_validate_file_name_structure_required_file():
    """Test validating required files (README.md, AGENTS.md)."""
    result = validate_file_name_structure("README.md")

    assert result["file_type"] == "required_file"
    assert result["valid"] is True
    assert len(result["issues"]) == 0

    # Test AGENTS.md as well
    result2 = validate_file_name_structure("AGENTS.md")
    assert result2["file_type"] == "required_file"
    assert result2["valid"] is True
