"""Configuration for text-to-speech generation."""

from typing import Any, Dict

# Default voice settings
DEFAULT_VOICE_SETTINGS: Dict[str, Any] = {
    "voice": "en",
    "speed": 1.0,
    "pitch": 1.0,
    "lang": "en",
    "slow": False,
}

# Supported languages and voices
SUPPORTED_LANGUAGES: Dict[str, str] = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
}

# Default output format
OUTPUT_FORMAT: str = "mp3"
