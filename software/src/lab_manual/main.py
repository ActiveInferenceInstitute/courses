"""Main functions for lab manual rendering."""

import re
from pathlib import Path
from typing import List, Optional

from . import config
from .utils import (
    LabElement,
    TableConfig,
    create_data_table_html,
    create_lab_header_html,
    create_measurement_table_html,
    create_object_selection_html,
    ensure_output_directory,
    expand_fillable_fields,
    get_output_path,
    html_to_pdf,
    markdown_to_html,
    read_markdown_file,
)


def parse_lab_elements(markdown_content: str) -> List[LabElement]:
    """Parse lab-specific elements from Markdown content.
    
    Scans the Markdown content for lab directives and extracts them
    as LabElement objects with their configurations.
    
    Args:
        markdown_content: Raw Markdown content
        
    Returns:
        List of LabElement objects found in the content
    """
    elements = []
    
    # Parse data tables
    table_pattern = r"<!-- lab:data-table\s*(.*?)\s*-->(.*?)<!-- /lab:data-table -->"
    for match in re.finditer(table_pattern, markdown_content, re.DOTALL):
        attrs_str = match.group(1).strip()
        table_content = match.group(2).strip()
        
        # Parse rows
        rows = 5
        rows_match = re.search(r"rows=(\d+)", attrs_str)
        if rows_match:
            rows = int(rows_match.group(1))
        
        # Parse columns from markdown table header
        columns = config.DEFAULT_MEASUREMENT_COLUMNS.copy()
        if "|" in table_content:
            lines = table_content.strip().split("\n")
            if lines:
                header_cols = [col.strip() for col in lines[0].split("|") if col.strip()]
                if header_cols:
                    columns = header_cols
        
        # Parse title
        title = None
        title_match = re.search(r'title="([^"]+)"', attrs_str)
        if title_match:
            title = title_match.group(1)
        
        elements.append(LabElement(
            element_type="data-table",
            content=table_content,
            config={"rows": rows, "columns": columns, "title": title},
            start_pos=match.start(),
            end_pos=match.end(),
        ))
    
    # Parse object selection
    obj_pattern = r"<!-- lab:object-selection -->(.*?)<!-- /lab:object-selection -->"
    for match in re.finditer(obj_pattern, markdown_content, re.DOTALL):
        elements.append(LabElement(
            element_type="object-selection",
            content=match.group(1).strip(),
            config={"in_room": True, "not_in_room": True},
            start_pos=match.start(),
            end_pos=match.end(),
        ))
    
    # Parse measurement feasibility
    feas_pattern = r"<!-- lab:measurement-feasibility -->(.*?)<!-- /lab:measurement-feasibility -->"
    for match in re.finditer(feas_pattern, markdown_content, re.DOTALL):
        elements.append(LabElement(
            element_type="measurement-feasibility",
            content=match.group(1).strip(),
            config={},
            start_pos=match.start(),
            end_pos=match.end(),
        ))
    
    # Parse calculation
    calc_pattern = r"<!-- lab:calculation -->(.*?)<!-- /lab:calculation -->"
    for match in re.finditer(calc_pattern, markdown_content, re.DOTALL):
        elements.append(LabElement(
            element_type="calculation",
            content=match.group(1).strip(),
            config={},
            start_pos=match.start(),
            end_pos=match.end(),
        ))

    # Parse reflection
    refl_pattern = r"<!-- lab:reflection -->(.*?)<!-- /lab:reflection -->"
    for match in re.finditer(refl_pattern, markdown_content, re.DOTALL):
        elements.append(LabElement(
            element_type="reflection",
            content=match.group(1).strip(),
            config={},
            start_pos=match.start(),
            end_pos=match.end(),
        ))
    
    # Sort by position
    elements.sort(key=lambda e: e.start_pos)
    
    return elements


def generate_data_table(
    rows: int = 5,
    columns: Optional[List[str]] = None,
    title: Optional[str] = None,
    fillable: bool = True,
) -> str:
    """Generate HTML for a data table.
    
    Args:
        rows: Number of rows in the table
        columns: List of column headers
        title: Optional table title
        fillable: Whether cells should be fillable
        
    Returns:
        HTML string for the table
    """
    if columns is None:
        columns = config.DEFAULT_MEASUREMENT_COLUMNS.copy()
    
    table_config = TableConfig(
        rows=rows,
        columns=columns,
        fillable=fillable,
        title=title,
    )
    
    return create_data_table_html(table_config)


def generate_measurement_table(
    rows: int = 5,
    aspects: Optional[List[str]] = None,
    include_device: bool = True,
    include_unit: bool = True,
    include_value: bool = False,
) -> str:
    """Generate HTML for a measurement table.
    
    Args:
        rows: Number of rows
        aspects: Optional list of pre-filled physical aspects
        include_device: Include measurement device column
        include_unit: Include measurement unit column
        include_value: Include measured value column
        
    Returns:
        HTML string for the measurement table
    """
    return create_measurement_table_html(
        rows=rows,
        aspects=aspects,
        include_device=include_device,
        include_unit=include_unit,
        include_value=include_value,
    )


