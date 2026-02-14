"""Comprehensive tests for verifying all imports work correctly."""

import importlib
import sys
from pathlib import Path

import pytest


def test_all_core_module_imports():
    """Verify all core modules can be imported."""
    # Core modules that should always be available
    modules = [
        "src.batch_processing",
        "src.module_organization",
        "src.file_validation",
        "src.html_website",
    ]

    for module_name in modules:
        try:
            importlib.import_module(module_name)
        except ImportError as e:
            pytest.fail(f"Failed to import {module_name}: {e}")

    # Modules that require WeasyPrint (may fail on system library issues)
    weasyprint_modules = [
        "src.format_conversion",
        "src.markdown_to_pdf",
    ]

    for module_name in weasyprint_modules:
        try:
            importlib.import_module(module_name)
        except (ImportError, OSError) as e:
            # WeasyPrint may fail due to missing system libraries (libgobject, etc.)
            # This is documented in README.md - not a code issue
            if "libgobject" in str(e) or "weasyprint" in str(e).lower():
                pytest.skip(f"WeasyPrint system libraries not available: {e}")
            pytest.fail(f"Failed to import {module_name}: {e}")


def test_text_to_speech_module_imports():
    """Verify text_to_speech module imports work."""
    try:
        from src.text_to_speech import generate_speech, batch_generate_speech
        assert generate_speech is not None
        assert batch_generate_speech is not None
    except ImportError as e:
        pytest.fail(f"Failed to import text_to_speech module: {e}")


def test_speech_to_text_module_imports():
    """Verify speech_to_text module imports work."""
    try:
        from src.speech_to_text import transcribe_audio, batch_transcribe_audio
        assert transcribe_audio is not None
        assert batch_transcribe_audio is not None
    except ImportError as e:
        pytest.fail(f"Failed to import speech_to_text module: {e}")


def test_batch_processing_imports():
    """Verify batch_processing module imports work."""
    try:
        from src.batch_processing.main import (
            clear_all_outputs,
            process_module_by_type,
            process_module_website,
            process_syllabus,
        )
        assert clear_all_outputs is not None
        assert process_module_by_type is not None
        assert process_module_website is not None
        assert process_syllabus is not None
    except ImportError as e:
        pytest.fail(f"Failed to import batch_processing functions: {e}")


def test_format_conversion_imports():
    """Verify format_conversion module imports work."""
    try:
        from src.format_conversion.main import convert_file, get_supported_formats
        assert convert_file is not None
        assert get_supported_formats is not None
    except (ImportError, OSError) as e:
        # WeasyPrint may fail due to missing system libraries
        if "libgobject" in str(e) or "weasyprint" in str(e).lower():
            pytest.skip(f"WeasyPrint system libraries not available: {e}")
        pytest.fail(f"Failed to import format_conversion functions: {e}")


def test_module_organization_imports():
    """Verify module_organization module imports work."""
    try:
        from src.module_organization.main import (
            create_module_structure,
            get_module_statistics,
            validate_module_structure,
        )
        assert create_module_structure is not None
        assert get_module_statistics is not None
        assert validate_module_structure is not None
    except ImportError as e:
        pytest.fail(f"Failed to import module_organization functions: {e}")


def test_html_website_imports():
    """Verify html_website module imports work."""
    try:
        from src.html_website.main import generate_module_website
        assert generate_module_website is not None
    except ImportError as e:
        pytest.fail(f"Failed to import html_website functions: {e}")


def test_text_to_speech_utils_imports():
    """Verify text_to_speech utils can be imported and use real gTTS."""
    try:
        from src.text_to_speech.utils import (
            extract_text_from_markdown,
            read_text_file,
            text_to_speech_audio,
        )
        assert extract_text_from_markdown is not None
        assert read_text_file is not None
        assert text_to_speech_audio is not None

        # Verify gTTS is imported (real implementation)
        from gtts import gTTS
        assert gTTS is not None
    except ImportError as e:
        pytest.fail(f"Failed to import text_to_speech utils or gTTS: {e}")


def test_speech_to_text_utils_imports():
    """Verify speech_to_text utils can be imported and use real speech_recognition."""
    try:
        from src.speech_to_text.utils import (
            convert_audio_to_wav,
            is_audio_file,
            read_audio_file,
            transcribe_audio_segment,
        )
        assert convert_audio_to_wav is not None
        assert is_audio_file is not None
        assert read_audio_file is not None
        assert transcribe_audio_segment is not None

        # Verify speech_recognition is imported (real implementation)
        import speech_recognition as sr
        assert sr is not None
    except ImportError as e:
        pytest.fail(f"Failed to import speech_to_text utils or speech_recognition: {e}")


def test_no_import_time_errors():
    """Verify that importing modules doesn't cause errors at import time."""
    modules_to_test = [
        "src.batch_processing",
        "src.module_organization",
        "src.file_validation",
        "src.html_website",
        "src.text_to_speech",
        "src.speech_to_text",
    ]

    for module_name in modules_to_test:
        try:
            # Clear any cached imports
            if module_name in sys.modules:
                del sys.modules[module_name]

            # Import should not raise
            module = importlib.import_module(module_name)
            assert module is not None
        except Exception as e:
            pytest.fail(f"Import of {module_name} raised error at import time: {e}")

    # Modules that require WeasyPrint (may fail on system library issues)
    weasyprint_modules = [
        "src.format_conversion",
        "src.markdown_to_pdf",
    ]

    for module_name in weasyprint_modules:
        try:
            # Clear any cached imports
            if module_name in sys.modules:
                del sys.modules[module_name]

            # Import should not raise
            module = importlib.import_module(module_name)
            assert module is not None
        except (OSError, ImportError) as e:
            # WeasyPrint may fail due to missing system libraries
            if "libgobject" in str(e) or "weasyprint" in str(e).lower():
                pytest.skip(f"WeasyPrint system libraries not available for {module_name}: {e}")
            pytest.fail(f"Import of {module_name} raised error at import time: {e}")
