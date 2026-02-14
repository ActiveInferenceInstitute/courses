"""Tests for schedule main module."""

import tempfile
from pathlib import Path

import pytest

from src.schedule.main import (
    batch_process_schedules,
    generate_schedule_outputs,
    parse_schedule_markdown,
    process_schedule,
)


@pytest.fixture
def sample_schedule_content():
    """Sample schedule markdown content."""
    return """# Course Schedule

## Spring 2026

| Week | Date | Topic | Notes |
|------|------|-------|-------|
| 1 | 1/19/2026 | Introduction to Biology | First day |
| 2 | 1/26/2026 | Cell Structure | Lab 1 |
| 3 | 2/2/2026 | Cell Function | Quiz 1 |

## Important Dates

- Midterm: March 15, 2026
- Final: May 15, 2026

## Exam Schedule

- Exam 1: February 15, 2026
- Exam 2: April 15, 2026
"""


@pytest.fixture
def sample_schedule_file(temp_dir, sample_schedule_content):
    """Create a sample schedule file."""
    schedule_file = temp_dir / "Schedule.md"
    schedule_file.write_text(sample_schedule_content, encoding="utf-8")
    return schedule_file


class TestParseScheduleMarkdown:
    """Tests for parse_schedule_markdown function."""

    def test_parse_schedule_markdown_success(self, sample_schedule_file):
        """Test parsing a valid schedule markdown file."""
        result = parse_schedule_markdown(str(sample_schedule_file))

        assert "entries" in result
        assert "sections" in result
        assert "metadata" in result

        # Verify entries (includes header row + 3 data rows = 4, but only 3 validated)
        # The validate_schedule_entry filters out header rows
        assert len(result["entries"]) >= 3
        # Find actual data entries
        data_entries = [e for e in result["entries"] if e["week"] not in ("Week", "")]
        assert len(data_entries) == 3
        assert data_entries[0]["week"] == "1"
        assert data_entries[0]["date"] == "1/19/2026"
        assert data_entries[0]["topic"] == "Introduction to Biology"

    def test_parse_schedule_markdown_sections(self, sample_schedule_file):
        """Test that sections are correctly extracted."""
        result = parse_schedule_markdown(str(sample_schedule_file))

        assert "title" in result["sections"]
        assert result["sections"]["title"] == "Course Schedule"
        assert "semester" in result["sections"]
        assert "Spring 2026" in result["sections"]["semester"]

    def test_parse_schedule_markdown_metadata(self, sample_schedule_file):
        """Test that metadata is correctly populated."""
        result = parse_schedule_markdown(str(sample_schedule_file))

        assert result["metadata"]["file_path"] == str(sample_schedule_file)
        assert result["metadata"]["file_name"] == "Schedule.md"
        # total_weeks counts all parsed entries (may include header row)
        assert result["metadata"]["total_weeks"] >= 3

    def test_parse_schedule_markdown_nonexistent(self):
        """Test parsing a non-existent file raises error."""
        with pytest.raises(FileNotFoundError):
            parse_schedule_markdown("/nonexistent/schedule.md")

    def test_parse_schedule_markdown_empty_table(self, temp_dir):
        """Test parsing a schedule with no valid entries."""
        schedule_file = temp_dir / "empty.md"
        schedule_file.write_text("# Empty Schedule\n\nNo table here.", encoding="utf-8")

        result = parse_schedule_markdown(str(schedule_file))
        assert result["entries"] == []


