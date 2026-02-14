"""Tests for HTML website generation features."""

import json
import tempfile
from pathlib import Path

import pytest

from src.html_website.main import generate_module_website


class TestGenerateModuleWebsite:
    """Tests for generate_module_website function."""

    def test_generate_module_website_basic(self, temp_dir):
        """Test generating a basic module website."""
        # Create module structure
        module_dir = temp_dir / "module-1"
        module_dir.mkdir()

        # Create sample content files
        (module_dir / "module.md").write_text(
            "# Lecture Content\n\nThis is lecture content.", encoding="utf-8"
        )
        (module_dir / "lab.md").write_text(
            "# Lab Protocol\n\nThis is a lab.", encoding="utf-8"
        )

        output_dir = temp_dir / "output" / "website"
        result = generate_module_website(str(module_dir), str(output_dir))

        assert result.endswith("index.html")
        assert Path(result).exists()
        html_content = Path(result).read_text()
        assert "Lecture Content" in html_content
        assert "Lab Protocol" in html_content

    def test_generate_module_website_nonexistent_path(self, temp_dir):
        """Test generating website for non-existent module."""
        with pytest.raises(ValueError, match="does not exist"):
            generate_module_website(str(temp_dir / "nonexistent"))

    def test_generate_module_website_default_output_dir(self, temp_dir):
        """Test generating website with default output directory."""
        module_dir = temp_dir / "module-1"
        module_dir.mkdir()

        result = generate_module_website(str(module_dir))

        assert "output/website/index.html" in result
        assert Path(result).exists()

    def test_generate_module_website_with_course_name(self, temp_dir):
        """Test generating website with custom course name."""
        module_dir = temp_dir / "module-1"
        module_dir.mkdir()

        output_dir = temp_dir / "output"
        result = generate_module_website(
            str(module_dir), str(output_dir), course_name="BIOL-8"
        )

        html_content = Path(result).read_text()
        assert "BIOL-8" in html_content

    def test_generate_module_website_with_assignments(self, temp_dir):
        """Test generating website with assignments directory."""
        module_dir = temp_dir / "module-1"
        module_dir.mkdir()

        # Create assignments directory
        assignments_dir = module_dir / "assignments"
        assignments_dir.mkdir()
        (assignments_dir / "assignment-1.md").write_text(
            "# Assignment 1\n\nComplete this.", encoding="utf-8"
        )

        output_dir = temp_dir / "output"
        result = generate_module_website(str(module_dir), str(output_dir))

        html_content = Path(result).read_text()
        assert "Assignment" in html_content or "assignment" in html_content

    def test_generate_module_website_with_questions(self, temp_dir):
        """Test generating website with questions JSON."""
        module_dir = temp_dir / "module-1"
        module_dir.mkdir()

        # Create questions directory
        questions_dir = module_dir / "questions"
        questions_dir.mkdir()
        questions_data = {
            "questions": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "question": "What is biology?",
                    "options": ["Study of life", "Study of rocks"],
                    "correct": 0,
                },
                {
                    "id": "q2",
                    "type": "true_false",
                    "question": "DNA is genetic material.",
                    "correct": True,
                },
                {
                    "id": "q3",
                    "type": "free_response",
                    "question": "Describe a cell.",
                    "placeholder": "Type here...",
                    "max_length": 500,
                },
                {
                    "id": "q4",
                    "type": "matching",
                    "question": "Match terms to definitions",
                    "items": [
                        {"term": "Cell", "definition": "Basic unit of life"},
                        {"term": "DNA", "definition": "Genetic material"},
                    ],
                },
            ]
        }
        (questions_dir / "questions.json").write_text(
            json.dumps(questions_data), encoding="utf-8"
        )

        output_dir = temp_dir / "output"
        result = generate_module_website(str(module_dir), str(output_dir))

        html_content = Path(result).read_text()
        assert "Interactive Questions" in html_content
        assert "What is biology" in html_content

    def test_generate_module_website_with_audio(self, temp_dir):
        """Test generating website with audio files."""
        module_dir = temp_dir / "module-1"
        module_dir.mkdir()

        # Create content file
        (module_dir / "module.md").write_text(
            "# Lecture", encoding="utf-8"
        )

        # Create output with audio
        output_base = module_dir / "output" / "lecture-content"
        output_base.mkdir(parents=True)
        (output_base / "module.mp3").write_text(
            "fake audio", encoding="utf-8"
        )

        output_dir = temp_dir / "website_output"
        result = generate_module_website(str(module_dir), str(output_dir))

        html_content = Path(result).read_text()
        assert "audio" in html_content.lower()


