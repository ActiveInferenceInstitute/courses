# Changelog

All notable changes to the Active Inference Institute courses repository.

## [Unreleased] — 2026-08-26 (lint/format hardening)

### Fixed
- All 15 ruff findings in `software/tests/` resolved with real behavior,
  not suppression: dead local variables replaced by assertions that actually
  check the code under test (`validate_upload_readiness` size reporting,
  markdown→HTML content, dry-run path return), dependency-availability checks
  moved to `importlib.util.find_spec`, unused imports/variables removed, and
  resume-semantics assertions strengthened in the YouTube transcript tests.
- Stray debug scratch file `software/test_new_modules.py` deleted (it sat at
  `software/` root outside the pytest gate and shadowed nothing).
- Ruff now excludes the generated `published/` output trees
  (`extend-exclude` in `pyproject.toml`), removing 57 false findings from the
  rendered Japanese translation tree.

### Changed
- `software/tests/` formatted repo-standard via `ruff format` (54 files).

### Verified
- `uv run ruff check .` clean; `uv run ruff format --check .` clean;
  `uv run mypy src/` — Success (109 source files); CI-equivalent gate
  **995 passed / 0 failed / 34 deselected**.

## [Unreleased] — 2026-08-01

### Added
- **danvas**: role-based authorization (403 on insufficient permission),
  `store.validate_course_id` path-traversal guard, `store.store_transaction`
  (per-course lock), POST body cap (64 KiB) and `Content-Length` validation,
  corrupt-store fallback, field-length / calendar-date / event_type
  validation, `fsync` on store writes, URL-id whitelist at dispatch.
- `validation.get_module_directories` now discovers flat, two-level, and
  legacy module layouts (was legacy-only).
- New tests across danvas (traversal, auth, body-limit, corrupt-store,
  transaction), translation (safe `target_lang`, fail-loud), course_config
  (malformed TOML), course_generator (shell-quoting, dir_name uniqueness),
  validation (layout discovery), llm (chunk overlap), and scripts.
- `CHANGELOG.md` for the repository.

### Changed
- **translation**: `translate_text` rejects unsafe `target_lang` and raises if
  no chunk translates (no silent English-in-a-"translated"-file corruption).
- **course_config**: malformed TOML now raises (no silent setting loss);
  `get_rendering_config` returns a copy; `is_format_enabled` honors scalar
  boolean toggles.
- **llm**: stream errors wrapped as `RuntimeError` (parity with non-stream) and
  malformed lines are counted/warned; availability TTL-cached and probe uses
  configured timeout; `generate` implements retry/backoff; chunk overlap now
  honored.
- **course_generator**: audit script shell-quotes titles/dir_names; `chmod`
  only on write; `validate()` checks for duplicate course `dir_name`.
- **html_website**: quiz grader now really grades matching and requires
  non-empty free-response (was auto-correct for both).
- **text_to_speech**: uses cross-platform gTTS honoring `lang`/`slow` (was
  macOS-only `say`+ffmpeg ignoring them).
- **batch_processing**: robust course-id resolution (no IndexError on short
  paths); preprocessed-lab temp cleanup in `finally`.
- **markdown_to_pdf**: `pdf_options` (page_size/margins) now applied; dead API
  now functional.
- **format_conversion**: PDF-to-text guards `None` extraction; Markdown→DOCX
  preserves headings/lists; text→HTML/PDF truly HTML-escapes.
- **publish**: `flatten_module` avoids silent overwrite on name collision.
- **speech_to_text**: audio recorded in bounded chunks (no unbounded load).
- **validation**: dropped spurious "expected 0 modules" issue for
  unconfigured courses.
- **scripts**: `validate_outputs.py` / `publish_course.py` propagate their exit
  code via `sys.exit()` (pipeline failure detection); removed dead imports and
  unused locals; documented the intentional `sys.path` bootstrap with
  `# noqa: E402`.
- **mypy config**: added `ignore_missing_imports` for stub-less first-party
  deps (markdown, weasyprint, gtts, speech_recognition, pydub, docx).
- **docs**: corrected stale test/coverage claims; added danvas security
  hardening + threat-model docs; updated repository TODO.

### Fixed
- 4 genuine test-suite defects (wrong assertions / monkeypatch lambda
  signatures).
- danvas stored-XSS gaps (unescaped announcement author/timestamps,
  gradebook/roster fields, role badge class).
- danvas non-finite/negative grade handling (was crashing / poisoning
  aggregates).
- Non-deterministic generators via salted `hash()` (dashboards / lab_manual).

### Removed
- Dead `pdf_options` no-op, `get_theme`/`DEFAULT_THEME` re-export corrected
  (kept with `# noqa` for tests), unused imports and locals (ruff F401/F841).

### Type-check gate
- **`mypy src/` now passes with zero errors** across all 109 source files
  (was ~288 chronic errors).  The reconciliation was annotation-only — explicit
  return/param types, `cast()` for `Any`-returning third-party APIs
  (`json.loads`, `requests` responses), `# type: ignore[...]` on
  runtime-dynamic constructs and stub-less imports, plus `ignore_missing_imports`
  for first-party deps without type stubs.  No runtime behavior changed.
- The CI type-check (`mypy src/`), lint (`ruff check`), format
  (`ruff format --check`), and the 995-test CI gate are now all green.

### Notes
- The CI-equivalent test gate passes: **995 passed / 0 failed / 34
  deselected**, **75% source coverage**; `ruff check` and `ruff format --check`
  are clean.
- Live-network YouTube and WeasyPrint-render tests fail only where the
  environment blocks YouTube or lacks native Pango/cairo — environmental.
