"""Utility functions for lab manual parsing and rendering."""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import markdown


from . import config


@dataclass
class TableConfig:
    """Configuration for a data table."""

    rows: int = 5
    columns: List[str] = field(default_factory=lambda: config.DEFAULT_MEASUREMENT_COLUMNS.copy())
    fillable: bool = True
    title: Optional[str] = None


@dataclass
class MeasurementConfig:
    """Configuration for a measurement section."""

    aspects: List[str] = field(default_factory=list)
    include_device: bool = True
    include_unit: bool = True
    include_value: bool = False


@dataclass
class LabElement:
    """Represents a parsed lab element from Markdown."""

    element_type: str
    content: str
    config: Dict[str, Any] = field(default_factory=dict)
    start_pos: int = 0
    end_pos: int = 0


def parse_table_directive(content: str) -> Tuple[TableConfig, str]:
    """Parse a lab:data-table directive from Markdown content.

    Args:
        content: Markdown content containing the directive

    Returns:
        Tuple of (TableConfig, remaining content after directive)
    """
    pattern = r"<!-- lab:data-table\s*(.*?)\s*-->(.*?)<!-- /lab:data-table -->"
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return TableConfig(), content

    attrs_str = match.group(1).strip()
    table_content = match.group(2).strip()

    # Parse attributes
    table_config = TableConfig()

    # Parse rows attribute
    rows_match = re.search(r"rows=(\d+)", attrs_str)
    if rows_match:
        table_config.rows = int(rows_match.group(1))

    # Parse columns from table content if present
    if "|" in table_content:
        lines = table_content.strip().split("\n")
        if lines:
            header_line = lines[0]
            columns = [col.strip() for col in header_line.split("|") if col.strip()]
            if columns:
                table_config.columns = columns

    # Parse title
    title_match = re.search(r'title="([^"]+)"', attrs_str)
    if title_match:
        table_config.title = title_match.group(1)

    return table_config, content[match.end() :]


def parse_measurement_section(content: str) -> Tuple[MeasurementConfig, str]:
    """Parse a measurement section from Markdown content.

    Args:
        content: Markdown content

    Returns:
        Tuple of (MeasurementConfig, remaining content)
    """
    pattern = r"<!-- lab:measurement-feasibility -->(.*?)<!-- /lab:measurement-feasibility -->"
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return MeasurementConfig(), content

    measurement_config = MeasurementConfig()

    return measurement_config, content[match.end() :]


def parse_object_selection(content: str) -> Tuple[Dict[str, Any], str]:
    """Parse an object selection section.

    Args:
        content: Markdown content

    Returns:
        Tuple of (selection config dict, remaining content)
    """
    pattern = r"<!-- lab:object-selection -->(.*?)<!-- /lab:object-selection -->"
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return {}, content

    section_content = match.group(1).strip()

    selection_config = {
        "in_room": True,
        "not_in_room": True,
        "content": section_content,
    }

    return selection_config, content[match.end() :]


def parse_reflection(content: str) -> Tuple[Dict[str, Any], str]:
    """Parse a reflection section.

    Args:
        content: Markdown content

    Returns:
        Tuple of (reflection config dict, remaining content)
    """
    pattern = r"<!-- lab:reflection -->(.*?)<!-- /lab:reflection -->"
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return {}, content

    section_content = match.group(1).strip()

    return {"content": section_content}, content[match.end() :]


