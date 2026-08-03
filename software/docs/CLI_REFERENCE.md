# 💻 CLI Reference

> **Navigation**: [← Docs Index](README.md) | [Quick Start](QUICKSTART.md) | [Configuration](CONFIGURATION.md)

Complete reference for all **23 CLI scripts** in `software/scripts/`.

**Note**: Unless noted otherwise, all commands must be run from `software/` using `uv run`.
The repo-root `publish.py` is the exception — it runs as plain `python` from the repository root.

---

## 📑 Index

| Category | Scripts | Purpose |
| :--- | :--- | :--- |
| **[Rendering](#rendering)** | `generate_all_outputs.py`, `generate_module_renderings.py`, `generate_dashboards.py`, `generate_module_website.py`, `generate_syllabus_renderings.py` | Content generation |
| **[Publishing](#publishing)** | `publish.py`, `publish_all.py`, `publish_course.py`, `flatten_published.py` | Distribution |
| **[Validation](#validation)** | `validate_outputs.py`, `scan_modules.py`, `verify_no_mocks.py` | Quality control |
| **[Maintenance](#maintenance)** | `fix_structural_issues.py`, `renumber_questions.py`, `fix_stub_labs.py`, `fix_stub_questions.py`, `fix_stub_quizzes.py` | Content fixes |
| **[Import](#import)** | `import_legacy_materials.py` | Legacy migration |
| **[YouTube](#youtube)** | `transcribe_youtube.py`, `render_youtube_courses.py` | Video pipeline |
| **[Translation](#translation)** | `translate_course.py`, `translate_youtube.py`, `translate_published.py` | Localization |
| **[Utilities](#utilities)** | `summarize_courses.py` | Summaries |

---

## Rendering

### `generate_all_outputs.py`

The master rendering script. Processes one or all courses.

```bash
uv run python scripts/generate_all_outputs.py [OPTIONS]
```

- `--course <ID>`: Specific course (e.g., `ai-philosophy`, or `all`).
- `--module <N>`: Specific module number.
- `--formats <LIST>`: `txt,md,pdf,html,docx,mp3`.
- `--dry-run`: Preview actions.
- `--skip-clear`: Do not clear existing outputs.
- `--no-website`: Skip module website generation.

### `generate_module_renderings.py`

Render a specific module of a course (useful for fast dev loops).

```bash
uv run python scripts/generate_module_renderings.py --course ai-philosophy --module 1
```

- `--course <ID>`: Course to process (required; registered course IDs only).
- `--module <N>`: Module number to process (default: `1`).

### `generate_dashboards.py`

Generate the interactive `dashboard.html` for modules.

```bash
uv run python scripts/generate_dashboards.py --course <ID>
```

### `generate_module_website.py`

Generate a static `index.html` website for a module.

```bash
uv run python scripts/generate_module_website.py --course ai-philosophy --module 1
```

- `--course <ID>`: Course to process (required).
- `--module <N>`: Module number to process (default: `1`).

### `generate_syllabus_renderings.py`

Render syllabus files into PDF/HTML.

```bash
uv run python scripts/generate_syllabus_renderings.py --course ai-philosophy
```

- `--course <ID>`: Course to process (default: `ai-philosophy`).

---

## Publishing

### `publish.py` (Repo Root)

The top-level orchestrator. Reads `publish.toml`. Run from the **repository root** as plain `python`:

```bash
python publish.py --dry-run
python publish.py --course ai-101 --override-formats txt
```

### `publish_all.py`

The underlying script called by `publish.py`. Generates, publishes, and validates.

### `publish_course.py`

Publishes a single course, copying generated artifacts to `published/`.

```bash
uv run python scripts/publish_course.py --course ai-philosophy
```

### `flatten_published.py`

Flattens the `published/` directory structure (removes per-module subfolder nesting).

```bash
uv run python scripts/flatten_published.py            # auto-detect published/
uv run python scripts/flatten_published.py --dry-run  # preview only
uv run python scripts/flatten_published.py --path /custom/PUBLISHED
```

---

## Validation

### `validate_outputs.py`

Checks that `published/` contains valid files (non-empty, correct types).

```bash
uv run python scripts/validate_outputs.py --course ai-philosophy
```

### `scan_modules.py`

Scans `course_development/` for missing files (e.g., missing `lab.md`).

### `verify_no_mocks.py`

Enforces the repository's **No Mocks policy**: scans `tests/` for prohibited mock/stub
patterns (`unittest.mock`, `MagicMock`, `patch()`, etc.) and exits non-zero if any are found.

```bash
uv run python scripts/verify_no_mocks.py    # from software/
python software/scripts/verify_no_mocks.py  # from repo root
```

---

## Maintenance

### `fix_structural_issues.py`

Detects and attempts to fix common directory structure problems.

### `renumber_questions.py`

Renumbers study questions 1-20 continuously.

```bash
uv run python scripts/renumber_questions.py --course ai-philosophy
```

### `fix_stub_labs.py` / `fix_stub_questions.py` / `fix_stub_quizzes.py`

Generates real content for missing lab/quiz/question files (replacing template stubs).

```bash
uv run python scripts/fix_stub_labs.py --course ai-philosophy
```

---

## Import

### `import_legacy_materials.py`

Imports legacy-format materials into the standardized course structure.

```bash
uv run python scripts/import_legacy_materials.py --course ai-philosophy
uv run python scripts/import_legacy_materials.py --dry-run
uv run python scripts/import_legacy_materials.py --skip-questions
```

- `--course <ID>`: Course to import into.
- `--dry-run`: Preview what would be imported without importing.
- `--skip-questions` / `--skip-slides`: Skip importing chapter questions / slides.

---

## YouTube

### `transcribe_youtube.py`

Downloads audio and transcripts from YouTube channels/playlists.

```bash
uv run python scripts/transcribe_youtube.py --video-id <ID>
uv run python scripts/transcribe_youtube.py --whisper-model base
uv run python scripts/transcribe_youtube.py --list-only
```

- `--video-id <ID>`: Transcribe a single video.
- `--whisper-model <NAME>`: Use Whisper fallback (tiny, base, small, medium, large).
- `--list-only`: Enumerate videos only, save manifest.
- `--output <DIR>`: Output directory (default: `transcription/`).

### `render_youtube_courses.py`

Scaffolds course structures from YouTube playlists and renders them.

```bash
uv run python scripts/render_youtube_courses.py --list-playlists
uv run python scripts/render_youtube_courses.py --course active-inference-textbook-group --formats txt,md
uv run python scripts/render_youtube_courses.py --formats txt,md
```

- `--course <ID>`: Specific playlist/course.
- `--formats <LIST>`: Output formats.
- `--skip-scaffold`: Render existing courses only (no enumeration/scaffolding).
- `--force-scaffold`: Overwrite existing `module.md` files during scaffolding.

---

## Translation

### `translate_course.py`

Uses LLM to translate course content to target languages.

```bash
uv run python scripts/translate_course.py --course active-inference --lang es
```

- `--course <ID>`: Course to translate (required; registered course IDs only).
- `--lang <CODE>`: Target language code (required, e.g., `es`, `fr`, `de`).
- `--model <NAME>`: Ollama model override.

### `translate_youtube.py`

Translates YouTube transcripts.

```bash
uv run python scripts/translate_youtube.py --lang ja
```

### `translate_published.py`

Translates pre-published course outputs into target languages. Works on the `published/` directory structure.

```bash
uv run python scripts/translate_published.py --lang es
uv run python scripts/translate_published.py --course ai-philosophy --lang fr --dry-run
```

- `--course <ID>`: Published course directory name (default: `active-inference`).
- `--lang <CODE>`: Target language code (required).
- `--dry-run`: Preview without running the LLM.

---

## Utilities

### `summarize_courses.py`

Generates LLM-powered summaries of course content.

```bash
uv run python scripts/summarize_courses.py --course ai-philosophy
```

---

*Last Updated: 2026-08-02*
