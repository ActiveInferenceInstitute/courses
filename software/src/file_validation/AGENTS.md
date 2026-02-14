# File Validation Technical Documentation

## Overview

File and structure validation utilities for course modules, including naming convention checks, required file verification, and comprehensive validation reports.

## Module Purpose

Validate course module structure, file naming conventions, extensions, and provide detailed validation reports for module quality assurance.

## Module Boundaries

**What this module does:**
- Validates module file structure and organization
- Checks file naming conventions
- Verifies required files and directories exist
- Provides detailed validation reports
- Checks file sizes and extensions

**What this module does NOT do:**
- Does not create module structures (use `module_organization` module)
- Does not process or convert files (use conversion modules)
- Does not generate content (use content generation modules)
- Does not upload to external systems (use `canvas_integration` module)

## Dependencies

### Internal Dependencies (Other Modules)
- None (standalone module, Layer 0)

### External Dependencies (Libraries)
- None (uses only standard library: pathlib, os)

### System Dependencies
- None

## Independent Usage

**Can be used standalone**: Yes

**Standalone Example:**
```python
from src.file_validation.main import validate_module_files
result = validate_module_files("/path/to/module")
if result["valid"]:
    print("Module is valid")
else:
    print(f"Errors: {result.get('errors', [])}")
```

**Requirements for standalone use:**
- Module directory path
- No external dependencies required

## Integration Points

**Used by:**
- `batch_processing`: Validates modules before processing
- `canvas_integration`: Validates modules before Canvas upload

**Integration Pattern:**
- Conditional composition: Other modules call validation before proceeding
- Interface: Other modules import and call `validate_module_files()` from `main.py`

## Interface Contract

**Public API:**
- `validate_module_files(module_path) -> Dict[str, Any]`
- `check_naming_conventions(directory) -> List[str]`
- `verify_required_structure(module_path) -> bool`
- `validate_course_structure(course_path) -> Dict[str, Any]`
- `get_validation_report(module_path) -> Dict[str, Any]`
- `find_missing_materials(module_path) -> Dict[str, Any]`
- `check_file_sizes(module_path, max_size) -> List[str]`

**Return Value Guarantees:**
- `validate_module_files()`: Returns dict with `valid` (bool) and error details
- `check_naming_conventions()`: Returns list of file paths with violations
- `verify_required_structure()`: Returns bool indicating structure validity
- All functions return consistent dictionary structures

**Error Handling:**
- Returns error information in result dictionaries
- Does not raise exceptions for validation failures (returns `valid: False`)
- Raises exceptions only for invalid inputs (e.g., non-existent paths)

**Side Effects:**
- Read-only operations (no file modifications)
- No external API calls
- No file creation or deletion

## Function Signatures

### Main Functions

**File**: `src/file_validation/main.py`

#### `validate_module_files(module_path: str) -> Dict[str, Any]`

Validate files in a module directory.

**Args**:
- `module_path`: Path to module directory

**Returns**:
- Dictionary with validation results:
  - `valid`: bool indicating if module is valid
  - `missing_files`: List of missing required files
  - `missing_directories`: List of missing required directories
  - `naming_violations`: List of files with naming violations
  - `invalid_extensions`: List of files with invalid extensions
  - `error`: Error message if module path doesn't exist

#### `check_naming_conventions(directory: str) -> List[str]`

Check file naming convention compliance.

**Args**:
- `directory`: Directory to check

**Returns**:
- List of files with naming convention violations

#### `verify_required_structure(module_path: str) -> bool`

Verify module has required folder structure.

**Args**:
- `module_path`: Path to module directory

**Returns**:
- True if structure is complete, False otherwise

#### `validate_course_structure(course_path: str) -> Dict[str, Any]`

Validate entire course structure.

**Args**:
- `course_path`: Path to course directory

**Returns**:
- Dictionary with validation results:
  - `valid`: bool indicating if course is valid
  - `modules`: List of module validation results
  - `total_modules`: Total number of modules
  - `valid_modules`: Number of valid modules
  - `issues`: List of course-level issues

#### `get_validation_report(module_path: str) -> Dict[str, Any]`

Get detailed validation report for a module.

**Args**:
- `module_path`: Path to module directory

**Returns**:
- Dictionary with detailed validation report:
  - `module_path`: Path to module
  - `is_valid`: Overall validity
  - `structure_valid`: Structure validity
  - `files_valid`: Files validity
  - `naming_valid`: Naming conventions validity
  - `details`: Detailed breakdown
  - `recommendations`: List of recommendations

#### `find_missing_materials(module_path: str) -> Dict[str, Any]`

Find missing required materials in a module.

**Args**:
- `module_path`: Path to module directory

**Returns**:
- Dictionary with missing materials:
  - `missing_required`: List of missing required files/directories
  - `missing_optional`: List of missing optional materials
  - `suggestions`: Suggestions for completing module

#### `check_file_sizes(module_path: str, max_size: int = 50 * 1024 * 1024) -> List[str]`

Check for files that exceed maximum size.

**Args**:
- `module_path`: Path to module directory
- `max_size`: Maximum file size in bytes (default: 50MB)

**Returns**:
- List of files that exceed maximum size

### Utility Functions

**File**: `src/file_validation/utils.py`

#### `is_kebab_case(name: str) -> bool`

Check if a name follows kebab-case convention.

**Args**:
- `name`: Name to check

**Returns**:
- True if name is kebab-case, False otherwise

#### `has_module_prefix(name: str) -> bool`

