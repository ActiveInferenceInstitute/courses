# TO-DO — courses repository backlog

**Status:** Active
**Owner:** Dr. Daniel Ari Friedman (docxology), Active Inference Institute
**Last reviewed:** 2026-08-02 (mega-deep documentation review + implementation pass)

**Section guide:**
- **Minor** = typo, broken link, formatting, single stale number
- **Medium** = stale section rewrite, doc restructure, added missing guide
- **Major** = large doc system overhaul, cross-cutting refactors

---

## Minor

- [x] ✓ `software/docs/AGENTS.md:11` "18 files" → 17 (actual file count). (f4789c39)
- [x] ✓ `software/docs/AGENTS.md:36` "all 22 scripts" → 23. (f4789c39)
- [x] ✓ `software/docs/AGENTS.md:37` "all 17 courses" → 14 courses. (f4789c39)
- [x] ✓ `software/docs/AGENTS.md:54` "21 modules" — verified correct (21 modules); no change.
- [x] ✓ `software/docs/README.md:39` "all 22 CLI scripts" → 23. (f4789c39)
- [x] ✓ `software/docs/README.md:42` "1,021+ test suite" → 1,014 collected / ~995 CI-passing / 34 deselected. (f4789c39)
- [x] ✓ `software/docs/README.md:43` "all 17 courses" → 14 courses. (f4789c39)
- [x] ✓ `ARCHITECTURE.md:119` "65+" test files → 67. (f4789c39)
- [x] ✓ `TESTING.md:14` "65+" → 67 test files. (f4789c39)
- [x] ✓ `TESTING.md:48` nonexistent test node `TestProcessModuleByType::test_success` → real node (`test_process_module_by_type_structure`). (f4789c39)
- [x] ✓ `TESTING.md:68` `--cov-fail-under=70` presented as project threshold — no threshold configured; reworded. (f4789c39)
- [x] ✓ `TESTING.md` tables now list the 4 previously undocumented test files (`test_*_extended.py` ×3, `test_youtube_render.py`). (pending commit)
- [x] ✓ `CONTENT_AUTHORING.md:120` "Coming Soon" placeholder endorsement → no-placeholder rule. (f4789c39)
- [x] ✓ `COURSE_CATALOG.md:248` `has_course_subdir` registry field — not a real key; removed. (f4789c39)
- [x] ✓ `QUICKSTART.md:76-79` course-ID list missing `ai-comedy` and `youtube`; added. (f4789c39)
- [x] ✓ `CLI_REFERENCE.md:157` `python -m scripts.translate_published` → `scripts/translate_published.py` convention. (f4789c39)
- [x] ✓ `ORCHESTRATION.md:5` "All examples use `uv run`" overstatement clarified (root `publish.py` runs bare `python`). (f4789c39)
- [x] ✓ `COURSE_GENERATOR.md:5/:39` — noted comedy/crochet have 5 units × 40 modules. (f4789c39)
- [x] ✓ `software/README.md:232` "1,021 tests collected" → 1,014 + CI-gate detail. (2cedf6fe)
- [x] ✓ `software/src/AGENTS.md:3` "Test Coverage: 1020 tests passed" → current reality. (2cedf6fe)
- [x] ✓ Root `AGENTS.md:7` "1,021 passing tests" → 1,014 (~995 CI, 34 deselected). (2cedf6fe)
- [x] ✓ Root `AGENTS.md:17` "21 modules, 22 scripts, 18 docs, 1,021 tests" → "21 modules, 23 scripts, 17 docs, 1,014 tests". (2cedf6fe)
- [x] ✓ Root `AGENTS.md:65` "All 10 courses" → "All 14 courses". (2cedf6fe)
- [x] ✓ `README.md:11` "17 total entries in COURSE_REGISTRY" → 19. (2cedf6fe)
- [x] ✓ `README.md` YouTube sub-claims corrected (171 livestreams, 142 GuestStreams — measured from `youtube_courses.json`). (2cedf6fe)
- [x] ✓ `CLAUDE.md:30` `uv run black` → `uv run ruff format`; `:86` "(black and ruff)" → "(ruff and mypy)"; `:58` 22→23 scripts. (2cedf6fe)
- [x] ✓ `.agents/skills/courses/SKILL.md` — 22→23 CLI entry points, complete domain list (7), `active_inference` → `active-inference` command. (2cedf6fe)
- [x] ✓ `course_development/README.md:128` ~2,600 → ~821 YouTube videos. (2cedf6fe)
- [x] ✓ `publish.toml` — added missing `ai-comedy` toggle; youtube count comment fixed. (f4789c39)

