# Batch Processing Technical Documentation

## Overview

Batch processing utilities for converting entire course modules to multiple media formats (PDF, audio, DOCX, HTML, TXT, MD).

## Module Purpose

Process entire modules for multiple format conversions, maintaining directory structure and organizing outputs by curriculum element type.

## Module Boundaries

**What this module does:**

- Processes entire modules for format conversion
- Organizes outputs by curriculum element type
- Coordinates multiple conversion modules
- Generates comprehensive output summaries
- Clears output directories

**What this module does NOT do:**

- Does not perform individual file conversions (uses conversion modules)
- Does not validate module structure (uses `file_validation` module)
- Does not create module structures (uses `module_organization` module)
- Does not generate websites (uses `html_website` module, though it can trigger it)

## Dependencies

### Internal Dependencies (Other Modules)

- `markdown_to_pdf`: For PDF generation
- `text_to_speech`: For audio generation
- `format_conversion`: For multi-format conversions
- `file_validation`: For module validation (optional, used in some workflows)

### External Dependencies (Libraries)

- Standard library only (pathlib, os, logging)

### System Dependencies

- Dependencies of the conversion modules it uses

## Independent Usage

**Can be used standalone**: Yes (if dependencies are available)

**Standalone Example:**

```python
from src.batch_processing.main import process_module_by_type
results = process_module_by_type("/path/to/module", "/path/to/output")
print(f"Generated: {results['summary']}")
```

**Requirements for standalone use:**

- Module directory path
- Core conversion modules available (`markdown_to_pdf`, `text_to_speech`, `format_conversion`)
- System dependencies for conversion modules

## Integration Points

**Used by:**

- `html_website`: Uses `process_module_by_type()` to generate content before website creation
- Generation scripts: Use batch processing functions for course-wide generation

**Integration Pattern:**

- Orchestration: This module orchestrates multiple conversion modules
- Sequential composition: Other modules call this after validation
- Interface: Other modules import and call functions from `main.py`

## Interface Contract

**Public API:**

- `process_module_by_type(module_path, output_dir) -> Dict[str, Any]`
- `process_module_to_pdf(module_path, output_dir) -> List[str]`
- `process_module_to_audio(module_path, output_dir) -> List[str]`
- `process_syllabus(syllabus_path, output_dir) -> Dict[str, Any]`
- `clear_all_outputs(repo_root) -> Dict[str, Any]`

**Return Value Guarantees:**

- `process_module_by_type()`: Returns dict with `summary` (format counts) and `errors`
- `process_module_to_*()`: Returns list of output file paths
- `clear_all_outputs()`: Returns dict with `total_files_removed` and `errors`
- All functions return consistent dictionary structures

**Error Handling:**

- Raises `ValueError` for invalid inputs
- Returns errors in result dictionaries (continues processing on individual file errors)
- Logs errors for debugging

**Side Effects:**

- Creates output files and directories
- Modifies file system (creates files, may clear directories)
- No external API calls (delegates to conversion modules)
- Uses logging for operation tracking

## Function Signatures

### Output Management

#### `clear_all_outputs(repo_root: Path) -> Dict[str, Any]`

Clear all output directories before regeneration.

**Args**:

- `repo_root`: Root path of the repository

**Returns**:

- Dictionary with summary:
  - `cleared_directories`: List of cleared directory paths
  - `total_files_removed`: Total count of files removed
  - `errors`: List of errors encountered

**Logging**:

- Logs start and completion of clearing process
- Logs each directory cleared with file counts
- Logs errors encountered during clearing

### Main Functions

**File**: `src/batch_processing/main.py`

#### `process_module_to_pdf(module_path: str, output_dir: str) -> List[str]`

Convert all Markdown files in a module to PDF.

**Args**:

- `module_path`: Path to module directory
- `output_dir`: Output directory for PDF files

**Returns**:

- List of output PDF file paths

**Raises**:

- `ValueError`: If module path doesn't exist
- `OSError`: If PDF conversion fails

**Dependencies**:

- `markdown_to_pdf.main.render_markdown_to_pdf`

#### `process_module_to_audio(module_path: str, output_dir: str) -> List[str]`

Convert all text/Markdown files in a module to audio.

**Args**:

- `module_path`: Path to module directory
- `output_dir`: Output directory for audio files

**Returns**:

- List of output audio file paths

**Raises**:

- `ValueError`: If module path doesn't exist
- `OSError`: If audio generation fails

**Dependencies**:

- `text_to_speech.main.generate_speech`
- `text_to_speech.utils.extract_text_from_markdown`
- `text_to_speech.utils.read_text_file`

#### `process_module_to_text(module_path: str, output_dir: str) -> List[str]`

Transcribe all audio files in a module to text.

**Args**:

- `module_path`: Path to module directory
- `output_dir`: Output directory for text files

**Returns**:

- List of output text file paths

**Raises**:

- `ValueError`: If module path doesn't exist
- `OSError`: If transcription fails

**Dependencies**:

- `speech_to_text.main.transcribe_audio`

#### `generate_module_media(module_path: str, output_dir: str) -> Dict[str, Any]`

Generate all media formats for a module (PDF, audio, text transcriptions).

**Args**:

- `module_path`: Path to module directory
- `output_dir`: Base output directory for all media

**Returns**:

- Dictionary with results:
  - `pdf_files`: List of generated PDF files
  - `audio_files`: List of generated audio files
  - `text_files`: List of generated text transcriptions
  - `errors`: List of errors encountered

