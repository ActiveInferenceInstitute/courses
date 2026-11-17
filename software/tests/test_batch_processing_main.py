"""Comprehensive tests for batch processing main module."""

from pathlib import Path
import pytest

from src.batch_processing.main import (
    clear_all_outputs,
    generate_module_media,
    process_module_by_type,
    process_module_to_audio,
    process_module_to_pdf,
    process_module_to_text,
    process_module_website,
    process_syllabus,
)


class TestProcessModuleToPdf:
    """Tests for process_module_to_pdf function."""

    def test_process_module_to_pdf_success(self, sample_module_structure):
        """Test converting module markdown to PDFs."""
        output_dir = sample_module_structure.parent / "pdf_output"

        result = process_module_to_pdf(str(sample_module_structure), str(output_dir))

        assert isinstance(result, list)
        # PDFs should be generated for markdown files
        assert all(f.endswith(".pdf") for f in result)

    def test_process_module_to_pdf_nonexistent(self, temp_dir):
        """Test processing non-existent module raises ValueError."""
        with pytest.raises(ValueError, match="does not exist"):
            process_module_to_pdf(str(temp_dir / "nonexistent"), str(temp_dir / "output"))

    def test_process_module_to_pdf_empty_module(self, temp_dir):
        """Test processing empty module returns empty list."""
        empty_module = temp_dir / "empty_module"
        empty_module.mkdir()
        output_dir = temp_dir / "output"

        result = process_module_to_pdf(str(empty_module), str(output_dir))

        assert result == []


class TestProcessModuleToAudio:
    """Tests for process_module_to_audio function."""


    def test_process_module_to_audio_nonexistent(self, temp_dir):
        """Test processing non-existent module raises ValueError."""
        with pytest.raises(ValueError, match="does not exist"):
            process_module_to_audio(str(temp_dir / "nonexistent"), str(temp_dir / "output"))


class TestProcessModuleToText:
    """Tests for process_module_to_text function."""

    def test_process_module_to_text_nonexistent(self, temp_dir):
        """Test processing non-existent module raises ValueError."""
        # ValueError is raised before any transcribe_audio call — no mock needed
        with pytest.raises(ValueError, match="does not exist"):
            process_module_to_text(str(temp_dir / "nonexistent"), str(temp_dir / "output"))

    def test_process_module_to_text_no_audio(self, temp_dir):
        """Test processing module with no audio files."""
        module_dir = temp_dir / "module"
        module_dir.mkdir()
        output_dir = temp_dir / "output"

        # No audio files → transcribe_audio is never called, no mock needed
        result = process_module_to_text(str(module_dir), str(output_dir))

        assert result == []


class TestGenerateModuleMedia:
    """Tests for generate_module_media function."""


    def test_generate_module_media_nonexistent(self, temp_dir):
        """Test generating media for non-existent module raises ValueError."""
        with pytest.raises(ValueError, match="does not exist"):
            generate_module_media(str(temp_dir / "nonexistent"), str(temp_dir / "output"))


class TestProcessModuleByType:
    def test_authored_types_are_rendered_once_in_selected_formats(self, temp_dir):
        module = temp_dir / "01_systems"
        module.mkdir()
        (module / "module.md").write_text("# Systems\n\nLecture body.")
        (module / "questions.md").write_text("# Questions\n\nExplain a system.")
        (module / "lab.md").write_text("# Lab\n\nObserve a system.")
        assignments = module / "assignments"
        assignments.mkdir()
        (assignments / "assignment-1.md").write_text("# Assignment\n\nDescribe a system.")
        result = process_module_by_type(str(module), str(module / "output"), formats=["md", "txt"])
        assert result["errors"] == []
        assert result["summary"]["md"] == result["summary"]["txt"] == 4
        assert (module / "output/lecture-content/01_systems-module.md").read_bytes() == (module / "module.md").read_bytes()
        assert "Explain a system" in (module / "output/study-guides/01_systems-questions.txt").read_text()
        assert not list((module / "output").rglob("*.mp3"))

    def test_missing_source_is_rejected(self, temp_dir):
        with pytest.raises(ValueError, match="does not exist"):
            process_module_by_type(str(temp_dir / "missing"), str(temp_dir / "output"), formats=["md"])

    def test_copy_failure_is_retained_with_source_and_destination(self, temp_dir):
        module = temp_dir / "01_systems"
        module.mkdir()
        (module / "module.md").write_text("# Systems\n\nBody.")
        output = temp_dir / "output"
        output.write_text("blocking file")
        result = process_module_by_type(str(module), str(output), formats=["md"])
        assert result["summary"]["md"] == 0
        assert len(result["errors"]) == 1
        assert str(module / "module.md") in result["errors"][0]
        assert str(output / "lecture-content/01_systems-module.md") in result["errors"][0]
        assert output.read_text() == "blocking file"


