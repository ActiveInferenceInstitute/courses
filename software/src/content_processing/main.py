"""Main logic for the content_processing module."""

import re
import logging
from pathlib import Path
from typing import Optional, List

from . import config
from .utils import extract_questions_from_sectioned, format_as_continuous

logger = logging.getLogger(__name__)


def process_questions_file(
    filepath: Path,
    dry_run: bool = False,
    verbose: bool = False
) -> tuple[bool, int]:
    """Process a single questions.md file to use continuous numbering.

    Args:
        filepath: Path to the questions.md file
        dry_run: If True, show what would be changed without writing
        verbose: If True, log detailed processing information

    Returns:
        Tuple of (was_changed, question_count)
    """
    content = filepath.read_text()

    # Check if already in continuous format (no ### sections with Part headers)
    if not re.search(r'\n###\s+Part', content):
        # Already in continuous format
        count = len(re.findall(r'^\d+\.', content, re.MULTILINE))
        return False, count

    # Extract title from first line
    first_line = content.split('\n')[0]
    title = first_line.lstrip('# ').strip()

    # Extract questions
    questions = extract_questions_from_sectioned(content)

    if not questions:
        return False, 0

    # Generate new content
    new_content = format_as_continuous(questions, title)

    if verbose:
        logger.info(f"    Title: {title}")
        logger.info(f"    Questions extracted: {len(questions)}")

    # Write back
    if not dry_run:
        filepath.write_text(new_content)

    return True, len(questions)


def renumber_questions_in_course(
    repo_root: Path,
    courses: Optional[List[str]] = None,
    module_filter: Optional[str] = None,
    dry_run: bool = False,
    verbose: bool = False,
    course_registry: Optional[dict] = None,
) -> dict:
    """Renumber questions.md files in specified courses.

    Args:
        repo_root: Path to the repository root
        courses: List of course names (default: from config)
        module_filter: Optional specific module to process (e.g., 'module-03')
        dry_run: If True, show what would be changed without writing
        verbose: If True, log detailed processing information
        course_registry: Optional mapping of course IDs to registry metadata.
            When provided, used to resolve course paths. Pass
            ``batch_processing.config.COURSE_REGISTRY`` at the call site;
            omitting it keeps content_processing free of batch_processing imports.

    Returns:
        Dictionary with processing results
    """
    if courses is None:
        courses = config.DEFAULT_COURSES

    if course_registry is None:
        course_registry = {}

    results = {
        "courses_processed": [],
        "files_converted": 0,
        "total_questions": 0,
        "errors": [],
    }

    for course in courses:
        if course in course_registry:
            entry = course_registry[course]
            course_root = repo_root / entry["rel_path"]
            if entry.get("has_course_subdir", False):
                course_path = course_root / config.COURSE_CONTENT_DIR
            else:
                course_path = course_root
        else:
            # Fallback for legacy or unknown courses
            course_path = repo_root / config.COURSE_DEV_DIR / course / config.COURSE_CONTENT_DIR

        if not course_path.exists():
            results["errors"].append(f"Course path not found: {course_path}")
            continue

        course_result = {
            "name": course,
            "modules": [],
        }

        if module_filter:
            module_dirs = [course_path / module_filter]
        else:
            # Use the course-registry module_glob if available, else default to module-*
            module_glob = 'module-*'
            if course in course_registry:
                module_glob = course_registry[course].get('module_glob', module_glob)
            module_dirs = sorted(course_path.glob(module_glob))

        for module_dir in module_dirs:
            if not module_dir.exists():
                continue

            questions_file = module_dir / 'questions.md'

            if not questions_file.exists():
                continue

            try:
                was_changed, count = process_questions_file(
                    questions_file, dry_run=dry_run, verbose=verbose
                )

                course_result["modules"].append({
                    "name": module_dir.name,
                    "converted": was_changed,
                    "question_count": count,
                })

                if was_changed:
                    results["files_converted"] += 1
                results["total_questions"] += count

            except Exception as e:
                results["errors"].append(f"{module_dir.name}: {e}")

        results["courses_processed"].append(course_result)

    return results
