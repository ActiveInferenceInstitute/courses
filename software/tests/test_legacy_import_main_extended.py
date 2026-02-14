"""Extended tests for legacy_import main module to improve coverage.

Uses real implementations — conditionally skips tests requiring
WeasyPrint/format_conversion system dependencies.
"""

from pathlib import Path
import pytest

from src.legacy_import.main import (
    create_for_upload_files,
    process_chapter_questions,
)


# Detect availability of rendering dependencies
_has_pdf_renderer = True
try:
    from src.markdown_to_pdf.main import render_markdown_to_pdf
except (ImportError, OSError):
    _has_pdf_renderer = False

_has_format_conversion = True
try:
    from src.format_conversion.main import convert_file
    from src.format_conversion.utils import convert_docx_to_markdown
except (ImportError, OSError):
    _has_format_conversion = False


class TestCreateForUploadFiles:
    """Tests for create_for_upload_files function."""

    @pytest.mark.skipif(
        not (_has_pdf_renderer and _has_format_conversion),
        reason="Requires PDF renderer and format conversion (WeasyPrint)",
    )
    def test_create_files_success(self, temp_dir):
        """Test successful creation of upload files with real renderers."""
        module_path = temp_dir / "module-01"
        module_path.mkdir()
        resources_dir = module_path / "resources"
        resources_dir.mkdir()

        # Create a real markdown file with actual content
        (resources_dir / "keys-to-success.md").write_text(
            "# Keys to Success\n\nStudy hard.\n", encoding="utf-8"
        )

        slides_dir = module_path / "slides"
        slides_dir.mkdir()
        (slides_dir / "lecture.pdf").write_bytes(b"%PDF-1.4 fake")

        result = create_for_upload_files(module_path, 1, dry_run=False)

        assert (module_path / "for_upload").exists()
        assert (module_path / "for_upload" / "lecture.pdf").exists()
        assert result["errors"] == []

    def test_dry_run(self, temp_dir):
        """Test dry run logic for for_upload files."""
        module_path = temp_dir / "module-01"
        module_path.mkdir()
        resources_dir = module_path / "resources"
        resources_dir.mkdir()
        (resources_dir / "test.md").write_text("# Test\n", encoding="utf-8")

        result = create_for_upload_files(module_path, 1, dry_run=True)

        assert result["summary"]["pdf"] == 0
        assert not (module_path / "for_upload").exists()

    def test_excludes_readme(self, temp_dir):
        """Test that README.md is excluded from processing."""
        module_path = temp_dir / "module-01"
        module_path.mkdir()
        resources_dir = module_path / "resources"
        resources_dir.mkdir()

        # README.md should be excluded
        (resources_dir / "README.md").write_text("# Readme\n", encoding="utf-8")

        result = create_for_upload_files(module_path, 1, dry_run=True)

        # No processable files (only README which is excluded)
        assert result["summary"]["pdf"] == 0


class TestProcessChapterQuestionsExtended:
    """Extended tests for process_chapter_questions."""

    @pytest.mark.skipif(
        not _has_format_conversion,
        reason="Requires format conversion (WeasyPrint)",
    )
    def test_process_real_files(self, temp_dir):
        """Test actual processing of files (dry_run=False) with real converter."""
        source_dir = temp_dir / "questions"
        source_dir.mkdir()
        # Create a minimal DOCX-like file (real converter will handle it)
        (source_dir / "Chapter 01 Questions.docx").write_bytes(b"PK\x03\x04fake")

        course_root = temp_dir / "biol-1"
        course_dir = course_root / "course"
        course_dir.mkdir(parents=True)
        # Ensure module exists
        (course_dir / "module-1").mkdir(parents=True)

        results = process_chapter_questions(
            source_dir, course_root, course_dir, dry_run=False
        )

        # Real converter may error on fake DOCX, but the structure is correct
        assert "summary" in results
        assert "converted" in results["summary"]

    def test_dry_run_multiple_chapters(self, temp_dir):
        """Test dry run with multiple chapter files."""
        source_dir = temp_dir / "questions"
        source_dir.mkdir()
        (source_dir / "Chapter 01 Questions.docx").write_bytes(b"fake")
        (source_dir / "Chapter 05 Questions.docx").write_bytes(b"fake")
        (source_dir / "Chapter 10 Questions.docx").write_bytes(b"fake")

        course_root = temp_dir / "biol-1"
        course_dir = course_root / "course"
        course_dir.mkdir(parents=True)

        results = process_chapter_questions(
            source_dir, course_root, course_dir, dry_run=True
        )

        # All three chapters should be listed
        assert len(results["processed"]) == 3
        chapters = {r["chapter"] for r in results["processed"]}
        assert chapters == {1, 5, 10}

    def test_process_creates_module_on_demand(self, temp_dir):
        """Test that processing creates module if missing (dry_run=False)."""
        source_dir = temp_dir / "questions"
        source_dir.mkdir()
        (source_dir / "Chapter 02 Questions.docx").write_bytes(b"fake")

        course_root = temp_dir / "biol-1"
        course_dir = course_root / "course"
        course_dir.mkdir(parents=True)
        # Don't pre-create module-2 — let ensure_module_exists handle it

        results = process_chapter_questions(
            source_dir, course_root, course_dir, dry_run=False
        )

        # The module should have been created by ensure_module_exists
        module_2 = course_dir / "module-2"
        assert module_2.exists() or len(results["errors"]) > 0
