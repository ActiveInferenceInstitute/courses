# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Course rendering and publishing pipeline for the **Active Inference Institute**. Transforms Markdown course content into multiple output formats (PDF, HTML, DOCX, TXT, MD, MP3). Uses `uv` for dependency management and Python 3.11+.

## Commands

All `software/` commands use `uv run` from the `software/` directory:

```bash
# Install dependencies
cd software && uv sync

# Run all tests (with coverage)
cd software && uv run pytest tests/ -v

# Run a single test file
cd software && uv run pytest tests/test_batch_processing_main.py -v

# Run tests matching a keyword
cd software && uv run pytest tests/ -k "test_name_pattern"

# Lint
cd software && uv run ruff check src/

# Format
cd software && uv run ruff format src/ scripts/

# Type check
cd software && uv run mypy src/

# Render a single course (fast: txt+md only)
cd software && uv run python scripts/generate_all_outputs.py --course ai-philosophy --formats txt,md

# Full publish pipeline (from repo root)
python publish.py

# Dry run (preview without generating)
python publish.py --dry-run
```

## Architecture

### Two-level entry points

1. **Repo root**: `publish.py` reads `publish.toml` to orchestrate the full pipeline
2. **software/**: `scripts/generate_all_outputs.py` is the main CLI for rendering courses

### COURSE_REGISTRY (central configuration)

Defined in `software/src/batch_processing/config.py`. Maps course IDs (e.g., `ai-philosophy`) to structural metadata: paths, glob patterns, content file lists. All module discovery flows through this registry — no hardcoded paths.

### Script Count

- 23 CLI scripts in `scripts/`
- 21 modules in `src/`
- 67 test files in `tests/`

### Module layering

Software modules in `software/src/` follow strict dependency layers:

- **Layer 0** (independent): `module_organization`, `file_validation`, `publish`, `content_processing`, `validation`, `lab_manual`, `legacy_import`, `course_config`
- **Layer 1** (core converters): `markdown_to_pdf`, `text_to_speech`, `speech_to_text`
- **Layer 2** (format): `format_conversion`
- **Layer 3** (orchestration): `batch_processing`, `html_website`, `schedule`, `course_generator`, `youtube_transcript`
- **Layer 4** (pipeline): `canvas_integration`

Each module follows the pattern: `__init__.py`, `main.py` (public API), `utils.py` (internals), `config.py` (constants).

### course_generator module

Schema-driven curriculum generation with optional LLM enrichment via Ollama. Separate from the rendering pipeline — generates course structures rather than rendering them.

### Content flow

Source markdown in `course_development/` is rendered through the pipeline to `published/`. Each Active Inference module contains `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`, and `dashboard.html`.

## Key Conventions

- **No mocks in tests.** All tests use real implementations — real file operations, real library calls. This is a strict policy enforced across the codebase (see `.cursorrules` files).
- **uv-first.** Always use `uv run` for commands, never bare `python`.
- **Line length: 100** (ruff and mypy).
- **Type hints required** on all functions (`mypy --disallow-untyped-defs`).
- **Test markers**: `requires_internet` and `requires_api` for tests needing external access.
- **PDF generation** requires system libraries: `brew install cairo pango gdk-pixbuf glib` (macOS).

## Course IDs

- **Active Inference Core**: `ai-philosophy`, `ai-cognitive-science`, `ai-math`, `ai-computer-science`
- **Level-Adapted**: `ai-es` (elementary), `ai-family`, `ai-ms` (middle school), `ai-hs` (high school), `ai-101` (college intro), `ai-401` (advanced PhD)
- **Domain**: `ai-embodied`, `ai-organizations`, `ai-robotics`, `ai-crochet`, `ai-inventions`, `ai-metallurgy`, `ai-comedy` — Domain-specific
- **Archive**: `youtube` (transcript archive, ~821 videos / 38 playlists)
