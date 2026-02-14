# Markdown to PDF Technical Documentation

## Overview

Markdown to PDF conversion utilities using WeasyPrint for rendering.

## Module Purpose

Convert Markdown course materials to PDF format with customizable styling and batch processing support.

## Module Boundaries

**What this module does:**
- Converts Markdown files to PDF format
- Provides batch processing for multiple Markdown files
- Supports custom CSS styling for PDF output
- Configures PDF rendering options

**What this module does NOT do:**
- Does not convert other formats to PDF (use `format_conversion` module)
- Does not process entire modules (use `batch_processing` module)
- Does not validate Markdown structure (use `file_validation` module)
- Does not handle file organization (use `module_organization` module)

## Dependencies

### Internal Dependencies (Other Modules)
- None (standalone module, Layer 1)

### External Dependencies (Libraries)
- `weasyprint`: HTML/CSS to PDF rendering
- `markdown`: Markdown to HTML conversion

### System Dependencies
- System libraries for WeasyPrint (cairo, pango, gdk-pixbuf, glib on macOS/Linux)

## Independent Usage

**Can be used standalone**: Yes

**Standalone Example:**
```python
from src.markdown_to_pdf.main import render_markdown_to_pdf
render_markdown_to_pdf("input.md", "output.pdf")
```

**Requirements for standalone use:**
- WeasyPrint library installed
- System dependencies for WeasyPrint (see installation docs)
- Markdown file as input

## Integration Points

**Used by:**
- `format_conversion`: Uses `render_markdown_to_pdf()` for Markdown to PDF conversion
- `batch_processing`: Uses `render_markdown_to_pdf()` for batch PDF generation
- `schedule`: Uses `render_markdown_to_pdf()` for schedule PDF generation

**Integration Pattern:**
- Sequential composition: This module is called by other modules to generate PDFs
- Interface: Other modules import and call `render_markdown_to_pdf()` from `main.py`

## Interface Contract

**Public API:**
- `render_markdown_to_pdf(input_path, output_path, css_content=None, pdf_options=None) -> None`
- `batch_render_markdown(directory, output_dir) -> List[str]`
- `configure_pdf_options(template, options) -> Dict[str, Any]`

**Return Value Guarantees:**
- `render_markdown_to_pdf()`: Returns None, creates PDF file at output_path
- `batch_render_markdown()`: Returns list of output file paths (strings)
- `configure_pdf_options()`: Returns dictionary with configured options

**Error Handling:**
- Raises `FileNotFoundError` if input file doesn't exist
- Raises `ValueError` for invalid inputs
- Raises `OSError` if PDF generation fails

**Side Effects:**
- Creates PDF files at specified output paths
- Creates output directories if they don't exist
- No modification of input files
- No external API calls

## Function Signatures

### Main Functions

**File**: `src/markdown_to_pdf/main.py`

#### `render_markdown_to_pdf(input_path: str, output_path: str, css_content: Optional[str] = None, pdf_options: Optional[Dict[str, Any]] = None) -> None`

Convert a Markdown file to PDF format.

**Args**:
- `input_path`: Path to input Markdown file
- `output_path`: Path for output PDF file
- `css_content`: Optional custom CSS content (uses default if None)
- `pdf_options`: Optional PDF options (uses default if None)

**Raises**:
- `FileNotFoundError`: If input file doesn't exist
- `OSError`: If PDF generation fails

**Dependencies**:
- WeasyPrint library for HTML to PDF conversion
- Markdown parser for Markdown to HTML conversion

#### `batch_render_markdown(directory: str, output_dir: str) -> List[str]`

Batch convert all Markdown files in a directory to PDF.

**Args**:
- `directory`: Directory containing Markdown files
- `output_dir`: Output directory for PDF files

**Returns**:
- List of output file paths

**Raises**:
- `ValueError`: If directory doesn't exist
- `OSError`: If PDF generation fails for any file

#### `configure_pdf_options(template: str, options: Dict[str, Any]) -> Dict[str, Any]`

Configure PDF rendering options.

**Args**:
- `template`: Template name (currently only "default" is supported)
- `options`: Dictionary of rendering options to override defaults

**Returns**:
- Configured options dictionary

**Raises**:
- `ValueError`: If template is invalid

### Utility Functions

**File**: `src/markdown_to_pdf/utils.py`

#### `read_markdown_file(file_path: Path) -> str`

Read Markdown file content.

#### `markdown_to_html(markdown_content: str) -> str`

Convert Markdown content to HTML.

#### `html_to_pdf(html_content: str, css_content: str, output_path: Path) -> None`

Convert HTML content to PDF using WeasyPrint.

**Dependencies**:
- WeasyPrint library

#### `ensure_output_directory(output_path: Path) -> None`

Ensure output directory exists, creating if necessary.

#### `get_output_path(input_file: Path, output_dir: Path) -> Path`

Generate output PDF path from input Markdown file.

## Configuration

**File**: `src/markdown_to_pdf/config.py`

- `DEFAULT_PDF_OPTIONS`: Dictionary of default PDF rendering options:
  - `page_size`: "letter"
  - `margin_top`, `margin_bottom`, `margin_left`, `margin_right`: "1in"
  - `encoding`: "utf-8"

- `DEFAULT_CSS`: Default CSS template for PDF styling including:
  - Page settings (size, margins)
  - Typography (font families, sizes, line heights)
  - Heading styles
  - Code block styling
  - Table styling
  - Image handling

## Integration Points

### Dependencies on Other Modules

- None (standalone module)

### Used By

- **format_conversion**: Markdown to PDF conversion
- **batch_processing**: Batch PDF generation for modules
- Test orchestration workflows

### External Dependencies

- **WeasyPrint**: HTML/CSS to PDF rendering
- **Markdown parser**: Markdown to HTML conversion

## Error Handling

- Validates input file existence
- Creates output directories automatically
- Continues batch processing after individual file errors
- Raises appropriate exceptions for critical failures

## Conversion Process

1. Read Markdown file content
2. Convert Markdown to HTML
3. Apply CSS styling (default or custom)
4. Render HTML to PDF using WeasyPrint
5. Save PDF file

## Styling

Default CSS provides:
- Professional typography
- Proper page breaks
- Code block formatting
- Table styling
- Image handling
- Page layout with margins

Custom CSS can be provided to override default styling.
