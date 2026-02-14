"""Utility functions for HTML website generation."""

import json
from pathlib import Path
from typing import Dict, List, Optional

import markdown


def read_markdown_file(file_path: Path) -> str:
    """Read markdown file content.

    Args:
        file_path: Path to markdown file

    Returns:
        File content as string

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {file_path}")
    return file_path.read_text(encoding="utf-8")


def markdown_to_html(markdown_content: str) -> str:
    """Convert markdown content to HTML.

    Args:
        markdown_content: Markdown text content

    Returns:
        HTML content
    """
    md = markdown.Markdown(extensions=["extra", "codehilite", "tables"])
    return md.convert(markdown_content)


def find_audio_file(base_name: str, output_dir: Path, curriculum_type: str) -> Optional[Path]:
    """Find audio file for a given base name and curriculum type.

    Args:
        base_name: Base filename without extension
        output_dir: Output directory to search
        curriculum_type: Type of curriculum element (assignments, lecture-content, etc.)

    Returns:
        Path to audio file if found, None otherwise
    """
    audio_path = output_dir / curriculum_type / f"{base_name}.mp3"
    if audio_path.exists():
        return audio_path
    return None


def find_text_file(base_name: str, output_dir: Path, curriculum_type: str) -> Optional[Path]:
    """Find text file for a given base name and curriculum type.

    Args:
        base_name: Base filename without extension
        output_dir: Output directory to search
        curriculum_type: Type of curriculum element

    Returns:
        Path to text file if found, None otherwise
    """
    text_path = output_dir / curriculum_type / f"{base_name}.txt"
    if text_path.exists():
        return text_path
    return None


def get_relative_path(target: Path, base: Path) -> str:
    """Get relative path from base to target.

    Args:
        target: Target file path
        base: Base directory path

    Returns:
        Relative path string
    """
    try:
        return str(target.relative_to(base))
    except ValueError:
        return str(target)


def extract_quiz_questions(markdown_content: str) -> List[dict]:
    """Extract quiz questions from markdown content.

    Looks for sections with "Review Questions" or "Practice Problems".

    Args:
        markdown_content: Markdown content to parse

    Returns:
        List of question dictionaries with 'question' and 'options' keys
    """
    questions = []
    lines = markdown_content.split("\n")
    in_questions = False
    current_question = None

    for line in lines:
        line_lower = line.lower()
        if "review questions" in line_lower or "practice problems" in line_lower:
            in_questions = True
            continue

        if in_questions and line.strip():
            # Check if it's a numbered question
            if line.strip().startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")):
                if current_question:
                    questions.append(current_question)
                question_text = line.strip()
                # Remove leading number
                for i in range(1, 10):
                    if question_text.startswith(f"{i}. "):
                        question_text = question_text[len(f"{i}. "):]
                        break
                current_question = {
                    "question": question_text,
                    "options": [],
                    "correct": None,  # Will be determined by user interaction
                }
            elif current_question and line.strip().startswith("-"):
                # This is an option
                option_text = line.strip()[1:].strip()
                current_question["options"].append(option_text)

    if current_question:
        questions.append(current_question)

    return questions


def ensure_output_directory(directory: Path) -> None:
    """Ensure output directory exists.

    Args:
        directory: Directory path to create
    """
    directory.mkdir(parents=True, exist_ok=True)


def parse_questions_json(questions_file: Path) -> List[Dict]:
    """Parse questions from JSON file.

    Args:
        questions_file: Path to questions JSON file

    Returns:
        List of question dictionaries

    Raises:
        FileNotFoundError: If questions file doesn't exist
        json.JSONDecodeError: If JSON is invalid
    """
    if not questions_file.exists():
        raise FileNotFoundError(f"Questions file not found: {questions_file}")

    content = questions_file.read_text(encoding="utf-8")
    data = json.loads(content)

    if "questions" not in data:
        return []

    return data["questions"]


def find_questions_file(module_dir: Path) -> Optional[Path]:
    """Find questions JSON file in module directory.

    Args:
        module_dir: Path to module directory

    Returns:
        Path to questions file if found, None otherwise
    """
    questions_dir = module_dir / "questions"
    if not questions_dir.exists():
        return None

    questions_file = questions_dir / "questions.json"
    if questions_file.exists():
        return questions_file

    return None
