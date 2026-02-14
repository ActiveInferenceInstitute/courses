"""Configuration and constants for the legacy import module."""

from typing import Dict


# Total number of chapters/modules (1:1 mapping, chapters 1-17)
CHAPTER_COUNT = 17

# Glob patterns for source files
QUESTION_FILE_PATTERN = "*.docx"
SLIDE_FILE_PATTERN = "*.pdf"

# Markdown files excluded from for_upload processing
EXCLUDED_MD_FILES = {"README.md", "AGENTS.md"}

# Source directory names (relative to bio_1_2025 root)
SOURCE_QUESTIONS_SUBDIR = "files/Chapter Questions"
SOURCE_SLIDES_FULL_SUBDIR = "files/Slides/Slides_Full"
SOURCE_SLIDES_NOTES_SUBDIR = "files/Slides/Slides_Notes"


def get_chapter_to_module_mapping() -> Dict[int, int]:
    """Return mapping of chapter numbers to module numbers.

    Mapping: 17 chapters map to 17 modules (1:1 mapping)

    Returns:
        Dictionary mapping chapter numbers to module numbers
    """
    return {i: i for i in range(1, CHAPTER_COUNT + 1)}
