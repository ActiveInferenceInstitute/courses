# Module Organization Technical Documentation

## Overview

Automated module structure creation and management utilities for course modules.

## Module Purpose

Create and manage standard module folder structures, validate module organization, and provide module statistics.

## Function Signatures

### Main Functions

**File**: `src/module_organization/main.py`

#### `create_module_structure(course_path: str, module_number: int) -> str`

Create standard module folder structure.

**Args**:
- `course_path`: Path to course directory
- `module_number`: Module number

**Returns**:
- Path to created module directory

**Raises**:
- `ValueError`: If course_path doesn't exist or module already exists
- `OSError`: If directory creation fails

**Creates**:
- Module directory: `course/module-{number}/`
- `assignments/` subdirectory
- `README.md` file
- `AGENTS.md` file
- `assignments/README.md` file
- `assignments/AGENTS.md` file

#### `validate_module_structure(module_path: str) -> bool`

Validate that module structure matches requirements.

**Args**:
- `module_path`: Path to module directory

**Returns**:
- True if structure is valid, False otherwise

**Checks**:
- Required files exist
- Required directories exist

#### `initialize_module_files(module_path: str, template: str) -> None`

Initialize module with template files.

**Args**:
- `module_path`: Path to module directory
- `template`: Template identifier (currently only "default" is supported)

**Raises**:
- `ValueError`: If module_path doesn't exist or template is invalid

#### `create_next_module(course_path: str) -> str`

Create the next module in sequence for a course.

**Args**:
- `course_path`: Path to course directory

**Returns**:
- Path to created module directory

**Raises**:
- `ValueError`: If course_path doesn't exist
- `OSError`: If directory creation fails

#### `list_course_modules(course_path: str) -> List[str]`

List all modules in a course.

**Args**:
- `course_path`: Path to course directory

**Returns**:
- List of module directory paths as strings, sorted by module number

**Raises**:
- `ValueError`: If course_path doesn't exist

#### `get_module_statistics(module_path: str) -> dict`

Get statistics about a module.

**Args**:
- `module_path`: Path to module directory

**Returns**:
- Dictionary with module statistics:
  - `module_number`: Module number (or None if cannot be extracted)
  - `total_files`: Total number of files
  - `total_directories`: Total number of directories
  - `assignment_count`: Number of assignment files
  - `has_readme`: Whether README.md exists
  - `has_agents`: Whether AGENTS.md exists
  - `is_valid`: Whether module structure is valid

**Raises**:
- `ValueError`: If module_path doesn't exist

### Utility Functions

**File**: `src/module_organization/utils.py`

#### `ensure_directory_exists(directory: Path) -> None`

Create directory if it doesn't exist.

#### `write_template_file(file_path: Path, template: str, **kwargs) -> None`

Write a template file with substitutions.

#### `get_module_path(course_path: Path, module_number: int) -> Path`

Get path to module directory.

**Returns**:
- Path: `course_path/course/module-{module_number}`

#### `check_file_exists(file_path: Path) -> bool`

Check if a file exists.

#### `check_directory_exists(directory_path: Path) -> bool`

Check if a directory exists.

#### `list_missing_files(module_path: Path, required_files: List[str]) -> List[str]`

List required files that are missing.

#### `list_missing_directories(module_path: Path, required_dirs: List[str]) -> List[str]`

List required directories that are missing.

#### `get_module_number_from_path(module_path: Path) -> int`

Extract module number from module directory path.

Handles both naming conventions:
- BIOL-1 style: `module-1`, `module-2`, `module-10`
- BIOL-8 style: `module-01-topic-name`, `module-02-chemistry-of-life`

**Returns**:
- Module number

**Raises**:
- `ValueError`: If module number cannot be extracted

#### `matches_module_number(dirname: str, target: int) -> bool`

Check if a directory name matches a target module number.

Handles both naming conventions:
- BIOL-1 style: `module-1`, `module-2`, `module-10`
- BIOL-8 style: `module-01-topic-name`, `module-02-chemistry-of-life`

**Args**:
- `dirname`: Directory name (e.g., "module-1" or "module-01-topic-name")
- `target`: Target module number to match

**Returns**:
- True if the directory matches the target module number

**Examples**:
```python
matches_module_number("module-1", 1)  # True
matches_module_number("module-01-exploring-life-science", 1)  # True
matches_module_number("module-10", 1)  # False
matches_module_number("module-1", 10)  # False
```

#### `find_module_path(course_path: Path, module_number: int) -> Optional[Path]`

Find the module directory for a given module number.

Searches for module directories matching the module number,
supporting both naming conventions (`module-N` and `module-NN-topic-name`).

**Args**:
- `course_path`: Path to course directory
- `module_number`: Module number to find

**Returns**:
- Path to module directory if found, None otherwise

**Note**: Use this function when you need to find an existing module.
Use `get_module_path()` when constructing a path for a new module.

#### `list_all_modules(course_path: Path) -> List[Path]`

List all module directories in a course.

**Returns**:
- List of module directory paths, sorted by module number

#### `get_next_module_number(course_path: Path) -> int`

Get the next available module number for a course.

**Returns**:
- Next available module number (1 if no modules exist)

## Configuration

**File**: `src/module_organization/config.py`

- `README_TEMPLATE`: Template for module README.md
- `AGENTS_TEMPLATE`: Template for module AGENTS.md
- `ASSIGNMENTS_README_TEMPLATE`: Template for assignments/README.md
- `ASSIGNMENTS_AGENTS_TEMPLATE`: Template for assignments/AGENTS.md
- `REQUIRED_FILES`: List of required files in each module
- `REQUIRED_DIRECTORIES`: List of required directories in each module

## Integration Points

### Dependencies on Other Modules

- **file_validation**: Module structure validation (`validate_assignment_name`)

### Used By

- Test orchestration workflows
- Module creation scripts
- Course setup automation

## Module Structure

Created modules follow this structure:

```
module-{number}/
├── README.md
├── AGENTS.md
└── assignments/
    ├── README.md
    └── AGENTS.md
```

## Error Handling

- Validates course path existence
- Prevents duplicate module creation
- Validates module number extraction
- Provides clear error messages
