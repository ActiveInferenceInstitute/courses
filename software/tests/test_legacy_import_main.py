"""Tests for legacy_import main module.

Uses real implementations — WeasyPrint-dependent functionality is
conditionally skipped via pytest.importorskip or pytest.skip.
"""

import sys
from pathlib import Path
import pytest

from src.legacy_import.config import get_chapter_to_module_mapping
from src.legacy_import.utils import extract_chapter_number, create_comprehension_questions


# Check if format_conversion is available (requires WeasyPrint system libs)
_has_format_conversion = True
try:
    from src.format_conversion.utils import convert_docx_to_markdown
except (ImportError, OSError):
    _has_format_conversion = False


class TestProcessChapterQuestions:
    """Tests for process_chapter_questions function."""

    def test_returns_correct_structure(self, temp_dir):
        """Test that result dictionary has expected keys."""
        from src.legacy_import.main import process_chapter_questions

        source_dir = temp_dir / "questions"
        source_dir.mkdir()
        course_root = temp_dir / "biol-1"
        course_root.mkdir()
        course_dir = course_root / "course"
        course_dir.mkdir()

        results = process_chapter_questions(source_dir, course_root, course_dir, dry_run=True)

        assert "processed" in results
        assert "skipped" in results
        assert "errors" in results
        assert "summary" in results

    def test_no_docx_files(self, temp_dir):
        """Test with empty source directory returns empty results."""
        from src.legacy_import.main import process_chapter_questions

        source_dir = temp_dir / "questions"
        source_dir.mkdir()
        course_root = temp_dir / "biol-1"
        course_root.mkdir()
        course_dir = course_root / "course"
        course_dir.mkdir()

        results = process_chapter_questions(source_dir, course_root, course_dir, dry_run=False)

        assert results["processed"] == []
        assert results["summary"]["converted"] == 0

    def test_dry_run_records_files(self, temp_dir):
        """Test dry run mode processes files without converting."""
        from src.legacy_import.main import process_chapter_questions

        source_dir = temp_dir / "questions"
        source_dir.mkdir()
        (source_dir / "Chapter 01 Keys to Success.docx").write_bytes(b"fake")

        course_root = temp_dir / "biol-1"
        course_dir = course_root / "course"
        course_dir.mkdir(parents=True)

        results = process_chapter_questions(
            source_dir, course_root, course_dir, dry_run=True
        )

        # In dry run, files are listed but not converted
        assert len(results["processed"]) == 1
        assert results["processed"][0]["chapter"] == 1
        assert results["processed"][0]["module"] == 1

    def test_unmapped_chapter_skipped(self, temp_dir):
        """Test that chapters not in mapping are skipped."""
        from src.legacy_import.main import process_chapter_questions

        source_dir = temp_dir / "questions"
        source_dir.mkdir()
        (source_dir / "Chapter 99 Questions.docx").write_bytes(b"fake")

        course_root = temp_dir / "biol-1"
        course_dir = course_root / "course"
        course_dir.mkdir(parents=True)

        results = process_chapter_questions(source_dir, course_root, course_dir, dry_run=True)

        assert len(results["skipped"]) == 1
        assert "not in mapping" in results["skipped"][0]["reason"]

    def test_invalid_filename_errors(self, temp_dir):
        """Test that files without chapter numbers produce errors."""
        from src.legacy_import.main import process_chapter_questions

        source_dir = temp_dir / "questions"
        source_dir.mkdir()
        (source_dir / "random_file.docx").write_bytes(b"fake")

        course_root = temp_dir / "biol-1"
        course_dir = course_root / "course"
        course_dir.mkdir(parents=True)

        results = process_chapter_questions(source_dir, course_root, course_dir, dry_run=True)

        assert len(results["errors"]) == 1


