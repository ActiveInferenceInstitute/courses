# Published Outputs — Agent Guidelines

> **Quick Navigation**: [← Repository Root](../AGENTS.md) | [Software Engine](../software/AGENTS.md)

## Purpose

This directory contains **rendered outputs** produced by the publishing pipeline
(`publish.py` / `scripts/generate_all_outputs.py`) from source curricula in
[`course_development/`](../course_development/AGENTS.md). It is a generated artifact
tree, not a source directory.

## Critical Rules

### 1. Never Hand-Edit

Files here are generated artifacts. Manual edits will be overwritten or lost on the
next pipeline run. To change any published content:

1. Edit the source in `course_development/`.
2. Re-run the pipeline: `python publish.py` (repo root) or
   `uv run python scripts/generate_all_outputs.py --course <ID>` (from `software/`).

### 2. Source of Truth

The source of truth is always `course_development/`. If a published file is wrong,
fix the source module, not the generated output.

### 3. Layout

One top-level directory per course ID (as registered in `COURSE_REGISTRY` in
`software/src/batch_processing/config.py`), plus the `youtube/` transcript archive:

```text
published/
├── active-inference/   # Consolidated core (units -> modules)
├── ai-philosophy/      # Individual track / level / domain courses
├── ...
└── youtube/            # Rendered YouTube transcript archive
```

Rendered formats per module include PDF, DOCX, HTML, TXT, MD (and MP3 when
`[formats] mp3` is enabled in `publish.toml`), plus `dashboard.html` and per-element
`output/` subdirectories.

### 4. Clean Before Publish

`publish.toml` sets `clean_before_publish = true` by default: the pipeline clears
`published/` before regenerating, so stale renderings are removed automatically.

---

*Minimize surprise. Maximize evidence.*
