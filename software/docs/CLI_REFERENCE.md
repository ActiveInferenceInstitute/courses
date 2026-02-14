# 💻 CLI Reference

> **Navigation**: [← Docs Index](README.md) | [Quick Start](QUICKSTART.md) | [Configuration](CONFIGURATION.md)

Complete reference for all **23 CLI scripts** in `software/scripts/`.

**Note**: All commands must be run from `software/` using `uv run`.

---

## 📑 Index

| Category | Scripts | Purpose |
| :--- | :--- | :--- |
| **[Rendering](#rendering)** | `generate_all_outputs.py`, `generate_module_renderings.py`... | Content generation |
| **[Publishing](#publishing)** | `publish_all.py`, `publish_course.py` | Distribution |
| **[Validation](#validation)** | `validate_outputs.py`, `scan_modules.py` | Quality control |
| **[Maintenance](#maintenance)** | `fix_structural_issues.py`, `renumber_questions.py`... | Content fixes |
| **[YouTube](#youtube)** | `transcribe_youtube.py`, `render_youtube_courses.py`... | Video pipeline |
| **[Translation](#translation)** | `translate_course.py`, `translate_youtube.py` | Localization |

---

## Rendering

### `generate_all_outputs.py`

The master rendering script. Processes one or all courses.

```bash
uv run python scripts/generate_all_outputs.py [OPTIONS]
```

- `--course <ID>`: Specific course (e.g., `ai-philosophy`).
- `--module <N>`: Specific module number.
- `--formats <LIST>`: `txt,md,pdf,html,docx,mp3`.
- `--dry-run`: Preview actions.

### `generate_module_renderings.py`

Render a specific module directory (useful for fast dev loops).

```bash
uv run python scripts/generate_module_renderings.py <PATH_TO_MODULE> --formats txt,md
```

### `generate_dashboards.py`

Generate the interactive `dashboard.html` for modules.

```bash
uv run python scripts/generate_dashboards.py --course <ID>
```

### `generate_module_website.py`

Generate a static `index.html` website for a module.

### `generate_syllabus_renderings.py`

Render syllabus files into PDF/HTML.

---

## Publishing

### `publish.py` (Repo Root)

The top-level orchestrator. Reads `publish.toml`.

```bash
python publish.py --dry-run
python publish.py --course ai-101 --override-formats txt
```

### `publish_all.py`

The underlying script called by `publish.py`. Generates, publishes, and validates.

### `publish_course.py`

Copies generated artifacts from the build cache to `published/`.

---

## Validation

### `validate_outputs.py`

Checks that `published/` contains valid files (non-empty, correct types).

```bash
uv run python scripts/validate_outputs.py --course ai-philosophy
```

### `scan_modules.py`

Scans `course_development/` for missing files (e.g., missing `lab.md`).

---

## Maintenance

### `fix_structural_issues.py`

Detects and attempts to fix common directory structure problems.

### `renumber_questions.py`

Renumbers study questions 1-20 continuously.

```bash
uv run python scripts/renumber_questions.py --course ai-philosophy
```

### `fix_stub_*.py`

Generates boilerplate content for missing files (`labs`, `quizzes`, `questions`).

---

## YouTube

### `transcribe_youtube.py`

Downloads audio and transcripts from YouTube channels/playlists.

```bash
uv run python scripts/transcribe_youtube.py --video-id <ID>
```

### `render_youtube_courses.py`

Turns transcript JSONs into readable Markdown/PDF course modules.

---

## Translation

### `translate_course.py`

Uses LLM to translate course content to target languages.

```bash
uv run python scripts/translate_course.py active-inference es
```

### `translate_youtube.py`

Translates YouTube transcripts.

---
*Last Updated: 2026-02-14*