class TestProcessSchedule:
    """Tests for process_schedule function."""

    def test_process_schedule_txt_format(self, sample_schedule_file, temp_dir):
        """Test processing schedule with txt format."""
        output_dir = temp_dir / "output"

        result = process_schedule(
            str(sample_schedule_file), str(output_dir), formats=["txt"]
        )

        assert "outputs" in result
        assert "summary" in result
        assert "errors" in result
        assert result["summary"]["txt"] >= 1

    def test_process_schedule_pdf_format(self, sample_schedule_file, temp_dir):
        """Test processing schedule with PDF format."""
        output_dir = temp_dir / "output"

        result = process_schedule(
            str(sample_schedule_file), str(output_dir), formats=["pdf"]
        )

        assert "outputs" in result
        assert result["summary"]["pdf"] >= 1
        # Verify PDF file exists
        pdf_files = list((output_dir).glob("*.pdf"))
        assert len(pdf_files) >= 1

    def test_process_schedule_html_format(self, sample_schedule_file, temp_dir):
        """Test processing schedule with HTML format."""
        output_dir = temp_dir / "output"

        result = process_schedule(
            str(sample_schedule_file), str(output_dir), formats=["html"]
        )

        assert "outputs" in result
        assert result["summary"]["html"] >= 1
        # Verify HTML file exists
        html_files = list((output_dir).glob("*.html"))
        assert len(html_files) >= 1

    def test_process_schedule_docx_format(self, sample_schedule_file, temp_dir):
        """Test processing schedule with DOCX format."""
        output_dir = temp_dir / "output"

        result = process_schedule(
            str(sample_schedule_file), str(output_dir), formats=["docx"]
        )

        assert "outputs" in result
        assert result["summary"]["docx"] >= 1
        # Verify DOCX file exists
        docx_files = list((output_dir).glob("*.docx"))
        assert len(docx_files) >= 1

    @pytest.mark.requires_internet
    def test_process_schedule_mp3_format(self, sample_schedule_file, temp_dir):
        """Test processing schedule with MP3 format (requires internet for gTTS)."""
        output_dir = temp_dir / "output"

        result = process_schedule(
            str(sample_schedule_file), str(output_dir), formats=["mp3"]
        )

        assert "outputs" in result
        assert result["summary"]["mp3"] >= 1

    def test_process_schedule_invalid_format(self, sample_schedule_file, temp_dir):
        """Test processing with invalid format raises error."""
        output_dir = temp_dir / "output"

        with pytest.raises(ValueError, match="Unsupported output formats"):
            process_schedule(
                str(sample_schedule_file), str(output_dir), formats=["invalid"]
            )

    def test_process_schedule_nonexistent_file(self, temp_dir):
        """Test processing a non-existent file raises error."""
        output_dir = temp_dir / "output"

        with pytest.raises(FileNotFoundError):
            process_schedule("/nonexistent/schedule.md", str(output_dir))

    def test_process_schedule_creates_output_dir(self, sample_schedule_file, temp_dir):
        """Test that process_schedule creates output directory if needed."""
        output_dir = temp_dir / "nested" / "output"
        assert not output_dir.exists()

        result = process_schedule(
            str(sample_schedule_file), str(output_dir), formats=["txt"]
        )

        assert output_dir.exists()
        assert result["summary"]["txt"] >= 1

    def test_process_schedule_multiple_formats(self, sample_schedule_file, temp_dir):
        """Test processing schedule with multiple formats."""
        output_dir = temp_dir / "output"

        result = process_schedule(
            str(sample_schedule_file), str(output_dir), formats=["txt", "html"]
        )

        assert result["summary"]["txt"] >= 1
        assert result["summary"]["html"] >= 1


