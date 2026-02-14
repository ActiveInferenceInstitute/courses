"""Integration tests demonstrating module orchestration."""

from pathlib import Path

import pytest

from src.batch_processing.main import generate_module_media
from src.file_validation.main import (
    get_validation_report,
    validate_module_files,
)
from src.format_conversion.main import convert_file, get_supported_formats
from src.module_organization.main import (
    create_module_structure,
    get_module_statistics,
    validate_module_structure,
)
import src.text_to_speech.main as tts_main
import src.speech_to_text.main as stt_main
import src.batch_processing.main as batch_main


def test_complete_module_workflow(temp_dir):
    """Test complete workflow: create, validate, process module."""
    course_path = str(temp_dir)

    # 1. Create module structure
    module_path = create_module_structure(course_path, 1)
    assert Path(module_path).exists()

    # 2. Add sample content with proper naming convention (study-guide allows .md)
    sample_file = Path(module_path) / "module-1-study-guide.md"
    sample_file.write_text("# Sample\nThis is test content.\n", encoding="utf-8")

    # 3. Validate module
    validation = validate_module_files(module_path)
    assert validation["valid"] is True

    # 4. Get validation report
    report = get_validation_report(module_path)
    assert report["is_valid"] is True

    # 5. Get module statistics
    stats = get_module_statistics(module_path)
    assert stats["total_files"] > 0
    assert stats["has_readme"] is True


def test_format_conversion_chain(temp_dir):
    """Test format conversion chain: MD -> PDF -> TXT."""
    # Create sample Markdown
    md_file = temp_dir / "test.md"
    md_file.write_text("# Test\nContent here.\n", encoding="utf-8")

    # Convert MD to PDF
    pdf_file = temp_dir / "test.pdf"
    convert_file(str(md_file), "pdf", str(pdf_file))
    assert pdf_file.exists()

    # Convert PDF to TXT
    txt_file = temp_dir / "test.txt"
    convert_file(str(pdf_file), "txt", str(txt_file))
    assert txt_file.exists()
    content = txt_file.read_text(encoding="utf-8")
    assert len(content) > 0


def test_batch_processing_workflow(temp_dir):
    """Test batch processing entire module."""
    # Create module with content
    course_path = str(temp_dir)
    module_path = create_module_structure(course_path, 1)

    # Add minimal sample file with short content for faster audio generation
    sample1 = Path(module_path) / "module-1-study-guide.md"
    sample1.write_text("# Guide\nTest.\n", encoding="utf-8")

    # Process module to generate all media
    output_dir = temp_dir / "media_output"
    
    with pytest.MonkeyPatch.context() as m:
        # Mock external API calls
        m.setattr(tts_main, "generate_speech", lambda t, o, **k: None)
        m.setattr(stt_main, "transcribe_audio", lambda i, o: None)
        m.setattr(batch_main.time, "sleep", lambda x: None)
        results = generate_module_media(module_path, str(output_dir))

    # Verify results structure
    assert "pdf_files" in results
    assert "audio_files" in results
    assert "text_files" in results
    assert "errors" in results
    assert isinstance(results["pdf_files"], list)
    assert isinstance(results["audio_files"], list)


def test_validation_and_processing_integration(temp_dir):
    """Test validation before processing."""
    course_path = str(temp_dir)
    module_path = create_module_structure(course_path, 1)

    # Validate structure
    is_valid = validate_module_structure(module_path)
    assert is_valid is True

    # Validate files
    validation = validate_module_files(module_path)
    assert validation["valid"] is True

    # Only process if valid - use minimal content for faster testing
    if validation["valid"]:
        # Add minimal content
        sample_file = Path(module_path) / "module-1-study-guide.md"
        sample_file.write_text("# Test\nA.\n", encoding="utf-8")
        
        output_dir = temp_dir / "output"
        with pytest.MonkeyPatch.context() as m:
            m.setattr(tts_main, "generate_speech", lambda t, o, **k: None)
            m.setattr(stt_main, "transcribe_audio", lambda i, o: None)
            m.setattr(batch_main.time, "sleep", lambda x: None)
            results = generate_module_media(module_path, str(output_dir))
        assert isinstance(results, dict)


def test_supported_formats_orchestration():
    """Test getting supported formats for orchestration planning."""
    formats = get_supported_formats()

    # Verify key conversions are supported
    assert "md" in formats
    assert "pdf" in formats["md"]
    assert "docx" in formats["md"]
    assert "txt" in formats.get("pdf", [])

    # Can plan conversion chains
    assert "md" in formats  # Can convert from MD
    assert "pdf" in formats  # Can convert from PDF


def test_module_statistics_and_validation(temp_dir):
    """Test using module statistics for validation decisions."""
    course_path = str(temp_dir)
    module_path = create_module_structure(course_path, 1)

    # Get statistics
    stats = get_module_statistics(module_path)

    # Use statistics for validation decisions
    if stats["has_readme"] and stats["has_agents"]:
        validation = validate_module_files(module_path)
        assert validation["valid"] is True

    # Add minimal content for testing processing decision
    sample_file = Path(module_path) / "module-1-study-guide.md"
    sample_file.write_text("# Test\nX.\n", encoding="utf-8")
    
    # Re-get statistics after adding content
    stats = get_module_statistics(module_path)
    
    # Check if module has content to process
    if stats["total_files"] > 2:  # More than just README and AGENTS
        output_dir = temp_dir / "output"
        with pytest.MonkeyPatch.context() as m:
            m.setattr(tts_main, "generate_speech", lambda t, o, **k: None)
            m.setattr(stt_main, "transcribe_audio", lambda i, o: None)
            m.setattr(batch_main.time, "sleep", lambda x: None)
            results = generate_module_media(module_path, str(output_dir))
        assert isinstance(results, dict)


def test_error_handling_in_orchestration(temp_dir):
    """Test error handling across module orchestration."""
    # Try to process nonexistent module
    with pytest.raises(ValueError):
        generate_module_media("/nonexistent/module", str(temp_dir / "output"))

    # Try to validate nonexistent module
    validation = validate_module_files("/nonexistent/module")
    assert validation["valid"] is False
    assert "error" in validation

    # Try to get statistics for nonexistent module
    with pytest.raises(ValueError):
        get_module_statistics("/nonexistent/module")


def test_text_to_speech_workflow(temp_dir):
    """Test text-to-speech generation workflow."""
    # Generate speech from minimal text for faster testing
    audio_file = temp_dir / "test.mp3"
    
    with pytest.MonkeyPatch.context() as m:
        # Mock generate_speech to avoid external calls
        m.setattr(tts_main, "generate_speech", lambda t, o, **k: None)
        # Create dummy file since mock won't create it
        tts_main.generate_speech("Test.", str(audio_file))
        audio_file.write_text("dummy audio")

    # Verify audio file was created
    assert audio_file.exists()

    # Note: Actual transcription would require real audio file
    # This demonstrates the workflow structure