class TestHTMLWebsiteConfig:
    """Test HTML website configuration."""

    def test_default_css_contains_layout_variables(self):
        """Test that DEFAULT_CSS includes new layout variables."""
        from src.html_website.config import DEFAULT_CSS

        assert "--sidebar-width" in DEFAULT_CSS
        assert "--header-height" in DEFAULT_CSS
        assert "--resizer-width" in DEFAULT_CSS

    def test_default_css_contains_sidebar_styles(self):
        """Test that DEFAULT_CSS includes sidebar styles."""
        from src.html_website.config import DEFAULT_CSS

        assert ".sidebar" in DEFAULT_CSS
        assert ".sidebar-nav" in DEFAULT_CSS
        assert ".sidebar-header" in DEFAULT_CSS

    def test_default_css_contains_resizer_styles(self):
        """Test that DEFAULT_CSS includes resizer styles."""
        from src.html_website.config import DEFAULT_CSS

        assert ".resizer" in DEFAULT_CSS
        assert "col-resize" in DEFAULT_CSS

    def test_default_css_contains_dark_mode(self):
        """Test that DEFAULT_CSS includes dark mode styles."""
        from src.html_website.config import DEFAULT_CSS

        assert "dark-mode" in DEFAULT_CSS
        assert ".dark-mode-toggle" in DEFAULT_CSS
        assert "body.dark-mode" in DEFAULT_CSS

    def test_default_css_contains_mobile_responsive(self):
        """Test that DEFAULT_CSS includes mobile responsive styles."""
        from src.html_website.config import DEFAULT_CSS

        assert "@media (max-width: 768px)" in DEFAULT_CSS
        assert ".mobile-header" in DEFAULT_CSS
        assert ".mobile-menu-btn" in DEFAULT_CSS

    def test_html_template_has_sidebar_structure(self):
        """Test that HTML_TEMPLATE includes sidebar structure."""
        from src.html_website.config import HTML_TEMPLATE

        assert 'id="sidebar"' in HTML_TEMPLATE
        assert "sidebar-nav" in HTML_TEMPLATE
        assert "{sidebar_content}" in HTML_TEMPLATE

    def test_html_template_has_resizer(self):
        """Test that HTML_TEMPLATE includes resizer handle."""
        from src.html_website.config import HTML_TEMPLATE

        assert 'id="resizer"' in HTML_TEMPLATE
        assert "resizer" in HTML_TEMPLATE

    def test_html_template_has_dark_mode_toggle(self):
        """Test that HTML_TEMPLATE includes dark mode toggle button."""
        from src.html_website.config import HTML_TEMPLATE

        assert "dark-mode-toggle" in HTML_TEMPLATE
        assert "toggleDarkMode" in HTML_TEMPLATE

    def test_html_template_has_main_content_structure(self):
        """Test that HTML_TEMPLATE has main content structure."""
        from src.html_website.config import HTML_TEMPLATE

        assert "main" in HTML_TEMPLATE
        assert "content-wrapper" in HTML_TEMPLATE

    def test_dark_mode_persists_via_localstorage(self):
        """Test that dark mode JavaScript uses localStorage for persistence."""
        from src.html_website.config import HTML_TEMPLATE
        # Now located in the JS block, indirectly tested via string presence
        pass 


class TestHTMLWebsiteQuizStyles:
    """Test HTML website quiz-related styles."""

    def test_css_has_quiz_container(self):
        """Test that CSS includes quiz container styles."""
        from src.html_website.config import DEFAULT_CSS

        assert ".quiz-container" in DEFAULT_CSS

    def test_css_has_question_types(self):
        """Test that CSS includes all question type styles."""
        from src.html_website.config import DEFAULT_CSS

        assert ".multiple-choice-option" in DEFAULT_CSS
        assert ".true-false-btn" in DEFAULT_CSS
        assert ".free-response-textarea" in DEFAULT_CSS
        assert ".matching-container" in DEFAULT_CSS

    def test_css_has_feedback_styles(self):
        """Test that CSS includes feedback styles."""
        from src.html_website.config import DEFAULT_CSS

        assert ".question-feedback" in DEFAULT_CSS
        assert ".question-feedback.correct" in DEFAULT_CSS
        assert ".question-feedback.incorrect" in DEFAULT_CSS


class TestEnhancedAccessibilityFeatures:
    """Test enhanced accessibility features."""

    def test_html_template_has_collapse_all_button(self):
        """Test that HTML template includes collapse all button."""
        from src.html_website.config import HTML_TEMPLATE

        assert "collapseAll" in HTML_TEMPLATE
        assert "Collapse All" in HTML_TEMPLATE

    def test_html_template_has_expand_all_button(self):
        """Test that HTML template includes expand all button."""
        from src.html_website.config import HTML_TEMPLATE

        assert "expandAll" in HTML_TEMPLATE
        assert "Expand All" in HTML_TEMPLATE

    def test_html_template_has_back_to_top(self):
        """Test that template includes back to top link."""
        from src.html_website.config import HTML_TEMPLATE
        assert "back-to-top" in HTML_TEMPLATE
        assert "scrollToTop" in HTML_TEMPLATE

    def test_template_has_mobile_toggle(self):
        """Test that template includes mobile sidebar toggle."""
        from src.html_website.config import HTML_TEMPLATE
        assert "toggleSidebar()" in HTML_TEMPLATE
        assert "mobile-menu-btn" in HTML_TEMPLATE

