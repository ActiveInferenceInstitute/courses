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

# Maximum seconds of audio transcribed per recognizer.record() call.  Recording
# a whole (possibly hours-long) file into memory and handing it to the cloud
# API at once is an unbounded-resource bug; chunking bounds memory and request
# size.  Chunked results are joined with a space.
RECORDING_CHUNK_SECONDS: float = 30.0