**Raises**:

- `ValueError`: If module path doesn't exist

**Dependencies**:

- `process_module_to_pdf`
- `process_module_to_audio`
- `process_module_to_text`

#### `process_module_by_type(module_path: str, output_dir: str) -> Dict[str, Any]`

Process module files by curriculum element type and generate all format renderings.

Organizes outputs by curriculum element type (assignments, lab-protocols, lecture-content, study-guides) with all formats (PDF, MP3, DOCX, HTML, TXT, MD).

**Args**:

- `module_path`: Path to module directory
- `output_dir`: Base output directory for all renderings

**Returns**:

- Dictionary with results:
  - `by_type`: Dict mapping curriculum type to list of generated files
  - `summary`: Dict with counts of generated files by format
  - `errors`: List of errors encountered

**Raises**:

- `ValueError`: If module path doesn't exist

**Dependencies**:

- `markdown_to_pdf.main.render_markdown_to_pdf`
- `text_to_speech.main.generate_speech`
- `format_conversion.main.convert_file`

#### `process_syllabus(syllabus_path: str, output_dir: str) -> Dict[str, Any]`

Process syllabus files and generate all format renderings.

Organizes outputs by format type (pdf, mp3, docx, html, txt, md) rather than curriculum element type. Excludes README and AGENTS files from processing.

**Args**:

- `syllabus_path`: Path to syllabus directory
- `output_dir`: Base output directory for all renderings

**Returns**:

- Dictionary with results:
  - `by_format`: Dict mapping format type to list of generated files
  - `summary`: Dict with counts of generated files by format
  - `errors`: List of errors encountered

**Raises**:

- `ValueError`: If syllabus path doesn't exist

**Dependencies**:

- `markdown_to_pdf.main.render_markdown_to_pdf`
- `text_to_speech.main.generate_speech`
- `format_conversion.main.convert_file`

#### `process_module_website(module_path: str, output_dir: Optional[str] = None) -> str`

Generate HTML website for a module.

**Args**:

- `module_path`: Path to module directory
- `output_dir`: Optional output directory (defaults to module_path/output/website)

**Returns**:

- Path to generated HTML file

**Raises**:

- `ValueError`: If module path doesn't exist
- `OSError`: If website generation fails

**Dependencies**:

- `html_website.main.generate_module_website`

### Utility Functions

**File**: `src/batch_processing/utils.py`

#### `find_markdown_files(directory: Path) -> List[Path]`

Find all Markdown files in a directory recursively.

#### `find_audio_files(directory: Path) -> List[Path]`

Find all audio files in a directory recursively.

#### `should_process_file(file_path: Path, skip_directories: List[str]) -> bool`

Check if a file should be processed (not in skip directories).

#### `get_relative_output_path(file_path: Path, base_path: Path, output_base: Path) -> Path`

Get output path maintaining relative directory structure.

#### `ensure_output_directory(directory: Path) -> None`

Ensure output directory exists, creating if necessary.

## Configuration

**File**: `src/batch_processing/config.py`

- `MARKDOWN_PATTERNS`: File patterns for Markdown files (`["*.md", "*.markdown"]`)
- `AUDIO_PATTERNS`: File patterns for audio files (`["*.mp3", "*.wav", "*.m4a"]`)
- `SKIP_DIRECTORIES`: Directories to skip during processing (`[".git", "__pycache__", ".pytest_cache", ".venv"]`)
- `OUTPUT_DIRECTORIES`: Output directory names mapping (`{"pdf": "pdf_output", "audio": "audio_output", "text": "text_output", "media": "media_output"}`)

## Integration Points

### Dependencies on Other Modules

- **markdown_to_pdf**: PDF generation from Markdown
- **text_to_speech**: Audio generation from text
- **speech_to_text**: Text transcription from audio
- **format_conversion**: Format conversions (DOCX, HTML)

### Used By

- Test orchestration workflows
- Module processing scripts
- Course material generation pipelines

## Error Handling

All functions handle errors gracefully:

- Individual file processing errors are caught and logged
- Errors are collected in results dictionaries
- Processing continues for remaining files after errors
- All errors are logged with full stack traces via logging module

## Logging

### Logging Configuration

**Module**: `software/src/batch_processing/logging_config.py`

**Function**: `setup_logging(log_dir: Optional[Path] = None, log_level: int = logging.INFO, file_level: int = logging.DEBUG) -> logging.Logger`

Configures logging with:

- Console handler: INFO level and above, simplified format
- File handler: DEBUG level and above, detailed format with timestamps
- Log files: Timestamped files in `software/logs/generation_YYYY-MM-DD_HH-MM-SS.log`

### Logging Usage

All batch processing functions use the logger for:

- Progress tracking (INFO level)
- Error reporting (ERROR level with stack traces)
- Detailed debugging (DEBUG level)
- Warning messages (WARNING level)

### Output Clearing

**Function**: `clear_all_outputs(repo_root: Path) -> Dict[str, Any]`

Clears all output directories before regeneration:

- Finds all `output/` directories in course modules and syllabi
- Removes all files and subdirectories while preserving directory structure
- Logs each directory cleared with file counts
- Returns summary of cleared directories and total files removed
- Handles errors gracefully (logs but continues)

## File Processing

- Maintains relative directory structure in output
- Skips files in configured skip directories
- Processes files matching configured patterns
- Organizes outputs by curriculum element type when using `process_module_by_type`
- Organizes syllabus outputs by format type when using `process_syllabus`