def expand_fillable_fields(html: str) -> str:
    """Expand {fill} placeholders to interactive HTML elements.

    Args:
        html: HTML content with {fill} placeholders

    Returns:
        HTML with expanded input elements
    """
    # Replace {fill:text} with text input
    html = re.sub(r"\{fill:text\}", '<input type="text" class="fill-text" />', html)

    # Replace {fill:number} with number input
    html = re.sub(r"\{fill:number\}", '<input type="number" class="fill-number" />', html)

    # Replace {fill:textarea rows=N} with textarea
    def textarea_replacement(match: re.Match) -> str:
        attrs = match.group(1) if match.group(1) else ""
        rows_match = re.search(r"rows=(\d+)", attrs)
        rows = rows_match.group(1) if rows_match else "3"
        return f'<textarea class="fill-textarea" rows="{rows}"></textarea>'

    html = re.sub(r"\{fill:textarea\s*(.*?)\}", textarea_replacement, html)

    # Replace {fill:drawing} with drawing area box
    def drawing_replacement(match: re.Match) -> str:
        attrs = match.group(1) if match.group(1) else ""

        # Parse height attribute (default 300px)
        height_match = re.search(r"height=(\d+)", attrs)
        height = height_match.group(1) if height_match else "300"

        # Parse shape attribute (default rectangle)
        shape_match = re.search(r"shape=(\w+)", attrs)
        shape = shape_match.group(1) if shape_match else "rectangle"

        if shape == "circle":
            # Create circular drawing area
            return f"""<div class="fill-drawing-circle" style="width: {height}px; height: {height}px;"></div>"""
        else:
            # Create rectangular drawing area
            return f"""<div class="fill-drawing" style="min-height: {height}px;"></div>"""

    html = re.sub(r"\{fill:drawing\s*(.*?)\}", drawing_replacement, html)

    # Replace {fill} in table cells with fillable cell styling
    html = re.sub(r"<td>\s*\{fill\}\s*</td>", '<td class="fillable">&nbsp;</td>', html)

    # Replace standalone {fill} with text input
    html = re.sub(r"\{fill\}", '<input type="text" class="fill-text" />', html)

    return html


def create_data_table_html(table_config: TableConfig) -> str:
    """Create HTML for a data table.

    Args:
        table_config: Configuration for the table

    Returns:
        HTML string for the table
    """
    html = ""

    if table_config.title:
        html += f"<h3>{table_config.title}</h3>\n"

    html += '<table class="lab-table">\n'

    # Header row
    html += "<thead><tr>\n"
    html += '<th class="row-number">#</th>\n'
    for col in table_config.columns:
        html += f"<th>{col}</th>\n"
    html += "</tr></thead>\n"

    # Data rows
    html += "<tbody>\n"
    for i in range(1, table_config.rows + 1):
        html += "<tr>\n"
        html += f'<td class="row-number">{i}</td>\n'
        for _ in table_config.columns:
            if table_config.fillable:
                html += '<td class="fillable">&nbsp;</td>\n'
            else:
                html += "<td>&nbsp;</td>\n"
        html += "</tr>\n"
    html += "</tbody>\n"
    html += "</table>\n"

    return html


def create_measurement_table_html(
    rows: int = 5,
    aspects: Optional[List[str]] = None,
    include_device: bool = True,
    include_unit: bool = True,
    include_value: bool = False,
) -> str:
    """Create HTML for a measurement table.

    Args:
        rows: Number of rows
        aspects: Pre-filled aspects (optional)
        include_device: Include device column
        include_unit: Include unit column
        include_value: Include value column

    Returns:
        HTML string for the measurement table
    """
    columns = ["Physical Aspect"]
    if include_device:
        columns.append("Measurement Device")
    if include_unit:
        columns.append("Measurement Unit")
    if include_value:
        columns.append("Measured Value")

    html = '<table class="measurement-table">\n'

    # Header row
    html += "<thead><tr>\n"
    html += '<th class="row-number">#</th>\n'
    for col in columns:
        html += f"<th>{col}</th>\n"
    html += "</tr></thead>\n"

    # Data rows
    html += "<tbody>\n"
    for i in range(1, rows + 1):
        html += "<tr>\n"
        html += f'<td class="row-number">{i}</td>\n'

        # First column (aspect)
        if aspects and i <= len(aspects):
            html += f"<td>{aspects[i - 1]}</td>\n"
        else:
            html += '<td class="fillable">&nbsp;</td>\n'

        # Remaining columns are fillable
        for _ in columns[1:]:
            html += '<td class="fillable">&nbsp;</td>\n'

        html += "</tr>\n"
    html += "</tbody>\n"
    html += "</table>\n"

    return html


def create_object_selection_html(in_room: bool = True, not_in_room: bool = True) -> str:
    """Create HTML for object selection section.

    Args:
        in_room: Include "object in room" field
        not_in_room: Include "object not in room" field

    Returns:
        HTML string for the section
    """
    html = '<div class="object-selection">\n'
    html += "<h3>Object Selection</h3>\n"

    if in_room:
        html += '<div class="object-field">\n'
        html += '<span class="object-label">Object in room:</span>\n'
        html += '<span class="object-input"></span>\n'
        html += "</div>\n"

    if not_in_room:
        html += '<div class="object-field">\n'
        html += '<span class="object-label">Object NOT in room:</span>\n'
        html += '<span class="object-input"></span>\n'
        html += "</div>\n"

    html += "</div>\n"

    return html


