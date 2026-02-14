"""Tests for content_processing/utils.py utility functions."""

from src.content_processing.utils import (
    extract_questions_from_sectioned,
    format_as_continuous,
    normalize_whitespace,
    extract_headers,
    count_questions,
    extract_numbered_items,
    validate_question_format,
)


class TestExtractQuestionsFromSectioned:
    """Tests for extract_questions_from_sectioned function."""

    def test_empty_content(self):
        """Empty content returns empty list."""
        result = extract_questions_from_sectioned("")
        assert result == []

    def test_no_bullet_points(self):
        """Content without bullet points returns empty."""
        content = "# Title\n\nSome text content"
        result = extract_questions_from_sectioned(content)
        assert result == []

    def test_asterisk_bullet_points(self):
        """Extracts questions from asterisk bullets."""
        content = """# Questions
* What is biology?
* How do cells divide?
"""
        result = extract_questions_from_sectioned(content)
        assert len(result) == 2
        assert "What is biology?" in result
        assert "How do cells divide?" in result

    def test_dash_bullet_points(self):
        """Extracts questions from dash bullets."""
        content = """# Questions
- First question here?
- Second question here?
"""
        result = extract_questions_from_sectioned(content)
        assert len(result) == 2

    def test_skips_short_items(self):
        """Items with <= 5 characters are skipped."""
        content = """# List
* Hi
* What is the definition of a cell?
"""
        result = extract_questions_from_sectioned(content)
        assert len(result) == 1
        assert "What is the definition of a cell?" in result


class TestFormatAsContinuous:
    """Tests for format_as_continuous function."""

    def test_empty_questions(self):
        """Empty question list returns just title."""
        result = format_as_continuous([], "Test Title")
        assert "# Test Title" in result

    def test_single_question(self):
        """Single question is numbered."""
        result = format_as_continuous(["What is DNA?"], "Biology")
        assert "# Biology" in result
        assert "1. What is DNA?" in result

    def test_multiple_questions(self):
        """Multiple questions are numbered sequentially."""
        questions = ["First question?", "Second question?", "Third question?"]
        result = format_as_continuous(questions, "Quiz")
        assert "1. First question?" in result
        assert "2. Second question?" in result
        assert "3. Third question?" in result


class TestNormalizeWhitespace:
    """Tests for normalize_whitespace function."""

    def test_removes_trailing_whitespace(self):
        """Trailing whitespace is removed from lines."""
        content = "Line one   \nLine two \n"
        result = normalize_whitespace(content)
        assert "   \n" not in result
        assert " \n" not in result

    def test_collapses_multiple_blank_lines(self):
        """More than 2 consecutive blank lines are collapsed to 2."""
        content = "Line one\n\n\n\n\nLine two"
        result = normalize_whitespace(content)
        # Should have at most 2 blank lines (3 consecutive newlines)
        assert "\n\n\n\n" not in result  # 4+ newlines should not exist

    def test_ends_with_single_newline(self):
        """Output ends with exactly one newline."""
        content = "Content here"
        result = normalize_whitespace(content)
        assert result.endswith('\n')
        assert not result.endswith('\n\n')

    def test_preserves_single_blank_lines(self):
        """Single blank lines are preserved."""
        content = "Paragraph one\n\nParagraph two"
        result = normalize_whitespace(content)
        assert "Paragraph one\n\nParagraph two" in result


class TestExtractHeaders:
    """Tests for extract_headers function."""

    def test_empty_content(self):
        """Empty content returns empty list."""
        result = extract_headers("")
        assert result == []

    def test_single_h1(self):
        """Single H1 header is extracted."""
        content = "# Main Title\n\nSome content"
        result = extract_headers(content)
        assert len(result) == 1
        assert result[0] == (1, "Main Title")

    def test_multiple_levels(self):
        """Multiple header levels are extracted with correct levels."""
        content = """# Title
## Section One
### Subsection
## Section Two
"""
        result = extract_headers(content)
        assert len(result) == 4
        assert result[0] == (1, "Title")
        assert result[1] == (2, "Section One")
        assert result[2] == (3, "Subsection")
        assert result[3] == (2, "Section Two")

    def test_ignores_non_headers(self):
        """Non-header lines are ignored."""
        content = """# Header
This is not #a header
Neither is this
"""
        result = extract_headers(content)
        assert len(result) == 1


class TestCountQuestions:
    """Tests for count_questions function."""

    def test_empty_content(self):
        """Empty content returns all zeros."""
        result = count_questions("")
        assert result == {"numbered": 0, "bulleted": 0, "inline": 0}

    def test_numbered_questions(self):
        """Numbered questions are counted."""
        content = """1. First question?
2. Second question?
3. Third question?
"""
        result = count_questions(content)
        assert result["numbered"] == 3

    def test_bulleted_questions(self):
        """Bulleted questions are counted."""
        content = """* Question one
* Question two
- Question three
"""
        result = count_questions(content)
        assert result["bulleted"] == 3

    def test_inline_questions(self):
        """Lines with ? are counted as inline."""
        content = """What is this?
How does it work?
This is a statement.
"""
        result = count_questions(content)
        assert result["inline"] == 2

    def test_mixed_types(self):
        """Mixed question types all counted correctly."""
        content = """1. Numbered question?
* Bulleted question?
Is this inline?
"""
        result = count_questions(content)
        assert result["numbered"] == 1
        assert result["bulleted"] == 1
        assert result["inline"] == 1


class TestExtractNumberedItems:
    """Tests for extract_numbered_items function."""

    def test_empty_content(self):
        """Empty content returns empty list."""
        result = extract_numbered_items("")
        assert result == []

    def test_single_item(self):
        """Single numbered item is extracted."""
        content = "1. First item here"
        result = extract_numbered_items(content)
        assert result == ["First item here"]

    def test_multiple_items(self):
        """Multiple numbered items extracted in order."""
        content = """1. First
2. Second
3. Third
"""
        result = extract_numbered_items(content)
        assert result == ["First", "Second", "Third"]

    def test_double_digit_numbers(self):
        """Double digit numbers work."""
        content = "12. Twelfth item"
        result = extract_numbered_items(content)
        assert result == ["Twelfth item"]

    def test_ignores_non_numbered(self):
        """Non-numbered lines are ignored."""
        content = """1. Numbered
Regular text
2. Also numbered
* Bulleted
"""
        result = extract_numbered_items(content)
        assert len(result) == 2


class TestValidateQuestionFormat:
    """Tests for validate_question_format function."""

    def test_valid_format(self):
        """Valid question file passes."""
        content = """# Module 1 Questions

1. What is biology?
2. How do cells work?
"""
        result = validate_question_format(content)
        assert result["valid"] is True
        assert result["has_title"] is True
        assert result["question_count"] == 2
        assert result["issues"] == []

    def test_missing_title(self):
        """Missing title is reported."""
        content = """1. What is biology?
2. How do cells work?
"""
        result = validate_question_format(content)
        assert result["valid"] is False
        assert result["has_title"] is False
        assert "Missing title" in result["issues"][0]

    def test_no_questions(self):
        """No questions is reported."""
        content = "# Title\n\nJust some text."
        result = validate_question_format(content)
        assert result["valid"] is False
        assert "No questions found" in str(result["issues"])

    def test_bulleted_questions_counted(self):
        """Bulleted questions are also counted."""
        content = """# Questions
* First question?
* Second question?
"""
        result = validate_question_format(content)
        assert result["valid"] is True
        assert result["question_count"] == 2
