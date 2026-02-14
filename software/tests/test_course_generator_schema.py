"""Tests for course_generator schema definitions."""

import pytest
from src.course_generator.schema import (
    ModuleConfig,
    CourseConfig,
    CurriculumConfig,
    MODULE_TOPICS,
    MODULE_FILES,
    RESOURCE_FILES,
    ROOT_FILES,
    COURSE_FILES,
)


class TestModuleConfig:
    """Tests for ModuleConfig dataclass."""

    def test_valid_module(self):
        """Test creating a valid module configuration."""
        mod = ModuleConfig(
            number=1, topic="systems", subtitle="Test Systems",
            key_concepts=["boundaries"], learning_goals=["Define systems"],
        )
        assert mod.number == 1
        assert mod.topic == "systems"
        assert mod.dir_name == "01_systems"

    def test_dir_name_format(self):
        """Test directory name generation for all modules."""
        for i, topic in enumerate(MODULE_TOPICS, 1):
            mod = ModuleConfig(number=i, topic=topic, subtitle="Test")
            assert mod.dir_name == f"{i:02d}_{topic}"

    def test_invalid_number_too_low(self):
        """Test that module number 0 raises ValueError."""
        with pytest.raises(ValueError, match="Module number must be 1-8"):
            ModuleConfig(number=0, topic="systems", subtitle="Test")

    def test_invalid_number_too_high(self):
        """Test that module number 9 raises ValueError."""
        with pytest.raises(ValueError, match="Module number must be 1-8"):
            ModuleConfig(number=9, topic="systems", subtitle="Test")

    def test_invalid_topic(self):
        """Test that an unknown topic raises ValueError."""
        with pytest.raises(ValueError, match="not in MODULE_TOPICS"):
            ModuleConfig(number=1, topic="invalid_topic", subtitle="Test")

    def test_default_lists(self):
        """Test that key_concepts and learning_goals default to empty."""
        mod = ModuleConfig(number=1, topic="systems", subtitle="Test")
        assert mod.key_concepts == []
        assert mod.learning_goals == []


class TestCourseConfig:
    """Tests for CourseConfig dataclass."""

    def test_valid_course(self):
        """Test creating a valid course configuration."""
        course = CourseConfig(
            number=1, dir_name="01_test", title="Test Course",
            perspective="Testing", lab_type="Test Lab",
        )
        assert course.number == 1
        assert course.title == "Test Course"

    def test_invalid_number(self):
        """Test that course number 5 raises ValueError."""
        with pytest.raises(ValueError, match="Course number must be 1-4"):
            CourseConfig(
                number=5, dir_name="05_test", title="Test",
                perspective="Testing", lab_type="Test Lab",
            )

    def test_default_modules(self):
        """Test that modules default to an empty list."""
        course = CourseConfig(
            number=1, dir_name="01_test", title="Test",
            perspective="Testing", lab_type="Test Lab",
        )
        assert course.modules == []


class TestCurriculumConfig:
    """Tests for CurriculumConfig dataclass."""

    def _make_full_curriculum(self) -> CurriculumConfig:
        """Helper to build a valid 4-course, 32-module curriculum."""
        courses = []
        for c in range(1, 5):
            modules = [
                ModuleConfig(number=i, topic=t, subtitle=f"Sub {t}")
                for i, t in enumerate(MODULE_TOPICS, 1)
            ]
            courses.append(CourseConfig(
                number=c, dir_name=f"{c:02d}_test", title=f"Course {c}",
                perspective="Testing", lab_type="Test Lab", modules=modules,
            ))
        return CurriculumConfig(
            id="test_curriculum", title="Test Curriculum",
            audience="Testers", tone="Testing tone.", courses=courses,
        )

    def test_valid_curriculum(self):
        """Test creating a valid curriculum."""
        cur = self._make_full_curriculum()
        assert cur.id == "test_curriculum"
        assert cur.total_modules == 32
        assert cur.total_files > 200

    def test_validate_passes(self):
        """Test that a valid curriculum passes validation."""
        cur = self._make_full_curriculum()
        errors = cur.validate()
        assert errors == []

    def test_validate_wrong_course_count(self):
        """Test validation catches wrong number of courses."""
        cur = CurriculumConfig(
            id="test", title="Test", audience="Testers",
            tone="Test.", courses=[],
        )
        errors = cur.validate()
        assert any("Expected 4 courses" in e for e in errors)

    def test_validate_wrong_module_count(self):
        """Test validation catches wrong number of modules."""
        course = CourseConfig(
            number=1, dir_name="01_test", title="Test",
            perspective="Testing", lab_type="Test Lab", modules=[],
        )
        cur = CurriculumConfig(
            id="test", title="Test", audience="Testers",
            tone="Test.", courses=[course] * 4,
        )
        errors = cur.validate()
        assert any("0 modules" in e for e in errors)

    def test_validate_wrong_topic_order(self):
        """Test validation catches wrong topic ordering."""
        modules = [
            ModuleConfig(number=i, topic=t, subtitle=f"Sub {t}")
            for i, t in enumerate(reversed(MODULE_TOPICS), 1)
        ]
        course = CourseConfig(
            number=1, dir_name="01_test", title="Test",
            perspective="Testing", lab_type="Test Lab", modules=modules,
        )
        cur = CurriculumConfig(
            id="test", title="Test", audience="Testers",
            tone="Test.", courses=[course] * 4,
        )
        errors = cur.validate()
        assert any("topic order mismatch" in e for e in errors)

    def test_empty_id_raises(self):
        """Test that empty ID raises ValueError."""
        with pytest.raises(ValueError, match="must not be empty"):
            CurriculumConfig(id="", title="Test", audience="T", tone="T.")

    def test_empty_title_raises(self):
        """Test that empty title raises ValueError."""
        with pytest.raises(ValueError, match="must not be empty"):
            CurriculumConfig(id="test", title="", audience="T", tone="T.")


class TestConstants:
    """Tests for module-level constants."""

    def test_module_topics_count(self):
        """Test that there are exactly 8 module topics."""
        assert len(MODULE_TOPICS) == 8

    def test_module_topics_order(self):
        """Test the canonical topic ordering."""
        assert MODULE_TOPICS[0] == "systems"
        assert MODULE_TOPICS[-1] == "planning"

    def test_module_files_count(self):
        """Test that there are 7 files per module."""
        assert len(MODULE_FILES) == 7

    def test_resource_files_count(self):
        """Test that there are 8 resource files."""
        assert len(RESOURCE_FILES) == 8

    def test_root_files_count(self):
        """Test that there are 4 root files."""
        assert len(ROOT_FILES) == 4

    def test_course_files_count(self):
        """Test that there are 3 course-level files."""
        assert len(COURSE_FILES) == 3
