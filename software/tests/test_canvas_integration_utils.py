"""Tests for canvas_integration utility functions."""

from pathlib import Path

import pytest

from src.canvas_integration.utils import (
    get_canvas_api_url,
    get_file_mime_type,
    validate_file_size,
)


def test_get_canvas_api_url():
    """Test building Canvas API URL."""
    url = get_canvas_api_url("canvas.instructure.com", "/api/v1/courses/{course_id}", course_id="123")
    assert "canvas.instructure.com" in url
    assert "/api/v1/courses/123" in url


def test_get_canvas_api_url_with_kwargs():
    """Test building Canvas API URL with multiple kwargs."""
    url = get_canvas_api_url(
        "canvas.instructure.com",
        "/api/v1/courses/{course_id}/folders/{folder_id}",
        course_id="123",
        folder_id="456",
    )
    assert "canvas.instructure.com" in url
    assert "/api/v1/courses/123" in url
    assert "/folders/456" in url


def test_validate_file_size_valid(temp_dir):
    """Test validate_file_size with valid file size."""
    test_file = temp_dir / "test.txt"
    test_file.write_text("Small content", encoding="utf-8")

    assert validate_file_size(test_file) is True


def test_validate_file_size_nonexistent():
    """Test validate_file_size with nonexistent file."""
    nonexistent_file = Path("/nonexistent/file.txt")
    assert validate_file_size(nonexistent_file) is False


def test_get_file_mime_type_pdf(temp_dir):
    """Test get_file_mime_type for PDF."""
    pdf_file = temp_dir / "test.pdf"
    pdf_file.touch()
    assert get_file_mime_type(pdf_file) == "application/pdf"


def test_get_file_mime_type_markdown(temp_dir):
    """Test get_file_mime_type for Markdown."""
    md_file = temp_dir / "test.md"
    md_file.touch()
    assert get_file_mime_type(md_file) == "text/markdown"


def test_get_file_mime_type_html(temp_dir):
    """Test get_file_mime_type for HTML."""
    html_file = temp_dir / "test.html"
    html_file.touch()
    assert get_file_mime_type(html_file) == "text/html"


def test_get_file_mime_type_txt(temp_dir):
    """Test get_file_mime_type for text."""
    txt_file = temp_dir / "test.txt"
    txt_file.touch()
    assert get_file_mime_type(txt_file) == "text/plain"


def test_get_file_mime_type_docx(temp_dir):
    """Test get_file_mime_type for DOCX."""
    docx_file = temp_dir / "test.docx"
    docx_file.touch()
    assert get_file_mime_type(docx_file) == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"


def test_get_file_mime_type_pptx(temp_dir):
    """Test get_file_mime_type for PPTX."""
    pptx_file = temp_dir / "test.pptx"
    pptx_file.touch()
    assert get_file_mime_type(pptx_file) == "application/vnd.openxmlformats-officedocument.presentationml.presentation"


def test_get_file_mime_type_unknown(temp_dir):
    """Test get_file_mime_type for unknown file type."""
    unknown_file = temp_dir / "test.unknown"
    unknown_file.touch()
    assert get_file_mime_type(unknown_file) == "application/octet-stream"
