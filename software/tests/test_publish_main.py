"""Tests for the publish module — COURSE_REGISTRY-aware publishing."""

from src.publish.main import publish_course


class TestPublishCourse:
    """Publish course tests — uses flat module structure (AIF convention)"""

    def test_publish_ai_philosophy_structure(self, temp_dir):
        """Test publishing an AIF course (flat module structure)."""
        course_dir = temp_dir / "ai-philosophy"
        course_dir.mkdir()

        # Flat module directory (no course/ subdir — AIF convention)
        mod1 = course_dir / "01_philosophy"
        mod1.mkdir(parents=True)
        (mod1 / "output").mkdir()
        (mod1 / "output" / "test.pdf").write_text("content")

        # Syllabus as single file
        syl_path = course_dir / "syllabus.md"
        syl_path.write_text("# Syllabus")

        publish_root = temp_dir / "PUBLISHED"
        results = publish_course(str(course_dir), str(publish_root))

        assert results["course"] == "ai-philosophy"
        assert results["modules_published"] == 1

        assert (publish_root / "ai-philosophy" / "01_philosophy" / "test.pdf").exists()

    def test_publish_flat_structure_no_syllabus_subdir(self, temp_dir):
        """Test publishing without a syllabus directory."""
        course_dir = temp_dir / "ai-philosophy"
        course_dir.mkdir()

        mod1 = course_dir / "01_systems"
        mod1.mkdir()
        (mod1 / "output").mkdir()
        (mod1 / "output" / "gen.pdf").write_text("content")

        publish_root = temp_dir / "PUBLISHED"
        results = publish_course(str(course_dir), str(publish_root))

        assert results["course"] == "ai-philosophy"
        assert results["modules_published"] == 1
        assert (publish_root / "ai-philosophy" / "01_systems" / "gen.pdf").exists()

    def test_clean_directory(self, temp_dir):
        """Test that destination is cleaned before publishing."""
        course_dir = temp_dir / "ai-math"
        course_dir.mkdir()
        mod1 = course_dir / "01_systems"
        mod1.mkdir()
        (mod1 / "output").mkdir()
        (mod1 / "output" / "new.pdf").write_text("new")

        publish_root = temp_dir / "PUBLISHED"
        dest_mod = publish_root / "ai-math" / "01_systems"
        dest_mod.mkdir(parents=True)
        (dest_mod / "old.pdf").write_text("old")

        publish_course(str(course_dir), str(publish_root))

        assert (dest_mod / "new.pdf").exists()
        assert not (dest_mod / "old.pdf").exists()
