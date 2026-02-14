"""Utility functions for the legacy import module."""

import re
import logging
from pathlib import Path

from src.module_organization.main import create_module_structure

logger = logging.getLogger(__name__)


def extract_chapter_number(filename: str) -> int:
    """Extract chapter number from filename.

    Args:
        filename: Filename like "Chapter 01 Keys to Success.docx" or
                 "General Biology Chapter 01 Slides.pdf"

    Returns:
        Chapter number as integer

    Raises:
        ValueError: If chapter number cannot be extracted
    """
    # Pattern for "Chapter NN" or "Chapter 0N"
    match = re.search(r"Chapter\s+0?(\d+)", filename, re.IGNORECASE)
    if match:
        return int(match.group(1))

    raise ValueError(f"Could not extract chapter number from filename: {filename}")


def ensure_module_exists(course_root: Path, module_num: int, dry_run: bool) -> Path:
    """Ensure module exists, creating it if necessary.

    Args:
        course_root: Course root directory (e.g., biol-1)
        module_num: Module number
        dry_run: If True, only check existence without creating

    Returns:
        Path to module directory
    """
    from src.module_organization.utils import get_module_path

    module_path = get_module_path(course_root, module_num)

    if not module_path.exists():
        if dry_run:
            logger.info(f"[DRY RUN] Would create module-{module_num}")
        else:
            logger.info(f"Creating module-{module_num}")
            try:
                created_path = create_module_structure(str(course_root), module_num)
                logger.debug(f"Successfully created module {module_num} at {created_path}")
            except ValueError as e:
                # Module might already exist from concurrent creation
                if "already exists" in str(e):
                    logger.debug(f"Module {module_num} already exists (concurrent creation)")
                else:
                    logger.error(f"Could not create module {module_num}: {e}")
                    raise
            except Exception as e:
                logger.error(
                    f"Unexpected error creating module {module_num}: {e}", exc_info=True
                )
                raise

    return module_path


def create_comprehension_questions(
    module_path: Path, module_num: int, dry_run: bool
) -> None:
    """Create comprehension-questions.md file in resources directory.

    Args:
        module_path: Path to module directory
        module_num: Module number
        dry_run: If True, only show what would be created
    """
    resources_dir = module_path / "resources"
    if not dry_run:
        resources_dir.mkdir(parents=True, exist_ok=True)

    file_path = resources_dir / "comprehension-questions.md"
    if not file_path.exists():
        if dry_run:
            logger.info("[DRY RUN] Would create resources/comprehension-questions.md")
        else:
            content = (
                f"# Comprehension Questions - Module {module_num}\n\n"
                f"Comprehension questions for Module {module_num}.\n"
            )
            file_path.write_text(content, encoding="utf-8")
            logger.debug(f"Created: {file_path}")


def create_questions_directory(
    module_path: Path, module_num: int, dry_run: bool
) -> None:
    """Create questions directory with questions.json, README.md, and AGENTS.md.

    Args:
        module_path: Path to module directory
        module_num: Module number
        dry_run: If True, only show what would be created
    """
    questions_dir = module_path / "questions"

    if dry_run:
        logger.info("[DRY RUN] Would create questions/ directory")
        return

    questions_dir.mkdir(parents=True, exist_ok=True)

    # Create questions.json if it doesn't exist
    questions_json = questions_dir / "questions.json"
    if not questions_json.exists():
        questions_json.write_text('{\n  "questions": []\n}\n', encoding="utf-8")
        logger.debug(f"Created: {questions_json}")

    # Create README.md if it doesn't exist
    readme = questions_dir / "README.md"
    if not readme.exists():
        readme_content = f"""# Module {module_num} Questions

## Overview

This directory contains interactive questions for Module {module_num}. Questions are stored in JSON format and are displayed interactively on the module website.

## Question Files

- **`questions.json`**: Main question file containing all interactive questions for this module

## Question Types

The questions support multiple interactive formats:

- **Multiple Choice**: Select one correct answer from multiple options
- **Free Response**: Text input for open-ended answers
- **True/False**: Binary choice questions
- **Matching**: Match terms with their definitions or related concepts

## Usage

Questions are automatically processed and displayed on the module website at `output/website/index.html`. Students can interact with questions directly in the browser.

## Documentation

- **[AGENTS.md](AGENTS.md)**: Technical documentation for question format and processing
"""
        readme.write_text(readme_content, encoding="utf-8")
        logger.debug(f"Created: {readme}")

    # Create AGENTS.md if it doesn't exist
    agents = questions_dir / "AGENTS.md"
    if not agents.exists():
        agents_content = f"""# Module {module_num} Questions Technical Documentation

## Overview

Technical documentation for question format, structure, and processing for Module {module_num}.

## Question Format

Questions are stored in JSON format with the following structure:

```json
{{
  "questions": [
    {{
      "id": "unique-question-id",
      "type": "multiple_choice|free_response|true_false|matching",
      "question": "Question text",
      ...
    }}
  ]
}}
```

## Question Types

### Multiple Choice

```json
{{
  "id": "q1",
  "type": "multiple_choice",
  "question": "Question text",
  "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
  "correct": 0,
  "explanation": "Explanation of correct answer"
}}
```

- `options`: Array of answer choices
- `correct`: Index (0-based) of correct answer
- `explanation`: Optional explanation shown after answer

### Free Response

```json
{{
  "id": "q2",
  "type": "free_response",
  "question": "Question text",
  "placeholder": "Optional placeholder text",
  "max_length": 500
}}
```

- `placeholder`: Optional placeholder text for textarea
- `max_length`: Optional maximum character count

### True/False

```json
{{
  "id": "q3",
  "type": "true_false",
  "question": "Question text",
  "correct": true,
  "explanation": "Explanation of answer"
}}
```

- `correct`: Boolean value (true or false)
- `explanation`: Optional explanation

### Matching

```json
{{
  "id": "q4",
  "type": "matching",
  "question": "Match the terms with definitions",
  "items": [
    {{"term": "Term 1", "definition": "Definition 1"}},
    {{"term": "Term 2", "definition": "Definition 2"}}
  ]
}}
```

- `items`: Array of term-definition pairs to match

## Processing

Questions are processed by the HTML website generation module:

- **Module**: `software/src/html_website/main.py`
- **Function**: `generate_module_website()`
- **Utility**: `parse_questions_json()` from `html_website/utils.py`

## Output

Questions are rendered as interactive HTML elements on the module website with:
- Answer validation
- Feedback and explanations
- Progress tracking
- State persistence
"""
        agents.write_text(agents_content, encoding="utf-8")
        logger.debug(f"Created: {agents}")
