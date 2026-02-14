"""Tests for batch processing orchestration functions.

Uses real function calls with temporary file structures.
No mocks — tests verify orchestration logic through actual file I/O.
"""

from pathlib import Path
import pytest

from src.batch_processing.main import (
    process_course_modules,
    process_course_syllabus,
    process_course_labs,
    process_course_practice_tests,
)


class TestProcessCourseModules:
    """Tests for process_course_modules function."""

    def test_process_course_modules_success(self, temp_dir):
        """Test successful processing of course modules."""
        # Setup course structure with markdown content
        course_dir = temp_dir / "course"
        course_dir.mkdir()
        mod1 = course_dir / "module-01"
        mod1.mkdir()
        (mod1 / "test.md").write_text("# Module 1\n\nContent.", encoding="utf-8")
        mod2 = course_dir / "module-02"
        mod2.mkdir()
        (mod2 / "test.md").write_text("# Module 2\n\nContent.", encoding="utf-8")

        result = process_course_modules(
            temp_dir, "Test Course", formats=["txt"]
        )

        assert result["course"] == "Test Course"
        assert len(result["modules"]) == 2
        # Real processing with txt format should not raise
        module_names = {m["name"] for m in result["modules"]}
        assert "module-01" in module_names
        assert "module-02" in module_names

    def test_process_course_modules_missing_dir(self, temp_dir):
        """Test processing with missing course directory."""
        result = process_course_modules(temp_dir, "Test Course")

        assert result["modules"] == []
        assert result["errors"] == []

    def test_process_course_modules_filter(self, temp_dir):
        """Test filtering modules by number using real matches_module_number."""
        course_dir = temp_dir / "course"
        course_dir.mkdir()
        mod1 = course_dir / "module-01"
        mod1.mkdir()
        (mod1 / "test.md").write_text("# Module 1", encoding="utf-8")
        mod2 = course_dir / "module-02"
        mod2.mkdir()
        (mod2 / "test.md").write_text("# Module 2", encoding="utf-8")

        # Filter to module 1 only — uses real matches_module_number
        result = process_course_modules(
            temp_dir, "Test Course", module_filter=1, formats=["txt"]
        )

        assert len(result["modules"]) == 1
        assert result["modules"][0]["name"] == "module-01"

    def test_process_course_modules_no_matching_filter(self, temp_dir):
        """Test filtering with non-existent module number."""
        course_dir = temp_dir / "course"
        course_dir.mkdir()
        (course_dir / "module-01").mkdir()

        result = process_course_modules(
            temp_dir, "Test Course", module_filter=99, formats=["txt"]
        )

        # Module 99 doesn't exist, so no modules processed
        assert len(result["modules"]) == 0


class TestProcessCourseSyllabus:
    """Tests for process_course_syllabus function."""

    def test_process_course_syllabus_success(self, temp_dir):
        """Test successful syllabus processing."""
        syl_dir = temp_dir / "syllabus"
        syl_dir.mkdir()
        (syl_dir / "Syllabus.md").write_text(
            "# Course Syllabus\n\nWeek 1: Introduction.", encoding="utf-8"
        )

        result = process_course_syllabus(
            temp_dir, "Test Course", formats=["txt"]
        )

        assert result["processed"] is True
        assert result["errors"] == []

    def test_process_course_syllabus_missing_dir(self, temp_dir):
        """Test processing with missing syllabus directory."""
        result = process_course_syllabus(temp_dir, "Test Course")

        assert result["processed"] is False
        assert result["errors"] == []

    def test_process_course_syllabus_empty_dir(self, temp_dir):
        """Test processing with empty syllabus directory."""
        (temp_dir / "syllabus").mkdir()

        result = process_course_syllabus(
            temp_dir, "Test Course", formats=["txt"]
        )

        # Empty dir should still be processed (just no files)
        assert result["errors"] == []


class TestProcessCourseLabs:
    """Tests for process_course_labs function."""

    def test_process_course_labs_with_lab_files(self, temp_dir):
        """Test lab processing with real lab markdown files."""
        labs_dir = temp_dir / "course" / "labs"
        labs_dir.mkdir(parents=True)
        (labs_dir / "lab-01.md").write_text(
            "# Lab 1: Introduction\n\n## Objectives\n\nLearn basics.",
            encoding="utf-8",
        )

        result = process_course_labs(
            temp_dir, "Test Course", formats=["pdf", "html"]
        )

        assert result["processed"] is True
        assert result["errors"] == []

    def test_process_course_labs_missing_dir(self, temp_dir):
        """Test processing with missing labs directory."""
        result = process_course_labs(temp_dir, "Test Course")

        assert result["processed"] is False
        assert result["errors"] == []

    def test_process_course_labs_no_formats(self, temp_dir):
        """Test processing with no compatible formats."""
        labs_dir = temp_dir / "course" / "labs"
        labs_dir.mkdir(parents=True)
        (labs_dir / "lab-01.md").write_text("# Lab 1", encoding="utf-8")

        result = process_course_labs(
            temp_dir, "Test Course", formats=["docx", "mp3"]
        )

        # No lab-compatible formats requested
        assert result["processed"] is False
        assert result["files"] == []


class TestProcessCoursePracticeTests:
    """Tests for process_course_practice_tests function."""

    def test_process_practice_tests_with_files(self, temp_dir):
        """Test practice test processing with real markdown."""
        pt_dir = temp_dir / "course" / "practice_tests"
        pt_dir.mkdir(parents=True)
        (pt_dir / "practice-test-1.md").write_text(
            "# Practice Test 1\n\n1. What is biology?\n",
            encoding="utf-8",
        )

        result = process_course_practice_tests(
            temp_dir, "Test Course", formats=["pdf"]
        )

        assert result["processed"] is True
        assert len(result["files"]) == 1

    def test_process_practice_tests_missing_dir(self, temp_dir):
        """Test processing with missing directory."""
        result = process_course_practice_tests(temp_dir, "Test Course")

        assert result["processed"] is False

    def test_process_practice_tests_skip_formats(self, temp_dir):
        """Test skipping when PDF not requested."""
        pt_dir = temp_dir / "course" / "practice_tests"
        pt_dir.mkdir(parents=True)
        (pt_dir / "test-1.md").write_text("# Test", encoding="utf-8")

        result = process_course_practice_tests(
            temp_dir, "Test Course", formats=["docx", "html"]
        )

        assert result["processed"] is False
        assert result["files"] == []
