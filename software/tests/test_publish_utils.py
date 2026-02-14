"""Tests for publish utils module."""

import shutil
from pathlib import Path
import pytest

from src.publish.utils import (
    flatten_module,
    flatten_published,
    copy_labs_and_dashboards,
    copy_practice_tests,
    copy_slides,
    copy_slides_to_modules,
    copy_exams,
    clean_directory,
    copy_directory_contents,
    get_course_config,
    clean_published,
)
from src.publish import config


class TestFlattenModule:
    """Tests for flatten_module function."""

    def test_moves_files_to_root(self, temp_dir):
        """Test that files in subdirectories are moved to module root."""
        module_dir = temp_dir / "module-01"
        module_dir.mkdir()
        subdir = module_dir / "assignments"
        subdir.mkdir()
        (subdir / "hw1.pdf").write_text("content", encoding="utf-8")
        (subdir / "hw2.pdf").write_text("content", encoding="utf-8")

        moved = flatten_module(module_dir)

        assert moved == 2
        assert (module_dir / "hw1.pdf").exists()
        assert (module_dir / "hw2.pdf").exists()
        assert not subdir.exists()

    def test_handles_name_conflicts(self, temp_dir):
        """Test name conflict resolution with subdir prefix."""
        module_dir = temp_dir / "module-01"
        module_dir.mkdir()
        sub_a = module_dir / "dir_a"
        sub_a.mkdir()
        sub_b = module_dir / "dir_b"
        sub_b.mkdir()
        (sub_a / "file.pdf").write_text("from a", encoding="utf-8")
        (sub_b / "file.pdf").write_text("from b", encoding="utf-8")

        moved = flatten_module(module_dir)

        assert moved == 2
        # One should be file.pdf, the other dir_b_file.pdf (or vice versa)
        files = list(module_dir.glob("*.pdf"))
        assert len(files) == 2

    def test_dry_run_no_modification(self, temp_dir):
        """Test dry_run doesn't move files."""
        module_dir = temp_dir / "module-01"
        module_dir.mkdir()
        subdir = module_dir / "assignments"
        subdir.mkdir()
        (subdir / "hw1.pdf").write_text("content", encoding="utf-8")

        moved = flatten_module(module_dir, dry_run=True)

        assert moved == 1  # counted but not moved
        assert (subdir / "hw1.pdf").exists()
        assert not (module_dir / "hw1.pdf").exists()

    def test_empty_module(self, temp_dir):
        """Test flattening module with no subdirectories."""
        module_dir = temp_dir / "module-01"
        module_dir.mkdir()

        moved = flatten_module(module_dir)

        assert moved == 0


class TestFlattenPublished:
    """Tests for flatten_published function."""

    def test_flattens_all_modules(self, temp_dir):
        """Test flattening across multiple courses and modules."""
        pub = temp_dir / "PUBLISHED"
        course = pub / "biol-1"
        mod1 = course / "module-01"
        sub = mod1 / "assignments"
        sub.mkdir(parents=True)
        (sub / "hw.pdf").write_text("content", encoding="utf-8")

        total = flatten_published(pub)

        assert total == 1
        assert (mod1 / "hw.pdf").exists()

    def test_skips_configured_dirs(self, temp_dir):
        """Test that labs, dashboards, syllabus, slides, exams, practice_tests are skipped."""
        pub = temp_dir / "PUBLISHED"
        course = pub / "biol-1"
        for name in ["labs", "dashboards", "syllabus", "slides", "exams", "practice_tests"]:
            skip_dir = course / name / "subdir"
            skip_dir.mkdir(parents=True)
            (skip_dir / "file.pdf").write_text("content", encoding="utf-8")

        total = flatten_published(pub)

        assert total == 0


