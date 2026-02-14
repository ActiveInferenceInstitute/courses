# Content Processing Module

> **Navigation**: [← README](../README.md) | [ARCHITECTURE](../../docs/ARCHITECTURE.md)

This module provides content transformation functions for processing course materials.

---

## Purpose

Transform and normalize course content files, including:

- Question renumbering (sectioned → continuous format)
- Whitespace normalization
- Header extraction and analysis
- Question counting and validation

## Public API

### Main Functions

```python
from src.content_processing import (
    process_questions_file,      # Process single questions.md file
    renumber_questions_in_course # Process all questions in a course
)
```

### Utility Functions

```python
from src.content_processing.utils import (
    extract_questions_from_sectioned,  # Extract questions from bullet format
    format_as_continuous,              # Format questions as numbered list
    normalize_whitespace,              # Clean up whitespace in markdown
    extract_headers,                   # Extract headers with levels
    count_questions,                   # Count questions by type
    extract_numbered_items,            # Extract numbered list items
    validate_question_format           # Validate questions.md format
)
```

## Usage Examples

### Process Questions Files

```python
from pathlib import Path
from src.content_processing import process_questions_file, renumber_questions_in_course

# Process a single file
was_changed, count = process_questions_file(
    Path("module-01/questions.md"),
    dry_run=False,
    verbose=True
)

# Process all questions in a course
results = renumber_questions_in_course(
    repo_root=Path("/path/to/repo"),
    courses=["biol-1"],
    dry_run=True
)
```

### Content Analysis

```python
from src.content_processing.utils import (
    count_questions,
    extract_headers,
    validate_question_format
)

# Count questions by type
content = Path("questions.md").read_text()
counts = count_questions(content)
print(f"Numbered: {counts['numbered']}, Bulleted: {counts['bulleted']}")

# Extract document structure
headers = extract_headers(content)
for level, text in headers:
    print(f"{'#' * level} {text}")

# Validate format
result = validate_question_format(content)
if not result["valid"]:
    print(f"Issues: {result['issues']}")
```

### Text Normalization

```python
from src.content_processing.utils import normalize_whitespace

# Clean up markdown content
content = Path("document.md").read_text()
clean = normalize_whitespace(content)
Path("document.md").write_text(clean)
```

## Function Reference

| Function | Purpose | Returns |
|----------|---------|---------|
| `process_questions_file()` | Process single questions.md | `(changed, count)` |
| `renumber_questions_in_course()` | Process all course questions | `dict` with results |
| `normalize_whitespace()` | Clean markdown whitespace | Normalized string |
| `extract_headers()` | Extract headers from markdown | `List[(level, text)]` |
| `count_questions()` | Count questions by type | `dict` with counts |
| `extract_numbered_items()` | Extract numbered list items | `List[str]` |
| `validate_question_format()` | Validate questions.md format | `dict` with results |

## Module Structure

```text
content_processing/
├── __init__.py      # Public exports
├── config.py        # Configuration constants
├── main.py          # High-level processing functions
├── utils.py         # Low-level utility functions
└── AGENTS.md        # This file
```

## Testing

```bash
# Run content_processing tests
uv run pytest tests/test_content_processing*.py -v
```
