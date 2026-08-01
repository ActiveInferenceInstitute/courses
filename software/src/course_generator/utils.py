"""Utility functions for course generation."""

import logging
import re
from pathlib import Path

logger = logging.getLogger("course_generator")


def slugify(text: str) -> str:
    """Convert text to a URL/directory-safe slug.

    Args:
        text: Input text to slugify.

    Returns:
        Lowercase, underscore-separated slug string.

    Examples:
        >>> slugify("Hello World")
        'hello_world'
        >>> slugify("Active Inference: Philosophy")
        'active_inference_philosophy'
    """
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s_-]", "", text)
    text = re.sub(r"[\s-]+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text.strip("_")


def resolve_repo_root(start_path: Path | None = None) -> Path:
    """Find the repository root by looking for pyproject.toml or .git.

    Args:
        start_path: Starting directory for upward search.
            Defaults to the software/ directory.

    Returns:
        Path to the repository root.

    Raises:
        FileNotFoundError: If no repo root markers are found.
    """
    if start_path is None:
        # Default: software/ is two levels below this file
        start_path = Path(__file__).parent.parent.parent

    current = start_path.resolve()
    for _ in range(10):  # Max 10 levels up
        if (current / ".git").exists():
            return current
        if (current / "pyproject.toml").exists():
            # Could be the software dir itself — check for .git above
            if (current.parent / ".git").exists():
                return current.parent
            return current
        current = current.parent

    raise FileNotFoundError(f"Could not find repository root starting from {start_path}")


def count_files(directory: Path, pattern: str = "*") -> int:
    """Count files matching a glob pattern in a directory tree.

    Args:
        directory: Root directory to search.
        pattern: Glob pattern to match (default: all files).

    Returns:
        Number of matching files.
    """
    if not directory.exists():
        return 0
    return sum(1 for _ in directory.rglob(pattern) if _.is_file())


def validate_structure(
    curriculum_dir: Path, expected_files: list[str] | None = None
) -> dict[str, list[str]]:
    """Validate that a curriculum directory has the expected structure.

    Checks for the presence of all expected directories and files.

    Args:
        curriculum_dir: Path to the curriculum root directory.
        expected_files: Optional list of expected relative file paths.

    Returns:
        Dictionary with 'present', 'missing', and 'extra' file lists.
    """
    result: dict[str, list[str]] = {
        "present": [],
        "missing": [],
        "extra": [],
    }

    if expected_files is None:
        logger.warning("No expected files list provided, skipping validation")
        return result

    actual_files = set()
    if curriculum_dir.exists():
        for f in curriculum_dir.rglob("*"):
            if f.is_file() and not any(part.startswith(".") for part in f.parts):
                actual_files.add(str(f.relative_to(curriculum_dir)))

    expected_set = set(expected_files)

    result["present"] = sorted(actual_files & expected_set)
    result["missing"] = sorted(expected_set - actual_files)
    result["extra"] = sorted(actual_files - expected_set)

    return result


def format_table_row(cells: list[str]) -> str:
    """Format a list of cell values as a Markdown table row.

    Args:
        cells: List of cell content strings.

    Returns:
        Formatted Markdown table row string.
    """
    return "| " + " | ".join(cells) + " |"


def format_table_separator(num_cols: int) -> str:
    """Generate a Markdown table separator row.

    Args:
        num_cols: Number of columns.

    Returns:
        Formatted separator row string.
    """
    return "| " + " | ".join(["---"] * num_cols) + " |"
