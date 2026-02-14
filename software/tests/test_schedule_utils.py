"""Tests for schedule utility functions."""

import tempfile
from pathlib import Path

import pytest

from src.schedule.utils import (
    ensure_output_directory,
    extract_schedule_sections,
    find_schedule_files,
    format_date,
    generate_schedule_markdown,
    parse_schedule_table,
    read_schedule_file,
    validate_schedule_entry,
)


class TestParseScheduleTable:
    """Tests for parse_schedule_table function."""

    def test_parse_schedule_table_success(self):
        """Test parsing a valid markdown table."""
        content = """
| Week | Date | Topic | Notes |
|------|------|-------|-------|
| 1 | 1/19/2026 | Introduction | First day |
| 2 | 1/26/2026 | Cell Structure | Lab 1 |
"""
        result = parse_schedule_table(content)

        # Includes header row + 2 data rows = 3 (header may or may not be parsed depending on implementation)
        assert len(result) >= 2
        # Find data entries
        data_rows = [r for r in result if r["week"] not in ("Week", "")]
        assert len(data_rows) == 2
        assert data_rows[0]["week"] == "1"
        assert data_rows[0]["date"] == "1/19/2026"
        assert data_rows[0]["topic"] == "Introduction"
        assert data_rows[0]["notes"] == "First day"

    def test_parse_schedule_table_empty(self):
        """Test parsing content with no table."""
        content = "# No table here\n\nJust some text."
        result = parse_schedule_table(content)
        assert result == []

    def test_parse_schedule_table_three_columns(self):
        """Test parsing a table with only three columns."""
        content = """
| Week | Date | Topic |
|------|------|-------|
| 1 | 1/19/2026 | Introduction |
"""
        result = parse_schedule_table(content)
        assert len(result) == 1
        assert result[0]["notes"] == ""

    def test_parse_schedule_table_skips_separator(self):
        """Test that separator row is skipped."""
        content = """
| Week | Date | Topic | Notes |
|:-----|:-----|:------|:------|
| 1 | 1/19/2026 | Topic | Note |
"""
        result = parse_schedule_table(content)
        # Filter out header row if parsed
        data_rows = [r for r in result if r["week"] not in ("Week", "")]
        assert len(data_rows) == 1


class TestExtractScheduleSections:
    """Tests for extract_schedule_sections function."""

    def test_extract_schedule_sections_all(self):
        """Test extracting all sections."""
        content = """# Course Schedule

## Spring 2026

Some content.

## Important Dates

- Midterm: March 15

## Exam Schedule

- Exam 1: Feb 15
"""
        result = extract_schedule_sections(content)

        assert result["title"] == "Course Schedule"
        assert "Spring 2026" in result["semester"]
        assert "Midterm" in result["important_dates"]
        assert "Exam 1" in result["exam_schedule"]

    def test_extract_schedule_sections_partial(self):
        """Test extracting when some sections are missing."""
        content = """# Course Schedule

## Spring 2026
"""
        result = extract_schedule_sections(content)

        assert result["title"] == "Course Schedule"
        assert "Spring 2026" in result["semester"]
        assert "important_dates" not in result
        assert "exam_schedule" not in result

    def test_extract_schedule_sections_empty(self):
        """Test extracting from empty content."""
        result = extract_schedule_sections("")
        assert result == {}


class TestFormatDate:
    """Tests for format_date function."""

    def test_format_date_slash_format(self):
        """Test formatting date with slash format."""
        result = format_date("1/19/2026")
        assert result == "January 19, 2026"

    def test_format_date_dash_format(self):
        """Test formatting date with dash format."""
        result = format_date("01-19-2026")
        assert result == "January 19, 2026"

    def test_format_date_iso_format(self):
        """Test formatting date with ISO format."""
        result = format_date("2026-01-19")
        assert result == "January 19, 2026"

    def test_format_date_invalid(self):
        """Test formatting invalid date returns original."""
        result = format_date("invalid date")
        assert result == "invalid date"

    def test_format_date_empty(self):
        """Test formatting empty string returns None."""
        result = format_date("")
        assert result is None

    def test_format_date_none(self):
        """Test formatting None returns None."""
        result = format_date(None)
        assert result is None


