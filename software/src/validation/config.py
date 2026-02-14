"""Configuration for validation module."""

from pathlib import Path
from typing import Dict, List

# All supported output formats
ALL_SUPPORTED_FORMATS = ["pdf", "docx", "html", "txt", "mp3", "md"]

# Default required formats when no --formats specified (minimum viable output)
DEFAULT_REQUIRED_FORMATS = ["pdf", "docx"]

# Format-aware validation: These are the base file types (without extension)
STUDY_GUIDE_BASE_TYPES = ["keys-to-success", "questions"]

# Default expected output formats
EXPECTED_FORMATS = ["pdf", "docx", "html", "txt", "mp3"]

# Default required study guide files per module (MP3 is optional)
# NOTE: Use get_expected_study_guide_files(formats) for format-aware validation
EXPECTED_STUDY_GUIDE_FILES = [
    "keys-to-success.pdf",
    "keys-to-success.docx",
    "keys-to-success.html",
    "keys-to-success.txt",
    "questions.pdf",
    "questions.docx",
    "questions.html",
    "questions.txt",
]

# Optional study guide files (not counted toward validity)
OPTIONAL_STUDY_GUIDE_FILES = [
    "keys-to-success.mp3",
    "questions.mp3",
]


def get_expected_study_guide_files(formats: List[str] = None) -> List[str]:
    """Get expected study guide files based on requested formats.
    
    Args:
        formats: List of format extensions to validate (e.g., ["pdf", "docx", "md"])
                 If None, uses DEFAULT_REQUIRED_FORMATS
    
    Returns:
        List of expected file suffixes like ["keys-to-success.pdf", "questions.pdf", ...]
    """
    if formats is None:
        formats = DEFAULT_REQUIRED_FORMATS
    
    # Filter to only formats that produce study guide files (not md which is just a copy)
    renderable_formats = [f for f in formats if f in ["pdf", "docx", "html", "txt"]]
    
    files = []
    for base_type in STUDY_GUIDE_BASE_TYPES:
        for fmt in renderable_formats:
            files.append(f"{base_type}.{fmt}")
    
    return files


# Syllabus format configuration
SYLLABUS_REQUIRED_FORMATS = ["pdf", "docx"]  # Minimum for syllabus
SYLLABUS_OPTIONAL_FORMATS = ["html", "txt", "mp3", "md"]  # Nice to have


def get_syllabus_required_formats(formats: List[str] = None) -> List[str]:
    """Get required syllabus formats based on requested formats.
    
    Args:
        formats: List of format extensions requested (e.g., ["pdf", "docx", "md"])
                 If None, uses SYLLABUS_REQUIRED_FORMATS
    
    Returns:
        List of formats to require for syllabus validation
    """
    if formats is None:
        return SYLLABUS_REQUIRED_FORMATS
    
    # Only require formats that were actually requested AND are renderable
    renderable = ["pdf", "docx", "html", "txt"]
    return [f for f in formats if f in renderable]

# Expected website files
EXPECTED_WEBSITE_FILES = ["index.html"]

# Output directories
OUTPUT_DIRS = {
    "study_guides": "study-guides",
    "website": "website",
    "labs": "labs",
    "dashboards": "dashboards",
}

# Lab output formats (labs support PDF and HTML rendering)
LAB_OUTPUT_FORMATS = ["pdf", "html"]

# Course configurations
COURSE_CONFIG: Dict[str, Dict] = {
    "ai-philosophy": {
        "expected_modules": 8,
        "module_prefix": "",
        "module_glob": "[0-9][0-9]_*",
    },
    "ai-cognitive-science": {
        "expected_modules": 8,
        "module_prefix": "",
        "module_glob": "[0-9][0-9]_*",
    },
    "ai-math": {
        "expected_modules": 8,
        "module_prefix": "",
        "module_glob": "[0-9][0-9]_*",
    },
    "ai-computer-science": {
        "expected_modules": 8,
        "module_prefix": "",
        "module_glob": "[0-9][0-9]_*",
    },
}

# Syllabus expected outputs
SYLLABUS_EXPECTED_FORMATS = ["pdf", "docx", "html", "txt", "mp3"]

# Published directory name
PUBLISHED_DIR_NAME = "published"

# Logging configuration
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FORMAT = "[%(levelname)s] %(asctime)s - %(message)s"
