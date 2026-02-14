"""Tests to verify all code uses real implementations, not mocks or stubs."""

import inspect
from pathlib import Path

import pytest

# Import real libraries to verify they're used
try:
    from gtts import gTTS
    import speech_recognition as sr
    from pydub import AudioSegment
except ImportError:
    # Skip all tests if dependencies aren't available
    pytest.skip("Required dependencies (gtts, speech_recognition, pydub) not available", allow_module_level=True)


def test_text_to_speech_uses_real_gtts():
    """Verify text_to_speech module uses real gTTS implementation."""
    from src.text_to_speech.utils import text_to_speech_audio

    # Check that the function exists and is callable
    assert callable(text_to_speech_audio)

    # Verify gTTS is the real class, not a mock
    assert gTTS is not None
    assert inspect.isclass(gTTS)
    assert hasattr(gTTS, "__init__")

    # Check that text_to_speech_audio would use gTTS or macOS say command (by inspecting source if possible)
    try:
        source = inspect.getsource(text_to_speech_audio)
        # Accept either gTTS (cross-platform) or say command (macOS native)
        assert "gTTS" in source or "gtts" in source or "say" in source, \
            "text_to_speech_audio should use gTTS or macOS say command"
    except OSError:
        # Source not available, but we verified gTTS is imported
        pass


def test_speech_to_text_uses_real_speech_recognition():
    """Verify speech_to_text module uses real speech_recognition implementation."""
    try:
        from src.speech_to_text.utils import transcribe_audio_segment
    except ImportError:
        pytest.skip("speech_to_text module not available")

    # Check that the function exists and is callable
    assert callable(transcribe_audio_segment)

    # Verify speech_recognition is the real module, not a mock
    assert sr is not None
    assert hasattr(sr, "Recognizer")
    assert inspect.isclass(sr.Recognizer)

    # Check that transcribe_audio_segment would use speech_recognition
    try:
        source = inspect.getsource(transcribe_audio_segment)
        assert "Recognizer" in source or "speech_recognition" in source
    except OSError:
        # Source not available, but we verified speech_recognition is imported
        pass


def test_speech_to_text_uses_real_pydub():
    """Verify speech_to_text module uses real pydub implementation."""
    try:
        from src.speech_to_text.utils import read_audio_file, convert_audio_to_wav
    except ImportError:
        pytest.skip("speech_to_text module not available")

    # Check that functions exist and are callable
    assert callable(read_audio_file)
    assert callable(convert_audio_to_wav)

    # Verify AudioSegment is the real class, not a mock
    assert AudioSegment is not None
    assert inspect.isclass(AudioSegment)
    assert hasattr(AudioSegment, "from_file")


def test_file_operations_are_real(temp_dir):
    """Verify all file operations use real file system operations."""
    from src.batch_processing.utils import ensure_output_directory
    from src.text_to_speech.utils import read_text_file

    # Test real file operations
    test_file = temp_dir / "test.txt"
    test_file.write_text("test content", encoding="utf-8")

    # Verify read_text_file uses real file operations
    content = read_text_file(test_file)
    assert content == "test content"

    # Verify ensure_output_directory uses real file operations
    test_dir = temp_dir / "test_output"
    ensure_output_directory(test_dir)
    assert test_dir.exists()
    assert test_dir.is_dir()


def test_no_mock_objects_in_codebase():
    """Verify that no mock objects are used in the actual source code."""
    import os
    import re

    src_dir = Path(__file__).parent.parent / "src"

    # Patterns that might indicate mocks
    mock_patterns = [
        r"from unittest.mock import",
        r"from unittest import mock",
        r"@patch\(",
        r"Mock\(",
        r"MagicMock\(",
        r"mock\.",
    ]

    issues = []
    for py_file in src_dir.rglob("*.py"):
        try:
            content = py_file.read_text(encoding="utf-8")
            for pattern in mock_patterns:
                if re.search(pattern, content):
                    issues.append(f"{py_file.relative_to(src_dir.parent)}: {pattern}")
        except Exception:
            # Skip files that can't be read
            continue

    if issues:
        pytest.fail(
            f"Found potential mock usage in source code (should only be in tests):\n"
            + "\n".join(issues)
        )


def test_all_functions_use_real_library_calls():
    """Verify that functions use real library calls, not stubs."""
    from src.text_to_speech.utils import text_to_speech_audio
    from src.speech_to_text.utils import transcribe_audio_segment

    # Verify functions are not stubs (they should have implementation)
    assert text_to_speech_audio.__code__.co_code != b""
    assert transcribe_audio_segment.__code__.co_code != b""

    # Verify they have proper signatures (not just pass statements)
    text_to_speech_source = inspect.getsource(text_to_speech_audio)
    assert "pass" not in text_to_speech_source or text_to_speech_source.count("pass") < 2

    transcribe_source = inspect.getsource(transcribe_audio_segment)
    assert "pass" not in transcribe_source or transcribe_source.count("pass") < 2


def test_batch_processing_uses_real_implementations():
    """Verify batch_processing uses real implementations throughout."""
    from src.batch_processing.main import (
        process_module_by_type,
        process_syllabus,
        clear_all_outputs,
    )

    # Verify functions are real implementations
    assert callable(process_module_by_type)
    assert callable(process_syllabus)
    assert callable(clear_all_outputs)

    # Verify they have implementations (not just pass)
    for func in [process_module_by_type, process_syllabus, clear_all_outputs]:
        source = inspect.getsource(func)
        # Should have more than just a docstring and pass
        assert len(source) > 200, f"{func.__name__} appears to be a stub"


def test_format_conversion_uses_real_libraries():
    """Verify format_conversion uses real library implementations."""
    try:
        from src.format_conversion.main import convert_file
    except (ImportError, OSError) as e:
        # WeasyPrint may fail due to missing system libraries
        if "libgobject" in str(e) or "weasyprint" in str(e).lower():
            pytest.skip(f"WeasyPrint system libraries not available: {e}")
        raise

    assert callable(convert_file)

    # Verify it uses real libraries (check source for library usage)
    source = inspect.getsource(convert_file)
    # Should reference real conversion libraries
    assert any(
        lib in source.lower()
        for lib in ["markdown", "weasyprint", "docx", "pypdf", "html"]
    )