class TestProcessSlides:
    """Tests for process_slides function."""

    def test_returns_correct_structure(self, temp_dir):
        """Test that result dictionary has expected keys."""
        from src.legacy_import.main import process_slides

        slides_full = temp_dir / "full"
        slides_full.mkdir()
        slides_notes = temp_dir / "notes"
        slides_notes.mkdir()
        course_root = temp_dir / "biol-1"
        course_root.mkdir()

        results = process_slides(slides_full, slides_notes, course_root, dry_run=True)

        assert "processed" in results
        assert "skipped" in results
        assert "errors" in results
        assert "summary" in results

    def test_missing_directories(self, temp_dir):
        """Test with non-existent slide directories."""
        from src.legacy_import.main import process_slides

        slides_full = temp_dir / "nonexistent_full"
        slides_notes = temp_dir / "nonexistent_notes"
        course_root = temp_dir / "biol-1"
        course_root.mkdir()

        results = process_slides(slides_full, slides_notes, course_root, dry_run=True)

        assert results["processed"] == []

    def test_dry_run_records_slides(self, temp_dir):
        """Test dry run mode with slide PDFs."""
        from src.legacy_import.main import process_slides

        slides_full = temp_dir / "full"
        slides_full.mkdir()
        (slides_full / "General Biology Chapter 01 Slides.pdf").write_bytes(b"fake")

        slides_notes = temp_dir / "notes"
        slides_notes.mkdir()

        course_root = temp_dir / "biol-1"
        course_dir = course_root / "course"
        course_dir.mkdir(parents=True)

        results = process_slides(slides_full, slides_notes, course_root, dry_run=True)

        assert len(results["processed"]) == 1
        assert results["processed"][0]["type"] == "full"
        assert results["processed"][0]["chapter"] == 1

    def test_copies_full_and_notes(self, temp_dir):
        """Test processing both full and notes slides with real file copy."""
        from src.legacy_import.main import process_slides

        slides_full = temp_dir / "full"
        slides_full.mkdir()
        (slides_full / "Chapter 01 Slides.pdf").write_bytes(b"fullpdf")

        slides_notes = temp_dir / "notes"
        slides_notes.mkdir()
        (slides_notes / "Chapter 01 Notes.pdf").write_bytes(b"notespdf")

        course_root = temp_dir / "biol-1"
        course_dir = course_root / "course"
        # Create module-1 for real get_module_path
        mod1 = course_dir / "module-1"
        mod1.mkdir(parents=True)

        results = process_slides(slides_full, slides_notes, course_root, dry_run=False)

        assert results["summary"]["copied"] == 2
        types = {r["type"] for r in results["processed"]}
        assert "full" in types
        assert "notes" in types


class TestProcessForUploadAllModules:
    """Tests for process_for_upload_all_modules function."""

    def test_returns_correct_structure(self, temp_dir):
        """Test that result dictionary has expected keys."""
        from src.legacy_import.main import process_for_upload_all_modules

        course_dir = temp_dir / "course"
        course_dir.mkdir()

        results = process_for_upload_all_modules(course_dir, dry_run=True)

        assert "modules_processed" in results
        assert "modules_errors" in results
        assert "total_pdf" in results
        assert "total_docx" in results
        assert "total_slides" in results
        assert "errors" in results

    def test_empty_course_directory(self, temp_dir):
        """Test with no module directories."""
        from src.legacy_import.main import process_for_upload_all_modules

        course_dir = temp_dir / "course"
        course_dir.mkdir()

        results = process_for_upload_all_modules(course_dir, dry_run=True)

        assert results["modules_processed"] == 0

    def test_processes_module_directories(self, temp_dir):
        """Test that module directories are found and processed."""
        from src.legacy_import.main import process_for_upload_all_modules

        course_dir = temp_dir / "course"
        for i in range(1, 3):
            mod = course_dir / f"module-{i:02d}"
            mod.mkdir(parents=True)

        results = process_for_upload_all_modules(course_dir, dry_run=True)

        assert results["modules_processed"] == 2

    def test_skips_non_module_dirs(self, temp_dir):
        """Test that non-module directories are skipped."""
        from src.legacy_import.main import process_for_upload_all_modules

        course_dir = temp_dir / "course"
        (course_dir / "module-01").mkdir(parents=True)
        (course_dir / "labs").mkdir(parents=True)
        (course_dir / "syllabus").mkdir(parents=True)

        results = process_for_upload_all_modules(course_dir, dry_run=True)

        assert results["modules_processed"] == 1


class TestChapterToModuleMapping:
    """Tests for chapter-to-module mapping correctness."""

    def test_mapping_is_one_to_one(self):
        """Test that mapping is 1:1 for chapters 1-17."""
        mapping = get_chapter_to_module_mapping()

        assert len(mapping) == 17
        for i in range(1, 18):
            assert mapping[i] == i

    def test_mapping_keys_are_ints(self):
        """Test that all keys and values are integers."""
        mapping = get_chapter_to_module_mapping()

        for k, v in mapping.items():
            assert isinstance(k, int)
            assert isinstance(v, int)
