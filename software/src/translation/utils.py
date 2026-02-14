"""Utilities for the translation module."""

import logging
from pathlib import Path

from .config import SUPPORTED_LANGUAGES, TRANSLATABLE_EXTENSIONS

logger = logging.getLogger(__name__)


def get_language_name(code: str) -> str:
    """Get language name from language code.

    Args:
        code: ISO language code (e.g. "es", "fr").

    Returns:
        Full language name, or the code itself if not found.
    """
    name = SUPPORTED_LANGUAGES.get(code.lower(), code)
    if name == code:
        logger.warning(f"Unknown language code '{code}', using as-is")
    return name


def get_output_path(input_path: Path, target_lang: str) -> Path:
    """Generate output path for translated file.

    Example: input.md -> input_es.md

    Args:
        input_path: Path to the source file.
        target_lang: Target language code.

    Returns:
        Path for the translated output file.
    """
    stem = input_path.stem
    suffix = input_path.suffix
    return input_path.parent / f"{stem}_{target_lang}{suffix}"


def validate_file_extension(file_path: Path) -> bool:
    """Check if a file has a translatable extension.

    Args:
        file_path: Path to the file to check.

    Returns:
        True if the file extension is in TRANSLATABLE_EXTENSIONS.
    """
    return file_path.suffix.lower() in TRANSLATABLE_EXTENSIONS
