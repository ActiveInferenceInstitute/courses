# Schedule Processing Technical Documentation

## Overview

Schedule processing and generation utilities for parsing, processing, and exporting course schedules in multiple formats.

## Module Purpose

Parse schedule markdown files, extract structured schedule data, and generate schedule outputs in various formats (PDF, HTML, DOCX, TXT, MP3).

## Function Signatures

### Main Functions

**File**: `src/schedule/main.py`

#### `parse_schedule_markdown(schedule_path: str) -> Dict[str, Any]`

Parse schedule markdown file and extract structured data.

**Args**:
- `schedule_path`: Path to schedule markdown file

**Returns**:
- Dictionary with parsed schedule data:
  - `entries`: List of schedule entry dictionaries (week, date, topic, notes)
  - `sections`: Dictionary with additional sections (title, semester, important_dates, exam_schedule)
  - `metadata`: Dictionary with file metadata (file_path, file_name, total_weeks)

**Raises**:
- `FileNotFoundError`: If schedule file doesn't exist
- `ValueError`: If schedule cannot be parsed

**Dependencies**:
- `utils.parse_schedule_table`
- `utils.extract_schedule_sections`
- `utils.read_schedule_file`
- `utils.validate_schedule_entry`

#### `process_schedule(schedule_path: str, output_dir: str, formats: Optional[List[str]] = None) -> Dict[str, Any]`

Process schedule file and generate outputs in specified formats.

**Args**:
- `schedule_path`: Path to schedule markdown file
- `output_dir`: Output directory for generated files
- `formats`: List of output formats (default: all supported formats)

**Returns**:
- Dictionary with results:
  - `outputs`: Dictionary mapping format to list of output file paths
  - `summary`: Dictionary with counts of generated files by format
  - `errors`: List of errors encountered

**Raises**:
- `FileNotFoundError`: If schedule file doesn't exist
- `ValueError`: If schedule cannot be parsed or format is unsupported

**Dependencies**:
- `parse_schedule_markdown`
- `generate_schedule_outputs`
- `markdown_to_pdf.main.render_markdown_to_pdf` (for PDF)
- `format_conversion.main.convert_file` (for HTML, DOCX)
- `text_to_speech.utils.extract_text_from_markdown` (for TXT, MP3)
- `text_to_speech.main.generate_speech` (for MP3)

#### `generate_schedule_outputs(schedule_data: Dict[str, Any], output_dir: Path, base_name: str, formats: List[str]) -> Dict[str, List[str]]`

Generate schedule outputs in specified formats.

**Args**:
- `schedule_data`: Parsed schedule data dictionary
- `output_dir`: Output directory
- `base_name`: Base name for output files
- `formats`: List of output formats to generate

**Returns**:
- Dictionary mapping format to list of output file paths

**Raises**:
- `ValueError`: If format is not supported
- `OSError`: If file generation fails

**Dependencies**:
- `utils.generate_schedule_markdown`
- `markdown_to_pdf.main.render_markdown_to_pdf` (for PDF)
- `format_conversion.main.convert_file` (for HTML, DOCX)
- `text_to_speech.utils.extract_text_from_markdown` (for TXT, MP3)
- `text_to_speech.main.generate_speech` (for MP3)

#### `batch_process_schedules(directory: str, output_dir: str, formats: Optional[List[str]] = None) -> Dict[str, Any]`

Batch process all schedule files in a directory.

**Args**:
- `directory`: Directory containing schedule files
- `output_dir`: Output directory for generated files
- `formats`: List of output formats (default: all supported formats)

**Returns**:
- Dictionary with results:
  - `processed_files`: List of processed schedule file paths
  - `outputs`: Dictionary mapping format to list of output file paths
  - `summary`: Dictionary with counts of generated files by format
  - `errors`: List of errors encountered

**Raises**:
- `ValueError`: If directory doesn't exist

**Dependencies**:
- `process_schedule`
- `utils.find_schedule_files`

### Utility Functions

**File**: `src/schedule/utils.py`