class TestProcessSyllabus:
    """Tests for process_syllabus function."""

    def test_process_syllabus_structure(self, temp_dir):
        """Test that process_syllabus returns correct structure."""
        syllabus_dir = temp_dir / "syllabus"
        syllabus_dir.mkdir()
        (syllabus_dir / "Syllabus.md").write_text("# Syllabus\n\nCourse overview", encoding="utf-8")

        output_dir = temp_dir / "output"
        result = process_syllabus(str(syllabus_dir), str(output_dir), formats=["md", "txt"])

        assert result["errors"] == []
        assert (output_dir / "Syllabus.md").read_bytes() == (syllabus_dir / "Syllabus.md").read_bytes()
        assert "Course overview" in (output_dir / "Syllabus.txt").read_text()

    def test_process_syllabus_nonexistent(self, temp_dir):
        """Test processing non-existent syllabus raises ValueError."""
        with pytest.raises(ValueError, match="does not exist"):
            process_syllabus(str(temp_dir / "nonexistent"), str(temp_dir / "output"))

    def test_process_syllabus_skips_readme(self, temp_dir):
        """Test that README and AGENTS files are skipped."""
        syllabus_dir = temp_dir / "syllabus"
        syllabus_dir.mkdir()
        (syllabus_dir / "README.md").write_text("# README", encoding="utf-8")
        (syllabus_dir / "AGENTS.md").write_text("# AGENTS", encoding="utf-8")
        (syllabus_dir / "Syllabus.md").write_text("# Syllabus", encoding="utf-8")

        output_dir = temp_dir / "output"
        result = process_syllabus(str(syllabus_dir), str(output_dir), formats=["md"])

        assert result["errors"] == []
        assert {path.name for path in output_dir.iterdir()} == {"Syllabus.md"}


class TestClearAllOutputs:
    def test_explicit_cleanup_preserves_guides_and_unselected_files(self, temp_dir):
        output = temp_dir / "output"
        output.mkdir()
        for name in ("selected.md", "other.pdf", "README.md", "AGENTS.md", ".keep"):
            (output / name).write_text(name)
        before_inode = output.stat().st_ino
        result = clear_all_outputs(temp_dir, plans=[{"artifacts": [
            {"destination": output / name} for name in ("selected.md", "README.md", ".keep")
        ]}])
        assert result["errors"] == []
        assert result["total_files_removed"] == 1
        assert {path.name for path in output.iterdir()} == {"other.pdf", "README.md", "AGENTS.md", ".keep"}
        assert output.stat().st_ino == before_inode

    def test_escape_rejected_before_any_unlink(self, temp_dir):
        root = temp_dir / "admitted"
        root.mkdir()
        own = root / "selected.md"
        own.write_text("own")
        outside = temp_dir / "outside.md"
        outside.write_text("outside")
        alias = root / "escape.md"
        alias.symlink_to(outside)
        with pytest.raises(ValueError):
            clear_all_outputs(root, plans=[{"artifacts": [
                {"destination": own}, {"destination": alias},
            ]}])
        assert own.read_text() == "own"
        assert outside.read_text() == "outside"


class TestProcessModuleByTypeFormats:
    """Tests for process_module_by_type formats parameter."""


    def test_formats_txt_only(self, temp_dir):
        """formats=["txt"] only generates TXT, skips others."""
        module_dir = temp_dir / "module-01"
        module_dir.mkdir()
        (module_dir / "keys-to-success.md").write_text(
            "# Keys to Success\n\nStudy hard.", encoding="utf-8"
        )

        output_dir = temp_dir / "output"
        result = process_module_by_type(str(module_dir), str(output_dir), formats=["txt"])

        assert result["summary"]["txt"] >= 1
        assert result["summary"]["pdf"] == 0
        assert result["summary"]["mp3"] == 0
        assert result["summary"]["docx"] == 0
        assert result["summary"]["html"] == 0

    @pytest.mark.parametrize("formats", [[], ["txt", "xyz"]])
    def test_invalid_formats_reject_before_output_creation(self, temp_dir, formats):
        module = temp_dir / "01_systems"
        module.mkdir()
        (module / "module.md").write_text("# Systems\n\nBody.")
        with pytest.raises(ValueError):
            process_module_by_type(str(module), str(temp_dir / "output"), formats=formats)
        assert not (temp_dir / "output").exists()


