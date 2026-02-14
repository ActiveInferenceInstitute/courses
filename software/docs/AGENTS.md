# Documentation Standards

> **Navigation**: [← README](README.md) | [Architecture](ARCHITECTURE.md) | [Contributing](CONTRIBUTING.md) | [Testing](TESTING.md)

Standards and processes for maintaining documentation in the Active Inference Institute course rendering pipeline.

---

## Documentation Map

### This Directory (`software/docs/`) — 18 files

**Getting Started:**

| File | Purpose | Audience |
|------|---------|----------|
| [README.md](README.md) | Documentation hub, module index | All |
| [QUICKSTART.md](QUICKSTART.md) | Installation, setup, commands | New users |
| [CONTENT_AUTHORING.md](CONTENT_AUTHORING.md) | Writing course content | Content authors |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Code standards, testing, new modules | Contributors |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Common issues and solutions | Everyone |

**Architecture and Design:**

| File | Purpose | Audience |
|------|---------|----------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | System design, COURSE_REGISTRY | Developers |
| [MODULES.md](MODULES.md) | API reference for all 21 modules | Developers |
| [ORCHESTRATION.md](ORCHESTRATION.md) | Multi-module workflows | Developers |
| [CONFIGURATION.md](CONFIGURATION.md) | All config files and schemas | Developers |

**Reference:**

| File | Purpose | Audience |
|------|---------|----------|
| [CLI_REFERENCE.md](CLI_REFERENCE.md) | Complete reference for all 21 scripts | Users/Developers |
| [COURSE_CATALOG.md](COURSE_CATALOG.md) | Full catalog of all 14+ courses | Everyone |
| [TESTING.md](TESTING.md) | Test suite guide (65+ test files) | Developers |
| [AGENTS.md](AGENTS.md) | Documentation standards (this file) | Contributors |

**Subsystems:**

| File | Purpose | Audience |
|------|---------|----------|
| [COURSE_GENERATOR.md](COURSE_GENERATOR.md) | Schema-driven curriculum generation | Developers |
| [DANVAS.md](DANVAS.md) | Self-hosted course management server | Instructors/Developers |
| [TRANSLATION.md](TRANSLATION.md) | LLM-based translation (11 languages) | Content authors |
| [YOUTUBE.md](YOUTUBE.md) | YouTube transcript pipeline | Developers |

### Source and Tests

| File | Purpose |
|------|---------|
| [src/README.md](../src/README.md) | Source code overview (21 modules) |
| [tests/README.md](../tests/README.md) | Test suite overview |
| [scripts/README.md](../scripts/README.md) | CLI scripts reference |

---

## Required Elements

### Every Document Must Include

1. **Navigation header** — links to related docs
2. **Purpose statement** — what this document covers
3. **Last Updated** date at the bottom

### Code Examples

- All examples must use `uv run` for running Python
- All examples must be tested and working
- Use Active Inference course paths (not biology) in examples
- Include both CLI and Python API examples where applicable

```bash
# CLI example
uv run python scripts/generate_all_outputs.py --course ai-philosophy --formats txt,md
```

```python
# Python API example
from src.batch_processing.main import process_module_by_type
result = process_module_by_type("path/to/module", "path/to/output")
```

---

## Module Documentation Format

Each module (`src/module_name/`) should have:

### 1. Scope and Purpose

```markdown
## Purpose

Brief description of what this module does.

## What This Module Does

- Feature 1
- Feature 2

## What This Module Does NOT Do

- Out-of-scope items
```

### 2. Dependencies

```markdown
## Dependencies

### Internal (other modules)
- `module_name`: purpose

### External (libraries)
- `library_name`: purpose and version

### System
- System tools required (e.g., Cairo for PDF)
```

### 3. Public API

Document all functions in `main.py`:

```markdown
## Public API

### `function_name(param1: type, param2: type) -> return_type`

Description of what this function does.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `param1` | `str` | Description |
| `param2` | `int` | Description |

**Returns:** Description of return value

**Raises:** `ValueError` when input is invalid

**Example:**
```python
from src.module.main import function_name
result = function_name("arg1", 42)
```

```

---

## Style Guidelines

### Markdown

- Use ATX headers (`#`, `##`, `###`)
- One blank line between sections
- Code blocks with language specifiers
- Tables for structured data
- Relative paths for internal links

### Naming

- Files: `UPPERCASE.md` for top-level docs
- Headers: Title Case for H1, Sentence case for H2+
- Functions: `snake_case`
- Classes: `PascalCase`

### Links

```markdown
# Internal (relative)
[Quick Start](QUICKSTART.md)
[config.py](../src/batch_processing/config.py)

# Anchored
[Section](#section-name)
```

---

## Quality Standards

### Accuracy

- [ ] All code examples are tested and working
- [ ] Function signatures match actual implementation
- [ ] Course references use Active Inference (not biology)
- [ ] All commands use `uv run`
- [ ] Paths reference `published/` (not `PUBLISHED/`)

### Completeness

- [ ] All public functions documented
- [ ] All parameters described
- [ ] Error conditions documented
- [ ] Common use cases covered

### Clarity

- [ ] No jargon without explanation
- [ ] Examples progress from simple to complex
- [ ] Cross-references to related docs

---

## Testing Standards

### Naming Convention

```
tests/test_{module_name}_{submodule}.py
```

### Test Structure

```python
class TestFunctionName:
    """Tests for function_name."""

    def test_function_name_success(self, temp_dir):
        """Test normal operation."""
        result = function_name(valid_input)
        assert result["key"] == expected_value

    def test_function_name_error(self, temp_dir):
        """Test error handling."""
        with pytest.raises(ValueError):
            function_name(invalid_input)
```

### Running Tests

```bash
# All tests
uv run pytest tests/ -v

# Specific module
uv run pytest tests/test_batch_processing_main.py -v

# With coverage
uv run pytest tests/ --cov=src --cov-report=html
```

---

## Documentation Checklist

### New Document

- [ ] Navigation header with links
- [ ] Purpose statement
- [ ] Proper heading hierarchy
- [ ] Code blocks with language specifiers
- [ ] Working code examples using `uv run`
- [ ] Cross-references to related docs
- [ ] Last Updated date

### Document Update

- [ ] All affected examples updated
- [ ] Links still valid
- [ ] Statistics current
- [ ] Active Inference branding throughout
- [ ] Last Updated date bumped

---

*Last Updated: 2026-02-14*
