"""Configuration for validation module."""

# Default required formats when no --formats specified (minimum viable output)
DEFAULT_REQUIRED_FORMATS = ["pdf", "docx"]


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


# Published directory name
PUBLISHED_DIR_NAME = "published"

# Logging configuration
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FORMAT = "[%(levelname)s] %(asctime)s - %(message)s"
