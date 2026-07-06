---
name: courses
version: "1.0.0"
description: >
  AI agent skill for the Active Inference Institute courses repository.
  Covers course content, the Python publishing engine, and CI/test infrastructure.
tags: [active-inference, courses, education, python, publishing]
platforms: [hermes, agentskills.io]
requires: [uv, python>=3.11]
---

# Courses Repository — Agent Skill

## What this repo is

The **ActiveInferenceInstitute/courses** repository contains:

- **14 courses** across levels (ES, Family, MS, HS, 101, Core, 401) and domains (metallurgy, robotics, organisations, embodied, inventions)
- **464 modules** following the 8-topic spine: Systems → Agents → Perception → Cognition → Action → Learning → Communication → Planning
- A **Python publishing engine** (`software/`) that renders Markdown + TOML course configs into PDF, DOCX, HTML, and audio artefacts
- A **YouTube transcript archive** and spoken-word generation pipeline
- **1,021 passing tests** — all real implementations, no mocks

## Directory map

```
courses/
├── course_development/      # Source curricula (Markdown + course.toml files)
├── published/               # Rendered outputs (generated, not hand-edited)
├── software/                # Python engine
│   ├── src/                 # 21 importable modules
│   ├── scripts/             # 22 CLI entry points
│   ├── tests/               # 1,021 tests
│   └── docs/                # Architecture, CONTRIBUTING, QUICKSTART, …
├── summaries/               # Auto-generated course summaries
├── publish.py               # Top-level pipeline entry point
└── publish.toml             # Publishing config: toggle courses, formats, options
```

## Key entry points

| Task | Command |
|------|---------|
| Install deps | `cd software && uv sync --extra dev` |
| Run all tests | `cd software && uv run pytest tests/ -v` |
| Publish one course | `uv run python scripts/generate_all_outputs.py --course active_inference` |
| Top-level publish | `python publish.py` |
| Lint | `cd software && uv run ruff check src/ scripts/` |
| Type check | `cd software && uv run mypy src/` |
| Verify no-mocks | `cd software && python scripts/verify_no_mocks.py` |

## How agents should work with this repo

### 1. Read before writing

Every directory has an `AGENTS.md` that explains its purpose, rules, and links to children. Always read the relevant `AGENTS.md` before editing.

### 2. No mocks, stubs, or fakes — ever

This is a hard policy. Test with real implementations, real temp files (use the `temp_dir` fixture), and real library calls. The `verify_no_mocks.py` script and CI enforce this.

### 3. Module structure in `src/`

Every module follows the three-file pattern:
- `main.py` — public API (the only file other modules may import from)
- `utils.py` — private helpers
- `config.py` — constants and schemas

### 4. The 8-topic spine is sacred

All courses must follow the same topic ordering in every unit. Do not add, remove, or reorder topics.

### 5. Audience-level gating

Match formalism, code, and lab style to the target audience level (see AGENTS.md for the table). Do not add calculus to the K-5 course.

### 6. Generated files

`published/` is generated. Never hand-edit files there. Re-run the publishing pipeline to update them.

## CI / pre-commit

- **GitHub Actions** (`.github/workflows/ci.yml`): lint → no-mocks → tests (py3.11 + py3.12)
- **pre-commit** (`.pre-commit-config.yaml`): ruff, ruff-format, mypy, no-mocks, standard hooks
- Install hooks: `pre-commit install` (from repo root)

## Adding a new course

1. Create `course_development/<slug>/course.toml` and module Markdown files
2. Register the slug in `src/batch_processing/config.py` → `COURSE_REGISTRY`
3. Enable in `publish.toml` (set to `false` initially if experimental)
4. Run `uv run python scripts/generate_all_outputs.py --course <slug>` to smoke-test
5. Add/extend tests in `tests/`

## Key docs

- `software/docs/QUICKSTART.md` — installation & first run
- `software/docs/ARCHITECTURE.md` — system design and module map
- `software/docs/CONTRIBUTING.md` — contribution rules (no-mocks policy, code standards)
- `software/docs/TESTING.md` — test patterns
- `software/docs/COURSE_CATALOG.md` — all courses at a glance
