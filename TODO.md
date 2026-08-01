# TO-DO — courses repository backlog

**Status:** Active
**Owner:** Dr. Daniel Ari Friedman (docxology), Active Inference Institute
**Last reviewed:** 2026-08-01 (deepest hostile red-team review + implementation pass)

---

## Completed / Closed (this review + implementation pass)

> All findings from the red-team review have been implemented, tested, and
> verified.  Real results below: CI-equivalent gate **995 passed / 0 failed /
> 34 deselected**; `ruff check src/ scripts/` clean; `ruff format --check`
> clean; **`mypy src/` — Success: no issues found in 109 source files**.

### Type-check gate (mypy) reconciled
- `mypy src/` now passes with **zero errors** across all 109 source files
  (was ~288 chronic errors before this pass).  Additions were annotation-only:
  real return/param types, `cast()` for genuinely-`Any` third-party returns
  (json.loads, requests responses), and targeted `# type: ignore[...]` for
  runtime-dynamic constructs and stub-less third-party imports.  No runtime
  behavior changed.

### Test-suite defects
- Fixed 4 genuine test bugs: `test_generate_all_outputs::test_main_execution`
  (wrong `"ai-philosophy"` vs `"Philosophy"` assertion), and monkeypatch
  lambda-signature `TypeError`s in `test_transcribe_youtube` (×2) and
  `test_render_youtube_courses`.
- *Note:* `test_youtube_render::test_enumerate_known_playlist` and
  `test_lab_manual_main::test_render_to_pdf` fail only where live YouTube is
  blocked / native Pango is absent — environmental, not code defects.

### danvas (src/danvas) — security hardening
- **Path traversal** — `course_id` validated against a strict
  `[A-Za-z0-9_-]` whitelist (`store.validate_course_id`) enforced in both the
  HTTP dispatch and data layer, plus resolved-path containment in
  `_store_path`. Traversal ids (`..`, `/`, `%`) → 404.
- **Authorization** — role-based `check_permission` wired into `_dispatch`;
  mutating handlers deny with 403 when the principal's role lacks the
  permission. Local-first default role `instructor`; configurable via
  `DANVAS_ROLE`. Threat model documented in `danvas/AGENTS.md`.
- **Body limits** — POST bodies capped (`MAX_POST_BODY` 64 KiB);
  `Content-Length` validated; oversized/invalid → 400.
- **Input validation** — non-finite/negative grades rejected; calendar
  `date` (`YYYY-MM-DD`) and `event_type` whitelist validated; announcement /
  author / user-name / event-title length caps.
- **Concurrency & durability** — mutations run inside `store.store_transaction`
  (per-course lock preventing lost updates); writes `fsync` before
  `os.replace`; corrupt store falls back to empty instead of 500-crashing.
- **XSS** — escaped `author`/`posted_at`/grade/roster fields; role badge class
  allowlisted.
- Added tests: path-traversal rejection, 403 role enforcement, oversized-body
  rejection, invalid Content-Length, corrupt-store fallback, store
  transaction persistence.

### src modules
- **translation** — `translate_text` rejects unsafe `target_lang` and raises
  `RuntimeError` when every chunk fails (no more silent "translated" English
  file). Tests added.
- **course_config** — malformed TOML now raises (no silent setting loss);
  `get_rendering_config` returns a deepcopy (no global-default mutation);
  `is_format_enabled` honors scalar `pdf = false`.
- **llm** — streaming path wraps errors as `RuntimeError` (parity with
  non-stream), counts/warns malformed lines; availability probe uses the
  configured timeout and is TTL-cached; `generate` implements the advertised
  retry/backoff. `split_text_into_chunks` now honors `overlap_tokens`.
- **course_generator** — audit script titles/dir_names shell-quoted (blocks
  injection); chmod only on write; `validate()` catches duplicate course
  `dir_name`; removed dangling docstring.
- **html_website** — quiz JS really grades matching (compares to
  `correct-match` hidden fields) and requires non-empty free-response instead
  of auto-marking correct.
- **text_to_speech** — uses cross-platform gTTS honoring `lang`/`slow` (was
  macOS-only `say`+ffmpeg that ignored them).
- **batch_processing** — removed IndexError-prone course-id lookup (robust
  suffix match); preprocessed-lab temp file cleanup now in `finally`.
- **markdown_to_pdf** — `pdf_options` (page_size/margins) now actually applied
  via `@page` CSS (dead feature fixed).
- **format_conversion** — `pdf_to_text` guards `None` extraction (no literal
  "None"); `markdown_to_docx` preserves headings/lists instead of flattening;
  text→pdf/html truly HTML-escapes.
- **publish** — `flatten_module` no longer silently overwrites on name
  collision (unique-name fallback).
- **speech_to_text** — audio capture chunked (no unbounded full-file load).
- **validation** — `get_module_directories` layout-aware (flat `XX_topic`,
  two-level `unit/XX_topic`, and legacy `course/module-*`); spurious
  "expected 0 modules" issue for unconfigured courses fixed.
- **lab_manual** — non-deterministic `hash()`-based checkbox ids replaced with
  deterministic `feas_{idx}`.
- **llm/dashboards** — replaced salt-affected `hash()` seed with deterministic
  `zlib.crc32`.

### scripts
- `validate_outputs.py` / `publish_course.py`: `main()` return code now
  propagated via `sys.exit()` (pipeline failure detection).
- Removed dead/unused imports (F401), unused locals (F841), pointless
  f-strings (F541) across scripts; applied `# noqa: E402` to the intentional
  `sys.path` bootstrap imports; `generate_dashboards` re-export preserved for
  tests.

### lint / format
- `ruff check src/ scripts/` — **clean**.
- `ruff format --check src/ scripts/` — **clean** (ran `ruff format`).
- Docs corrected: README / `software/AGENTS.md` / SKILL.md now state the
  measured reality (1,014 tests collected, ~995 CI-passing, 77% source
  coverage) instead of stale "1,021 / 100% / 17%".

---

## Environmental notes (not repo defects)
- Live-network YouTube and WeasyPrint-render tests fail only where the
  environment blocks YouTube or lacks native Pango/cairo — deselected/failing
  purely environmentally, not code bugs.