def create_feasibility_html(question: str, options: List[str]) -> str:
    """Create HTML for a feasibility question with checkbox options.

    Args:
        question: The question text
        options: List of checkbox options

    Returns:
        HTML string for the section
    """
    html = '<div class="feasibility-section">\n'
    html += f'<div class="feasibility-question">{question}</div>\n'
    html += '<div class="feasibility-options">\n'

    for idx, option in enumerate(options):
        id_ = f"feas_{idx}"
        html += '<div class="fill-checkbox">\n'
        html += f'<input type="checkbox" id="{id_}" />\n'
        html += f'<label for="{id_}">{option}</label>\n'
        html += "</div>\n"

    html += "</div>\n"
    html += "</div>\n"

    return html


def create_reflection_html(prompt: str = "", min_height: str = "100px") -> str:
    """Create HTML for a reflection box.

    Args:
        prompt: Optional prompt text
        min_height: Minimum height of the box

    Returns:
        HTML string for the reflection box
    """
    html = '<div class="reflection-box">\n'
    if prompt:
        html += f"<p><em>{prompt}</em></p>\n"
    html += f'<textarea class="fill-textarea" style="min-height: {min_height}"></textarea>\n'
    html += "</div>\n"

    return html


def create_lab_header_html(
    lab_title: str,
    course_name: str = "",
    include_name: bool = True,
    include_date: bool = True,
    include_section: bool = True,
) -> str:
    """Create HTML for lab header with student info fields.

    Args:
        lab_title: Title of the lab
        course_name: Course name
        include_name: Include name field
        include_date: Include date field
        include_section: Include section field

    Returns:
        HTML string for the header
    """
    html = f"<h1>{lab_title}</h1>\n"

    if course_name:
        html += f'<p style="text-align: center; font-style: italic;">{course_name}</p>\n'

    html += '<div class="lab-header">\n'

    if include_name:
        html += '<div class="lab-header-field">\n'
        html += '<span class="lab-header-label">Name:</span>\n'
        html += '<span class="lab-header-value"></span>\n'
        html += "</div>\n"

    if include_date:
        html += '<div class="lab-header-field">\n'
        html += '<span class="lab-header-label">Date:</span>\n'
        html += '<span class="lab-header-value"></span>\n'
        html += "</div>\n"

    if include_section:
        html += '<div class="lab-header-field">\n'
        html += '<span class="lab-header-label">Section:</span>\n'
        html += '<span class="lab-header-value"></span>\n'
        html += "</div>\n"

    html += "</div>\n"

    return html


def markdown_to_html(content: str) -> str:
    """Convert Markdown content to HTML using markdown library.

    Args:
        content: Markdown string

    Returns:
        HTML string
    """
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "nl2br"],
    )
    return md.convert(content)


def read_markdown_file(file_path: Path) -> str:
    """Read a Markdown file and return its contents.

    Args:
        file_path: Path to Markdown file

    Returns:
        File contents as string

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return file_path.read_text(encoding="utf-8")


def ensure_output_directory(output_path: Path) -> None:
    """Ensure the output directory exists.

    Args:
        output_path: Path to output file or directory
    """
    if output_path.is_dir():
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)


def html_to_pdf(html_content: str, css_content: str, output_path: Path) -> None:
    """Convert HTML content to PDF using WeasyPrint.

    Args:
        html_content: HTML string
        css_content: CSS string
        output_path: Path for output PDF
    """
    from weasyprint import HTML, CSS

    html_obj = HTML(string=html_content)
    css_obj = CSS(string=css_content)
    html_obj.write_pdf(output_path, stylesheets=[css_obj])


def get_output_path(input_path: Path, output_dir: Path, extension: str = ".pdf") -> Path:
    """Generate output path for a file.

    Args:
        input_path: Path to input file
        output_dir: Output directory
        extension: Output file extension

    Returns:
        Path for output file
    """
    stem = input_path.stem
    return output_dir / f"{stem}{extension}"
