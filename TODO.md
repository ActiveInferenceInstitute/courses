# TO-DO — courses repository backlog

**Status:** Active
**Owner:** Dr. Daniel Ari Friedman (docxology), Active Inference Institute
**Last reviewed:** 2026-11-12 (education-contract pass; open items reconciled with
counts measured on this date)

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
- [x] ✓ `TESTING.md` tables now list the 4 previously undocumented test files (`test_*_extended.py` ×3, `test_youtube_render.py`). (f4789c39)
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

- None from the earlier passes.

### Gate and documentation pass — 2026-11-12

- [x] Added `run.sh`: one entry point, one command per arm (`lint`, `types`,
  `no-mocks`, `test`, `test-full`, `docs`, `gnn`, `metrics`, `all`). CI calls
  the same arms.
- [x] Rewrote `.github/workflows/ci.yml`: three independent jobs (`static`,
  `test`, `gnn-conformance`), no `needs:` chain, one environment sync per job.
  The `verify-no-mocks` job became the `no-mocks` arm inside `static`; it had
  been running `python scripts/verify_no_mocks.py` with no interpreter setup,
  which fails on a runner that only has `python3`.
- [x] Extracted the GNN conformance heredocs into
  `software/scripts/verify_gnn_conformance.py`; the job and `./run.sh gnn` now
  run the same script against `.github/gnn-pin.json`.
- [x] Added `docs/` (hub, run guide, flat index, folder guide) and
  `docs/_generated/` (`GATE_METRICS.md`, `ARM_TIMINGS.md`) produced by
  `software/scripts/generate_gate_metrics.py`.
- [x] Added `software/scripts/check_docs.py` — the repository had no
  documentation check (no mkdocs, no markdown-link-check); it resolves relative
  links in the documentation surfaces and fails on a stale generated document.
