"""Utility functions for content processing.

Functions migrated from scripts/renumber_questions.py and shared logic
from labs/questions/quizzes generation.
"""

import re
import logging
from pathlib import Path
from typing import List, Dict, Tuple, Any

logger = logging.getLogger(__name__)


def extract_questions_from_sectioned(content: str) -> list[str]:
    """Extract all questions from a sectioned questions.md file.

    Handles format like:
    1.  **Topic Header**
        *   Question one?
        *   Question two?

    Args:
        content: The markdown content to parse

    Returns:
        List of question strings extracted from bullet points
    """
    questions = []

    # Find all bullet point questions (lines starting with * or -)
    lines = content.split("\n")
    for line in lines:
        stripped = line.strip()
        # Match lines that start with * or - and contain a question
        if stripped.startswith("*") or stripped.startswith("-"):
            # Remove the bullet point marker
            question = stripped.lstrip("*- \t")
            if question and len(question) > 5:  # Skip very short items
                questions.append(question)

    return questions


def format_as_continuous(questions: list[str], title: str) -> str:
    """Format questions as a continuous numbered list.

    Args:
        questions: List of question strings
        title: Title for the questions document

    Returns:
        Formatted markdown string with numbered questions
    """
    lines = [f"# {title}", ""]

    for i, q in enumerate(questions, 1):
        lines.append(f"{i}. {q}")
        lines.append("")

    return "\n".join(lines)


def normalize_whitespace(content: str) -> str:
    """Normalize whitespace in markdown content.

    - Removes trailing whitespace from lines
    - Collapses multiple blank lines into at most two
    - Ensures file ends with single newline

    Args:
        content: The markdown content to normalize

    Returns:
        Normalized markdown content
    """
    lines = content.split("\n")

    # Remove trailing whitespace from each line
    lines = [line.rstrip() for line in lines]

    # Collapse multiple blank lines
    result = []
    blank_count = 0
    for line in lines:
        if line == "":
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)

    # Ensure single trailing newline
    while result and result[-1] == "":
        result.pop()
    result.append("")

    return "\n".join(result)


def extract_headers(content: str) -> List[Tuple[int, str]]:
    """Extract all markdown headers from content.

    Args:
        content: The markdown content to parse

    Returns:
        List of tuples (level, header_text) where level is 1-6
    """
    headers = []
    lines = content.split("\n")

    for line in lines:
        # Match markdown headers (# Header, ## Header, etc.)
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            headers.append((level, text))

    return headers


def count_questions(content: str) -> Dict[str, int]:
    """Count questions in markdown content by type.

    Detects numbered questions (1. Question?), bullet questions (* Question?),
    and questions ending with ? within text.

    Args:
        content: The markdown content to analyze

    Returns:
        Dictionary with counts:
        - numbered: Questions starting with number and period
        - bulleted: Questions starting with * or -
        - inline: Lines containing ? (potential questions)
    """
    lines = content.split("\n")

    counts = {
        "numbered": 0,
        "bulleted": 0,
        "inline": 0,
    }

    for line in lines:
        stripped = line.strip()
        if re.match(r"^\d+\.", stripped):
            counts["numbered"] += 1
        elif stripped.startswith("*") or stripped.startswith("-"):
            counts["bulleted"] += 1
        elif "?" in stripped:
            counts["inline"] += 1

    return counts


def extract_numbered_items(content: str) -> List[str]:
    """Extract all numbered list items from markdown content.

    Args:
        content: The markdown content to parse

    Returns:
        List of text for each numbered item
    """
    items = []
    lines = content.split("\n")

    for line in lines:
        # Match numbered list items: "1. Text" or "12. Text"
        match = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if match:
            items.append(match.group(1))

    return items


def validate_question_format(content: str) -> Dict[str, Any]:
    """Validate that a questions.md file has proper format.

    Args:
        content: The markdown content to validate

    Returns:
        Dictionary with validation results:
        - valid: bool indicating if format is correct
        - has_title: bool if file has # header
        - question_count: number of detected questions
        - issues: list of format issues found
    """
    result: Dict[str, Any] = {
        "valid": True,
        "has_title": False,
        "question_count": 0,
        "issues": [],
    }

    lines = content.split("\n")

    # Check for title
    for line in lines:
        if line.startswith("# "):
            result["has_title"] = True
            break

    if not result["has_title"]:
        result["issues"].append("Missing title (# Header)")
        result["valid"] = False

    # Count questions
    counts = count_questions(content)
    result["question_count"] = counts["numbered"] + counts["bulleted"]

    if result["question_count"] == 0:
        result["issues"].append("No questions found")
        result["valid"] = False

    return result


