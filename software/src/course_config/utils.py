"""Utility functions for course configuration loading and merging."""

import copy
import logging
import tomllib
from pathlib import Path
from typing import Any, Dict, List

from .config import CONFIG_FILENAME, DEFAULT_CONFIG, VALID_SECTIONS

logger = logging.getLogger(__name__)


def load_toml_file(path: Path) -> Dict[str, Any]:
    """Load and parse a TOML file.

    Args:
        path: Path to the TOML file.

    Returns:
        Parsed TOML data as a dict.

    Raises:
        FileNotFoundError: If the file does not exist.
        tomllib.TOMLDecodeError: If the file is not valid TOML.
    """
    with open(path, "rb") as f:
        return tomllib.load(f)


def deep_merge(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Deep-merge two dicts. Values in *override* take precedence.

    - Dict values are merged recursively.
    - All other types (lists, scalars) are replaced wholesale.

    Args:
        base: Base dict (not mutated).
        override: Override dict whose values win.

    Returns:
        New merged dict.
    """
    result = copy.deepcopy(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


def find_config_chain(course_path: Path, repo_root: Path) -> List[Path]:
    """Walk from *course_path* up to the ``course_development/`` boundary.

    Collects every ``course.toml`` file found along the way and returns
    them **outermost-first** so that the caller can merge from general to
    specific.

    Args:
        course_path: Path to a course or module directory.
        repo_root: Repository root (parent of ``course_development/``).

    Returns:
        List of ``course.toml`` paths, outermost first.
    """
    course_dev_dir = (repo_root / "course_development").resolve()
    if not course_dev_dir.exists():
        return []

    # Collect directories from course_path up to (but not including) course_development/
    chain_dirs: List[Path] = []
    current = course_path.resolve()

    while current != course_dev_dir and current != course_dev_dir.parent:
        chain_dirs.append(current)
        parent = current.parent
        if parent == current:
            break  # filesystem root
        current = parent

    # Reverse so outermost comes first
    chain_dirs.reverse()

    # Collect existing course.toml files
    config_files: List[Path] = []
    for directory in chain_dirs:
        config_path = directory / CONFIG_FILENAME
        if config_path.is_file():
            config_files.append(config_path)

    return config_files


def resolve_config_chain(config_files: List[Path]) -> Dict[str, Any]:
    """Merge a chain of TOML config files onto ``DEFAULT_CONFIG``.

    Args:
        config_files: Ordered list of config file paths (outermost first).

    Returns:
        Fully merged configuration dict.
    """
    result = copy.deepcopy(DEFAULT_CONFIG)
    for config_path in config_files:
        try:
            toml_data = load_toml_file(config_path)
            result = deep_merge(result, toml_data)
            logger.debug("Merged config from %s", config_path)
        except Exception as e:
            logger.warning("Failed to load config %s: %s", config_path, e)
    return result


def validate_config(config: Dict[str, Any]) -> List[str]:
    """Validate a merged config dict and return warnings for issues.

    Does **not** raise — problems are returned as warning strings so
    the pipeline can proceed with best-effort defaults.

    Args:
        config: Merged course configuration dict.

    Returns:
        List of human-readable warning strings (empty if valid).
    """
    warnings: List[str] = []

    for key in config:
        if key not in VALID_SECTIONS:
            warnings.append(f"Unknown config section: '{key}'")

    # --- metadata ---
    metadata = config.get("metadata", {})
    if not isinstance(metadata, dict):
        warnings.append("'metadata' should be a table/dict")
    else:
        if "authors" in metadata and not isinstance(metadata["authors"], list):
            warnings.append("'metadata.authors' should be a list")
        if "tags" in metadata and not isinstance(metadata["tags"], list):
            warnings.append("'metadata.tags' should be a list")

    # --- audience ---
    audience = config.get("audience", {})
    if not isinstance(audience, dict):
        warnings.append("'audience' should be a table/dict")
    else:
        if "estimated_hours" in audience and not isinstance(
            audience["estimated_hours"], (int, float)
        ):
            warnings.append("'audience.estimated_hours' should be a number")

    # --- localization ---
    localization = config.get("localization", {})
    if not isinstance(localization, dict):
        warnings.append("'localization' should be a table/dict")
    else:
        if "rtl" in localization and not isinstance(localization["rtl"], bool):
            warnings.append("'localization.rtl' should be a boolean")

    # --- rendering ---
    rendering = config.get("rendering", {})
    if not isinstance(rendering, dict):
        warnings.append("'rendering' should be a table/dict")
    else:
        audio = rendering.get("audio", {})
        if isinstance(audio, dict):
            if "slow" in audio and not isinstance(audio["slow"], bool):
                warnings.append("'rendering.audio.slow' should be a boolean")
            if "speed" in audio and not isinstance(audio["speed"], (int, float)):
                warnings.append("'rendering.audio.speed' should be a number")

    return warnings
