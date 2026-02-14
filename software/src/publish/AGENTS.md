# Publish Module — Technical Documentation

## Overview

The publish module handles copying generated course materials from development directories to the published output directories.

## Module Interface

### Main Functions

#### `publish_course(course_path: str, publish_root: str = None) -> Dict[str, Any]`

Publishes course materials to the published directory.

**Args:**

- `course_path`: Path to the course directory (e.g., 'biol-1')
- `publish_root`: Root directory for publishing (default: PUBLISHED in repo root)

**Returns:**

- Dictionary with keys: `course`, `modules_published`, `syllabus_files`, `total_files`, `modules`, `errors`

### Utility Functions

**File**: `src/publish/utils.py`

#### Core Utilities

##### `get_course_config(course_name: str) -> Dict[str, str]`

Get configuration for a specific course.

##### `clean_directory(path: Path) -> None`

Clean a directory (remove all contents) or create if doesn't exist.

##### `copy_directory_contents(src: Path, dst: Path, exclude_patterns: Optional[List[str]] = None) -> int`

Copy contents of source directory to destination.

#### Flattening Functions

##### `flatten_module(module_dir: Path, dry_run: bool = False, verbose: bool = False) -> int`

Flatten a single module directory by moving files from subdirs to root.

##### `flatten_published(published_dir: Path, skip_dirs: Optional[List[str]] = None, dry_run: bool = False, verbose: bool = False) -> int`

Flatten all module directories in PUBLISHED. Skips: labs, dashboards, syllabus, slides, exams.

##### `clean_published(published_dir: Path) -> None`

Remove all content from PUBLISHED directory.

#### Copy Functions

##### `copy_labs_and_dashboards(repo_root: Path, courses: Optional[List[str]] = None, verbose: bool = False) -> int`

Copy labs and dashboards to PUBLISHED directory.

##### `copy_slides(repo_root: Path, courses: Optional[List[str]] = None, verbose: bool = False) -> int`

Copy slide PDFs from resources/slides to PUBLISHED/slides directory.

##### `copy_slides_to_modules(repo_root: Path, courses: Optional[List[str]] = None, verbose: bool = False) -> int`

Copy slide PDFs into each module's published folder. Supports two naming conventions:

- `module-{num}-slides-*.pdf` (biol-1 style)
- `Module {XX} - Topic.pdf` (biol-8 style)

##### `copy_exams(repo_root: Path, verbose: bool = False) -> int`

Copy exam files from course/exams to PUBLISHED directory.

##### `copy_practice_tests(repo_root: Path, courses: Optional[List[str]] = None, verbose: bool = False) -> int`

Copy practice test files (markdown and rendered outputs) to PUBLISHED directory.

## Configuration

Course configurations in `config.py`:

| Course | Module Source | Syllabus Source | Include Syllabus |
|--------|--------------|-----------------|------------------|
| biol-1 | `output` | `output` | Yes |
| biol-8 | `output` | `output` | Yes |

## Usage

```python
from src.publish.main import publish_course
from src.publish.utils import copy_slides_to_modules, flatten_published

# Publish a course
results = publish_course("course_development/biol-8")
print(f"Published {results['modules_published']} modules")

# Copy slides to module folders
from pathlib import Path
copy_slides_to_modules(Path("/path/to/repo"))

# Flatten published directory
flatten_published(Path("/path/to/PUBLISHED"))
```

## Integration Points

- **batch_processing**: Generates output files before publishing
- **format_conversion**: Creates multi-format outputs (PDF, DOCX, HTML, TXT, MD)
- **PUBLISHED/**: Target directory for published content
