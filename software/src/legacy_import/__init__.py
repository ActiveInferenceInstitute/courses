"""Legacy import module for importing materials from bio_1_2025 to biol-1 structure."""

from .main import (
    process_chapter_questions,
    process_slides,
    create_for_upload_files,
    process_for_upload_all_modules,
)
from .utils import (
    extract_chapter_number,
    ensure_module_exists,
    create_comprehension_questions,
    create_questions_directory,
)
from .config import (
    get_chapter_to_module_mapping,
    CHAPTER_COUNT,
    QUESTION_FILE_PATTERN,
    SLIDE_FILE_PATTERN,
    EXCLUDED_MD_FILES,
)

__all__ = [
    "process_chapter_questions",
    "process_slides",
    "create_for_upload_files",
    "process_for_upload_all_modules",
    "extract_chapter_number",
    "ensure_module_exists",
    "create_comprehension_questions",
    "create_questions_directory",
    "get_chapter_to_module_mapping",
    "CHAPTER_COUNT",
    "QUESTION_FILE_PATTERN",
    "SLIDE_FILE_PATTERN",
    "EXCLUDED_MD_FILES",
]