class TestCopyPracticeTests:
    """Tests for copy_practice_tests function."""

    def test_copies_practice_test_files(self, temp_dir):
        """Test copying practice test files including answer keys."""
        practice_tests_dir = temp_dir / "course_development" / "biol-1" / "course" / "practice_tests"
        practice_tests_dir.mkdir(parents=True)
        (practice_tests_dir / "practice-test-01.md").write_text("# Practice Test 1", encoding="utf-8")
        (practice_tests_dir / "practice-test-01_key.md").write_text("# Answer Key", encoding="utf-8")
        (practice_tests_dir / "README.md").write_text("# README", encoding="utf-8")

        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_practice_tests(temp_dir, courses=["biol-1"])

        assert copied == 2  # Both practice-test-01.md and practice-test-01_key.md (not README)
        assert (pub / "biol-1" / "practice_tests" / "practice-test-01.md").exists()
        assert (pub / "biol-1" / "practice_tests" / "practice-test-01_key.md").exists()
        assert not (pub / "biol-1" / "practice_tests" / "README.md").exists()

    def test_copies_practice_test_outputs(self, temp_dir):
        """Test copying practice test output files (PDF, DOCX) including keys."""
        practice_tests_dir = temp_dir / "course_development" / "biol-1" / "course" / "practice_tests"
        practice_tests_dir.mkdir(parents=True)
        output_dir = practice_tests_dir / "output"
        output_dir.mkdir()
        (output_dir / "practice-test-01.pdf").write_bytes(b"pdf")
        (output_dir / "practice-test-01_key.pdf").write_bytes(b"pdf key")

        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_practice_tests(temp_dir, courses=["biol-1"])

        assert copied == 2  # Both PDFs are copied
        assert (pub / "biol-1" / "practice_tests" / "practice-test-01.pdf").exists()
        assert (pub / "biol-1" / "practice_tests" / "practice-test-01_key.pdf").exists()

    def test_copies_multiple_courses(self, temp_dir):
        """Test copying practice tests from multiple courses."""
        for course in ["biol-1", "biol-8"]:
            practice_tests_dir = temp_dir / "course_development" / course / "course" / "practice_tests"
            practice_tests_dir.mkdir(parents=True)
            (practice_tests_dir / "practice-test-01.md").write_text(f"# {course} test", encoding="utf-8")

        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_practice_tests(temp_dir, courses=["biol-1", "biol-8"])

        assert copied == 2
        assert (pub / "biol-1" / "practice_tests" / "practice-test-01.md").exists()
        assert (pub / "biol-8" / "practice_tests" / "practice-test-01.md").exists()

    def test_missing_practice_tests_directory(self, temp_dir):
        """Test with non-existent practice tests directory."""
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_practice_tests(temp_dir, courses=["biol-1"])

        assert copied == 0


class TestCopyLabsAndDashboards:
    """Tests for copy_labs_and_dashboards function."""

    def test_copies_lab_files(self, temp_dir):
        """Test copying lab markdown and output files."""
        labs_dir = temp_dir / "course_development" / "biol-1" / "course" / "labs"
        labs_dir.mkdir(parents=True)
        (labs_dir / "lab-01.md").write_text("# Lab 1", encoding="utf-8")
        output_dir = labs_dir / "output"
        output_dir.mkdir()
        (output_dir / "lab-01.pdf").write_text("pdf", encoding="utf-8")

        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_labs_and_dashboards(temp_dir, courses=["biol-1"])

        assert copied == 2
        assert (pub / "biol-1" / "labs" / "lab-01.md").exists()
        assert (pub / "biol-1" / "labs" / "lab-01.pdf").exists()

    def test_copies_dashboard_files(self, temp_dir):
        """Test copying dashboard HTML files."""
        labs_dir = temp_dir / "course_development" / "biol-1" / "course" / "labs"
        labs_dir.mkdir(parents=True)
        dashboards_dir = labs_dir / "dashboards"
        dashboards_dir.mkdir()
        (dashboards_dir / "dashboard.html").write_text("<html>", encoding="utf-8")

        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_labs_and_dashboards(temp_dir, courses=["biol-1"])

        assert copied == 1
        assert (pub / "biol-1" / "dashboards" / "dashboard.html").exists()

    def test_missing_labs_directory(self, temp_dir):
        """Test with non-existent labs directory."""
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_labs_and_dashboards(temp_dir, courses=["biol-1"])

        assert copied == 0


class TestCopySlides:
    """Tests for copy_slides function."""

    def test_copies_slide_pdfs(self, temp_dir):
        """Test copying slide PDFs to PUBLISHED."""
        slides_dir = temp_dir / "course_development" / "biol-1" / "resources" / "slides"
        slides_dir.mkdir(parents=True)
        (slides_dir / "module-1-slides-full.pdf").write_bytes(b"pdf")
        (slides_dir / "module-1-slides-notes.pdf").write_bytes(b"pdf")

        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_slides(temp_dir, courses=["biol-1"])

        assert copied == 2
        assert (pub / "biol-1" / "slides" / "module-1-slides-full.pdf").exists()

    def test_missing_slides_directory(self, temp_dir):
        """Test with non-existent slides directory."""
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_slides(temp_dir, courses=["biol-1"])

        assert copied == 0


class TestCopySlidesToModules:
    """Tests for copy_slides_to_modules function."""

    def test_copies_slides_into_modules(self, temp_dir):
        """Test copying slides into matching module directories."""
        slides_dir = temp_dir / "course_development" / "biol-1" / "resources" / "slides"
        slides_dir.mkdir(parents=True)
        (slides_dir / "module-1-slides-full.pdf").write_bytes(b"pdf")

        pub = temp_dir / config.PUBLISH_ROOT_NAME
        mod = pub / "biol-1" / "module-01-topic"
        mod.mkdir(parents=True)

        copied = copy_slides_to_modules(temp_dir, courses=["biol-1"])

        assert copied == 1
        assert (mod / "module-1-slides-full.pdf").exists()

    def test_no_matching_slides(self, temp_dir):
        """Test when no slides match any module number."""
        slides_dir = temp_dir / "course_development" / "biol-1" / "resources" / "slides"
        slides_dir.mkdir(parents=True)
        (slides_dir / "module-99-slides-full.pdf").write_bytes(b"pdf")

        pub = temp_dir / config.PUBLISH_ROOT_NAME
        mod = pub / "biol-1" / "module-01-topic"
        mod.mkdir(parents=True)

        copied = copy_slides_to_modules(temp_dir, courses=["biol-1"])

        assert copied == 0


