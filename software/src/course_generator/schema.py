"""Schema definitions for Active Inference curriculum generation.

Dataclasses that encode the structure of any curriculum at three levels:
- CurriculumConfig: the top-level curriculum (e.g., "Elementary School")
- CourseConfig: one of the 4 disciplinary tracks within a curriculum
- ModuleConfig: one of the 8 topic modules within a course
"""

from __future__ import annotations

from dataclasses import dataclass, field


# ─── Shared constants ───────────────────────────────────────────────────────

MODULE_TOPICS: list[str] = [
    "systems",
    "agents",
    "perception",
    "cognition",
    "action",
    "learning",
    "communication",
    "planning",
]
"""Canonical 8-topic spine shared by all curricula, in order."""

MODULE_FILES: list[str] = [
    "module.md",
    "questions.md",
    "practice_quiz.md",
    "lab.md",
    "dashboard.html",
    "README.md",
    "AGENTS.md",
]
"""Standard set of files generated for every module directory."""

RESOURCE_FILES: list[str] = [
    "glossary.md",
    "notation_table.md",
    "references.md",
    "cross_course_map.md",
    "learning_pathways.md",
    "faq.md",
    "README.md",
    "AGENTS.md",
]
"""Standard set of files in the resources/ directory."""

ROOT_FILES: list[str] = [
    "README.md",
    "OVERVIEW.md",
    "AGENTS.md",
    "audit_modules.sh",
]
"""Standard set of files at the curriculum root."""

COURSE_FILES: list[str] = [
    "README.md",
    "AGENTS.md",
    "syllabus.md",
]
"""Standard set of files at the course level (per-course directory)."""


# ─── Dataclasses ────────────────────────────────────────────────────────────


@dataclass
class ModuleConfig:
    """Configuration for a single module within a course.

    Attributes:
        number: Module number (1-8), determines directory naming.
        topic: Canonical topic name from MODULE_TOPICS.
        subtitle: Age/domain-appropriate subtitle for this module.
        key_concepts: List of 3-5 key concepts taught in this module.
        learning_goals: List of 3-4 measurable learning objectives.
    """

    number: int
    topic: str
    subtitle: str
    key_concepts: list[str] = field(default_factory=list)
    learning_goals: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate module configuration."""
        if not 1 <= self.number <= 8:
            raise ValueError(f"Module number must be 1-8, got {self.number}")
        if self.topic not in MODULE_TOPICS:
            raise ValueError(f"Topic '{self.topic}' not in MODULE_TOPICS: {MODULE_TOPICS}")

    @property
    def dir_name(self) -> str:
        """Directory name for this module (e.g., '01_systems')."""
        return f"{self.number:02d}_{self.topic}"


@dataclass
class CourseConfig:
    """Configuration for one of the 4 courses within a curriculum.

    Attributes:
        number: Course number (1-4), determines directory naming.
        dir_name: Directory name (e.g., '01_story_time').
        title: Human-readable course title.
        perspective: The disciplinary lens for this course.
        lab_type: Default lab activity type (e.g., 'Storytime Activity').
        modules: List of 8 ModuleConfig instances.
    """

    number: int
    dir_name: str
    title: str
    perspective: str
    lab_type: str
    modules: list[ModuleConfig] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate course configuration."""
        if not 1 <= self.number <= 4:
            raise ValueError(f"Course number must be 1-4, got {self.number}")


@dataclass
class CurriculumConfig:
    """Top-level configuration for an entire curriculum.

    Each curriculum contains 4 courses, each with 8 modules,
    following the canonical Active Inference topic spine.

    Attributes:
        id: Unique identifier (e.g., 'active_inference_es').
        title: Human-readable title.
        audience: Target audience description.
        tone: Tone and style guide for content generation.
        parent_dir: Parent directory relative to repo root.
        courses: List of 4 CourseConfig instances.
        files_per_module: Override of MODULE_FILES if needed.
        resource_files: Override of RESOURCE_FILES if needed.
    """

    id: str
    title: str
    audience: str
    tone: str
    parent_dir: str = "course_development"
    courses: list[CourseConfig] = field(default_factory=list)
    files_per_module: list[str] = field(default_factory=lambda: list(MODULE_FILES))
    resource_files: list[str] = field(default_factory=lambda: list(RESOURCE_FILES))

    def __post_init__(self) -> None:
        """Validate curriculum configuration."""
        if not self.id:
            raise ValueError("Curriculum ID must not be empty")
        if not self.title:
            raise ValueError("Curriculum title must not be empty")

    @property
    def total_modules(self) -> int:
        """Total number of modules across all courses."""
        return sum(len(c.modules) for c in self.courses)

    @property
    def total_files(self) -> int:
        """Estimated total number of files to be generated."""
        root = len(ROOT_FILES)
        resources = len(self.resource_files)
        course_level = len(self.courses) * len(COURSE_FILES)
        module_level = self.total_modules * len(self.files_per_module)
        return root + resources + course_level + module_level

    def validate(self) -> list[str]:
        """Run full validation and return list of error messages.

        Returns:
            List of error strings. Empty list means valid.
        """
        errors: list[str] = []

        if len(self.courses) != 4:
            errors.append(f"Expected 4 courses, got {len(self.courses)}")

        # Directory-name collisions would silently overwrite each other's
        # files during scaffolding; enforce uniqueness.
        dir_names = [c.dir_name for c in self.courses]
        seen: set[str] = set()
        for d in dir_names:
            if d in seen:
                errors.append(f"Duplicate course dir_name: {d!r}")
            seen.add(d)

        for course in self.courses:
            if len(course.modules) != 8:
                errors.append(
                    f"Course '{course.title}' has {len(course.modules)} modules, expected 8"
                )

            expected_topics = MODULE_TOPICS[:]
            actual_topics = [m.topic for m in course.modules]
            if actual_topics != expected_topics:
                errors.append(
                    f"Course '{course.title}' topic order mismatch: "
                    f"expected {expected_topics}, got {actual_topics}"
                )

        return errors
