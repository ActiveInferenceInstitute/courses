# Scripts

> **Navigation**: [← README](../README.md) | [AGENTS.md](../AGENTS.md) | [docs/](../docs/) | [src/](../src/)

Thin CLI orchestrators for course material generation and publishing. All business logic resides in `src/` modules; scripts handle CLI parsing and orchestration only. This directory contains **23 scripts** — see [docs/CLI_REFERENCE.md](../docs/CLI_REFERENCE.md) for the complete reference with verified options.

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
| `generate_dashboards.py` | `content_processing` | Dashboard generation |
| `publish_course.py` | `publish` | Publish to PUBLISHED/ |
| `flatten_published.py` | `publish.utils` | Flatten directory structure |
| `validate_outputs.py` | `validation` | Validate generated outputs |
| `scan_modules.py` | `content_processing.structure_scan` | Scan for missing files |
| `fix_structural_issues.py` | — (standalone) | Fix directory structure issues |
| `renumber_questions.py` | `content_processing` | Question renumbering |
| `import_legacy_materials.py` | `legacy_import` | Import legacy format |
| `fix_stub_labs.py` | `content_processing` | Generate labs from module content |
| `fix_stub_quizzes.py` | `content_processing` | Generate quizzes from module content |
| `fix_stub_questions.py` | `content_processing` | Generate study questions from module content |
| `transcribe_youtube.py` | `youtube_transcript` | YouTube transcription |
| `render_youtube_courses.py` | `youtube_transcript`, `batch_processing` | YouTube course rendering |
| `translate_course.py` | `translation` | Course translation |
| `translate_youtube.py` | `translation` | YouTube translation |
| `translate_published.py` | `translation` | Published-output translation |
| `summarize_courses.py` | `llm` | LLM course summaries |
| `verify_no_mocks.py` | — (policy checker) | Enforce no-mocks policy in tests |

---

## Primary Scripts

### `publish_all.py` — Top-Level Pipeline

The main orchestrator that runs the complete publish pipeline:

1. **Generate** → Create all output formats (PDF, DOCX, HTML, TXT, MD, MP3)
2. **Publish** → Copy to PUBLISHED/ directory
3. **Validate** → Verify all outputs

```bash
# Full publish
uv run python scripts/publish_all.py --clean --verbose

# Specific course
uv run python scripts/publish_all.py --course ai-philosophy

# Dry run (preview only)
uv run python scripts/publish_all.py --dry-run
```

| Option | Description |
|--------|-------------|
| `--clean` | Clear outputs before generation |
| `--verbose` | Detailed progress output |
| `--formats` | Comma-separated list: pdf,docx,html,txt,md,mp3 |
| `--course` | Specific registered course ID, or `all` |
| `--dry-run` | Preview without executing |

---

### `generate_all_outputs.py` — Course Output Generation

Generate all output formats for modules in a course:

```bash
# Generate for one course
uv run python scripts/generate_all_outputs.py --course ai-philosophy

# Generate for specific module
uv run python scripts/generate_all_outputs.py --course ai-philosophy --module 1

# All courses, all modules
uv run python scripts/generate_all_outputs.py --course all

# Dry run
uv run python scripts/generate_all_outputs.py --course ai-philosophy --dry-run
```

| Option | Description |
|--------|-------------|
| `--course` | Registered course ID (see `COURSE_REGISTRY`), or `all` |
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
uv run python scripts/publish_course.py --course ai-philosophy
```

| Option | Description |
|--------|-------------|
| `--course` | Registered course ID, or `all` |

**Module Used**: `src/publish`

---

### `validate_outputs.py` — Output Validation

Validate that generated outputs meet quality standards:

```bash
# Validate all courses
uv run python scripts/validate_outputs.py --course all

# Validate specific course
uv run python scripts/validate_outputs.py --course ai-philosophy

# Verbose output
uv run python scripts/validate_outputs.py --course all --verbose
```

| Option | Description |
|--------|-------------|
| `--course` | Registered course ID, or `all` |
| `--verbose` | Detailed validation output |

**Module Used**: `src/validation`

---

## Single-Item Scripts

### `generate_module_renderings.py` — Single Module Processing

Process one module of a course:

```bash
uv run python scripts/generate_module_renderings.py --course ai-philosophy --module 1
```

| Option | Description |
|--------|-------------|
| `--course` | Registered course ID (required) |
| `--module` | Module number (default: 1) |

**Module Used**: `src/batch_processing`

---

### `generate_module_website.py` — Website Generation

Generate interactive HTML website for a module:

```bash
uv run python scripts/generate_module_website.py --course ai-philosophy --module 1
```

| Option | Description |
|--------|-------------|
| `--course` | Registered course ID (required) |
| `--module` | Module number (default: 1) |

**Module Used**: `src/html_website`

---

### `generate_syllabus_renderings.py` — Syllabus Processing

Generate outputs for syllabus files of a course:

```bash
uv run python scripts/generate_syllabus_renderings.py --course ai-philosophy
```

| Option | Description |
|--------|-------------|
| `--course` | Registered course ID (default: `ai-philosophy`) |

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
| `--path` | PUBLISHED directory (default: auto-detect) |
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
uv run python scripts/renumber_questions.py --course ai-philosophy

# Dry run
uv run python scripts/renumber_questions.py --course ai-philosophy --dry-run
```

Before: `1.`, `2.`, `3.` per section
After: `1.`, `2.`, `3.`, `4.`, `5.`... continuously

**Module Used**: `src/content_processing`

---

### `verify_no_mocks.py` — No-Mocks Policy Enforcement

Scans `tests/` for prohibited mock/stub patterns (`unittest.mock`, `MagicMock`,
`patch()`, etc.) and exits non-zero if any are found. Runs in CI and as a
pre-commit hook.

```bash
uv run python scripts/verify_no_mocks.py    # from software/
python software/scripts/verify_no_mocks.py  # from repo root
```

**Note**: pytest's `monkeypatch` fixture is intentionally allowed — it sets
env vars / cwd / sys.path and does not create mock objects.

---

## Migration Scripts

### `import_legacy_materials.py` — Legacy Import

Import materials from a legacy course archive into the standardized structure:

```bash
uv run python scripts/import_legacy_materials.py --course ai-philosophy
uv run python scripts/import_legacy_materials.py --dry-run
uv run python scripts/import_legacy_materials.py --skip-questions
```

| Option | Description |
|--------|-------------|
| `--course` | Course to import into (registered ID) |
| `--dry-run` | Preview without importing |
| `--skip-questions` | Skip chapter questions |
| `--skip-slides` | Skip slides |

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
| [../docs/CLI_REFERENCE.md](../docs/CLI_REFERENCE.md) | Complete CLI reference (all 23 scripts) |
| [../docs/QUICKSTART.md](../docs/QUICKSTART.md) | Installation and quick commands |
| [../docs/ORCHESTRATION.md](../docs/ORCHESTRATION.md) | Multi-module workflows |
| [../src/README.md](../src/README.md) | Source module overview |
| [../src/AGENTS.md](../src/AGENTS.md) | Module API reference |