Check if a name has module prefix (e.g., "module-1-").

**Args**:
- `name`: Name to check

**Returns**:
- True if name has module prefix, False otherwise

#### `matches_pattern(name: str, pattern: Pattern[str]) -> bool`

Check if a name matches a pattern.

**Args**:
- `name`: Name to check
- `pattern`: Pattern to match against

**Returns**:
- True if name matches pattern, False otherwise

#### `get_file_extension(file_path: Path) -> str`

Get file extension (lowercase).

**Args**:
- `file_path`: Path to file

**Returns**:
- File extension (including dot) or empty string

#### `is_valid_extension(file_path: Path) -> bool`

Check if file has valid extension.

**Args**:
- `file_path`: Path to file

**Returns**:
- True if extension is valid, False otherwise

#### `validate_assignment_name(file_name: str) -> bool`

Validate assignment file name.

**Args**:
- `file_name`: File name to validate

**Returns**:
- True if name is valid, False otherwise

**Pattern**: `^module-\d+-assignment-\d+(-[a-z0-9-]+)?\.(md|pdf)$`

#### `validate_lecture_name(file_name: str) -> bool`

Validate lecture file name.

**Args**:
- `file_name`: File name to validate

**Returns**:
- True if name is valid, False otherwise

**Pattern**: `^module-\d+-lecture-[a-z0-9-]+\.(pdf|pptx)$`

#### `validate_lab_name(file_name: str) -> bool`

Validate lab protocol file name.

**Args**:
- `file_name`: File name to validate

**Returns**:
- True if name is valid, False otherwise

**Pattern**: `^module-\d+-lab-\d+-[a-z0-9-]+\.md$`

#### `validate_study_guide_name(file_name: str) -> bool`

Validate study guide file name.

**Args**:
- `file_name`: File name to validate

**Returns**:
- True if name is valid, False otherwise

**Pattern**: `^module-\d+-study-guide\.(md|pdf)$`

#### `validate_quiz_name(file_name: str) -> bool`

Validate quiz file name.

**Args**:
- `file_name`: File name to validate

**Returns**:
- True if name is valid, False otherwise

**Pattern**: `^module-\d+-quiz\.(md|pdf)$`

#### `check_required_files_exist(module_path: Path) -> List[str]`

Check which required files are missing.

**Args**:
- `module_path`: Path to module directory

**Returns**:
- List of missing required file names

#### `check_required_directories_exist(module_path: Path) -> List[str]`

Check which required directories are missing.

**Args**:
- `module_path`: Path to module directory

**Returns**:
- List of missing required directory names

#### `get_file_type(file_name: str) -> str`

Determine the type of course material file based on name.

**Args**:
- `file_name`: File name to analyze

**Returns**:
- File type: "assignment", "lecture", "lab", "study_guide", "quiz", or "unknown"

#### `extract_module_number_from_filename(file_name: str) -> int`

Extract module number from a file name.

**Args**:
- `file_name`: File name (e.g., "module-1-assignment-1.md")

**Returns**:
- Module number

**Raises**:
- `ValueError`: If module number cannot be extracted

#### `validate_file_name_structure(file_name: str) -> dict`

Validate and analyze file name structure.

**Args**:
- `file_name`: File name to validate

**Returns**:
- Dictionary with validation results:
  - `valid`: bool indicating if name is valid
  - `file_type`: Type of file (assignment, lecture, etc.)
  - `module_number`: Extracted module number (if available)
  - `issues`: List of validation issues

## Configuration

**File**: `src/file_validation/config.py`

- `REQUIRED_FILES`: List of required files in each module (`["README.md", "AGENTS.md"]`)
- `REQUIRED_DIRECTORIES`: List of required directories (`["assignments"]`)
- `KEBAB_CASE_PATTERN`: Regex pattern for kebab-case validation
- `MODULE_PREFIX_PATTERN`: Regex pattern for module prefix (`^module-\d+-`)
- `VALID_EXTENSIONS`: List of valid file extensions (`[".md", ".pdf", ".pptx", ".docx", ".txt", ".html"]`)
- `ASSIGNMENT_PATTERN`: Regex pattern for assignment file names
- `LECTURE_PATTERN`: Regex pattern for lecture file names
- `LAB_PATTERN`: Regex pattern for lab protocol file names
- `STUDY_GUIDE_PATTERN`: Regex pattern for study guide file names
- `QUIZ_PATTERN`: Regex pattern for quiz file names

## Integration Points

### Used By

- **canvas_integration**: Validates modules before Canvas upload
- **module_organization**: Validates module structure
- Test suites for module validation

## Validation Rules

### File Naming Conventions

- All course material files must have module prefix: `module-N-`
- Files must follow kebab-case naming
- Specific patterns for different file types:
  - Assignments: `module-N-assignment-M[-description].(md|pdf)`
  - Lectures: `module-N-lecture-description.(pdf|pptx)`
  - Lab protocols: `module-N-lab-M-description.md`
  - Study guides: `module-N-study-guide.(md|pdf)`
  - Quizzes: `module-N-quiz.(md|pdf)`

### Required Structure

- Module directory must contain:
  - `README.md` file
  - `AGENTS.md` file
  - `assignments/` directory

### File Extensions

- Only specified extensions are allowed for course materials
- Required files (README.md, AGENTS.md) are exempt from naming checks

## Error Handling

- Returns structured error information in validation results
- Continues validation even when individual checks fail
- Provides detailed recommendations for fixing issues