def parse_module(module_dir: Path) -> Dict[str, Any]:
    """Parse module.md and extract content for lab/quiz/question generation."""
    path = module_dir / "module.md"
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    data: Dict[str, Any] = {
        "title": "",
        "subtitle": "",
        "overview": "",
        "objectives": [],
        "key_concepts": [],
        "lesson_content": "",
        "summary": "",
        "activities": [],
        "subsections": [],
    }
    lines = text.split("\n")

    # Title (first H1)
    for ln in lines:
        if ln.startswith("# "):
            data["title"] = ln[2:].strip()
            break

    # Subtitle (first H2 that isn't a section header keyword)
    skip_kw = {
        "overview",
        "introduction",
        "learning",
        "key ",
        "core",
        "lesson",
        "summary",
        "reference",
        "further",
        "example",
        "contents",
        "activity",
        "connection",
        "practice",
    }
    found_title = False
    for ln in lines:
        if ln.startswith("# "):
            found_title = True
            continue
        if found_title and ln.startswith("## "):
            heading = ln[3:].strip().lower()
            if not any(kw in heading for kw in skip_kw):
                data["subtitle"] = ln[3:].strip()
                break

    # Split into H2 sections
    sections: Dict[str, str] = {}
    cur_key = ""
    cur_lines: List[str] = []
    for ln in lines:
        if ln.startswith("## "):
            if cur_key:
                sections[cur_key] = "\n".join(cur_lines).strip()
            cur_key = ln[3:].strip()
            cur_lines = []
        else:
            cur_lines.append(ln)
    if cur_key:
        sections[cur_key] = "\n".join(cur_lines).strip()

    # Overview
    for k in sections:
        if "overview" in k.lower() or "introduction" in k.lower():
            data["overview"] = sections[k]
            break

    # Objectives
    for k in sections:
        if "learning" in k.lower() and ("goal" in k.lower() or "objective" in k.lower()):
            for m in re.finditer(r"^\d+\.\s*(.+)$", sections[k], re.MULTILINE):
                obj = re.sub(r"\*\*([^*]+)\*\*", r"\1", m.group(1).strip())
                data["objectives"].append(obj)
            break

    # Key concepts
    for k in sections:
        if "key" in k.lower() and (
            "concept" in k.lower() or "vocab" in k.lower() or "term" in k.lower()
        ):
            for m in re.finditer(
                r"-\s*\*\*([^*]+)\*\*\s*[-—:]\s*(.+?)(?=\n-|\n\n|\Z)",
                sections[k],
                re.DOTALL,
            ):
                name = m.group(1).strip()
                defn = m.group(2).strip().replace("\n", " ")
                defn = re.sub(r"\*\*([^*]+)\*\*", r"\1", defn)
                defn = re.sub(r"^-\s*", "", defn)
                data["key_concepts"].append((name, defn))
            break

    # Lesson content
    for k in sections:
        if "lesson" in k.lower() or "core concept" in k.lower():
            data["lesson_content"] = sections[k]
            break

    # Extract H3 subsection titles from the lesson content
    for m in re.finditer(r"^### (.+)$", text, re.MULTILINE):
        heading = m.group(1).strip()
        if heading and not heading[0].isdigit():
            data["subsections"].append(heading)

    # Summary
    for k in sections:
        if k.lower() == "summary":
            data["summary"] = sections[k]
            break

    # Activity / Practice sections (if present)
    for k in sections:
        if "activity" in k.lower() or "practice" in k.lower():
            data["activities"].append(sections[k])

    return data


def get_audience_info(course: str) -> Dict[str, Any]:
    """Return audience-specific details for content generation."""
    if "es" in course and "embodied" not in course:
        return {
            "level": "elementary",
            "tone": "Grades K-5",
            "lab_style": "hands-on activity with drawing and discussion",
            "time_total": "30-40 minutes",
            "part_times": ["10 minutes", "15 minutes", "10 minutes"],
        }
    elif "ms" in course:
        return {
            "level": "middle",
            "tone": "Grades 6-8",
            "lab_style": "experiment and group investigation",
            "time_total": "40-50 minutes",
            "part_times": ["15 minutes", "20 minutes", "10 minutes"],
        }
    elif "hs" in course:
        return {
            "level": "high_school",
            "tone": "Grades 9-12",
            "lab_style": "structured analysis and collaborative discussion",
            "time_total": "45-55 minutes",
            "part_times": ["15 minutes", "20 minutes", "15 minutes"],
        }
    elif "101" in course:
        return {
            "level": "college",
            "tone": "College First Semester",
            "lab_style": "concept analysis, application, and reflection",
            "time_total": "50-60 minutes",
            "part_times": ["20 minutes", "20 minutes", "15 minutes"],
        }
    elif "401" in course:
        return {
            "level": "graduate",
            "tone": "Graduate Level",
            "lab_style": "research exercise and critical analysis",
            "time_total": "60-90 minutes",
            "part_times": ["25 minutes", "30 minutes", "20 minutes"],
        }
    elif "embodied" in course:
        return {
            "level": "practitioner",
            "tone": "Movement Practitioners",
            "lab_style": "somatic exploration and embodied reflection",
            "time_total": "45-60 minutes",
            "part_times": ["15 minutes", "20 minutes", "15 minutes"],
        }
    elif "organizations" in course:
        return {
            "level": "professional",
            "tone": "Organizational Leaders",
            "lab_style": "case analysis and strategic exercise",
            "time_total": "45-60 minutes",
            "part_times": ["15 minutes", "20 minutes", "15 minutes"],
        }
    elif "robotics" in course:
        return {
            "level": "technical",
            "tone": "Robotics Practitioners",
            "lab_style": "design exercise and system analysis",
            "time_total": "50-60 minutes",
            "part_times": ["20 minutes", "20 minutes", "15 minutes"],
        }
    else:
        return {
            "level": "general",
            "tone": "General Audience",
            "lab_style": "exploration and reflection",
            "time_total": "40-50 minutes",
            "part_times": ["15 minutes", "20 minutes", "10 minutes"],
        }
