# Changelog

All notable changes to the Active Inference Institute courses repository.

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

### Notes
- The CI-equivalent test gate passes: **995 passed / 0 failed / 34
  deselected**, **75% source coverage**; `ruff check` and `ruff format --check`
  are clean.
- The `mypy src/` gate remains red (~288 errors) from long-standing systemic
  type-annotation debt predating this pass (see `TODO.md` "Open — scoped").
- Live-network YouTube and WeasyPrint-render tests fail only where the
  environment blocks YouTube or lacks native Pango/cairo — environmental.
