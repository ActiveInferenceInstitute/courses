# Scripts

> **Navigation**: [← README](../README.md) | [AGENTS.md](../AGENTS.md) | [docs/](../docs/) | [src/](../src/)

Thin CLI orchestrators for course material generation and publishing. All business logic resides in `src/` modules; scripts handle CLI parsing and orchestration only.

---

## Thin Orchestrator Pattern

Scripts follow the "thin orchestrator" pattern:

```
Script (CLI parsing) → Module (business logic) → Output
```

Scripts do NOT contain business logic. They:

1. Parse command-line arguments
2. Call module functions from `src/`
3. Report results

---

## Script-to-Module Mapping

| Script | Primary Module(s) | Purpose |
|--------|-------------------|---------|
| `publish_all.py` | `batch_processing`, `publish`, `validation` | **Top-level pipeline** |
| `generate_all_outputs.py` | `batch_processing` | Generate all course outputs |
| `generate_module_renderings.py` | `batch_processing` | Single module processing |
| `generate_module_website.py` | `html_website` | Website generation |
| `generate_syllabus_renderings.py` | `schedule`, `batch_processing` | Syllabus processing |
| `publish_course.py` | `publish` | Publish to PUBLISHED/ |
| `validate_outputs.py` | `validation` | Validate generated outputs |
| `flatten_published.py` | `publish.utils` | Flatten directory structure |
| `renumber_questions.py` | `content_processing` | Question renumbering |
| `import_legacy_materials.py` | `legacy_import` | Import legacy format |
| `fix_stub_labs.py` | `content_processing` | Generate labs from module content |
| `fix_stub_quizzes.py` | `content_processing` | Generate quizzes from module content |
| `fix_stub_questions.py` | `content_processing` | Generate study questions from module content |

---

## Primary Scripts

### `publish_all.py` — Top-Level Pipeline

The main orchestrator that runs the complete publish pipeline:

1. **Generate** → Create all output formats (PDF, DOCX, HTML, TXT, MD, MP3)
2. **Publish** → Copy to PUBLISHED/ directory
3. **Validate** → Verify all outputs

```bash
# Full publish (~17 min with MP3)
uv run python scripts/publish_all.py --clean --verbose

# Skip MP3 for faster iteration (~5 min)
uv run python scripts/publish_all.py --clean --skip-mp3

# PDF-only for quick testing
uv run python scripts/publish_all.py --clean --formats pdf

# Specific course only
uv run python scripts/publish_all.py --course biol-8

# Dry run (preview only)
uv run python scripts/publish_all.py --dry-run
```

| Option | Description |
|--------|-------------|
| `--clean` | Clear outputs before generation |
| `--verbose` | Detailed progress output |
| `--skip-mp3` | Skip audio generation |
| `--formats` | Comma-separated list: pdf,docx,html,txt,md,mp3 |
| `--course` | Specific course: biol-1, biol-8, or all |
| `--dry-run` | Preview without executing |

---

### `generate_all_outputs.py` — Course Output Generation

Generate all output formats for modules in a course:

```bash
# Generate for one course
uv run python scripts/generate_all_outputs.py --course biol-8

# Generate for specific module
uv run python scripts/generate_all_outputs.py --course biol-1 --module 1

# All courses, all modules
uv run python scripts/generate_all_outputs.py --course all

# Dry run
uv run python scripts/generate_all_outputs.py --course biol-8 --dry-run
```

| Option | Description |
|--------|-------------|
| `--course` | Required: biol-1, biol-8, or all |
| `--module` | Optional: specific module number |
| `--formats` | Output formats (default: all) |
| `--dry-run` | Preview without generating |
| `--skip-clear` | Don't clear existing outputs |
| `--no-website` | Skip website generation |
| `--skip-labs` | Skip lab manual rendering |

**Module Used**: `src/batch_processing`

---

### `publish_course.py` — Publish to PUBLISHED/

Copy generated outputs to the PUBLISHED directory:

```bash
# Publish all courses
uv run python scripts/publish_course.py --course all

# Publish specific course
uv run python scripts/publish_course.py --course biol-8
```

| Option | Description |
|--------|-------------|
| `--course` | Required: biol-1, biol-8, or all |

**Module Used**: `src/publish`

---

### `validate_outputs.py` — Output Validation

Validate that generated outputs meet quality standards:

```bash
# Validate all courses
uv run python scripts/validate_outputs.py --course all

# Validate specific course
uv run python scripts/validate_outputs.py --course biol-8

# Verbose output
uv run python scripts/validate_outputs.py --course all --verbose
```

