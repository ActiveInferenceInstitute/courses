"""Utility functions for schedule processing."""

import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from . import config


def parse_schedule_table(content: str) -> List[Dict[str, str]]:
    """Parse schedule table from markdown content.

    Args:
        content: Markdown content containing schedule table

    Returns:
        List of dictionaries with schedule entries (week, date, topic, notes)
    """
    schedule_entries = []

    # Find table in markdown (between | characters)
    table_pattern = r"\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|"
    table_lines = re.findall(table_pattern, content, re.MULTILINE)

    for line in table_lines:
        # Skip header separator lines (|---|---|)
        if re.match(r"\|[\s\-:]+\|", line):
            continue

        # Extract columns
        columns = [col.strip() for col in line.split("|")[1:-1]]

        if len(columns) >= 3:
            entry = {
                "week": columns[config.SCHEDULE_COLUMNS.get("week", 0)],
                "date": columns[config.SCHEDULE_COLUMNS.get("date", 1)],
                "topic": columns[config.SCHEDULE_COLUMNS.get("topic", 2)],
                "notes": columns[config.SCHEDULE_COLUMNS.get("notes", 3)] if len(columns) > 3 else "",
            }
            schedule_entries.append(entry)

    return schedule_entries


def extract_schedule_sections(content: str) -> Dict[str, str]:
    """Extract sections from schedule markdown (title, dates, exams, etc.).

    Args:
        content: Markdown content

    Returns:
        Dictionary with section names as keys and content as values
    """
    sections = {}

    # Extract title
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if title_match:
        sections["title"] = title_match.group(1).strip()

    # Extract semester/year
    semester_match = re.search(r"##\s+(.+)$", content, re.MULTILINE)
    if semester_match:
        sections["semester"] = semester_match.group(1).strip()

    # Extract important dates section
    dates_match = re.search(r"## Important Dates\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if dates_match:
        sections["important_dates"] = dates_match.group(1).strip()

    # Extract exam schedule section
    exams_match = re.search(r"## Exam Schedule\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if exams_match:
        sections["exam_schedule"] = exams_match.group(1).strip()

    return sections


def format_date(date_str: str) -> Optional[str]:
    """Format date string to standard format.

    Args:
        date_str: Date string in various formats (e.g., "1/19/2026", "01/19/2026")

    Returns:
        Formatted date string or None if parsing fails
    """
    if not date_str:
        return None

    # Try to parse common date formats
    date_formats = ["%m/%d/%Y", "%m-%d-%Y", "%Y-%m-%d"]
    for fmt in date_formats:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            return dt.strftime("%B %d, %Y")
        except ValueError:
            continue

    return date_str  # Return original if parsing fails


def validate_schedule_entry(entry: Dict[str, str]) -> bool:
    """Validate a schedule entry has required fields.

    Args:
        entry: Schedule entry dictionary

    Returns:
        True if entry is valid, False otherwise
    """
    required_fields = ["week", "date", "topic"]
    return all(field in entry and entry[field].strip() for field in required_fields)


def generate_schedule_markdown(
    entries: List[Dict[str, str]], sections: Optional[Dict[str, str]] = None
) -> str:
    """Generate formatted markdown from schedule entries.

    Args:
        entries: List of schedule entry dictionaries
        sections: Optional dictionary with additional sections (title, semester, etc.)

    Returns:
        Formatted markdown string
    """
    lines = []

    # Add title and semester
    if sections:
        if "title" in sections:
            lines.append(f"# {sections['title']}")
        if "semester" in sections:
            lines.append(f"## {sections['semester']}")
        lines.append("")

    # Generate table
    lines.append("| Week | Date | Topic | Notes |")
    lines.append("|------|------|-------|-------|")

    for entry in entries:
        week = entry.get("week", "")
        date = entry.get("date", "")
        topic = entry.get("topic", "")
        notes = entry.get("notes", "")
        lines.append(f"| {week} | {date} | {topic} | {notes} |")

    lines.append("")

    # Add additional sections
    if sections:
        if "important_dates" in sections:
            lines.append("## Important Dates")
            lines.append("")
            lines.append(sections["important_dates"])
            lines.append("")

        if "exam_schedule" in sections:
            lines.append("## Exam Schedule")
            lines.append("")
            lines.append(sections["exam_schedule"])
            lines.append("")

    return "\n".join(lines)


def find_schedule_files(directory: Path) -> List[Path]:
    """Find schedule markdown files in a directory.

    Args:
        directory: Directory to search

    Returns:
        List of schedule file paths
    """
    schedule_files = []
    for pattern in config.SCHEDULE_FILE_PATTERNS:
        if "*" in pattern:
            # Handle glob patterns
            schedule_files.extend(directory.rglob(pattern))
        else:
            # Exact filename match
            if (directory / pattern).exists():
                schedule_files.append(directory / pattern)

    return sorted(set(schedule_files))


def read_schedule_file(file_path: Path) -> str:
    """Read schedule markdown file content.

    Args:
        file_path: Path to schedule file

    Returns:
        File content as string

    Raises:
        FileNotFoundError: If file doesn't exist
        OSError: If file cannot be read
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Schedule file not found: {file_path}")

    return file_path.read_text(encoding="utf-8")


def ensure_output_directory(output_path: Path) -> None:
    """Ensure output directory exists, creating if necessary.

    Args:
        output_path: Path to output file or directory
    """
    if output_path.is_file() or output_path.suffix:
        output_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        output_path.mkdir(parents=True, exist_ok=True)
