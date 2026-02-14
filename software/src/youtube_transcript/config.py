"""Configuration constants for YouTube transcript module."""

# Default channel
DEFAULT_CHANNEL_URL = "https://www.youtube.com/@ActiveInference"

# Subtitle preferences
SUBTITLE_LANGUAGE = "en"
SUBTITLE_FORMAT = "vtt"

# Whisper defaults
DEFAULT_WHISPER_MODEL = "base"

# Rate limiting
RATE_LIMIT_DELAY = 1.0  # seconds between videos
RATE_LIMIT_BATCH_DELAY = 2.0  # extra delay every N videos
RATE_LIMIT_BATCH_SIZE = 50

# Output structure
OUTPUT_DIR_NAME = "transcription"
CAPTIONS_SUBDIR = "captions"
TRANSCRIPTS_SUBDIR = "transcripts"
MANIFEST_FILENAME = "manifest.json"
