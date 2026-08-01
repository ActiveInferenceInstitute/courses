"""Scaffold generator — creates directory structures and files from schema.

This module handles deterministic file system operations:
creating directories, writing files, and managing the overall
curriculum layout. Content is delegated to `content.py`.
"""

import logging
import os
from pathlib import Path

from .schema import CurriculumConfig, CourseConfig, ModuleConfig
from . import content

logger = logging.getLogger("course_generator")


def generate_curriculum(
    config: CurriculumConfig,
    output_root: Path,
    overwrite: bool = False,
) -> dict[str, int]:
    """Generate the complete curriculum directory structure and files.

    Args:
        config: Curriculum configuration.
        output_root: Root output directory (e.g., repo_root/course_development).
        overwrite: If True, overwrite existing files.

    Returns:
        Dictionary with counts: files_created, files_skipped, dirs_created.

    Raises:
        ValueError: If config validation fails.
    """
    errors = config.validate()
    if errors:
        raise ValueError(f"Invalid curriculum config: {'; '.join(errors)}")

    stats = {"files_created": 0, "files_skipped": 0, "dirs_created": 0}

    # Resolve the curriculum directory
    curriculum_dir = output_root / config.id
    _ensure_dir(curriculum_dir, stats)

    logger.info(
        f"Generating curriculum '{config.title}' at {curriculum_dir} (~{config.total_files} files)"
    )

    # Root-level files
    _write_root_files(config, curriculum_dir, overwrite, stats)

    # Resources directory
    _write_resources(config, curriculum_dir, overwrite, stats)

    # Courses and modules
    for course in config.courses:
        course_dir = curriculum_dir / course.dir_name
        _ensure_dir(course_dir, stats)
        _write_course_files(config, course, course_dir, overwrite, stats)

        for module in course.modules:
            module_dir = course_dir / module.dir_name
            _ensure_dir(module_dir, stats)
            _write_module_files(config, course, module, module_dir, overwrite, stats)

    logger.info(
        f"Generation complete: {stats['files_created']} created, "
        f"{stats['files_skipped']} skipped, {stats['dirs_created']} dirs"
    )
    return stats


def generate_single_course(
    config: CurriculumConfig,
    course_number: int,
    output_root: Path,
    overwrite: bool = False,
) -> dict[str, int]:
    """Generate a single course within a curriculum.

    Args:
        config: Curriculum configuration.
        course_number: Course number (1-4) to generate.
        output_root: Root output directory.
        overwrite: If True, overwrite existing files.

    Returns:
        Dictionary with generation stats.

    Raises:
        ValueError: If course_number is invalid.
    """
    course = next((c for c in config.courses if c.number == course_number), None)
    if course is None:
        raise ValueError(f"No course with number {course_number}")

    stats = {"files_created": 0, "files_skipped": 0, "dirs_created": 0}
    curriculum_dir = output_root / config.id
    course_dir = curriculum_dir / course.dir_name
    _ensure_dir(course_dir, stats)
    _write_course_files(config, course, course_dir, overwrite, stats)

    for module in course.modules:
        module_dir = course_dir / module.dir_name
        _ensure_dir(module_dir, stats)
        _write_module_files(config, course, module, module_dir, overwrite, stats)

    logger.info(f"Course {course.title}: {stats['files_created']} files created")
    return stats


# ─── Private writers ────────────────────────────────────────────────────────


def _ensure_dir(path: Path, stats: dict[str, int]) -> None:
    """Create directory if it doesn't exist."""
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        stats["dirs_created"] += 1
        logger.debug(f"Created directory: {path}")


def _write_file(
    path: Path,
    file_content: str,
    overwrite: bool,
    stats: dict[str, int],
) -> bool:
    """Write content to a file, respecting the overwrite flag.

    Returns:
        ``True`` if the file was actually written, ``False`` if it was
        skipped because it already exists and *overwrite* is ``False``.
    """
    if path.exists() and not overwrite:
        stats["files_skipped"] += 1
        logger.debug(f"Skipped (exists): {path}")
        return False

    path.write_text(file_content, encoding="utf-8")
    stats["files_created"] += 1
    logger.debug(f"Wrote: {path}")
    return True


def _write_root_files(
    config: CurriculumConfig,
    curriculum_dir: Path,
    overwrite: bool,
    stats: dict[str, int],
) -> None:
    """Write root-level files (README, OVERVIEW, AGENTS, audit script)."""
    renderers = {
        "README.md": content.render_root_readme,
        "OVERVIEW.md": content.render_root_overview,
        "AGENTS.md": content.render_root_agents,
    }

    for filename, renderer in renderers.items():
        _write_file(
            curriculum_dir / filename,
            renderer(config),
            overwrite,
            stats,
        )

    # Audit script (special: needs executable permission)
    audit_path = curriculum_dir / "audit_modules.sh"
    wrote = _write_file(audit_path, content.render_audit_script(config), overwrite, stats)
    if wrote:
        os.chmod(audit_path, 0o755)


def _write_resources(
    config: CurriculumConfig,
    curriculum_dir: Path,
    overwrite: bool,
    stats: dict[str, int],
) -> None:
    """Write all resource files."""
    res_dir = curriculum_dir / "resources"
    _ensure_dir(res_dir, stats)

    renderers = {
        "glossary.md": content.render_resource_glossary,
        "notation_table.md": content.render_resource_notation,
        "references.md": content.render_resource_references,
        "cross_course_map.md": content.render_resource_cross_course_map,
        "learning_pathways.md": content.render_resource_learning_pathways,
        "faq.md": content.render_resource_faq,
        "README.md": content.render_resource_readme,
        "AGENTS.md": content.render_resource_agents,
    }

    for filename, renderer in renderers.items():
        _write_file(res_dir / filename, renderer(config), overwrite, stats)


def _write_course_files(
    config: CurriculumConfig,
    course: CourseConfig,
    course_dir: Path,
    overwrite: bool,
    stats: dict[str, int],
) -> None:
    """Write course-level files (README, AGENTS, syllabus)."""
    _write_file(
        course_dir / "README.md",
        content.render_course_readme(course, config),
        overwrite,
        stats,
    )
    _write_file(
        course_dir / "AGENTS.md",
        content.render_course_agents(course, config),
        overwrite,
        stats,
    )
    _write_file(
        course_dir / "syllabus.md",
        content.render_course_syllabus(course, config),
        overwrite,
        stats,
    )


def _write_module_files(
    config: CurriculumConfig,
    course: CourseConfig,
    module: ModuleConfig,
    module_dir: Path,
    overwrite: bool,
    stats: dict[str, int],
) -> None:
    """Write all 7 files for a single module."""
    renderers = {
        "module.md": content.render_module_md,
        "questions.md": content.render_questions_md,
        "practice_quiz.md": content.render_quiz_md,
        "lab.md": content.render_lab_md,
        "README.md": content.render_readme_md,
        "AGENTS.md": content.render_agents_md,
        "dashboard.html": content.render_dashboard_html,
    }

    for filename, renderer in renderers.items():
        _write_file(
            module_dir / filename,
            renderer(module, course, config),
            overwrite,
            stats,
        )
