"""Configuration for the translation module.

Single source of truth for all translation settings.
"""

from typing import Dict, List

# Supported language codes mapped to their full names
SUPPORTED_LANGUAGES: Dict[str, str] = {
    "ar": "Arabic",
    "de": "German",
    "es": "Spanish",
    "fr": "French",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh": "Chinese (Simplified)",
}

# Default source language
DEFAULT_SOURCE_LANG: str = "English"

# LLM chunk size (max tokens per chunk for translation batches)
DEFAULT_CHUNK_SIZE: int = 4096

# Output file suffix pattern: {basename}_{lang}.{ext}
OUTPUT_SUFFIX_PATTERN: str = "{lang}"

# File extensions eligible for translation
TRANSLATABLE_EXTENSIONS: List[str] = [".md", ".txt"]
