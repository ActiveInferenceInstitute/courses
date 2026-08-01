"""Utility functions for Markdown to PDF conversion."""

import os
import platform
import subprocess
from pathlib import Path
from typing import Optional

import markdown

# Ensure Homebrew libraries are discoverable on macOS (required for WeasyPrint)
if platform.system() == "Darwin":
    try:
        _brew_prefix = subprocess.check_output(
            ["brew", "--prefix"], text=True, stderr=subprocess.DEVNULL
        ).strip()
        _brew_lib = os.path.join(_brew_prefix, "lib")
        _current = os.environ.get("DYLD_LIBRARY_PATH", "")
        if _brew_lib not in _current:
            os.environ["DYLD_LIBRARY_PATH"] = f"{_brew_lib}:{_current}" if _current else _brew_lib
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass  # Homebrew not installed; skip


def read_markdown_file(file_path: Path) -> str:
    """Read Markdown file content.

    Args:
        file_path: Path to Markdown file

    Returns:
        File content as string

    Raises:
        FileNotFoundError: If file doesn't exist
        UnicodeDecodeError: If file encoding is invalid
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {file_path}")

    return file_path.read_text(encoding="utf-8")


def markdown_to_html(markdown_text: str, extensions: Optional[list] = None) -> str:
    """Convert Markdown text to HTML.

    Args:
        markdown_text: Markdown content
        extensions: List of Markdown extensions to use

    Returns:
        HTML content
    """
    if extensions is None:
        extensions = [
            "extra",
            "codehilite",
            "tables",
            "fenced_code",
        ]

    md = markdown.Markdown(extensions=extensions)
    html_content = md.convert(markdown_text)

    return html_content


def html_to_pdf(
    html_content: str,
    css_content: str,
    output_path: Path,
    pdf_options: Optional[dict] = None,
) -> None:
    """Convert HTML content to PDF.

    Args:
        html_content: HTML content
        css_content: CSS styling
        output_path: Path for output PDF file
        pdf_options: Optional page options (``page_size``, ``margin_*``) to
            apply via an ``@page`` rule.

    Raises:
        OSError: If PDF generation fails
    """
    try:
        from weasyprint import HTML, CSS
    except OSError as import_err:
        raise OSError(
            f"Failed to generate PDF: {import_err}\n\n"
            "WeasyPrint requires system libraries. Install them with:\n"
            "  brew install glib pango cairo gdk-pixbuf\n\n"
            "See: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html"
        ) from import_err

    stylesheets = [CSS(string=css_content)]

    if pdf_options:
        page_rules = ["@page {"]
        if pdf_options.get("page_size"):
            page_rules.append(f"    size: {pdf_options['page_size']};")
        margins = {
            "margin_top": "margin-top",
            "margin_bottom": "margin-bottom",
            "margin_left": "margin-left",
            "margin_right": "margin-right",
        }
        for key, css_key in margins.items():
            val = pdf_options.get(key)
            if val:
                page_rules.append(f"    {css_key}: {val};")
        page_rules.append("}")
        if len(page_rules) > 2:  # only add a stylesheet if a page rule was set
            stylesheets.append(CSS(string="\n".join(page_rules)))

    try:
        html_doc = HTML(string=html_content)
        html_doc.write_pdf(output_path, stylesheets=stylesheets)
    except Exception as e:
        raise OSError(f"Failed to generate PDF: {e}") from e


def ensure_output_directory(output_path: Path) -> None:
    """Ensure output directory exists.

    Args:
        output_path: Path to output file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)


def get_output_path(input_path: Path, output_dir: Optional[Path] = None) -> Path:
    """Get output PDF path from input Markdown path.

    Args:
        input_path: Path to input Markdown file
        output_dir: Optional output directory (if None, uses input directory)

    Returns:
        Path to output PDF file
    """
    if output_dir is None:
        output_dir = input_path.parent

    output_filename = input_path.stem + ".pdf"
    return output_dir / output_filename
