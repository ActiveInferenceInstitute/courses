"""Utility functions for format conversion."""

from pathlib import Path
from typing import Optional


def get_file_extension(file_path: Path) -> str:
    """Get file extension (lowercase, without dot).

    Args:
        file_path: Path to file

    Returns:
        File extension without dot
    """
    return file_path.suffix.lower().lstrip(".")


def ensure_output_directory(output_path: Path) -> None:
    """Ensure output directory exists.

    Args:
        output_path: Path to output file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)


def get_output_path(
    input_path: Path, output_format: str, output_dir: Optional[Path] = None
) -> Path:
    """Get output file path from input path and format.

    Args:
        input_path: Path to input file
        output_format: Target format (without dot)
        output_dir: Optional output directory (if None, uses input directory)

    Returns:
        Path to output file
    """
    if output_dir is None:
        output_dir = input_path.parent

    output_filename = input_path.stem + "." + output_format
    return output_dir / output_filename


def convert_markdown_to_pdf(input_path: Path, output_path: Path) -> None:
    """Convert Markdown file to PDF.

    Args:
        input_path: Path to input Markdown file
        output_path: Path to output PDF file
    """
    from ..markdown_to_pdf.main import render_markdown_to_pdf

    render_markdown_to_pdf(str(input_path), str(output_path))


def convert_markdown_to_html(input_path: Path, output_path: Path) -> None:
    """Convert Markdown file to HTML.

    Args:
        input_path: Path to input Markdown file
        output_path: Path to output HTML file
    """
    from ..markdown_to_pdf.utils import markdown_to_html, read_markdown_file

    markdown_content = read_markdown_file(input_path)
    html_content = markdown_to_html(markdown_content)

    # Add basic HTML structure
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{input_path.stem}</title>
</head>
<body>
{html_content}
</body>
</html>"""

    output_path.write_text(full_html, encoding="utf-8")


def convert_html_to_pdf(input_path: Path, output_path: Path) -> None:
    """Convert HTML file to PDF.

    Args:
        input_path: Path to input HTML file
        output_path: Path to output PDF file
    """
    from weasyprint import HTML

    html_content = input_path.read_text(encoding="utf-8")
    HTML(string=html_content).write_pdf(output_path)


def convert_text_to_pdf(input_path: Path, output_path: Path) -> None:
    """Convert text file to PDF.

    Args:
        input_path: Path to input text file
        output_path: Path to output PDF file
    """
    from html import escape

    from weasyprint import HTML

    text_content = input_path.read_text(encoding="utf-8")
    # Escape HTML and wrap in pre tag
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        pre {{ font-family: monospace; white-space: pre-wrap; }}
    </style>
</head>
<body>
    <pre>{escape(text_content)}</pre>
</body>
</html>"""
    HTML(string=html_content).write_pdf(output_path)


def convert_text_to_html(input_path: Path, output_path: Path) -> None:
    """Convert text file to HTML.

    Args:
        input_path: Path to input text file
        output_path: Path to output HTML file
    """
    from html import escape

    text_content = input_path.read_text(encoding="utf-8")
    # Escape HTML and wrap in pre tag
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{escape(input_path.stem)}</title>
</head>
<body>
    <pre>{escape(text_content)}</pre>
</body>
</html>"""
    output_path.write_text(html_content, encoding="utf-8")


def convert_markdown_to_docx(input_path: Path, output_path: Path) -> None:
    """Convert Markdown file to DOCX.

    Preserves headings (H1-H6), ordered/unordered lists, and paragraphs so the
    DOCX keeps the course document's structure instead of flattening it.

    Args:
        input_path: Path to input Markdown file
        output_path: Path to output DOCX file
    """
    from docx import Document

    from ..markdown_to_pdf.utils import markdown_to_html, read_markdown_file

    # Read Markdown and convert to HTML so we can walk real block structure.
    markdown_content = read_markdown_file(input_path)
    html_content = markdown_to_html(markdown_content)

    doc = Document()

    from html.parser import HTMLParser

    class DocxBuilder(HTMLParser):
        """Walk markdown-generated HTML and emit docx paragraphs/headings."""

        def __init__(self, document):
            super().__init__()
            self.doc = document
            self.pending = []
            self.in_li = False
            self.list_depth = 0

        def handle_starttag(self, tag, attrs):
            if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                self._flush_para()
                self._heading_level = int(tag[1])
                self.in_heading = True
            elif tag == "p":
                self.pending = []
            elif tag in ("ul", "ol"):
                self.list_depth += 1
            elif tag == "li":
                self._flush_para()
                self.in_li = True
                self.pending = []
            elif tag in ("strong", "b"):
                pass
            elif tag == "br":
                self.pending.append(" ")

        def handle_endtag(self, tag):
            if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                self._flush_heading()
                self.in_heading = False
            elif tag == "p":
                self._flush_paragraph()
            elif tag in ("ul", "ol"):
                self.list_depth = max(0, self.list_depth - 1)
            elif tag == "li":
                self._flush_list_item()
                self.in_li = False

        def handle_data(self, data):
            self.pending.append(data.strip())

        def _text(self):
            return " ".join(t for t in self.pending if t).strip()

        def _flush_para(self):
            self.pending = []

        def _flush_paragraph(self):
            text = self._text()
            if text:
                self.doc.add_paragraph(text)
            self.pending = []

        def _flush_heading(self):
            if getattr(self, "in_heading", False):
                text = self._text()
                if text:
                    self.doc.add_heading(text, level=self._heading_level)
            self.pending = []

        def _flush_list_item(self):
            if self.in_li:
                text = self._text()
                if text:
                    self.doc.add_paragraph(text, style="List Bullet")
            self.pending = []

    parser = DocxBuilder(doc)
    parser.feed(html_content)
    parser.close()

    doc.save(str(output_path))


