"""Tests for course_generator scaffold (file system generation)."""

import pytest
from pathlib import Path
from src.course_generator.schema import (
    CurriculumConfig, CourseConfig, ModuleConfig, MODULE_TOPICS,
)
from src.course_generator.scaffold import generate_curriculum, generate_single_course
from src.course_generator.config import CURRICULUM_ES, ALL_CURRICULA


def _make_test_curriculum() -> CurriculumConfig:
    """Build a minimal valid curriculum for testing."""
    courses = []
    for c in range(1, 5):
        modules = [
            ModuleConfig(
                number=i, topic=t, subtitle=f"Test {t.title()}",
                key_concepts=[f"{t}_concept"], learning_goals=[f"Learn {t}"],
            )
            for i, t in enumerate(MODULE_TOPICS, 1)
        ]
        courses.append(CourseConfig(
            number=c, dir_name=f"{c:02d}_test_course", title=f"Test Course {c}",
            perspective="Testing perspective", lab_type="Test Lab",
            modules=modules,
        ))
    return CurriculumConfig(
        id="test_scaffold", title="Test Scaffold Curriculum",
        audience="Test audience", tone="Test tone.", courses=courses,
    )


class TestGenerateCurriculum:
    """Tests for the generate_curriculum function."""

    def test_creates_all_files(self, tmp_path):
        """Test that generate_curriculum creates the expected file count."""
        config = _make_test_curriculum()
        stats = generate_curriculum(config, tmp_path)
        assert stats["files_created"] > 0
        assert stats["files_skipped"] == 0

    def test_expected_file_count(self, tmp_path):
        """Test that the file count matches the config estimate."""
        config = _make_test_curriculum()
        stats = generate_curriculum(config, tmp_path)
        assert stats["files_created"] == config.total_files

    def test_root_files_exist(self, tmp_path):
        """Test that root-level files are created."""
        config = _make_test_curriculum()
        generate_curriculum(config, tmp_path)
        cur_dir = tmp_path / config.id
        assert (cur_dir / "README.md").exists()
        assert (cur_dir / "OVERVIEW.md").exists()
        assert (cur_dir / "AGENTS.md").exists()
        assert (cur_dir / "audit_modules.sh").exists()

    def test_audit_script_executable(self, tmp_path):
        """Test that audit_modules.sh has execute permissions."""
        config = _make_test_curriculum()
        generate_curriculum(config, tmp_path)
        audit = tmp_path / config.id / "audit_modules.sh"
        import os
        assert os.access(audit, os.X_OK)

    def test_resource_files_exist(self, tmp_path):
        """Test that all resource files are created."""
        config = _make_test_curriculum()
        generate_curriculum(config, tmp_path)
        res_dir = tmp_path / config.id / "resources"
        assert (res_dir / "glossary.md").exists()
        assert (res_dir / "notation_table.md").exists()
        assert (res_dir / "references.md").exists()
        assert (res_dir / "cross_course_map.md").exists()
        assert (res_dir / "learning_pathways.md").exists()
        assert (res_dir / "faq.md").exists()

    def test_course_dirs_exist(self, tmp_path):
        """Test that all 4 course directories are created."""
        config = _make_test_curriculum()
        generate_curriculum(config, tmp_path)
        cur_dir = tmp_path / config.id
        for course in config.courses:
            assert (cur_dir / course.dir_name).is_dir()

    def test_module_dirs_exist(self, tmp_path):
        """Test that all 32 module directories are created."""
        config = _make_test_curriculum()
        generate_curriculum(config, tmp_path)
        cur_dir = tmp_path / config.id
        for course in config.courses:
            for module in course.modules:
                mod_dir = cur_dir / course.dir_name / module.dir_name
                assert mod_dir.is_dir(), f"Missing: {mod_dir}"

    def test_module_files_exist(self, tmp_path):
        """Test that all 7 files exist in each module."""
        config = _make_test_curriculum()
        generate_curriculum(config, tmp_path)
        cur_dir = tmp_path / config.id
        expected_files = [
            "module.md", "questions.md", "practice_quiz.md",
            "lab.md", "dashboard.html", "README.md", "AGENTS.md",
        ]
        course = config.courses[0]
        module = course.modules[0]
        mod_dir = cur_dir / course.dir_name / module.dir_name
        for f in expected_files:
            assert (mod_dir / f).exists(), f"Missing: {mod_dir / f}"

    def test_no_overwrite_by_default(self, tmp_path):
        """Test that existing files are not overwritten."""
        config = _make_test_curriculum()
        generate_curriculum(config, tmp_path)
        stats2 = generate_curriculum(config, tmp_path)
        assert stats2["files_created"] == 0
        assert stats2["files_skipped"] == config.total_files

    def test_overwrite_flag(self, tmp_path):
        """Test that overwrite=True recreates all files."""
        config = _make_test_curriculum()
        generate_curriculum(config, tmp_path)
        stats2 = generate_curriculum(config, tmp_path, overwrite=True)
        assert stats2["files_created"] == config.total_files

    def test_no_placeholder_content(self, tmp_path):
        """Test that generated files contain no placeholder markers."""
        config = _make_test_curriculum()
        generate_curriculum(config, tmp_path)
        cur_dir = tmp_path / config.id
        for md_file in cur_dir.rglob("*.md"):
            text = md_file.read_text()
            assert "[TODO]" not in text, f"Placeholder in {md_file}"
            assert "[PLACEHOLDER]" not in text, f"Placeholder in {md_file}"

    def test_invalid_config_raises(self, tmp_path):
        """Test that an invalid config raises ValueError."""
        config = CurriculumConfig(
            id="bad", title="Bad", audience="None", tone="None.", courses=[],
        )
        with pytest.raises(ValueError, match="Invalid curriculum"):
            generate_curriculum(config, tmp_path)


class TestGenerateSingleCourse:
    """Tests for generate_single_course."""

    def test_generates_one_course(self, tmp_path):
        """Test generating a single course."""
        config = _make_test_curriculum()
        stats = generate_single_course(config, 1, tmp_path)
        assert stats["files_created"] > 0
        course_dir = tmp_path / config.id / config.courses[0].dir_name
        assert course_dir.is_dir()

    def test_invalid_course_number(self, tmp_path):
        """Test that invalid course number raises ValueError."""
        config = _make_test_curriculum()
        with pytest.raises(ValueError, match="No course with number"):
            generate_single_course(config, 99, tmp_path)


class TestRealCurriculaGeneration:
    """Test generation with real curriculum configs from config.py."""

    def test_es_curriculum_file_count(self, tmp_path):
        """Test that the ES curriculum generates the expected file count."""
        stats = generate_curriculum(CURRICULUM_ES, tmp_path)
        assert stats["files_created"] == CURRICULUM_ES.total_files

    def test_all_curricula_validate(self):
        """Test that all 8 registered curricula pass validation."""
        for cid, config in ALL_CURRICULA.items():
            errors = config.validate()
            assert errors == [], f"Curriculum {cid} has errors: {errors}"
