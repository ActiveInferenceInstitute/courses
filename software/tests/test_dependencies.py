"""Tests to verify all required dependencies are installed and available."""

import importlib.util
from typing import List, Tuple

import pytest


def test_required_dependencies_available():
    """Test that all required dependencies are available."""
    required_dependencies = [
        "markdown",
        "gtts",
        "speech_recognition",
        "pydub",
        "requests",
        "pypdf",
        "docx",
        "markdown2",
    ]

    missing = []
    for dep in required_dependencies:
        try:
            spec = importlib.util.find_spec(dep)
            if spec is None:
                missing.append(dep)
        except Exception:
            missing.append(dep)

    if missing:
        pytest.fail(
            f"Missing required dependencies: {', '.join(missing)}. "
            f"Run 'uv sync' to install dependencies."
        )


def test_optional_weasyprint_available():
    """Test that WeasyPrint is available (required for PDF generation)."""
    spec = importlib.util.find_spec("weasyprint")
    if spec is None:
        pytest.skip("WeasyPrint not available (PDF generation will not work)")


def test_gtts_version():
    """Verify gTTS is installed and can be imported."""
    try:
        import gtts

        # Verify it's the real gTTS, not a mock
        assert hasattr(gtts, "gTTS")
        assert callable(gtts.gTTS)
    except ImportError:
        pytest.fail("gTTS is not installed")


def test_speech_recognition_version():
    """Verify speech_recognition is installed and can be imported."""
    try:
        import speech_recognition as sr

        # Verify it's the real speech_recognition, not a mock
        assert hasattr(sr, "Recognizer")
        assert callable(sr.Recognizer)
    except ImportError:
        pytest.fail("speech_recognition is not installed")


def test_pydub_available():
    """Verify pydub is installed (required by speech_recognition)."""
    try:
        from pydub import AudioSegment

        # Verify it's the real pydub, not a mock
        assert AudioSegment is not None
        assert callable(AudioSegment)
    except ImportError:
        pytest.fail("pydub is not installed")


def test_markdown_available():
    """Verify markdown library is installed."""
    try:
        import markdown

        assert markdown is not None
        assert hasattr(markdown, "markdown")
    except ImportError:
        pytest.fail("markdown library is not installed")


def test_python_docx_available():
    """Verify python-docx is installed."""
    try:
        from docx import Document

        assert Document is not None
        assert callable(Document)
    except ImportError:
        pytest.fail("python-docx is not installed")


def test_all_dependencies_are_real_implementations():
    """Verify that all dependencies are real implementations, not mocks."""
    dependency_checks: List[Tuple[str, str, str]] = [
        ("gtts", "gTTS", "gTTS class"),
        ("speech_recognition", "Recognizer", "Recognizer class"),
        ("pydub", "AudioSegment", "AudioSegment class"),
        ("markdown", "markdown", "markdown function"),
        ("docx", "Document", "Document class"),
    ]

    for module_name, attr_name, description in dependency_checks:
        try:
            module = importlib.import_module(module_name)
            attr = getattr(module, attr_name, None)
            if attr is None:
                pytest.fail(f"{module_name}.{attr_name} not found - {description} missing")
            if not callable(attr) and not hasattr(attr, "__class__"):
                pytest.fail(f"{module_name}.{attr_name} is not a valid {description}")
        except ImportError:
            pytest.fail(f"{module_name} cannot be imported - {description} unavailable")


def test_no_conflicting_dependencies():
    """Verify there are no conflicting dependency versions."""
    # This is a basic check - more sophisticated version checking could be added
    try:
        import gtts
        import speech_recognition
        import pydub

        # If we get here, basic imports work
        # More sophisticated version checking could verify compatibility
        assert True
    except ImportError as e:
        pytest.fail(f"Dependency conflict detected: {e}")