def _process_lab_content(markdown_content: str) -> str:
    """Process Markdown content and expand lab directives to HTML.
    
    Args:
        markdown_content: Raw Markdown with lab directives
        
    Returns:
        HTML string with expanded lab elements
    """
    # Parse all lab elements
    elements = parse_lab_elements(markdown_content)
    
    # Process content from end to start to preserve positions
    result = markdown_content
    for element in reversed(elements):
        replacement_html = ""
        
        if element.element_type == "data-table":
            replacement_html = create_data_table_html(TableConfig(
                rows=element.config.get("rows", 5),
                columns=element.config.get("columns", config.DEFAULT_MEASUREMENT_COLUMNS),
                title=element.config.get("title"),
                fillable=True,
            ))
        
        elif element.element_type == "object-selection":
            replacement_html = create_object_selection_html(
                in_room=element.config.get("in_room", True),
                not_in_room=element.config.get("not_in_room", True),
            )
        
        elif element.element_type == "measurement-feasibility":
            # Convert the content to HTML and add feasibility styling
            content_html = markdown_to_html(element.content)
            replacement_html = f'<div class="feasibility-section">\n{content_html}\n</div>'
        
        elif element.element_type == "calculation":
            content_html = markdown_to_html(element.content)
            replacement_html = f'<div class="calculation-box">\n{content_html}\n</div>'

        elif element.element_type == "reflection":
            content_html = markdown_to_html(element.content)
            replacement_html = f'<div class="reflection-box">\n{content_html}\n</div>'
        
        # Replace directive with generated HTML
        result = result[:element.start_pos] + replacement_html + result[element.end_pos:]
    
    # Convert remaining markdown to HTML
    result = markdown_to_html(result)
    
    # Expand fillable fields
    result = expand_fillable_fields(result)
    
    return result


def render_lab_manual(
    input_path: str,
    output_path: str,
    output_format: str = "pdf",
    lab_title: Optional[str] = None,
    course_name: Optional[str] = None,
    include_header: bool = True,
) -> str:
    """Render a lab manual from Markdown to PDF or HTML.
    
    Args:
        input_path: Path to input Markdown file
        output_path: Path for output file
        output_format: Output format ("pdf" or "html")
        lab_title: Optional custom lab title (defaults to filename)
        course_name: Optional course name for header
        include_header: Include lab header with name/date fields
        
    Returns:
        Path to generated output file
        
    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If output format is invalid
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    output_format = output_format.lower()
    if output_format not in ("pdf", "html"):
        raise ValueError(f"Invalid output format: {output_format}. Must be 'pdf' or 'html'.")
    
    # Ensure output directory exists
    ensure_output_directory(output_file)
    
    # Read and process content
    markdown_content = read_markdown_file(input_file)
    
    # Extract title from first heading if not provided
    if lab_title is None:
        title_match = re.search(r"^#\s+(.+)$", markdown_content, re.MULTILINE)
        if title_match:
            lab_title = title_match.group(1).strip()
        else:
            lab_title = input_file.stem.replace("-", " ").replace("_", " ").title()
    
    # When header is included, strip the leading H1 and course subtitle
    # from markdown to avoid duplication (header already provides these)
    if include_header:
        # Remove leading H1
        markdown_content = re.sub(
            r"^#\s+.+\n*", "", markdown_content, count=1
        )
        # Remove course subtitle line (bold text with pipe)
        markdown_content = re.sub(
            r"^\*\*.+\*\*\s*\|.+\n*", "", markdown_content, count=1
        )
        # Remove source Name/Date line to avoid duplication with header fields
        # Matches: **Name:** _____ **Date:** _____  (with optional underscores or blanks)
        markdown_content = re.sub(
            r"^\*\*Name:\*\*\s*_*\s*\*\*Date:\*\*\s*_*\s*\n*", "", markdown_content, count=1
        )
        # Remove leading horizontal rule left behind
        markdown_content = re.sub(r"^---\s*\n*", "", markdown_content, count=1)

    # Process lab content
    content_html = _process_lab_content(markdown_content)

    # Build header if requested
    header_html = ""
    if include_header:
        header_html = create_lab_header_html(
            lab_title=lab_title,
            course_name=course_name or "",
            include_name=True,
            include_date=True,
            include_section=False,
        )
    
    # Combine header and content
    full_content = header_html + content_html
    
    if output_format == "html":
        # Generate HTML
        html_output = config.LAB_HTML_TEMPLATE.format(
            title=lab_title,
            css=config.LAB_MANUAL_CSS,
            content=full_content,
            javascript=config.LAB_INTERACTIVE_JS,
        )
        output_file.write_text(html_output, encoding="utf-8")
    else:
        # Generate PDF
        html_output = config.LAB_HTML_TEMPLATE.format(
            title=lab_title,
            css=config.LAB_MANUAL_CSS,
            content=full_content,
            javascript="",  # No JS in PDF
        )
        html_to_pdf(html_output, config.LAB_MANUAL_CSS, output_file)
    
    return str(output_file)


def batch_render_lab_manuals(
    directory: str,
    output_dir: str,
    output_format: str = "pdf",
    course_name: Optional[str] = None,
    max_lab: Optional[int] = None,
) -> List[str]:
    """Batch render lab manuals from a directory.
    
    Args:
        directory: Directory containing Markdown lab files
        output_dir: Output directory for rendered files
        output_format: Output format ("pdf" or "html")
        course_name: Optional course name
        max_lab: If specified, only process labs 1 through max_lab
        
    Returns:
        List of output file paths
        
    Raises:
        ValueError: If directory doesn't exist
    """
    source_dir = Path(directory)
    if not source_dir.exists() or not source_dir.is_dir():
        raise ValueError(f"Directory does not exist: {directory}")
    
    output_directory = Path(output_dir)
    output_directory.mkdir(parents=True, exist_ok=True)
    
    output_files = []
    
    # Find all lab manual files (check for 'lab' in filename)
    lab_files = [
        f for f in source_dir.glob("*.md")
        if "lab" in f.name.lower()
    ]
    
    # Also include any markdown file if no lab-specific files found
    if not lab_files:
        lab_files = list(source_dir.glob("*.md"))
    
    # Filter by max_lab if specified
    if max_lab is not None:
        import re
        def get_lab_number(filename: str) -> int:
            """Extract lab number from filename like 'lab-01_topic.md' or 'lab-1.md'."""
            match = re.search(r'lab-?(\d+)', filename, re.IGNORECASE)
            return int(match.group(1)) if match else 999
        
        lab_files = [f for f in lab_files if get_lab_number(f.name) <= max_lab]
        print(f"  Filtering to labs 1-{max_lab}: {len(lab_files)} lab files")
    
    extension = ".html" if output_format.lower() == "html" else ".pdf"
    
    for md_file in lab_files:
        try:
            output_path = get_output_path(md_file, output_directory, extension)
            render_lab_manual(
                str(md_file),
                str(output_path),
                output_format=output_format,
                course_name=course_name,
            )
            output_files.append(str(output_path))
        except Exception as e:
            print(f"Error rendering {md_file}: {e}")
            continue
    
    return output_files


def get_lab_template(template_name: str = "basic") -> str:
    """Get a lab manual Markdown template.
    
    Args:
        template_name: Name of template ("basic", "measurement", "observation")
        
    Returns:
        Markdown template string
        
    Raises:
        ValueError: If template name is invalid
    """
    templates = {
        "basic": """# Lab Title