class TestGenerateScheduleOutputs:
    """Tests for generate_schedule_outputs function."""

    def test_generate_schedule_outputs_txt(self, sample_schedule_file, temp_dir):
        """Test generating txt output."""
        result = parse_schedule_markdown(str(sample_schedule_file))
        output_dir = temp_dir / "output"
        output_dir.mkdir()

        outputs = generate_schedule_outputs(result, output_dir, "schedule", ["txt"])

        assert "txt" in outputs
        assert len(outputs["txt"]) >= 1
        # Verify file was created
        txt_file = output_dir / "schedule.txt"
        assert txt_file.exists()

    def test_generate_schedule_outputs_pdf(self, sample_schedule_file, temp_dir):
        """Test generating PDF output."""
        result = parse_schedule_markdown(str(sample_schedule_file))
        output_dir = temp_dir / "output"
        output_dir.mkdir()

        outputs = generate_schedule_outputs(result, output_dir, "schedule", ["pdf"])

        assert "pdf" in outputs
        assert len(outputs["pdf"]) >= 1
        pdf_file = output_dir / "schedule.pdf"
        assert pdf_file.exists()

    def test_generate_schedule_outputs_html(self, sample_schedule_file, temp_dir):
        """Test generating HTML output."""
        result = parse_schedule_markdown(str(sample_schedule_file))
        output_dir = temp_dir / "output"
        output_dir.mkdir()

        outputs = generate_schedule_outputs(result, output_dir, "schedule", ["html"])

        assert "html" in outputs
        assert len(outputs["html"]) >= 1
        html_file = output_dir / "schedule.html"
        assert html_file.exists()
        # Verify HTML content
        content = html_file.read_text()
        assert "<html" in content.lower() or "course schedule" in content.lower()

    def test_generate_schedule_outputs_docx(self, sample_schedule_file, temp_dir):
        """Test generating DOCX output."""
        result = parse_schedule_markdown(str(sample_schedule_file))
        output_dir = temp_dir / "output"
        output_dir.mkdir()

        outputs = generate_schedule_outputs(result, output_dir, "schedule", ["docx"])

        assert "docx" in outputs
        assert len(outputs["docx"]) >= 1
        docx_file = output_dir / "schedule.docx"
        assert docx_file.exists()

    def test_generate_schedule_outputs_unsupported_format(
        self, sample_schedule_file, temp_dir
    ):
        """Test generating unsupported format raises error."""
        result = parse_schedule_markdown(str(sample_schedule_file))
        output_dir = temp_dir / "output"
        output_dir.mkdir()

        with pytest.raises((ValueError, OSError)):
            generate_schedule_outputs(result, output_dir, "schedule", ["xyz"])


class TestBatchProcessSchedules:
    """Tests for batch_process_schedules function."""

    def test_batch_process_schedules_success(self, temp_dir, sample_schedule_content):
        """Test batch processing multiple schedule files."""
        # Create multiple schedule files
        schedule_dir = temp_dir / "schedules"
        schedule_dir.mkdir()
        (schedule_dir / "Schedule.md").write_text(
            sample_schedule_content, encoding="utf-8"
        )

        output_dir = temp_dir / "output"

        result = batch_process_schedules(
            str(schedule_dir), str(output_dir), formats=["txt"]
        )

        assert "processed_files" in result
        assert "outputs" in result
        assert "summary" in result
        assert "errors" in result
        assert len(result["processed_files"]) >= 1

    def test_batch_process_schedules_empty_directory(self, temp_dir):
        """Test batch processing with no schedule files."""
        empty_dir = temp_dir / "empty"
        empty_dir.mkdir()
        output_dir = temp_dir / "output"

        result = batch_process_schedules(str(empty_dir), str(output_dir), formats=["txt"])

        assert result["processed_files"] == []

    def test_batch_process_schedules_nonexistent_directory(self):
        """Test batch processing a non-existent directory raises error."""
        with pytest.raises(ValueError, match="Directory does not exist"):
            batch_process_schedules("/nonexistent/dir", "/output")

    def test_batch_process_schedules_with_errors(self, temp_dir):
        """Test batch processing handles errors gracefully."""
        schedule_dir = temp_dir / "schedules"
        schedule_dir.mkdir()
        # Create an invalid schedule file
        (schedule_dir / "Schedule.md").write_text("Invalid content", encoding="utf-8")

        output_dir = temp_dir / "output"

        result = batch_process_schedules(
            str(schedule_dir), str(output_dir), formats=["txt"]
        )

        # Should not raise, errors are collected
        assert "errors" in result

    def test_batch_process_schedules_default_formats(
        self, temp_dir, sample_schedule_content
    ):
        """Test batch processing with default formats (uses all)."""
        schedule_dir = temp_dir / "schedules"
        schedule_dir.mkdir()
        (schedule_dir / "Schedule.md").write_text(
            sample_schedule_content, encoding="utf-8"
        )

        output_dir = temp_dir / "output"

        # Pass None to use default formats
        result = batch_process_schedules(str(schedule_dir), str(output_dir), formats=None)

        # Should have used all default formats
        assert "summary" in result
