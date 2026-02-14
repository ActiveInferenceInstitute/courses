"""Tests for course_generator main CLI and orchestration."""

import pytest
from pathlib import Path
from src.course_generator.main import main, generate, list_curricula, validate
from src.course_generator.config import ALL_CURRICULA


class TestListCurricula:
    """Tests for list_curricula function."""

    def test_returns_all_eight(self):
        """Test that list_curricula returns all 8 curricula."""
        result = list_curricula()
        assert len(result) == 8

    def test_entries_have_required_fields(self):
        """Test that each entry has the expected fields."""
        result = list_curricula()
        for entry in result:
            assert "id" in entry
            assert "title" in entry
            assert "audience" in entry
            assert "total_files" in entry
            assert "type" in entry

    def test_types_are_valid(self):
        """Test type values are age-level or domain."""
        result = list_curricula()
        types = {e["type"] for e in result}
        assert types == {"age-level", "domain"}

    def test_five_age_level(self):
        """Test there are 5 age-level curricula."""
        result = list_curricula()
        age = [e for e in result if e["type"] == "age-level"]
        assert len(age) == 5

    def test_three_domain(self):
        """Test there are 3 domain curricula."""
        result = list_curricula()
        domain = [e for e in result if e["type"] == "domain"]
        assert len(domain) == 3


class TestGenerate:
    """Tests for the generate function."""

    def test_generate_single(self, tmp_path):
        """Test generating a single curriculum."""
        stats = generate("active_inference_es", output_dir=tmp_path)
        assert stats["files_created"] > 0
        assert (tmp_path / "active_inference_es" / "README.md").exists()

    def test_generate_unknown_raises(self, tmp_path):
        """Test that unknown ID raises KeyError."""
        with pytest.raises(KeyError, match="Unknown curriculum"):
            generate("nonexistent_curriculum", output_dir=tmp_path)


class TestValidate:
    """Tests for the validate function."""

    def test_validate_nonexistent_dir(self):
        """Test validate on non-existent directory."""
        result = validate("/nonexistent/path")
        assert "error" in result


class TestMainCLI:
    """Tests for the main CLI function."""

    def test_list_command(self):
        """Test 'list' command returns 0."""
        exit_code = main(["list"])
        assert exit_code == 0

    def test_generate_command(self, tmp_path):
        """Test 'generate' command for a single curriculum."""
        exit_code = main([
            "generate", "active_inference_es",
            "--output", str(tmp_path),
        ])
        assert exit_code == 0
        assert (tmp_path / "active_inference_es").is_dir()

    def test_validate_command_nonexistent(self):
        """Test 'validate' on non-existent dir returns 1."""
        exit_code = main(["validate", "/nonexistent/path"])
        assert exit_code == 1

    def test_no_command(self):
        """Test running without a command returns 1."""
        exit_code = main([])
        assert exit_code == 1