## Objectives

- Objective 1
- Objective 2

## Materials

- Material 1
- Material 2

## Procedure

1. Step 1
2. Step 2

## Data Collection

<!-- lab:data-table rows=5 -->
| Observation | Value | Notes |
|-------------|-------|-------|
| {fill}      | {fill}| {fill}|
<!-- /lab:data-table -->

## Analysis

<!-- lab:reflection -->
Analyze your results here.
<!-- /lab:reflection -->

## Conclusions

{fill:textarea rows=5}
""",
        "measurement": """# Measurement Lab

## Objective

Explore different ways to measure physical properties of objects.

## Part 1: Object Selection

<!-- lab:object-selection -->
Object in room: {fill:text}
Object NOT in room: {fill:text}
<!-- /lab:object-selection -->

## Part 2: Physical Aspects

Think of 5 different physical aspects you could measure for each object.

<!-- lab:data-table rows=5 title="Physical Aspects Table" -->
| Physical Aspect | Measurement Device | Measurement Unit |
|-----------------|-------------------|------------------|
| {fill}          | {fill}            | {fill}           |
<!-- /lab:data-table -->

## Part 3: Feasibility Analysis

<!-- lab:measurement-feasibility -->
Which physical aspects COULD we measure tonight for the object in the room?
{fill:textarea rows=3}

How might we get those other measurements?
- [ ] Internet access
- [ ] Money/funding
- [ ] Institutional review
- [ ] Moving equipment
- [ ] Other: {fill:text}
<!-- /lab:measurement-feasibility -->

## Part 4: Reflection

<!-- lab:reflection -->
Compare the measurement approaches for both objects.
{fill:textarea rows=5}
<!-- /lab:reflection -->
""",
        "observation": """# Observation Lab

## Objective

Practice systematic observation and recording.

## Observations

<!-- lab:data-table rows=10 title="Observation Log" -->
| Time | Observation | Notes |
|------|-------------|-------|
| {fill} | {fill} | {fill} |
<!-- /lab:data-table -->

## Summary

<!-- lab:reflection -->
Summarize your key observations.
<!-- /lab:reflection -->
""",
    }
    
    if template_name not in templates:
        raise ValueError(f"Unknown template: {template_name}. Available: {list(templates.keys())}")
    
    return templates[template_name]