#### `parse_schedule_table(content: str) -> List[Dict[str, str]]`

Parse schedule table from markdown content.

**Args**:
- `content`: Markdown content containing schedule table

**Returns**:
- List of dictionaries with schedule entries (week, date, topic, notes)

#### `extract_schedule_sections(content: str) -> Dict[str, str]`

Extract sections from schedule markdown (title, dates, exams, etc.).

**Args**:
- `content`: Markdown content

**Returns**:
- Dictionary with section names as keys and content as values

#### `format_date(date_str: str) -> Optional[str]`

Format date string to standard format.

**Args**:
- `date_str`: Date string in various formats (e.g., "1/19/2026", "01/19/2026")

**Returns**:
- Formatted date string or None if parsing fails

#### `validate_schedule_entry(entry: Dict[str, str]) -> bool`

Validate a schedule entry has required fields.

**Args**:
- `entry`: Schedule entry dictionary

**Returns**:
- True if entry is valid, False otherwise

#### `generate_schedule_markdown(entries: List[Dict[str, str]], sections: Optional[Dict[str, str]] = None) -> str`

Generate formatted markdown from schedule entries.

**Args**:
- `entries`: List of schedule entry dictionaries
- `sections`: Optional dictionary with additional sections (title, semester, etc.)

**Returns**:
- Formatted markdown string

#### `find_schedule_files(directory: Path) -> List[Path]`

Find schedule markdown files in a directory.

**Args**:
- `directory`: Directory to search

**Returns**:
- List of schedule file paths

#### `read_schedule_file(file_path: Path) -> str`

Read schedule markdown file content.

**Args**:
- `file_path`: Path to schedule file

**Returns**:
- File content as string

**Raises**:
- `FileNotFoundError`: If file doesn't exist
- `OSError`: If file cannot be read

#### `ensure_output_directory(output_path: Path) -> None`

Ensure output directory exists, creating if necessary.

**Args**:
- `output_path`: Path to output file or directory

## Configuration

**File**: `src/schedule/config.py`

- `SUPPORTED_OUTPUT_FORMATS`: List of supported output formats (`["pdf", "html", "docx", "txt", "mp3"]`)
- `SCHEDULE_FILE_PATTERNS`: File patterns for schedule files (`["Schedule.md", "schedule.md", "*schedule*.md"]`)
- `SCHEDULE_COLUMNS`: Table column mappings for schedule parsing:
  - `week`: 0
  - `date`: 1
  - `topic`: 2
  - `notes`: 3
- `DEFAULT_HEADERS`: Default schedule table headers (`["Week", "Date", "Topic", "Notes"]`)

## Integration Points

### Dependencies on Other Modules

- **markdown_to_pdf**: PDF generation from markdown
- **format_conversion**: Format conversions (HTML, DOCX)
- **text_to_speech**: Audio generation from text

### Used By

- Batch processing workflows
- Schedule generation scripts
- Course material processing pipelines

## Error Handling

- Validates schedule file existence
- Validates schedule entry structure
- Validates output format support
- Continues batch processing after individual file errors
- Collects errors in results dictionaries

## Schedule Format

### Input Format

Schedule markdown files should contain:
- Title (H1 heading)
- Semester/Year (H2 heading)
- Schedule table with columns: Week, Date, Topic, Notes
- Optional sections: Important Dates, Exam Schedule

### Table Format

```markdown
| Week | Date | Topic | Notes |
|------|------|-------|-------|
| 1 | 1/19/2026 | Biology: The Study of Life | |
```

### Output Formats

- **PDF**: Generated from markdown using markdown_to_pdf module
- **HTML**: Converted from markdown using format_conversion module
- **DOCX**: Converted from markdown using format_conversion module
- **TXT**: Extracted text from markdown
- **MP3**: Generated audio from extracted text using text_to_speech module

## Processing Workflow

1. Parse schedule markdown file
2. Extract schedule table entries
3. Extract additional sections (title, dates, exams)
4. Validate schedule entries
5. Generate outputs in requested formats
6. Return results with file paths and summary
