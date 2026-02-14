"""Main functions for speech-to-text transcription."""

import tempfile
from pathlib import Path
from typing import List, Optional

from . import config
from .utils import (
    convert_audio_to_wav,
    ensure_output_directory,
    get_output_path,
    is_audio_file,
    read_audio_file,
    transcribe_audio_segment,
)


def transcribe_audio(
    audio_path: str, output_path: str, language: str = "en"
) -> str:
    """Transcribe audio file to text using real speech recognition.

    Args:
        audio_path: Path to input audio file
        output_path: Path for output text file
        language: Language code (default: "en")

    Returns:
        Transcribed text content

    Raises:
        FileNotFoundError: If audio file doesn't exist
        OSError: If transcription fails
    """
    audio_file = Path(audio_path)
    output_file = Path(output_path)

    if not audio_file.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    # Ensure output directory exists
    ensure_output_directory(output_file)

    # Read audio file
    audio = read_audio_file(audio_file)

    # Convert to WAV format for speech recognition
    # Use temporary file for conversion
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        temp_wav_path = Path(temp_wav.name)
        try:
            convert_audio_to_wav(audio, temp_wav_path)

            # Transcribe audio
            transcribed_text = transcribe_audio_segment(temp_wav_path, language=language)

            # Write transcribed text to output file
            output_file.write_text(transcribed_text, encoding="utf-8")

            return transcribed_text
        finally:
            # Clean up temporary file
            if temp_wav_path.exists():
                temp_wav_path.unlink()


def batch_transcribe_audio(input_dir: str, output_dir: str) -> List[str]:
    """Batch transcribe audio files in a directory.

    Args:
        input_dir: Directory containing audio files
        output_dir: Output directory for text files

    Returns:
        List of output file paths

    Raises:
        ValueError: If directory doesn't exist
        OSError: If transcription fails for any file
    """
    source_dir = Path(input_dir)
    if not source_dir.exists() or not source_dir.is_dir():
        raise ValueError(f"Directory does not exist: {input_dir}")

    output_directory = Path(output_dir)
    output_directory.mkdir(parents=True, exist_ok=True)

    output_files = []

    # Find all audio files
    audio_files = [f for f in source_dir.iterdir() if f.is_file() and is_audio_file(f)]

    for audio_file in audio_files:
        try:
            output_path = get_output_path(audio_file, output_directory)
            transcribe_audio(str(audio_file), str(output_path))
            output_files.append(str(output_path))
        except Exception as e:
            # Log error but continue with other files
            print(f"Error transcribing {audio_file}: {e}")
            continue

    return output_files


def transcribe_from_markdown(markdown_path: str, output_path: str) -> str:
    """Extract text from Markdown and transcribe (if audio is referenced).

    This function extracts text from Markdown files. If the Markdown references
    audio files, those could be transcribed. For now, this extracts and returns
    the text content.

    Args:
        markdown_path: Path to Markdown file
        output_path: Path for output text file

    Returns:
        Extracted text content

    Raises:
        FileNotFoundError: If Markdown file doesn't exist
        OSError: If processing fails
    """
    from ..text_to_speech.utils import extract_text_from_markdown, read_text_file

    md_file = Path(markdown_path)
    if not md_file.exists():
        raise FileNotFoundError(f"Markdown file not found: {markdown_path}")

    # Read Markdown content
    markdown_content = read_text_file(md_file)

    # Extract plain text from Markdown
    text_content = extract_text_from_markdown(markdown_content)

    # Write to output file
    output_file = Path(output_path)
    ensure_output_directory(output_file)
    output_file.write_text(text_content, encoding="utf-8")

    return text_content
