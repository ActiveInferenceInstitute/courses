"""Tests for batch processing orchestration functions.

Uses real function calls with temporary file structures — no mocks.
Tests use flat module structure (AIF convention).
"""

from src.batch_processing.main import (
    process_course_modules,
)


class TestProcessCourseModules:
    """Tests for process_course_modules function."""

    def test_process_course_modules_success(self, temp_dir):
        """Test successful processing of course modules."""
        # Flat module structure: modules directly under course_dir
        mod1 = temp_dir / "module-01"
        mod1.mkdir()
        (mod1 / "module.md").write_text("# Module 1\n\nContent.", encoding="utf-8")
        mod2 = temp_dir / "module-02"
        mod2.mkdir()
        (mod2 / "module.md").write_text("# Module 2\n\nContent.", encoding="utf-8")

        result = process_course_modules(temp_dir, "Test Course", formats=["txt"])

        assert result["course"] == "Test Course"
        assert len(result["modules"]) == 2
        module_names = {m["name"] for m in result["modules"]}
        assert "module-01" in module_names
        assert "module-02" in module_names

    def test_process_course_modules_missing_dir(self, temp_dir):
        """Test processing with missing course directory."""
        result = process_course_modules(temp_dir, "Test Course")

        assert result["modules"] == []
        assert result["errors"] == []

    def test_process_course_modules_filter(self, temp_dir):
        """Test filtering modules by module number."""
        mod1 = temp_dir / "module-01"
        mod1.mkdir()
        (mod1 / "module.md").write_text("# Module 1", encoding="utf-8")
        mod2 = temp_dir / "module-02"
        mod2.mkdir()
        (mod2 / "module.md").write_text("# Module 2", encoding="utf-8")

        result = process_course_modules(temp_dir, "Test Course", module_filter=1, formats=["txt"])

        assert len(result["modules"]) == 1
        assert result["modules"][0]["name"] == "module-01"

    def test_process_course_modules_no_matching_filter(self, temp_dir):
        """Test filtering with non-existent module number."""
        mod1 = temp_dir / "01_systems"
        mod1.mkdir()

        result = process_course_modules(temp_dir, "Test Course", module_filter=99, formats=["txt"])

        assert len(result["modules"]) == 0