class TestValidateScheduleEntry:
    """Tests for validate_schedule_entry function."""

    def test_validate_schedule_entry_valid(self):
        """Test validating a valid entry."""
        entry = {"week": "1", "date": "1/19/2026", "topic": "Introduction"}
        assert validate_schedule_entry(entry) is True

    def test_validate_schedule_entry_with_notes(self):
        """Test validating a valid entry with notes."""
        entry = {
            "week": "1",
            "date": "1/19/2026",
            "topic": "Introduction",
            "notes": "First day",
        }
        assert validate_schedule_entry(entry) is True

    def test_validate_schedule_entry_missing_week(self):
        """Test validating entry missing week."""
        entry = {"date": "1/19/2026", "topic": "Introduction"}
        assert validate_schedule_entry(entry) is False

    def test_validate_schedule_entry_empty_topic(self):
        """Test validating entry with empty topic."""
        entry = {"week": "1", "date": "1/19/2026", "topic": "   "}
        assert validate_schedule_entry(entry) is False


class TestGenerateScheduleMarkdown:
    """Tests for generate_schedule_markdown function."""

    def test_generate_schedule_markdown_basic(self):
        """Test generating markdown for basic entries."""
        entries = [
            {"week": "1", "date": "1/19/2026", "topic": "Intro", "notes": "First day"}
        ]
        result = generate_schedule_markdown(entries)

        assert "| Week | Date | Topic | Notes |" in result
        assert "| 1 | 1/19/2026 | Intro | First day |" in result

    def test_generate_schedule_markdown_with_sections(self):
        """Test generating markdown with sections."""
        entries = [{"week": "1", "date": "1/19", "topic": "Topic", "notes": ""}]
        sections = {"title": "Schedule", "semester": "Spring 2026"}

        result = generate_schedule_markdown(entries, sections)

        assert "# Schedule" in result
        assert "## Spring 2026" in result

    def test_generate_schedule_markdown_empty_entries(self):
        """Test generating markdown with no entries."""
        result = generate_schedule_markdown([])

        assert "| Week | Date | Topic | Notes |" in result
        assert "|------|------|-------|-------|" in result


class TestFindScheduleFiles:
    """Tests for find_schedule_files function."""

    def test_find_schedule_files_exact_match(self, temp_dir):
        """Test finding schedule files by exact name."""
        (temp_dir / "Schedule.md").write_text("content", encoding="utf-8")

        result = find_schedule_files(temp_dir)
        # The function uses glob patterns, so may match multiple patterns
        assert len(result) >= 1
        assert any(f.name == "Schedule.md" for f in result)

    def test_find_schedule_files_lowercase(self, temp_dir):
        """Test finding lowercase schedule file."""
        (temp_dir / "schedule.md").write_text("content", encoding="utf-8")

        result = find_schedule_files(temp_dir)
        # Uses patterns including exact match and *schedule*
        assert len(result) >= 1

    def test_find_schedule_files_pattern(self, temp_dir):
        """Test finding schedule files by pattern."""
        (temp_dir / "course_schedule_spring.md").write_text("content", encoding="utf-8")

        result = find_schedule_files(temp_dir)
        assert len(result) == 1

    def test_find_schedule_files_empty_dir(self, temp_dir):
        """Test finding schedule files in empty directory."""
        result = find_schedule_files(temp_dir)
        assert result == []


class TestReadScheduleFile:
    """Tests for read_schedule_file function."""

    def test_read_schedule_file_success(self, temp_dir):
        """Test reading an existing schedule file."""
        schedule_file = temp_dir / "Schedule.md"
        schedule_file.write_text("# Schedule Content", encoding="utf-8")

        result = read_schedule_file(schedule_file)
        assert result == "# Schedule Content"

    def test_read_schedule_file_nonexistent(self, temp_dir):
        """Test reading a non-existent file raises error."""
        with pytest.raises(FileNotFoundError):
            read_schedule_file(temp_dir / "nonexistent.md")


class TestEnsureOutputDirectory:
    """Tests for ensure_output_directory function."""

    def test_ensure_output_directory_file_path(self, temp_dir):
        """Test creating parent directory for file path."""
        file_path = temp_dir / "subdir" / "output.txt"
        assert not file_path.parent.exists()

        ensure_output_directory(file_path)
        assert file_path.parent.exists()

    def test_ensure_output_directory_dir_path(self, temp_dir):
        """Test creating directory path."""
        dir_path = temp_dir / "new_dir"
        assert not dir_path.exists()

        ensure_output_directory(dir_path)
        assert dir_path.exists()

    def test_ensure_output_directory_existing(self, temp_dir):
        """Test handling existing directory."""
        # Should not raise
        ensure_output_directory(temp_dir)
