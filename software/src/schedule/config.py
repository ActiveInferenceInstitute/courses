"""Configuration for schedule processing."""

from typing import Dict, List

# Supported schedule output formats
SUPPORTED_OUTPUT_FORMATS: List[str] = ["pdf", "html", "docx", "txt", "mp3"]

# Schedule file patterns
SCHEDULE_FILE_PATTERNS: List[str] = ["Schedule.md", "schedule.md", "*schedule*.md"]

# Table column mappings for schedule parsing
SCHEDULE_COLUMNS: Dict[str, int] = {
    "week": 0,
    "date": 1,
    "topic": 2,
    "notes": 3,
}

# Default schedule table headers
DEFAULT_HEADERS: List[str] = ["Week", "Date", "Topic", "Notes"]
