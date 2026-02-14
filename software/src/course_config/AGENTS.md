# specialized-agent: course_config

> **Purpose**: Provides layered TOML-based configuration for courses.
> **Key Function**: `load_course_config(course_path, repo_root)`

## Overview

The `course_config` module implements a hierarchical configuration system that merges TOML files from the bottom up. This allows for global defaults, curriculum-level overrides, course-level settings, and module-specific configurations.

The hierarchy is:
`DEFAULT_CONFIG` <- `curriculum.toml` <- `course.toml` <- `module.toml`

## Public API

### `load_course_config(course_path: Path, repo_root: Path) -> Dict[str, Any]`

Walks from `course_path` up to the `course_development/` boundary, collecting all `course.toml` files and merging them.

- **Args**:
  - `course_path`: Path to a course or module directory.
  - `repo_root`: Root path of the repository.
- **Returns**: Merged configuration dict.

### Configuration Accessors

- `get_rendering_config(config) -> Dict`: Extract rendering settings.
- `get_metadata(config) -> Dict`: Extract course metadata.
- `get_localization(config) -> Dict`: Extract localization settings.
- `get_tts_settings(config) -> Dict`: Extract Text-to-Speech settings (`lang`, `slow`, `speed`).
- `get_pdf_css(config) -> Optional[str]`: Get custom CSS path for PDF rendering.
- `get_enabled_formats(config) -> List[str]`: Get list of enabled output formats (e.g., `['pdf', 'html']`).
- `is_format_enabled(config, fmt) -> bool`: Check if a specific format is enabled.

## Configuration Structure

Example `course.toml`:

```toml
[metadata]
title = "My Course"
perspective = "Engineering"

[rendering]
pdf = { enabled = true, css_file = "custom.css" }
audio = { enabled = true, lang = "en", speed = 1.1 }
html = { enabled = true }
```

## Dependencies

- **Internal**: `config.py` (defaults), `utils.py` (merging logic).
- **External**: `tomli` (implicit via utils).
