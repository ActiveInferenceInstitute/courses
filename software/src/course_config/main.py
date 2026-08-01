"""Public API for per-course configuration."""

import copy
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

from .config import DEFAULT_CONFIG
from .utils import find_config_chain, resolve_config_chain, validate_config

logger = logging.getLogger(__name__)


def load_course_config(course_path: Path, repo_root: Path) -> Dict[str, Any]:
    """Load merged configuration for a course path.

    Walks from *course_path* up to the ``course_development/`` boundary,
    collecting all ``course.toml`` files and merging them bottom-up::

        DEFAULT_CONFIG <- curriculum TOML <- course TOML <- module TOML

    If no TOML files exist the caller gets ``DEFAULT_CONFIG`` unchanged,
    so the pipeline works identically with zero config files.

    Args:
        course_path: Path to a course or module directory.
        repo_root: Root path of the repository.

    Returns:
        Merged configuration dict with all defaults filled in.
    """
    config_files = find_config_chain(course_path, repo_root)
    config = resolve_config_chain(config_files)

    warnings = validate_config(config)
    for w in warnings:
        logger.warning("Config validation (%s): %s", course_path.name, w)

    return config


def get_rendering_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Extract the rendering section from a config.

    Args:
        config: Merged course config dict.

    Returns:
        Rendering sub-dict.
    """
    result: Dict[str, Any] = copy.deepcopy(config.get("rendering", DEFAULT_CONFIG["rendering"]))
    return result


def is_format_enabled(config: Dict[str, Any], fmt: str) -> bool:
    """Check whether a specific output format is enabled.

    Args:
        config: Merged course config dict.
        fmt: Format name (``"pdf"``, ``"html"``, ``"audio"``, ``"docx"``,
             ``"txt"``, ``"md"``).  Also accepts ``"mp3"`` as an alias
             for ``"audio"``.

    Returns:
        ``True`` if the format is enabled (the default).
    """
    rendering = config.get("rendering", {})
    config_key = "audio" if fmt == "mp3" else fmt
    format_config = rendering.get(config_key, {})
    if isinstance(format_config, dict):
        enabled: bool = format_config.get("enabled", True)
        return enabled
    # A scalar boolean value (e.g. `pdf = false` in TOML) is a direct toggle.
    if isinstance(format_config, bool):
        return format_config
    # Any other type (unknown format, malformed) defaults to enabled.
    return True


def get_metadata(config: Dict[str, Any]) -> Dict[str, Any]:
    """Extract the metadata section from a config.

    Args:
        config: Merged course config dict.

    Returns:
        Metadata sub-dict.
    """
    result: Dict[str, Any] = config.get("metadata", DEFAULT_CONFIG["metadata"])
    return result


def get_localization(config: Dict[str, Any]) -> Dict[str, Any]:
    """Extract the localization section from a config.

    Args:
        config: Merged course config dict.

    Returns:
        Localization sub-dict.
    """
    result: Dict[str, Any] = config.get("localization", DEFAULT_CONFIG["localization"])
    return result


def get_tts_settings(config: Dict[str, Any]) -> Dict[str, Any]:
    """Extract text-to-speech settings from ``rendering.audio``.

    Returns a dict with keys ``lang``, ``slow``, ``speed`` suitable for
    passing to gTTS.

    Args:
        config: Merged course config dict.

    Returns:
        TTS settings dict.
    """
    rendering = config.get("rendering", {})
    audio = rendering.get("audio", {})
    return {
        "lang": audio.get("lang", "en"),
        "slow": audio.get("slow", False),
        "speed": audio.get("speed", 1.0),
    }


def get_pdf_css(config: Dict[str, Any]) -> Optional[str]:
    """Get custom CSS file path for PDF rendering, if specified.

    Args:
        config: Merged course config dict.

    Returns:
        CSS file path string, or ``None`` if not specified.
    """
    rendering = config.get("rendering", {})
    pdf = rendering.get("pdf", {})
    css_file = pdf.get("css_file", "")
    return css_file if css_file else None


def get_enabled_formats(config: Dict[str, Any]) -> List[str]:
    """Get list of enabled output format names.

    Returns format names as used by the pipeline:
    ``pdf``, ``mp3``, ``docx``, ``html``, ``txt``, ``md``.

    Args:
        config: Merged course config dict.

    Returns:
        List of enabled format name strings.
    """
    format_map = {
        "pdf": "pdf",
        "audio": "mp3",
        "docx": "docx",
        "html": "html",
        "txt": "txt",
        "md": "md",
    }
    enabled: List[str] = []
    rendering = config.get("rendering", {})
    for config_key, pipeline_name in format_map.items():
        format_config = rendering.get(config_key, {})
        if isinstance(format_config, dict) and format_config.get("enabled", True):
            enabled.append(pipeline_name)
    return enabled