## Medium

- [x] ✓ Broken CLI examples fixed: `ORCHESTRATION.md:102` `process_course_modules` missing `course_name`; `ORCHESTRATION.md:170` `generate_module_website.py <path>` → `--course/--module`; `CLI_REFERENCE.md:44` `generate_module_renderings.py <PATH>` → `--course/--module`; `CLI_REFERENCE.md:145` `translate_course.py` positional → `--course/--lang`; `DANVAS.md:86` `pytest tests/test_danvas/` → real flat test files. (f4789c39)
- [x] ✓ `MODULES.md` signature drift fixed: `create_module_structure`, `upload_module_to_canvas`, `render_markdown_to_pdf`, `generate_speech`, `transcribe_audio`, `convert_file`, `generate_module_website`, `course_generator.generate`, `transcribe_channel`. (f4789c39)
- [x] ✓ `validate_published_directory` → `validate_published` in `MODULES.md` and `ORCHESTRATION.md`. (f4789c39)
- [x] ✓ Layer taxonomy reconciled: `publish`/`validation` moved to Layer 4 (matching ARCHITECTURE.md). (f4789c39)
- [x] ✓ `TRANSLATION.md:79` `OLLAMA_MODEL` default `llama3.2` → `gemma3:4b`; `:69` chunk "~2,000 tokens" → 4,096. (f4789c39)
- [x] ✓ `YOUTUBE.md` — "~2,600 videos" → 38 playlists / ~821 videos; `manifest.json` fiction → real `youtube_courses.json` + per-playlist numbered-video-dir structure. (f4789c39)
- [x] ✓ `COURSE_CATALOG.md:16/:177` "~2600 videos" → 38 playlists / ~821 videos. (f4789c39)
- [x] ✓ `CLI_REFERENCE.md` — all 23 scripts documented (added `flatten_published.py`, `import_legacy_materials.py`, `verify_no_mocks.py`). (f4789c39)
- [x] ✓ Created `published/AGENTS.md` (root AGENTS.md links were dead; repo rule requires AGENTS.md at every level). (2cedf6fe)
- [x] ✓ Biology-era drift removed from `src/*/AGENTS.md`: content_processing, html_website, legacy_import, module_organization, publish, schedule, validation (biol-1/biol-8/bio_1_2025 → Active Inference course examples). (2cedf6fe)
- [x] ✓ `llm/AGENTS.md` default model `llama3.2` → `gemma3:4b` (matches `llm/config.py`). (2cedf6fe)
- [x] ✓ `CONTRIBUTING.md:71` "100% test coverage" claim → measured reality (~75% source, no fail-under gate). (f4789c39)
- [x] ✓ `QUICKSTART.md:57-58` `uv run python publish.py` from repo root → `python publish.py --dry-run`. (f4789c39)
- [x] ✓ `course_development/youtube/AGENTS.md` — corrected playlist/video counts. (f4789c39)

## Major

- [x] ✓ **CLI_REFERENCE.md completeness** — all 23 scripts documented; every example command now copy-pasteable (verified against `argparse` definitions). (f4789c39)
- [x] ✓ **YOUTUBE.md archive rewrite** — replaced fictional `manifest.json`/`transcripts/`/`rendered/` layout with the real `youtube_courses.json` + per-playlist numbered-video-dir structure. (f4789c39)
- [x] ✓ **Cross-cutting stale-count sweep** — every numeric claim in root + software/docs + software developer docs now matches measured ground truth (see REVIEW_LOG_2026-08-02.md). (f4789c39, 2cedf6fe)
- [x] ✓ **published/AGENTS.md** — new doc for the generated-outputs directory, fixing 2 dead links from root AGENTS.md. (2cedf6fe)

## Open / deferred

- None from this pass.

### Maintenance pass — 2026-08-26 (lint/format/quality gate hardening)

- [x] `software/tests/` ruff findings (15) resolved: dead locals replaced with
  real assertions (`test_canvas_integration_main.py` upload-readiness,
  `test_format_conversion_utils.py` HTML content), dependency probes use
  `importlib.util.find_spec` (`test_dependencies.py`,
  `test_legacy_import_main*.py`), unused imports/vars removed
  (`test_danvas_comprehensive.py`, `test_flatten_published.py`),
  resume-semantics assertions strengthened
  (`test_youtube_transcript_main.py`). All verified by test run.
