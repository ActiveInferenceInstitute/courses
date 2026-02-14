# Lab Manual Module

## Overview

The lab manual module provides tools for rendering rich lab manuals from Markdown with support for:

- Interactive data tables with fillable cells
- Measurement recording tables
- Object selection sections
- Feasibility analysis with checkboxes
- Reflection boxes
- PDF/HTML output

## Module Architecture

```
src/lab_manual/
├── __init__.py      # Public API exports
├── config.py        # CSS, templates, constants
├── main.py          # Core rendering functions
├── utils.py         # Parsing and HTML utilities
├── AGENTS.md        # This file
└── README.md        # Usage documentation
```

## Standalone: Yes

This module can be used independently. Core dependencies are:

- `markdown` - For Markdown to HTML conversion
- `weasyprint` - For PDF generation

## Key Functions

### main.py

- `render_lab_manual(input_path: str, output_path: str, output_format: str = "pdf", lab_title: Optional[str] = None, course_name: Optional[str] = None) -> str`
  - Main rendering function for lab manuals
  - Supports PDF and HTML output formats
  - Auto-extracts title from first heading

- `parse_lab_elements(markdown_content: str) -> List[LabElement]`
  - Parse lab directives from Markdown
  - Returns list of LabElement objects with type, content, config

- `generate_data_table(rows: int = 5, columns: Optional[List[str]] = None, title: Optional[str] = None) -> str`
  - Generate HTML for a data table
  - Configurable rows, columns, and title

- `generate_measurement_table(rows: int = 5, aspects: Optional[List[str]] = None, include_device: bool = True, include_unit: bool = True) -> str`
  - Generate measurement-specific table
  - Optional pre-filled aspects

- `batch_render_lab_manuals(directory: str, output_dir: str, output_format: str = "pdf") -> List[str]`
  - Batch process all lab files in directory

- `get_lab_template(template_name: str = "basic") -> str`
  - Get pre-built Markdown templates
  - Available: "basic", "measurement", "observation"

### utils.py

- `parse_table_directive(content: str) -> Tuple[TableConfig, str]`
- `parse_object_selection(content: str) -> Tuple[Dict, str]`
- `parse_reflection(content: str) -> Tuple[Dict, str]`
- `expand_fillable_fields(html: str) -> str`
- `create_data_table_html(table_config: TableConfig) -> str`
- `create_measurement_table_html(rows: int, ...) -> str`
- `create_object_selection_html(in_room: bool, not_in_room: bool) -> str`
- `create_feasibility_html(question: str, options: List[str]) -> str`
- `create_reflection_html(prompt: str, min_height: str) -> str`
- `create_lab_header_html(lab_title: str, course_name: str, ...) -> str`

## Lab Directive Syntax

The module extends Markdown with custom directives:

### Data Table

```markdown
<!-- lab:data-table rows=5 title="My Table" -->
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| {fill}   | {fill}   | {fill}   |
<!-- /lab:data-table -->
```

### Object Selection

```markdown
<!-- lab:object-selection -->
Object in room: {fill:text}
Object NOT in room: {fill:text}
<!-- /lab:object-selection -->
```

### Measurement Feasibility

```markdown
<!-- lab:measurement-feasibility -->
Question text here
- [ ] Checkbox option 1
- [ ] Checkbox option 2
{fill:textarea rows=3}
<!-- /lab:measurement-feasibility -->
```

### Reflection

```markdown
<!-- lab:reflection -->
Reflection prompt text
{fill:textarea rows=5}
<!-- /lab:reflection -->
```

### Fillable Field Types

- `{fill}` - Basic fillable (in tables becomes empty cell)
- `{fill:text}` - Inline text input
- `{fill:textarea rows=N}` - Multi-line text area

## Configuration

### config.py Constants

- `LAB_MANUAL_CSS` - Print-friendly CSS for worksheets
- `LAB_HTML_TEMPLATE` - HTML page template
- `DEFAULT_PDF_OPTIONS` - WeasyPrint PDF settings
- `LAB_DIRECTIVES` - Regex patterns for directives
- `DEFAULT_MEASUREMENT_COLUMNS` - Default table columns
- `LAB_INTERACTIVE_JS` - JavaScript for HTML interactivity

## Data Classes

### TableConfig

```python
@dataclass
class TableConfig:
    rows: int = 5
    columns: List[str] = field(default_factory=list)
    fillable: bool = True
    title: Optional[str] = None
```

### LabElement

```python
@dataclass
class LabElement:
    element_type: str  # "data-table", "object-selection", etc.
    content: str
    config: Dict[str, Any]
    start_pos: int
    end_pos: int
```

## Real Methods Policy

All functions use real implementations:

- Real Markdown parsing via `markdown` library
- Real PDF generation via `weasyprint`
- Real file I/O operations
- No mocks or stubs

## Error Handling

- `FileNotFoundError` - Input file missing
- `ValueError` - Invalid output format or template name
- `OSError` - PDF generation failure

## Dependencies

- Python 3.9+
- markdown
- weasyprint
