"""Tests for HTML website utility functions."""

import json
import tempfile
from pathlib import Path

import pytest

from src.html_website.utils import (
    ensure_output_directory,
    extract_quiz_questions,
    find_audio_file,
    find_questions_file,
    find_text_file,
    get_relative_path,
    markdown_to_html,
    parse_questions_json,
    read_markdown_file,
)


class TestReadMarkdownFile:
    """Tests for read_markdown_file function."""

    def test_read_markdown_file_success(self, temp_dir):
        """Test reading an existing markdown file."""
        md_file = temp_dir / "test.md"
        md_file.write_text("# Test Content", encoding="utf-8")

        result = read_markdown_file(md_file)
        assert result == "# Test Content"

    def test_read_markdown_file_nonexistent(self, temp_dir):
        """Test reading a non-existent file raises error."""
        with pytest.raises(FileNotFoundError):
            read_markdown_file(temp_dir / "nonexistent.md")


class TestMarkdownToHtml:
    """Tests for markdown_to_html function."""

    def test_markdown_to_html_heading(self):
        """Test converting markdown heading to HTML."""
        result = markdown_to_html("# Hello World")
        assert "<h1>Hello World</h1>" in result

    def test_markdown_to_html_paragraph(self):
        """Test converting markdown paragraph to HTML."""
        result = markdown_to_html("This is a paragraph.")
        assert "<p>This is a paragraph.</p>" in result

    def test_markdown_to_html_list(self):
        """Test converting markdown list to HTML."""
        result = markdown_to_html("- Item 1\n- Item 2")
        assert "<ul>" in result
        assert "<li>Item 1</li>" in result
        assert "<li>Item 2</li>" in result

    def test_markdown_to_html_code_block(self):
        """Test converting markdown code block to HTML."""
        result = markdown_to_html("```python\nprint('hello')\n```")
        assert "<code" in result

    def test_markdown_to_html_table(self):
        """Test converting markdown table to HTML."""
        table = "| Col1 | Col2 |\n|------|------|\n| A | B |"
        result = markdown_to_html(table)
        assert "<table>" in result
        assert "<th>Col1</th>" in result


class TestFindAudioFile:
    """Tests for find_audio_file function."""

    def test_find_audio_file_exists(self, temp_dir):
        """Test finding an existing audio file."""
        curriculum_dir = temp_dir / "assignments"
        curriculum_dir.mkdir()
        audio_file = curriculum_dir / "lecture.mp3"
        audio_file.write_text("fake audio", encoding="utf-8")

        result = find_audio_file("lecture", temp_dir, "assignments")
        assert result == audio_file

    def test_find_audio_file_not_exists(self, temp_dir):
        """Test finding a non-existent audio file."""
        result = find_audio_file("missing", temp_dir, "assignments")
        assert result is None


class TestFindTextFile:
    """Tests for find_text_file function."""

    def test_find_text_file_exists(self, temp_dir):
        """Test finding an existing text file."""
        curriculum_dir = temp_dir / "lecture-content"
        curriculum_dir.mkdir()
        text_file = curriculum_dir / "notes.txt"
        text_file.write_text("text content", encoding="utf-8")

        result = find_text_file("notes", temp_dir, "lecture-content")
        assert result == text_file

    def test_find_text_file_not_exists(self, temp_dir):
        """Test finding a non-existent text file."""
        result = find_text_file("missing", temp_dir, "lecture-content")
        assert result is None


class TestGetRelativePath:
    """Tests for get_relative_path function."""

    def test_get_relative_path_success(self, temp_dir):
        """Test getting relative path."""
        target = temp_dir / "subdir" / "file.txt"
        result = get_relative_path(target, temp_dir)
        assert result == "subdir/file.txt"

    def test_get_relative_path_same_directory(self, temp_dir):
        """Test getting relative path for same directory."""
        target = temp_dir / "file.txt"
        result = get_relative_path(target, temp_dir)
        assert result == "file.txt"

    def test_get_relative_path_unrelated_paths(self):
        """Test getting relative path for unrelated paths."""
        target = Path("/a/b/c/file.txt")
        base = Path("/x/y/z")
        result = get_relative_path(target, base)
        # Should return absolute path since it can't be made relative
        assert result == str(target)


