# Project State Report — courses repository, 2026-08-26 (check-and-improve pass)

## Scope

Repository: `ActiveInferenceInstitute/courses` (checked out at
`projects/ongoing/instituteos/repos/courses`). Baseline at dispatch:
`HEAD = 139c2981`, tree clean.

## State assessment

| Gate | Result |
| --- | --- |
| `uv run pytest tests/ -m "not requires_internet and not requires_api and not requires_whisper"` | 995 passed / 0 failed / 34 deselected |
| `uv run mypy src/` | Success (109 source files) |
| `uv run ruff check .` | 74 findings: 15 real in `software/tests/`, 57 false positives from generated `published/` tree, 2 in a stray root file |
| `uv run ruff format --check tests/` | 54 of 68 files unformatted |

Backlog (TODO.md): all prior rows closed; no open items. The actionable work
this pass came from the measured state above, not the backlog file.

## What was done (commit `85719255`)

1. **15 ruff findings in `tests/` fixed with real behavior** — dead locals
   replaced by assertions that verify the code under test (canvas
   upload-readiness size reporting; markdown→HTML `<h1>` content;
   legacy-import dry-run returned-path contract), dependency imports converted
   to `importlib.util.find_spec` availability probes (`test_dependencies.py`,
   `test_legacy_import_main*.py`), unused imports/variables removed,
   resume-semantics assertions strengthened in YouTube transcript tests.
2. **Stray debug scratch file deleted**: `software/test_new_modules.py` sat at
   `software/` root outside the pytest gate.
3. **`ruff format` applied to `tests/`** (54 files to repo standard).
4. **Ruff scope fix**: `extend-exclude = ["published"]` in
   `software/pyproject.toml` — generated pipeline output (rendered Japanese
   translation tree) no longer yields 57 false lint findings.
5. Docs updated per conventions: TODO.md maintenance-pass section,
   CHANGELOG.md entry.

## Verification after changes

- `ruff check .` clean; `ruff format --check .` clean
- `mypy src/` clean (109 files)
- Local gate re-run: 995 passed / 0 failed / 34 deselected

## PUSHED — 2026-08-26 ~12:57 PDT

- Pushed authored commit only: `85719255` → `origin/main`
  (`139c2981..85719255`).
- Post-push identity check: `git rev-parse HEAD` ==
  `git rev-parse origin/main` == `857192555dffabf43a5daac1ebe3d8008a92fc5f`.
- Hosted CI run `33007808995` on main: **completed / success**
  (Lint & Type Check ✓ · Verify No Mocks Policy ✓ · Tests Python 3.11 ✓ ·
  Tests Python 3.12 ✓).
- No pre-existing commits touched; no rebase/force-push.

## Remaining

- TODO.md has no open items. Environmental-only notes remain
  (YouTube/WeasyPrint network-render tests fail where the environment blocks
  those services — deselected by marker, not code defects).

## Incident note

A zero-byte git `index.lock` dated Aug 5 (21 days stale, held by no process)
blocked all staging in this repo's module gitdir and was removed before
committing.
