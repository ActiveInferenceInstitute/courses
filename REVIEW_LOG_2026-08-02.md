# REVIEW_LOG — 2026-08-02

**Repo:** ActiveInferenceInstitute/courses
**Branch:** main (origin/main) @ 2cb7883b
**Pass:** Mega-deep documentation review + implementation (docs-deep)
**Reviewer:** Hermes Agent (fleet docs pass)

---

## Phase 0 — Preflight

- `git fetch origin` + fast-forward pull: already up to date on `main` (HEAD 2cb7883b).
- Inventory: 35,410 tracked files; root docs (`README.md`, `AGENTS.md`, `CLAUDE.md`,
  `CONTRIBUTING.md`, `CHANGELOG.md`, `TODO.md`, `LICENSE`); `software/docs/` (17 files);
  `software/` README + AGENTS + per-module AGENTS.md (21 modules); `course_development/`
  README + AGENTS tree (14 courses); `.github/workflows/ci.yml`; `.aii/config.yaml`;
  `.agents/skills/courses/SKILL.md`.
- Ground truth established by direct measurement:
  - 23 CLI scripts in `software/scripts/`
  - 21 source modules in `software/src/` (dirs with `main.py`; excludes `__pycache__`)
  - 17 files in `software/docs/`
  - 19 entries in `COURSE_REGISTRY` (`software/src/batch_processing/config.py`)
  - 14 courses / 58 units / 464 topic modules
  - 67 test files; 1,014 tests collected; ~995 CI-passing; 34 deselected; ~75% source coverage
  - YouTube archive: 38 playlists / 821 videos (per `youtube_courses.json`) / 791 `module.md`
  - 6,463 `.md` files under `course_development/`
  - Python >= 3.11, uv-based, ruff lint+format (CI uses `ruff format --check`, not black)

## Phase 1 — Findings (summary; full detail in TODO.md)

- **Major:** CLI_REFERENCE.md omits 3 of 23 scripts; 5 broken copy-pasteable commands;
  nonexistent `validate_published_directory` in MODULES.md + ORCHESTRATION.md; 3 wrong
  function signatures in MODULES.md; YOUTUBE.md describes a fictional archive layout
  (`manifest.json`, `transcripts/`, `rendered/`); 7 per-module `src/*/AGENTS.md` files
  carry stale biology-repo references (biol-1/biol-8/bio_1_2025).
- **Medium:** stale counts ("17 courses", "22 scripts", "1,021 tests", "18 files",
  "~2,600 videos", "1020 tests passed", "65+ test files"); TRANSLATION.md wrong config
  defaults (`llama3.2` vs `gemma3:4b`, ~2,000 vs 4,096 tokens); layer-taxonomy conflict
  between MODULES.md and ARCHITECTURE.md; QUICKSTART.md runs `uv run` from repo root
  where no project exists; `publish.toml` missing `ai-comedy`; CONTRIBUTING.md "100%
  coverage" unenforced claim.
- **Minor:** CONTENT_AUTHORING.md endorses "Coming Soon" placeholders (conflicts with
  repo no-placeholder rule); TESTING.md references a nonexistent test node and an
  unconfigured `--cov-fail-under=70`; COURSE_CATALOG.md documents nonexistent
  `has_course_subdir` registry field; root AGENTS.md says "All 10 courses" (now 14);
  CLAUDE.md instructs `black` (repo uses ruff format); .agents SKILL.md stale counts.

## Phase 3 — Implemented

Two commits (docs-only; no runtime code changed):

- **f4789c39** — `docs: reconcile software/docs to measured repo reality`
  - software/docs: 17 files touched. Stale counts fixed (18→17 files, 22→23 scripts,
    17→14 courses, 1,021→1,014 tests, 65+→67 test files, ~2,600→~821 YouTube videos).
  - CLI_REFERENCE.md rewritten: all 23 scripts documented (added flatten_published.py,
    import_legacy_materials.py, verify_no_mocks.py); every example command verified
    against argparse definitions and fixed (generate_module_renderings,
    generate_module_website, translate_course, translate_published).
  - MODULES.md: 9 signature corrections verified against src code; publish/validation
    moved to Layer 4 per ARCHITECTURE.md; nonexistent has_course_subdir removed.
  - ORCHESTRATION.md: process_course_modules call fixed (missing course_name);
    validate_published_directory → validate_published.
  - TRANSLATION.md: OLLAMA_MODEL gemma3:4b, chunk 4,096 tokens.
  - YOUTUBE.md: fictional manifest.json/transcripts/rendered layout replaced with real
    youtube_courses.json + per-playlist numbered-video-dir structure.
  - QUICKSTART.md: publish.py runs as plain python from repo root; course IDs now
    include ai-comedy and youtube.
  - CONTRIBUTING.md/TESTING.md/CONTENT_AUTHORING.md: unenforced coverage claims removed,
    nonexistent test node fixed, placeholder policy aligned.
  - publish.toml: ai-comedy toggle added (was registered but unconfigured).
  - youtube/AGENTS.md: video counts corrected.
- **2cedf6fe** — `docs: fix root docs, published/AGENTS.md, and biology-era drift in src docs`
  - Created published/AGENTS.md (fixes 2 dead links from root AGENTS.md; satisfies the
    "AGENTS.md at every level" rule).
  - Root AGENTS.md / README.md / CLAUDE.md: stale counts fixed; "All 10 courses" → 14;
    CLAUDE.md format command switched from black to ruff format (matches CI).
  - Removed biology-repo references (biol-1/biol-8/bio_1_2025) from 7 per-module
    src AGENTS.md docs; examples now use Active Inference course paths.
  - llm/AGENTS.md default model → gemma3:4b (matches llm/config.py).
  - .agents SKILL.md: 23 CLI entry points, complete 7-domain list, corrected command.
  - software/README.md + software/src/AGENTS.md: test counts reconciled.

Pending third commit: TESTING.md tables list the 4 previously undocumented test files;
TODO.md + REVIEW_LOG finalize the pass.

## Phase 4 — Verification

- Link re-check (all touched docs) — see final sweep below.
- No runtime code touched; publish.toml gained ai-comedy toggle (config only).
- Heavy test suite not run (CI-equivalent ~995 tests); noted as deferred in TODO.

---
*Minimize surprise. Maximize evidence.*