class TestExtractQuizQuestions:
    """Tests for extract_quiz_questions function."""

    def test_extract_quiz_questions_review_section(self):
        """Test extracting questions from Review Questions section."""
        content = """
# Study Guide

## Review Questions

1. What is the cell?
- A basic unit of life
- A type of protein
- A chemical reaction

2. What is DNA?
- Genetic material
- A protein
"""
        result = extract_quiz_questions(content)
        assert len(result) == 2
        assert result[0]["question"] == "What is the cell?"
        assert len(result[0]["options"]) == 3

    def test_extract_quiz_questions_practice_section(self):
        """Test extracting questions from Practice Problems section."""
        content = """
# Module 1

## Practice Problems

1. Calculate the rate.
- Option A
- Option B
"""
        result = extract_quiz_questions(content)
        assert len(result) == 1
        assert result[0]["question"] == "Calculate the rate."

    def test_extract_quiz_questions_none(self):
        """Test extracting from content with no questions."""
        content = "# No questions here"
        result = extract_quiz_questions(content)
        assert result == []


class TestEnsureOutputDirectory:
    """Tests for ensure_output_directory function."""

    def test_ensure_output_directory_creates(self, temp_dir):
        """Test creating a new directory."""
        new_dir = temp_dir / "new" / "nested"
        assert not new_dir.exists()

        ensure_output_directory(new_dir)
        assert new_dir.exists()

    def test_ensure_output_directory_exists(self, temp_dir):
        """Test handling existing directory."""
        # Should not raise
        ensure_output_directory(temp_dir)


class TestParseQuestionsJson:
    """Tests for parse_questions_json function."""

    def test_parse_questions_json_success(self, temp_dir):
        """Test parsing valid questions JSON."""
        questions_file = temp_dir / "questions.json"
        data = {
            "questions": [
                {"question": "Q1", "type": "multiple_choice"},
                {"question": "Q2", "type": "true_false"},
            ]
        }
        questions_file.write_text(json.dumps(data), encoding="utf-8")

        result = parse_questions_json(questions_file)
        assert len(result) == 2
        assert result[0]["question"] == "Q1"

    def test_parse_questions_json_empty(self, temp_dir):
        """Test parsing JSON with no questions key."""
        questions_file = temp_dir / "questions.json"
        questions_file.write_text("{}", encoding="utf-8")

        result = parse_questions_json(questions_file)
        assert result == []

    def test_parse_questions_json_nonexistent(self, temp_dir):
        """Test parsing non-existent file raises error."""
        with pytest.raises(FileNotFoundError):
            parse_questions_json(temp_dir / "missing.json")

    def test_parse_questions_json_invalid(self, temp_dir):
        """Test parsing invalid JSON raises error."""
        questions_file = temp_dir / "invalid.json"
        questions_file.write_text("not valid json", encoding="utf-8")

        with pytest.raises(json.JSONDecodeError):
            parse_questions_json(questions_file)


class TestFindQuestionsFile:
    """Tests for find_questions_file function."""

    def test_find_questions_file_exists(self, temp_dir):
        """Test finding existing questions file."""
        questions_dir = temp_dir / "questions"
        questions_dir.mkdir()
        questions_file = questions_dir / "questions.json"
        questions_file.write_text("{}", encoding="utf-8")

        result = find_questions_file(temp_dir)
        assert result == questions_file

    def test_find_questions_file_no_directory(self, temp_dir):
        """Test finding questions file when directory doesn't exist."""
        result = find_questions_file(temp_dir)
        assert result is None

    def test_find_questions_file_no_file(self, temp_dir):
        """Test finding questions file when file doesn't exist."""
        questions_dir = temp_dir / "questions"
        questions_dir.mkdir()

        result = find_questions_file(temp_dir)
        assert result is None