- [x] Stray root-level `software/test_new_modules.py` (debug scratch file,
  outside the pytest gate) deleted.
- [x] `software/tests/` formatted with `ruff format` (54 files).
- [x] `ruff` now excludes generated `published/` output trees via
  `extend-exclude` in `pyproject.toml` — 57 false lint findings in the
  rendered Japanese translation tree no longer mask real ones; repo-wide
  `uv run ruff check .` and `ruff format --check .` both clean.
- [x] Verified after all changes: CI-equivalent gate **995 passed / 0 failed /
  34 deselected**; mypy clean (109 files).

Notes from the earlier doc-only pass:
  - Heavy test suite not run at that time (CI-equivalent gate is ~995 tests; run via
    `cd software && uv run pytest tests/ -m "not requires_internet and not requires_api and not requires_whisper"`).
    No runtime code was changed in this pass — doc/config edits only — so the gate is
    unaffected; `publish.toml` gained one course toggle (`ai-comedy`).
  - `youtube_courses.json` reports 821 videos vs 791 `module.md` on disk — the ~30-video
    gap is pre-render state (playlists enumerated but not yet transcribed); docs now use
    the metadata count with a "~" qualifier.
  - `DOMAINS_TO_DO.md` (330 proposed domains) is a forward-looking planning tracker, not
    stale; left untouched.
  - `youtube/AGENTS.md` and `YOUTUBE.md` intentionally still describe pipeline commands;
    verified against current script flags.

---

## Historical — previous review + implementation pass (2026-08-01, red-team)

> All findings from the previous hostile red-team review were implemented, tested, and
> verified: CI-equivalent gate **995 passed / 0 failed / 34 deselected**; `ruff check`
> clean; `ruff format --check` clean; **`mypy src/` — Success (109 source files)**.

### Type-check gate (mypy) reconciled
- `mypy src/` passes with zero errors across all 109 source files (was ~288 chronic
  errors). Annotation-only changes; no runtime behavior changed.

### Test-suite defects
- Fixed 4 genuine test bugs: `test_generate_all_outputs::test_main_execution` (wrong
  `"ai-philosophy"` assertion) and monkeypatch lambda-signature `TypeError`s in
  `test_transcribe_youtube` (×2) and `test_render_youtube_courses`.

### danvas (src/danvas) — security hardening
- Path-traversal guard (`store.validate_course_id`), role-based `check_permission` (403),
  POST body cap (64 KiB) + `Content-Length` validation, input validation (grades, dates,
  event types), concurrency via `store_transaction` + `fsync`, corrupt-store fallback,
  XSS escaping; threat model in `danvas/AGENTS.md`. Tests added.

### src modules
- translation (safe `target_lang`, fail-loud), course_config (malformed TOML raises,
  deepcopy, scalar `pdf = false`), llm (error wrapping, TTL-cached probe, retry/backoff,
  `overlap_tokens`), course_generator (shell-quoting, `chmod` on write, duplicate
  `dir_name` check), html_website (quiz JS really grades), text_to_speech (cross-platform
  gTTS honoring `lang`/`slow`), batch_processing (robust course-id suffix match, `finally`
  cleanup), markdown_to_pdf (`pdf_options` applied via `@page` CSS), format_conversion
  (None-guard, heading-preserving docx, true HTML escaping), publish (`flatten_module`
  unique-name fallback), speech_to_text (chunked capture), validation (layout-aware module
  discovery), lab_manual (deterministic `feas_{idx}`), llm/dashboards (deterministic
  `zlib.crc32`).

### scripts
- `validate_outputs.py` / `publish_course.py` propagate exit codes via `sys.exit()`;
  dead imports/locals removed; `# noqa: E402` documented bootstrap.

### lint / format
- `ruff check` and `ruff format --check` clean; docs corrected to measured reality
  (1,014 tests collected, ~995 CI-passing, 75% source coverage).

---

## Environmental notes (not repo defects)
- Live-network YouTube and WeasyPrint-render tests fail only where the environment blocks
  YouTube or lacks native Pango/cairo — deselected/failing purely environmentally, not
  code bugs.
