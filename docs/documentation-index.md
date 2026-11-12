# Documentation index

Flat index of the repository's long-lived documentation. Course-content guides
under `course_development/` (one `AGENTS.md` per unit and module, several
thousand files) are intentionally excluded: they are curriculum, not
repository documentation. Generated facts live in
[`_generated/`](_generated/README.md).

## Repository entry points

- **[README.md](../README.md)** — project overview, curriculum portfolio, status table.
- **[AGENTS.md](../AGENTS.md)** — root operating contract for agents.
- **[CLAUDE.md](../CLAUDE.md)** — Claude-specific repository instructions.
- **[CONTRIBUTING.md](../CONTRIBUTING.md)** — short contribution guide, pointing at the full one.
- **[TODO.md](../TODO.md)** — authoritative backlog.
- **[CHANGELOG.md](../CHANGELOG.md)** — notable changes.
- **[REVIEW_LOG_2026-08-02.md](../REVIEW_LOG_2026-08-02.md)** — point-in-time review record.

## Gate and CI

- **[docs/README.md](README.md)** — documentation hub and freshness rules.
- **[docs/RUN_GUIDE.md](RUN_GUIDE.md)** — the single gate entry point, `./run.sh`, and its arms.
- **[docs/documentation-index.md](documentation-index.md)** — this file.
- **[docs/AGENTS.md](AGENTS.md)** — rules for editing this directory.
- **[.github/workflows/ci.yml](../.github/workflows/ci.yml)** — the workflow; it calls the same `./run.sh` arms.
- **[.github/GNN.md](../.github/GNN.md)** — what the `gnn conformance (pinned)` job parses, and what it does not.
- **[.github/gnn-pin.json](../.github/gnn-pin.json)** — canonical GNN parser pin (`gnn-importer-pin/v1`).
- **[.pre-commit-config.yaml](../.pre-commit-config.yaml)** — local hooks (ruff, ruff-format, mypy, no-mocks).
- **[docs/_generated/GATE_METRICS.md](_generated/GATE_METRICS.md)** — generated counts and pin facts.
- **[docs/_generated/ARM_TIMINGS.md](_generated/ARM_TIMINGS.md)** — generated per-arm wall times and coverage.

## Engine documentation (`software/docs/`)

- **[README.md](../software/docs/README.md)** — engine documentation hub.
- **[QUICKSTART.md](../software/docs/QUICKSTART.md)** — install, sync, first render.
- **[CONTRIBUTING.md](../software/docs/CONTRIBUTING.md)** — code standards, no-mocks policy, module structure.
- **[TESTING.md](../software/docs/TESTING.md)** — test suite, markers, patterns.
- **[ARCHITECTURE.md](../software/docs/ARCHITECTURE.md)** — layered design and `COURSE_REGISTRY`.
- **[MODULES.md](../software/docs/MODULES.md)** — API reference for `software/src/`.
- **[ORCHESTRATION.md](../software/docs/ORCHESTRATION.md)** — multi-module workflows.
- **[PIPELINE.md](../software/docs/PIPELINE.md)** — end-to-end `publish.py` run and output layout.
- **[CONFIGURATION.md](../software/docs/CONFIGURATION.md)** — `publish.toml` and `pyproject.toml` schemas.
- **[CLI_REFERENCE.md](../software/docs/CLI_REFERENCE.md)** — every `software/scripts/*.py` entry point.
- **[COURSE_CATALOG.md](../software/docs/COURSE_CATALOG.md)** — registered courses and structure.
- **[COURSE_GENERATOR.md](../software/docs/COURSE_GENERATOR.md)** — schema-driven curriculum generation.
- **[CONTENT_AUTHORING.md](../software/docs/CONTENT_AUTHORING.md)** — writing modules, quizzes, labs.
- **[TRANSLATION.md](../software/docs/TRANSLATION.md)** — translation pipeline.
- **[DANVAS.md](../software/docs/DANVAS.md)** — the dashboard-canvas server.
- **[YOUTUBE.md](../software/docs/YOUTUBE.md)** — transcript and video pipeline.
- **[TROUBLESHOOTING.md](../software/docs/TROUBLESHOOTING.md)** — PDF, audio, and environment failures.
- **[AGENTS.md](../software/docs/AGENTS.md)** — documentation standards for the engine guides.

## Subsystem and folder guides

- **[software/README.md](../software/README.md)** — engine setup and dependency notes.
- **[software/AGENTS.md](../software/AGENTS.md)** — engine module reference for agents.
- **[software/src/README.md](../software/src/README.md)** — source layout.
- **[software/tests/README.md](../software/tests/README.md)** — test suite layout.
- **[software/scripts/README.md](../software/scripts/README.md)** — CLI script layout.
- **[course_development/README.md](../course_development/README.md)** — curriculum map.
- **[course_development/AGENTS.md](../course_development/AGENTS.md)** — curriculum authoring rules.
- **[published/AGENTS.md](../published/AGENTS.md)** — generated-output rules.
- **[summaries/AGENTS.md](../summaries/AGENTS.md)** — generated-summary rules.
- **[.aii/README.md](../.aii/README.md)** — InstituteOS sidecar metadata.
- **[.agents/skills/courses/SKILL.md](../.agents/skills/courses/SKILL.md)** — in-repo agent skill for this repository.

## Generated facts

- **[_generated/README.md](_generated/README.md)** — policy for the generated directory.
- **[_generated/GATE_METRICS.md](_generated/GATE_METRICS.md)** — counts, pin, exemplar total.
- **[_generated/ARM_TIMINGS.md](_generated/ARM_TIMINGS.md)** — measured arm wall times and coverage.