| Option | Description |
|--------|-------------|
| `--course` | Required: biol-1, biol-8, or all |
| `--verbose` | Detailed validation output |

**Module Used**: `src/validation`

---

## Single-Item Scripts

### `generate_module_renderings.py` — Single Module Processing

Process one module:

```bash
uv run python scripts/generate_module_renderings.py /path/to/module-01 --formats pdf,docx
```

| Option | Description |
|--------|-------------|
| `path` | Required: path to module directory |
| `--formats` | Output formats (default: all) |
| `--output-dir` | Custom output directory |

**Module Used**: `src/batch_processing`

---

### `generate_module_website.py` — Website Generation

Generate interactive HTML website for a module:

```bash
uv run python scripts/generate_module_website.py /path/to/module-01
```

| Option | Description |
|--------|-------------|
| `path` | Required: path to module directory |
| `--output-dir` | Custom output directory |
| `--course-name` | Course name for display |

**Module Used**: `src/html_website`

---

### `generate_syllabus_renderings.py` — Syllabus Processing

Generate outputs for syllabus files:

```bash
uv run python scripts/generate_syllabus_renderings.py /path/to/Schedule.md
```

| Option | Description |
|--------|-------------|
| `path` | Required: path to schedule file or directory |
| `--formats` | Output formats (default: all) |
| `--output-dir` | Custom output directory |

**Module Used**: `src/schedule`, `src/batch_processing`

---

## Utility Scripts

### `flatten_published.py` — Flatten Directory Structure

Move files from subdirectories to module root for simpler distribution:

```bash
# Flatten all published content
uv run python scripts/flatten_published.py

# Dry run
uv run python scripts/flatten_published.py --dry-run

# Verbose
uv run python scripts/flatten_published.py --verbose
```

| Option | Description |
|--------|-------------|
| `--dry-run` | Preview without modifying |
| `--verbose` | Show each file operation |

**Module Used**: `src/publish.utils.flatten_published`

---

### `renumber_questions.py` — Question Renumbering

Convert section-based question numbering to continuous numbering:

```bash
# Process all courses
uv run python scripts/renumber_questions.py --course all

# Specific course
uv run python scripts/renumber_questions.py --course biol-1

# Dry run
uv run python scripts/renumber_questions.py --course biol-8 --dry-run
```

Before: `1.`, `2.`, `3.` per section
After: `1.`, `2.`, `3.`, `4.`, `5.`... continuously

**Module Used**: `src/content_processing`

---

## Migration Scripts

### `import_legacy_materials.py` — Legacy Import

Import materials from legacy bio_1_2025 format:

```bash
uv run python scripts/import_legacy_materials.py /path/to/legacy --course biol-1
```

| Option | Description |
|--------|-------------|
| `source_path` | Required: path to legacy materials |
| `--course` | Target course directory |
| `--dry-run` | Preview without importing |

**Module Used**: `src/legacy_import`

---

## Output Formats

| Format | Extension | Description | Generator |
|--------|-----------|-------------|-----------|
| PDF | `.pdf` | Print-ready document | WeasyPrint |
| DOCX | `.docx` | Microsoft Word format | python-docx |
| HTML | `.html` | Web page | Markdown + custom |
| MP3 | `.mp3` | Audio narration | gTTS |
| TXT | `.txt` | Plain text extraction | Markdown strip |
| MD | `.md` | Markdown copy (prefixed) | Copy + rename |

---

## Naming Convention

Output files are prefixed with module name for unique identification:

```
module-01-questions.pdf       (not questions.pdf)
module-01-keys-to-success.mp3 (not keys-to-success.mp3)
module-01-assignment-01.docx  (not assignment-01.docx)
```

This ensures files remain identifiable when distributed or combined.

---

## Dependencies

### System Libraries (macOS)

```bash
# Required for PDF/DOCX generation
brew install cairo pango gdk-pixbuf glib

# Set library path (add to ~/.zshrc for persistence)
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
```

### Python Dependencies

All managed via `uv` and `pyproject.toml`:

```bash
cd software
uv sync
```

---

## Logging

Logs are written to `software/logs/generation_YYYY-MM-DD_HH-MM-SS.log`.

Each run creates a new timestamped log file with:

- Start/end times
- Files processed
- Errors encountered
- Summary statistics

---

## Related Documentation

| Document | Description |
|----------|-------------|
| [../docs/QUICKSTART.md](../docs/QUICKSTART.md) | Installation and quick commands |
| [../docs/ORCHESTRATION.md](../docs/ORCHESTRATION.md) | Multi-module workflows |
| [../src/README.md](../src/README.md) | Source module overview |
| [../src/AGENTS.md](../src/AGENTS.md) | Module API reference |