- [x] Corrected the test counts across the docs to that day's measurement:
  1,029 collected, 995 in the offline gate, 34 deselected. Those numbers went
  stale when the contract tests landed (#28); the measured figures and the nine
  files still quoting them are listed in the education-contract open items
  below.

Open items from this pass:

- [ ] **`./run.sh test-full` is red; #25 merged anyway.** The arm runs the 34
  `requires_internet`/`requires_api`/`requires_whisper` tests. On 2026-11-12 it
  reached 97% with
  `tests/test_youtube_render.py::TestEnumeratePlaylistVideos::test_enumerate_known_playlist`
  failing (`yt_dlp` `HTTP Error 400` from the YouTube playlist API), then blocked
  for more than two minutes in `tests/test_youtube_transcript_main.py` on caption
  download and was interrupted. The arm is a required arm, not an optional
  investigation: the estate condition was "every arm green locally before
  landing", so #25 landed in violation of it. Closing this needs either
  reachable network/API access or an explicit decision to make the network tests
  self-skip when unreachable. Until then, treat `test-full` as unproven and do
  not claim the full gate is green. See
  [`docs/RUN_GUIDE.md`](docs/RUN_GUIDE.md#known-red-arm--test-full).
- [ ] `software/docs/AGENTS.md` still describes 18 files under `software/docs/`;
  that remains accurate (re-counted 2026-11-12), but the repository-level
  `docs/` tree is not mentioned there. Owner: whoever owns the two hubs; blocked
  only on that cross-linking decision.
- [ ] `pre-commit` pins ruff `v0.9.0` while the project environment resolves
  ruff 0.14.x; the two can disagree on formatting. Not changed here. Owner:
  whoever next touches formatting; blocked on the pin bump itself, which needs a
  full `ruff format` pass to land with it.

### Education-contract pass — 2026-11-12

Completed in this pass:

- [x] Adopted `education-contract/v1` as the group's lead repository: canonical
  schema `specs/education/schema.json`, the pointer `education-contract.json`
  carrying its `schema_sha256`, and this repository's own bundle
  `specs/education/active-inference.json`. (3e834dfb)
- [x] Added the `contract` arm: `./run.sh contract` runs
  `software/scripts/check_education_contract.py` (registry plus every member's
  vendored schema and pointer) and `software/scripts/export_education_bundle.py
  --check` (the committed bundle still matches the course tree). It is part of
  `./run.sh all` and of the `static` CI job. (3e834dfb)
- [x] Added the shared engine `software/src/education_contract/` — `schema.py`,
  `rules.py`, `registry.py`, `catalog.py` — with
  `software/tests/test_education_contract.py` as the drift test. (3e834dfb)
- [x] Documented the contract for the eleven members in
  [`docs/workflows/education.md`](docs/workflows/education.md), linked from
  `docs/README.md` and `docs/documentation-index.md`. (3e834dfb)
- [x] Corrected the sidecar claim in that document: the `docs:` list is
  unvalidated in ten members, and `Parr_et_al_2022_ActInf_Textbook` is the
  exception rather than the rule. (f1e5af62)
- [x] Regenerated `docs/_generated/GATE_METRICS.md` and
  `docs/_generated/ARM_TIMINGS.md` from the tree, which is what keeps the
  measured counts out of hand-written prose for the facts the generator covers.
  (3e834dfb)

Open items from this pass:

- [ ] **This repository's bundle covers one course.** `specs/education/` holds
  `active-inference.json` plus the example, while the migration row for `courses`
  in [`docs/workflows/education.md`](docs/workflows/education.md) §6 names six
  more spine-shaped courses (`active_inference_101`, `_401`, `_es`, `_family`,
  `_hs`, `_ms`) that still need `export_education_bundle.py --course <name>`
  output added to `bundles`, `prerequisite_edges` authored from the prose in
  `course_development/active_inference/resources/learning_pathways.md`, and one
  authored `topic` per unit in `course_development/domains/` before it can be
  transcribed. Owner: the curriculum author; blocked on authored metadata, not
  on tooling — the extractor and the checker already exist.
- [ ] **GNN revision drift.** `.github/gnn-pin.json` pins v5.0.3
  (`8f293d9ba810e6eda5c09842d9c7ed9ffa5f92c1`) while the estate importer
  repositories moved to v5.1.0
  (`75c834bd8519dc7b5adc4d24f16bf393cfd1ecdf`, confirmed 2026-11-12 with
  `git ls-remote --tags`). This repository is not a bare importer: it owns five
  GNN exemplars under `course_development/gnn/01_gnn_syntax/models`, and the
  check asserts `gnn.__version__` against the pin's tag
  (`software/scripts/verify_gnn_conformance.py:86,139`), so a bump has to
  re-install the parser from the pinned commit into `software/.venv-gnn` and
  re-run `./run.sh gnn`. Owner: whoever owns the estate GNN pin; blocked on that
  decision plus network access — every hosted `CI` run currently fails within
  seconds (billing), so the evidence has to be local.
- [ ] **Documented test counts drifted again after #28.** Nine surfaces still
  quote 1,029 collected / 995 offline. `uv run pytest tests/ --collect-only`
  on 2026-11-12 reports **1,062 collected**, of which **1,028** are in the
  offline selection and **34** are the internet/API/whisper tests. Files:
  `README.md:6,207-209` (badge and prose), `AGENTS.md:7,56`,
  `software/README.md:232-233`, `software/AGENTS.md:9`,
  `software/docs/CONTRIBUTING.md:72-73`, `software/docs/README.md:44`,
  `software/docs/TESTING.md:29`, `docs/RUN_GUIDE.md:90`,
  `.agents/skills/courses/SKILL.md:20`. The module and script counts drifted with
  them: `docs/_generated/GATE_METRICS.md` reports **22** importable modules and
  **28** Python scripts, while `AGENTS.md:56`, `CLAUDE.md:70-71`,
  `docs/INTEGRATION.md:48` and `.aii/config.yaml:55` still say 21 modules and
  23 course scripts plus 3 gate tools (it is now 5 gate tools). Owner: the next
  docs pass; nothing external blocks it, and `./run.sh docs` does not check prose
  numbers.

### Documentation completion pass 3 — 2026-11-11

Completed in this pass:

- [x] Added `software/docs/PIPELINE.md` — the end-to-end `publish.py` run: stage order,
  `published/` output layout, and offline vs. network requirements. Linked from the docs
  index and the root `README.md`.
- [x] Fixed the broken relative link in `course_development/AGENTS.md`
  (`../active_inference/...` → `./active_inference/...`); it was the only broken relative
  link across the root, `.aii/`, and `software/docs/` guides.
- [x] Root `README.md`: added a table of contents, an honest Status table (what works
  offline vs. what needs network, system libraries, or a local LLM), a Documentation hub
  section, and a current last-updated date.
- [x] `software/docs/CONFIGURATION.md`: replaced the invalid `[project.dependencies]`
  TOML block with the real PEP 621 `dependencies = [...]` list; corrected the "add a new
  course" step, which described every toggle as defaulting to `false`.
- [x] `software/docs/ARCHITECTURE.md` and `software/AGENTS.md`: clarified that Ruff is the
  linter and formatter used in CI, with Black's config retained for compatibility.
- [x] Bumped `Last Updated` dates on
  `software/docs/{README,ARCHITECTURE,CONFIGURATION,TROUBLESHOOTING}.md`.
- [x] `.aii/readiness.json`: corrected `baseline.commit` from a commit that only exists on
  the `refactor/publish-format` branch to `origin/main` (`4e050dc6…`), and set
  `measured_at` to 2026-11-11.

Open items found in this pass, left for the owner:

- [ ] `published/` has no top-level `README.md`, and its committed `AGENTS.md` is deleted
  by `publish.py` when `clean_before_publish = true` (the clean step preserves only
  dot-prefixed entries). The guide is therefore transient after a full publish run.
  Decide whether to preserve it (e.g. teach the clean step to keep it) or generate it.
  Re-checked 2026-11-12: `published/README.md` is still absent and `published/AGENTS.md`
  is tracked. Owner: whoever owns the publish clean step; blocked on that decision.
- [ ] `software/transcription/captions/` and `software/transcription/transcripts/` (775
  tracked files each, re-counted 2026-11-12) have no folder guide. They are bulk generated
  transcript data, so no README was added under the "skip generated/vendored data" rule.
  Owner: the docs pass; blocked on that rule decision.
- [ ] `published/` subdirectories are tracked in Git even though `.gitignore` ignores
  `published/*/` — the tracked rendered outputs are stale relative to the pipeline and
  will churn on every publish (14,799 tracked files, re-counted 2026-11-12). Owner: the
  repository owner; blocked on whether to keep tracking them.
- [x] ✓ Test-count arithmetic — resolved by measurement, not by argument:
  `uv run pytest tests/ --collect-only` on 2026-11-12 reports 1,062 collected, 1,028 in
  the offline selection, 34 deselected. The 1,014 versus 995 + 34 split was measured
  before the suite grew; the figures that are current today are quoted with their files
  in the education-contract open items above.
- [ ] `464 modules` (root `AGENTS.md`; README badge `modules-464+`) understates a
  filesystem count: 512 module directories contain a `module.md` across the 14 courses
  (excluding the `youtube/` archive and the `gnn/` track; re-counted 2026-11-12). Confirm
  the intended counting rule before changing the figure. Owner: the curriculum author;
  blocked on that rule decision.

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
