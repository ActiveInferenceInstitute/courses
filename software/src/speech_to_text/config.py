"""Configuration for speech-to-text transcription."""

from typing import Any, Dict

# Default transcription settings
DEFAULT_TRANSCRIPTION_SETTINGS: Dict[str, Any] = {
    "language": "en",
    "show_all": False,
}

# Supported audio formats
SUPPORTED_AUDIO_FORMATS: list = [".mp3", ".wav", ".m4a", ".flac", ".ogg"]

# Output format
OUTPUT_FORMAT: str = "txt"
