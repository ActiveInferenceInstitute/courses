# Legacy Import Module - Technical Documentation

## Overview

Extracts and organizes legacy course materials (DOCX chapter questions, PDF slides) from the `bio_1_2025` archive into the standardized `biol-1` module structure. This is a one-time migration tool.

## Module Structure

```
src/legacy_import/
  __init__.py    - Public API exports
  config.py      - Constants and chapter-to-module mapping
  utils.py       - Helper functions (extraction, directory creation)
  main.py        - Core business logic (processing pipelines)
  AGENTS.md      - This file
```

## Public API

### config.py

#### `get_chapter_to_module_mapping() -> Dict[int, int]`
Returns a 1:1 mapping of chapter numbers (1-17) to module numbers (1-17).

#### Constants
- `CHAPTER_COUNT = 17` - Total number of chapters/modules
- `QUESTION_FILE_PATTERN = "*.docx"` - Glob pattern for question files
- `SLIDE_FILE_PATTERN = "*.pdf"` - Glob pattern for slide files
- `EXCLUDED_MD_FILES = {"README.md", "AGENTS.md"}` - Markdown files excluded from for_upload processing
- `SOURCE_QUESTIONS_SUBDIR` - Relative path to chapter questions source directory
- `SOURCE_SLIDES_FULL_SUBDIR` - Relative path to full slides source directory
- `SOURCE_SLIDES_NOTES_SUBDIR` - Relative path to notes slides source directory

### utils.py

#### `extract_chapter_number(filename: str) -> int`
Extracts chapter number from a filename containing "Chapter NN" pattern.
- **Args:** `filename` - e.g., "Chapter 01 Keys to Success.docx"
- **Returns:** Integer chapter number
- **Raises:** `ValueError` if pattern not found

#### `ensure_module_exists(course_root: Path, module_num: int, dry_run: bool) -> Path`
Ensures a module directory exists, creating it via `create_module_structure()` if needed.
- **Args:** `course_root` - Course root path (e.g., biol-1), `module_num` - Module number, `dry_run` - Skip creation if True
- **Returns:** Path to module directory

#### `create_comprehension_questions(module_path: Path, module_num: int, dry_run: bool) -> None`
Creates `resources/comprehension-questions.md` scaffold file in a module.

#### `create_questions_directory(module_path: Path, module_num: int, dry_run: bool) -> None`
Creates `questions/` directory with `questions.json`, `README.md`, and `AGENTS.md` scaffolds.

### main.py

#### `process_chapter_questions(source_dir: Path, course_root: Path, course_dir: Path, dry_run: bool) -> Dict[str, Any]`
Processes all DOCX chapter question files. Converts each to Markdown and places in the corresponding module's resources directory.
- **Args:** `source_dir` - Directory with DOCX files, `course_root` - Course root, `course_dir` - Course directory, `dry_run` - Preview mode
- **Returns:** Dict with `processed`, `skipped`, `errors`, and `summary` keys

#### `process_slides(slides_full_dir: Path, slides_notes_dir: Path, course_root: Path, dry_run: bool) -> Dict[str, Any]`
Copies PDF slides (full and notes variants) to module slides directories.
- **Args:** `slides_full_dir` - Full slides source, `slides_notes_dir` - Notes slides source, `course_root` - Course root, `dry_run` - Preview mode
- **Returns:** Dict with `processed`, `skipped`, `errors`, and `summary` keys

#### `create_for_upload_files(module_path: Path, module_num: int, dry_run: bool) -> Dict[str, Any]`
Creates `for_upload/` directory with PDF and DOCX conversions of markdown resources plus slide PDFs.
- **Args:** `module_path` - Module directory, `module_num` - Module number, `dry_run` - Preview mode
- **Returns:** Dict with `processed`, `errors`, and `summary` keys

#### `process_for_upload_all_modules(course_dir: Path, dry_run: bool) -> Dict[str, Any]`
Runs `create_for_upload_files()` for every module in the course directory.
- **Args:** `course_dir` - Course directory (e.g., biol-1/course), `dry_run` - Preview mode
- **Returns:** Dict with `modules_processed`, `modules_errors`, `total_pdf`, `total_docx`, `total_slides`, `errors` keys

## Dependencies

- `src.batch_processing.logging_config` - Logging setup
- `src.format_conversion.utils` - DOCX to Markdown conversion
- `src.format_conversion.main` - File format conversion
- `src.module_organization.main` - Module structure creation
- `src.module_organization.utils` - Module path resolution
- `src.markdown_to_pdf.main` - Markdown to PDF rendering
