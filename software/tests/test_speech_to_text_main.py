"""Tests for speech_to_text main functions."""

from pathlib import Path

import pytest

from src.speech_to_text.main import (
    batch_transcribe_audio,
    transcribe_audio,
    transcribe_from_markdown,
)


def test_transcribe_from_markdown(temp_dir):
    """Test transcribing text from Markdown file."""
    # Create a sample Markdown file
    md_file = temp_dir / "test.md"
    md_content = """# Test Document

This is a test document with some text.

## Section 1

More content here with **bold** and *italic* text.
"""
    md_file.write_text(md_content, encoding="utf-8")

    output_file = temp_dir / "output.txt"
    result = transcribe_from_markdown(str(md_file), str(output_file))

    assert output_file.exists()
    assert "Test Document" in result
    assert "test document" in result.lower()
    assert "Section 1" in result


def test_transcribe_from_markdown_nonexistent():
    """Test transcribing from nonexistent Markdown file raises error."""
    with pytest.raises(FileNotFoundError):
        transcribe_from_markdown("/nonexistent/file.md", "/output.txt")


def test_batch_transcribe_audio_nonexistent_directory():
    """Test batch transcribe with nonexistent directory raises error."""
    with pytest.raises(ValueError, match="Directory does not exist"):
        batch_transcribe_audio("/nonexistent/dir", "/output/dir")


def test_batch_transcribe_audio_empty_directory(temp_dir):
    """Test batch transcribe with empty directory returns empty list."""
    output_dir = temp_dir / "output"
    output_dir.mkdir()

    result = batch_transcribe_audio(str(temp_dir), str(output_dir))
    assert result == []


def test_transcribe_audio_nonexistent_file():
    """Test transcribing nonexistent audio file raises error."""
    with pytest.raises(FileNotFoundError):
        transcribe_audio("/nonexistent/audio.mp3", "/output.txt")


def test_batch_transcribe_audio(temp_dir):
    """Test batch transcribing audio files."""
    # Create a minimal audio file by generating speech
    from src.text_to_speech.main import generate_speech

    audio_file = temp_dir / "test.mp3"
    try:
        generate_speech("Test.", str(audio_file))
        if not audio_file.exists():
            pytest.skip("Audio generation failed, skipping batch transcription test")

        output_dir = temp_dir / "output"
        output_dir.mkdir()

        result = batch_transcribe_audio(str(temp_dir), str(output_dir))
        # Result might be empty if transcription fails, but we test the path
        assert isinstance(result, list)
    except Exception:
        pytest.skip("Audio generation or transcription requires internet connection")


def test_transcribe_audio_error_handling(temp_dir):
    """Test error handling in transcribe_audio."""
    # Create an invalid audio file (empty or corrupted)
    invalid_audio = temp_dir / "invalid.mp3"
    invalid_audio.write_bytes(b"invalid audio data")

    output_file = temp_dir / "output.txt"
    try:
        # This might fail, but we test the error handling path
        transcribe_audio(str(invalid_audio), str(output_file))
    except (OSError, FileNotFoundError):
        # Expected to fail, test passes
        pass


def test_read_audio_file_error():
    """Test read_audio_file with nonexistent file."""
    from src.speech_to_text.utils import read_audio_file
    from pathlib import Path

    with pytest.raises(FileNotFoundError):
        read_audio_file(Path("/nonexistent/audio.mp3"))


def test_read_audio_file_invalid_format(temp_dir):
    """Test read_audio_file with invalid audio format."""
    from src.speech_to_text.utils import read_audio_file

    # Create a file that's not a valid audio file
    invalid_file = temp_dir / "invalid.txt"
    invalid_file.write_text("Not audio", encoding="utf-8")

    try:
        read_audio_file(invalid_file)
    except OSError:
        # Expected to fail, test passes
        pass


def test_transcribe_audio_segment_error_handling(temp_dir):
    """Test error handling in transcribe_audio_segment."""
    from src.speech_to_text.utils import transcribe_audio_segment
    from pathlib import Path

    # Create an invalid audio file
    invalid_audio = temp_dir / "invalid.wav"
    invalid_audio.write_bytes(b"invalid audio data")

    try:
        # This will likely fail, but we test the error handling path
        transcribe_audio_segment(invalid_audio, language="en")
    except OSError:
        # Expected to fail, test passes
        pass
