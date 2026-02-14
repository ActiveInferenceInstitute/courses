"""Utility functions for speech-to-text transcription."""

from pathlib import Path
from typing import Optional

import speech_recognition as sr
from pydub import AudioSegment


def read_audio_file(audio_path: Path) -> AudioSegment:
    """Read audio file and convert to format suitable for speech recognition.

    Args:
        audio_path: Path to audio file

    Returns:
        AudioSegment object

    Raises:
        FileNotFoundError: If audio file doesn't exist
        OSError: If audio file cannot be read
    """
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    try:
        # Load audio file
        audio = AudioSegment.from_file(str(audio_path))
        return audio
    except Exception as e:
        raise OSError(f"Failed to read audio file: {audio_path}: {e}") from e


def convert_audio_to_wav(audio: AudioSegment, output_path: Path) -> None:
    """Convert audio to WAV format for speech recognition.

    Args:
        audio: AudioSegment object
        output_path: Path for output WAV file
    """
    try:
        audio.export(str(output_path), format="wav")
    except Exception as e:
        raise OSError(f"Failed to convert audio to WAV: {e}") from e


def transcribe_audio_segment(audio_path: Path, language: str = "en") -> str:
    """Transcribe audio file to text using speech recognition.

    Args:
        audio_path: Path to audio file (WAV format preferred)
        language: Language code (default: "en")

    Returns:
        Transcribed text

    Raises:
        OSError: If transcription fails
    """
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(str(audio_path)) as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Read audio data
            audio_data = recognizer.record(source)

        # Perform transcription using Google Speech Recognition
        # This uses real Google Speech Recognition API
        try:
            text = recognizer.recognize_google(audio_data, language=language)
            return text
        except sr.UnknownValueError:
            raise OSError("Speech recognition could not understand audio")
        except sr.RequestError as e:
            raise OSError(f"Speech recognition service error: {e}") from e

    except Exception as e:
        raise OSError(f"Failed to transcribe audio: {e}") from e


def ensure_output_directory(output_path: Path) -> None:
    """Ensure output directory exists.

    Args:
        output_path: Path to output file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)


def get_output_path(input_path: Path, output_dir: Optional[Path] = None) -> Path:
    """Get output text path from input audio path.

    Args:
        input_path: Path to input audio file
        output_dir: Optional output directory (if None, uses input directory)

    Returns:
        Path to output text file
    """
    if output_dir is None:
        output_dir = input_path.parent

    output_filename = input_path.stem + ".txt"
    return output_dir / output_filename


def is_audio_file(file_path: Path) -> bool:
    """Check if file is an audio file.

    Args:
        file_path: Path to file

    Returns:
        True if file is an audio file, False otherwise
    """
    return file_path.suffix.lower() in [".mp3", ".wav", ".m4a", ".flac", ".ogg"]