class TestProcessSyllabusFormats:
    """Tests for process_syllabus formats parameter."""


    def test_syllabus_formats_txt_only(self, temp_dir):
        """formats=["txt"] only generates TXT."""
        syllabus_dir = temp_dir / "syllabus"
        syllabus_dir.mkdir()
        (syllabus_dir / "Syllabus.md").write_text(
            "# Syllabus\n\nCourse overview.", encoding="utf-8"
        )

        output_dir = temp_dir / "output"
        result = process_syllabus(str(syllabus_dir), str(output_dir), formats=["txt"])

        assert result["summary"]["txt"] >= 1
        assert result["summary"]["pdf"] == 0
        assert result["summary"]["mp3"] == 0
        assert result["summary"]["docx"] == 0
        assert result["summary"]["html"] == 0


class TestProcessModuleWebsite:
    """Tests for process_module_website function."""

    def test_process_module_website_success(self, temp_dir):
        """Test generating module website."""
        module_dir = temp_dir / "module-1"
        module_dir.mkdir()

        output_dir = temp_dir / "output" / "website"
        result = process_module_website(str(module_dir), str(output_dir))

        assert result.endswith("index.html")
        assert Path(result).exists()

    def test_process_module_website_default_output(self, temp_dir):
        """Test generating module website with default output."""
        module_dir = temp_dir / "module-1"
        module_dir.mkdir()

        result = process_module_website(str(module_dir))

        assert "output/website/index.html" in result


class TestProcessModuleByTypeMdFormat:
    """Tests for process_module_by_type MD format support."""

    def test_formats_md_only(self, temp_dir):
        """formats=["md"] only generates MD, skips others."""
        module_dir = temp_dir / "module-01"
        module_dir.mkdir()
        (module_dir / "keys-to-success.md").write_text(
            "# Keys to Success\n\nStudy hard.", encoding="utf-8"
        )

        output_dir = temp_dir / "output"
        result = process_module_by_type(str(module_dir), str(output_dir), formats=["md"])

        assert result["summary"]["md"] >= 1
        assert result["summary"]["pdf"] == 0
        assert result["summary"]["mp3"] == 0
        assert result["summary"]["docx"] == 0
        assert result["summary"]["html"] == 0
        assert result["summary"]["txt"] == 0

    def test_formats_md_in_summary(self, temp_dir):
        """Verify MD count appears in summary when generating all formats."""
        module_dir = temp_dir / "module-01"
        module_dir.mkdir()
        (module_dir / "keys-to-success.md").write_text(
            "# Keys to Success\n\nStudy hard.", encoding="utf-8"
        )

        output_dir = temp_dir / "output"
        result = process_module_by_type(str(module_dir), str(output_dir), formats=["md", "txt"])

        assert "md" in result["summary"]
        assert result["summary"]["md"] >= 1
        # Check that the MD file was actually created
        md_files = list(output_dir.rglob("*.md"))
        assert len(md_files) >= 1


class TestProcessSyllabusMdFormat:
    """Tests for process_syllabus MD format support."""

    def test_syllabus_formats_md_only(self, temp_dir):
        """formats=["md"] only generates MD."""
        syllabus_dir = temp_dir / "syllabus"
        syllabus_dir.mkdir()
        (syllabus_dir / "Syllabus.md").write_text(
            "# Syllabus\n\nCourse overview.", encoding="utf-8"
        )

        output_dir = temp_dir / "output"
        result = process_syllabus(str(syllabus_dir), str(output_dir), formats=["md"])

        assert result["summary"]["md"] >= 1
        assert result["summary"]["pdf"] == 0
        assert result["summary"]["mp3"] == 0
        assert result["summary"]["docx"] == 0
        assert result["summary"]["html"] == 0
        assert result["summary"]["txt"] == 0

    def test_syllabus_md_file_created(self, temp_dir):
        """Verify MD file is actually created in output directory."""
        syllabus_dir = temp_dir / "syllabus"
        syllabus_dir.mkdir()
        (syllabus_dir / "Schedule.md").write_text(
            "# Schedule\n\nWeek 1: Introduction", encoding="utf-8"
        )

        output_dir = temp_dir / "output"
        result = process_syllabus(str(syllabus_dir), str(output_dir), formats=["md"])

        md_files = list(output_dir.rglob("*.md"))
        assert len(md_files) >= 1
        assert result["summary"]["md"] >= 1
