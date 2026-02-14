# Validation Module Technical Documentation

## Overview

The validation module provides functions to verify that course outputs have been generated correctly and published to the expected locations. It generates detailed logs and reports for quality assurance.

## Module Structure

```
validation/
├── __init__.py    # Module exports
├── config.py      # Expected output configuration
├── utils.py       # Helper utilities  
├── main.py        # Core validation functions
└── AGENTS.md      # This documentation
```

## Function Signatures

### main.py

```python
def validate_outputs(course_path: str) -> Dict[str, Any]
    """Validate that all expected outputs exist for a course.
    
    Args:
        course_path: Path to course directory (e.g., course_development/biol-8)
        
    Returns:
        Dictionary with validation results including valid status,
        modules checked/valid counts, and list of issues.
    """

def validate_published(published_path: str) -> Dict[str, Any]
    """Validate that published directory has expected structure.
    
    Args:
        published_path: Path to PUBLISHED directory
        
    Returns:
        Dictionary with validation results including file counts
        per course and any missing courses.
    """

def generate_validation_report(course_name: str, repo_root: str = None) -> Dict[str, Any]
    """Generate comprehensive validation report for a course.
    
    Args:
        course_name: Name of course (biol-1 or biol-8)
        repo_root: Optional repo root path (auto-detected if not provided)
        
    Returns:
        Dictionary with complete validation report including both
        source and published validation results.
    """

def get_output_summary(course_path: str) -> Dict[str, Any]
    """Get summary of outputs for a course.
    
    Args:
        course_path: Path to course directory
        
    Returns:
        Dictionary with output counts by format and module.
    """
```

### utils.py

```python
def count_files_by_extension(directory: Path) -> Dict[str, int]
    """Count files in directory by extension."""

def get_module_directories(course_path: Path) -> List[Path]
    """Get list of module directories in a course."""

def check_output_directory(module_path: Path) -> Tuple[bool, Dict[str, bool]]
    """Check if module has expected output directory structure."""

def check_study_guide_files(module_path: Path) -> Dict[str, bool]
    """Check which study guide files exist for a module."""

def check_website_files(module_path: Path) -> Dict[str, bool]
    """Check which website files exist for a module."""

def format_file_counts(counts: Dict[str, int]) -> str
    """Format file counts as readable string."""

def get_timestamp() -> str
    """Get current timestamp for logging."""
```

## Configuration (config.py)

### Expected Outputs Per Module

- **Study Guides**: keys-to-success and questions in PDF, DOCX, HTML, TXT, MP3
- **Website**: index.html

### Course Expectations

| Course | Expected Modules |
|--------|------------------|
| BIOL-1 | 17 |
| BIOL-8 | 15 |

## Usage

### Command Line

```bash
cd software
uv run python scripts/validate_outputs.py --course all
```

### Programmatic

```python
from src.validation import validate_outputs, generate_validation_report

# Validate a single course
results = validate_outputs("../course_development/biol-8")
print(f"Valid: {results['valid']}")
print(f"Modules: {results['modules_valid']}/{results['modules_checked']}")

# Generate full report
report = generate_validation_report("biol-8")
print(f"Source valid: {report['summary']['source_valid']}")
print(f"Published files: {report['summary']['published_files']}")
```

## Output Format

### validate_outputs() Result

```json
{
    "valid": true,
    "course": "biol-8",
    "timestamp": "2026-01-29 10:50:00",
    "modules_checked": 15,
    "modules_valid": 15,
    "modules": [...],
    "syllabus_valid": true,
    "issues": []
}
```

### validate_published() Result

```json
{
    "valid": true,
    "path": "/path/to/PUBLISHED",
    "timestamp": "2026-01-29 10:50:00",
    "courses": {
        "biol-1": {"files_by_type": {...}, "total_files": 100},
        "biol-8": {"files_by_type": {...}, "total_files": 150}
    },
    "total_files": 250,
    "issues": []
}
```

---

*Created: 2026-01-29*