def convert_docx_to_markdown(input_path: Path) -> str:
    """Convert DOCX file to Markdown format.

    Args:
        input_path: Path to input DOCX file

    Returns:
        Markdown content as string
    """
    from docx import Document

    doc = Document(str(input_path))
    markdown_lines = []

    for paragraph in doc.paragraphs:
        if not paragraph.text.strip():
            markdown_lines.append("")
            continue

        # Check if paragraph is a heading
        style_name = paragraph.style.name.lower()
        if "heading" in style_name:
            level = 1
            if "heading 1" in style_name or "title" in style_name:
                level = 1
            elif "heading 2" in style_name or "subtitle" in style_name:
                level = 2
            elif "heading 3" in style_name:
                level = 3
            elif "heading 4" in style_name:
                level = 4
            elif "heading 5" in style_name:
                level = 5
            elif "heading 6" in style_name:
                level = 6

            text = _extract_formatted_text(paragraph)
            markdown_lines.append(f"{'#' * level} {text}")
        else:
            # Regular paragraph - extract formatted text
            text = _extract_formatted_text(paragraph)
            if text.strip():
                markdown_lines.append(text)

        # Add blank line after paragraph
        markdown_lines.append("")

    # Process tables
    for table in doc.tables:
        markdown_lines.append("")
        # Extract table header
        if table.rows:
            header_row = table.rows[0]
            header_cells = [_extract_formatted_text(cell) for cell in header_row.cells]
            markdown_lines.append("| " + " | ".join(header_cells) + " |")
            markdown_lines.append("| " + " | ".join(["---"] * len(header_cells)) + " |")

            # Extract data rows
            for row in table.rows[1:]:
                cells = [_extract_formatted_text(cell) for cell in row.cells]
                markdown_lines.append("| " + " | ".join(cells) + " |")
        markdown_lines.append("")

    # Remove trailing blank lines
    while markdown_lines and not markdown_lines[-1].strip():
        markdown_lines.pop()

    return "\n".join(markdown_lines)


def _extract_formatted_text(paragraph) -> str:
    """Extract text from paragraph with formatting preserved as Markdown.

    Args:
        paragraph: docx paragraph object

    Returns:
        Formatted text string
    """
    text_parts = []

    for run in paragraph.runs:
        text = run.text
        if not text:
            continue

        # Apply formatting
        if run.bold:
            text = f"**{text}**"
        if run.italic:
            text = f"*{text}*"
        if run.underline:
            text = f"<u>{text}</u>"

        text_parts.append(text)

    return "".join(text_parts)


def convert_pdf_to_text(input_path: Path, output_path: Path) -> None:
    """Convert PDF file to text.

    Args:
        input_path: Path to input PDF file
        output_path: Path to output text file
    """
    from pypdf import PdfReader

    reader = PdfReader(str(input_path))
    text_content = []

    for page in reader.pages:
        # pypdf's extract_text() may return None for unscannable pages; guard
        # so we never write a literal "None" into the transcript.
        text_content.append(page.extract_text() or "")

    full_text = "\n\n".join(text_content)
    output_path.write_text(full_text, encoding="utf-8")


def convert_audio_to_text(input_path: Path, output_path: Path) -> None:
    """Convert audio file to text using speech-to-text.

    Args:
        input_path: Path to input audio file
        output_path: Path to output text file
    """
    from ..speech_to_text.main import transcribe_audio

    transcribe_audio(str(input_path), str(output_path))


def get_conversion_path(input_path: str, output_format: str) -> str:
    """Generate output path for file conversion.

    Args:
        input_path: Path to input file
        output_format: Target format (without dot)

    Returns:
        Output file path with new extension
    """
    input_file = Path(input_path)
    output_file = input_file.with_suffix(f".{output_format}")
    return str(output_file)