class TestCopyExams:
    """Tests for copy_exams function."""

    def test_copies_exam_files(self, temp_dir):
        """Test copying exam files excluding answer keys."""
        exams_dir = temp_dir / "course_development" / "biol-8" / "course" / "exams"
        exams_dir.mkdir(parents=True)
        (exams_dir / "exam-1.md").write_text("# Exam 1", encoding="utf-8")
        (exams_dir / "exam-1_key.md").write_text("# Key", encoding="utf-8")

        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_exams(temp_dir)

        assert copied == 1  # Only exam-1.md, not the key
        assert (pub / "biol-8" / "exams" / "exam-1.md").exists()
        assert not (pub / "biol-8" / "exams" / "exam-1_key.md").exists()

    def test_copies_exam_outputs(self, temp_dir):
        """Test copying exam output files (PDF, DOCX)."""
        exams_dir = temp_dir / "course_development" / "biol-8" / "course" / "exams"
        exams_dir.mkdir(parents=True)
        output_dir = exams_dir / "output"
        output_dir.mkdir()
        (output_dir / "exam-1.pdf").write_bytes(b"pdf")

        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_exams(temp_dir)

        assert copied == 1
        assert (pub / "biol-8" / "exams" / "exam-1.pdf").exists()

    def test_missing_exams_directory(self, temp_dir):
        """Test with non-existent exams directory."""
        pub = temp_dir / config.PUBLISH_ROOT_NAME
        pub.mkdir()

        copied = copy_exams(temp_dir)

        assert copied == 0


class TestCleanDirectory:
    """Tests for clean_directory function."""

    def test_cleans_existing_directory(self, temp_dir):
        """Test that existing content is removed."""
        target = temp_dir / "target"
        target.mkdir()
        (target / "old_file.txt").write_text("old", encoding="utf-8")

        clean_directory(target)

        assert target.exists()
        assert list(target.iterdir()) == []

    def test_creates_nonexistent_directory(self, temp_dir):
        """Test that non-existent directory is created."""
        target = temp_dir / "new_dir"

        clean_directory(target)

        assert target.exists()


class TestCopyDirectoryContents:
    """Tests for copy_directory_contents function."""

    def test_copies_files(self, temp_dir):
        """Test copying files from source to destination."""
        src = temp_dir / "src"
        src.mkdir()
        (src / "file1.txt").write_text("content1", encoding="utf-8")
        sub = src / "sub"
        sub.mkdir()
        (sub / "file2.txt").write_text("content2", encoding="utf-8")

        dst = temp_dir / "dst"

        count = copy_directory_contents(src, dst)

        assert count == 2
        assert (dst / "file1.txt").exists()
        assert (dst / "sub" / "file2.txt").exists()

    def test_excludes_patterns(self, temp_dir):
        """Test that excluded patterns are not copied."""
        src = temp_dir / "src"
        src.mkdir()
        (src / "good.txt").write_text("ok", encoding="utf-8")
        (src / ".DS_Store").write_text("junk", encoding="utf-8")

        dst = temp_dir / "dst"

        count = copy_directory_contents(src, dst)

        assert count == 1
        assert (dst / "good.txt").exists()

    def test_nonexistent_source(self, temp_dir):
        """Test with non-existent source directory."""
        count = copy_directory_contents(
            temp_dir / "nonexistent", temp_dir / "dst"
        )
        assert count == 0


class TestGetCourseConfig:
    """Tests for get_course_config function."""

    def test_known_course(self):
        """Test getting config for known course."""
        cfg = get_course_config("biol-1")
        assert "module_source_dir" in cfg

    def test_unknown_course_returns_default(self):
        """Test getting config for unknown course returns default."""
        cfg = get_course_config("unknown-course")
        assert cfg == config.DEFAULT_CONFIG


class TestCleanPublished:
    """Tests for clean_published function."""

    def test_removes_content(self, temp_dir):
        """Test that published content is removed."""
        pub = temp_dir / "PUBLISHED"
        pub.mkdir()
        (pub / "biol-1").mkdir()
        (pub / "file.txt").write_text("content", encoding="utf-8")

        clean_published(pub)

        # Directory should exist but be empty (except dotfiles)
        remaining = [p for p in pub.iterdir() if not p.name.startswith(".")]
        assert remaining == []

    def test_preserves_dotfiles(self, temp_dir):
        """Test that dotfiles are preserved."""
        pub = temp_dir / "PUBLISHED"
        pub.mkdir()
        (pub / ".gitkeep").write_text("", encoding="utf-8")
        (pub / "biol-1").mkdir()

        clean_published(pub)

        assert (pub / ".gitkeep").exists()
