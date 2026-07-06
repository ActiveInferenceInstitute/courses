"""Tests for content_processing utils module."""


from src.content_processing.utils import (
    extract_questions_from_sectioned,
    format_as_continuous,
)


class TestExtractQuestionsFromSectioned:
    """Tests for extract_questions_from_sectioned function."""

    def test_extracts_asterisk_bullets(self):
        """Test extraction of asterisk bullet questions."""
        content = (
            "# Questions\n\n"
            "### Part 1: Cell Biology\n\n"
            "1.  **Cell Structure**\n"
            "    *   What is the function of mitochondria in cellular respiration?\n"
            "    *   How does the cell membrane regulate molecular transport?\n"
        )

        questions = extract_questions_from_sectioned(content)

        assert len(questions) == 2
        assert "mitochondria" in questions[0]
        assert "cell membrane" in questions[1]

    def test_extracts_dash_bullets(self):
        """Test extraction of dash bullet questions."""
        content = (
            "# Questions\n\n"
            "### Part 1\n\n"
            "1.  **Topic**\n"
            "    -   What is the role of DNA in heredity?\n"
            "    -   How do enzymes catalyze biochemical reactions?\n"
        )

        questions = extract_questions_from_sectioned(content)

        assert len(questions) == 2
        assert "DNA" in questions[0]
        assert "enzymes" in questions[1]

    def test_skips_short_items(self):
        """Test that very short items (<=5 chars) are skipped."""
        content = (
            "# Questions\n\n"
            "    *   Yes\n"
            "    *   What is the role of ribosomes in protein synthesis?\n"
        )

        questions = extract_questions_from_sectioned(content)

        assert len(questions) == 1
        assert "ribosomes" in questions[0]

    def test_empty_content(self):
        """Test with empty content."""
        questions = extract_questions_from_sectioned("")
        assert questions == []

    def test_no_bullet_points(self):
        """Test content without any bullet points."""
        content = "# Questions\n\nSome text without bullets.\n"

        questions = extract_questions_from_sectioned(content)

        assert questions == []

    def test_multiple_sections(self):
        """Test extraction across multiple sections."""
        content = (
            "# Module Questions\n\n"
            "### Part 1: Basics\n\n"
            "1.  **Topic A**\n"
            "    *   How does photosynthesis convert light energy to chemical?\n\n"
            "### Part 2: Advanced\n\n"
            "2.  **Topic B**\n"
            "    *   What role does ATP play in cellular energy transfer?\n"
            "    *   How do mitotic spindle fibers ensure chromosome separation?\n"
        )

        questions = extract_questions_from_sectioned(content)

        assert len(questions) == 3


class TestFormatAsContinuous:
    """Tests for format_as_continuous function."""

    def test_basic_formatting(self):
        """Test basic continuous numbering output."""
        questions = ["What is biology?", "How do cells divide?"]
        result = format_as_continuous(questions, "Module 1 Questions")

        assert result.startswith("# Module 1 Questions\n")
        assert "1. What is biology?" in result
        assert "2. How do cells divide?" in result

    def test_empty_list(self):
        """Test formatting with empty question list."""
        result = format_as_continuous([], "Empty")

        assert result == "# Empty\n"

    def test_single_question(self):
        """Test formatting with single question."""
        result = format_as_continuous(["Only question?"], "Test")

        assert "1. Only question?" in result
        # Should not have "2."
        assert "2." not in result

    def test_preserves_question_text(self):
        """Test that question text is preserved exactly."""
        questions = ["What is **bold** text in markdown?"]
        result = format_as_continuous(questions, "Title")

        assert "1. What is **bold** text in markdown?" in result
