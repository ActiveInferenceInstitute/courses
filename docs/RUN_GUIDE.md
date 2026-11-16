# Run guide — the gate

`./run.sh <arm>` is the repository's single gate entry point. Each arm is one
command, `.github/workflows/ci.yml` invokes the same arms, and nothing in this
document restates a command that lives in the script.

---

## Prerequisites

```bash
# uv (manages Python and the locked environment)
curl -LsS https://astral.sh/uv/install.sh | sh

# the engine environment (once)
cd software && uv sync --extra dev
```

Setup is a separately authorized operation, not a side effect of a gate. Select
an existing engine interpreter with `COURSES_PYTHON`; the gate preserves that
selection and does not implicitly synchronize another environment.

`gnn` requires an existing `COURSES_GNN_PYTHON`, explicit `COURSES_GNN_MODE`
(`source` or `installed`), and independently reviewed `COURSES_GNN_BOOTSTRAP`
and `COURSES_GNN_MANIFEST`. Source mode additionally requires
`COURSES_GNN_PACKAGE_ROOT` and import resolution selecting its parent directory.
No install or environment creation occurs inside the gate; `--install` is removed.
See [the GNN pointer](../.github/GNN.md) for guard and provenance boundaries.

---

## Arms

| Arm | What it runs | Proves |
| --- | --- | --- |
| `lint` | `uv run ruff check src/ scripts/` then `uv run ruff format --check src/ scripts/` | Style and formatting match the committed configuration. |
| `types` | `uv run mypy src/` | `src/` type-checks under `disallow_untyped_defs`. |
| `no-mocks` | `uv run python scripts/verify_no_mocks.py` | No test imports or uses `unittest.mock`, `patch`, `MagicMock`, or a mock library. |
| `test` *(default)* | `uv run pytest tests/ -m "not requires_internet and not requires_api and not requires_whisper" --cov-report=xml --cov-report=json` | The offline gate: hermetic, no network, no external API, no Whisper. |
| `test-full` | `uv run pytest tests/` | Every test, including the network/API/Whisper-marked ones. Needs network; see below. |
| `docs` | `uv run python scripts/check_docs.py` | Every relative link in the documentation surfaces resolves, and `docs/_generated/GATE_METRICS.md` matches a fresh generation. |
| `contract` | Canonical checker and exporter through the registry in `run.sh` | Explicit roots, contained multi-bundle members, schema/semantic rules, export freshness and one complete JSON value on `--json`; either phase's failure is nonzero. |
| `gnn` | Selected `COURSES_GNN_PYTHON` and `verify_gnn_conformance.py` | Frozen bootstrap, independent full manifest, explicit origin and real guarded parse/syntax/type verdicts. |
| `metrics` | `uv run python scripts/generate_gate_metrics.py` | Rewrites `docs/_generated/` from the current tree. Not a check. |
| `all` | `lint`, `types`, `no-mocks`, `test`, `docs`, `contract` in order | The offline gate in one command. |

`test-full` remains required for full acceptance and needs the admitted external
services. Its historical failure is retained below, not silently converted into
a skip or rerun without service authorization.

The previously accepted focused engine paths are retained. The new source-mode
GNN controls and actual five-exemplar gate passed after correcting a file-path
caller. No fresh full-suite, coverage, installed-origin or hosted CI result is
claimed by this bounded qualification.

---

## CI mapping

| Job key | Display name | Arms |
| --- | --- | --- |
| `static` | Static checks (lint, types, no-mocks, docs, contract) | `lint`, `types`, `no-mocks`, `docs`, `contract` |
| `test` | Tests (Python 3.11 / 3.12) | `test` |
| `gnn-conformance` | gnn conformance (pinned) | `gnn` |

Jobs remain independent. The declared Python matrix explicitly selects its
interpreter; a local run on one interpreter is not evidence for every matrix row.
The GNN job provisions dependencies separately and requires reviewed artifact URLs
in `COURSES_GNN_BOOTSTRAP_URL` and `COURSES_GNN_MANIFEST_URL`. Their publication and
hosted variable configuration remain operational prerequisites, not local proof.

---

## Measurements

Generated timings and coverage are historical until measured against the final
source and runtime. Current receipts use version 2 and bind pre/post source and
runtime identity; drift is rejected. Coverage is accepted only with a matching
fresh provenance receipt. `GATE_TIMINGS=0` suppresses timing publication for bounded
qualification; it does not manufacture measurements. Preserve existing JSONL
history and never hand-edit generated numbers.

### Before → after, measured once each

macOS arm64, Python 3.11, commit `3632cf25`, 2026-11-12. "Before" is the command
the old workflow used; "after" is the arm that replaced it. The live table is
[`_generated/ARM_TIMINGS.md`](_generated/ARM_TIMINGS.md); this comparison is a
dated record, not a second source of truth.

| Check | Before | After | Result |
| --- | --- | --- | --- |
| Ruff lint + format | two `uv run ruff` calls, < 1 s each | `./run.sh lint`, 0.1–0.2 s | pass, 135 files formatted |
| mypy | `uv run mypy src/`, 23 s on a cold environment | `./run.sh types`, 9.7 s cold cache / 1.0–1.3 s warm | pass, 109 files |
| No-mocks | `python scripts/verify_no_mocks.py` — **not runnable** (no `python` on PATH) | `./run.sh no-mocks`, 0.1–0.2 s | pass, 68 files, 0 violations |
| Offline tests | `uv run pytest tests/ -m "not requires_internet and not requires_api and not requires_whisper"`, 92 s | `./run.sh test`, 85–91 s | 995 passed, 34 deselected, 75% coverage |
| Full tests | `uv run pytest tests/` | `./run.sh test-full` | **red on this host** — not an accepted gate result; see [Known red arm](#known-red-arm--test-full) |
| Docs | no check existed | `./run.sh docs`, 1.6–1.8 s | 66 files, 0 broken relative links, generated facts current |
| GNN conformance | two heredocs inside `ci.yml`, not runnable outside Actions | `./run.sh gnn`, 29.8 s first run (installs the pin) / 0.4 s after | pass, parser 5.0.3, 5 parsed, 5 type-checked |

Two changes account for the offline-test difference: the arm writes `xml` and
`json` coverage reports for CI and the generator, and `--cov-report=html` was
removed from `addopts`, so the HTML tree is no longer written on every run
(ask for it with `--cov-report=html`).

The old workflow ran five jobs — `lint`, `verify-no-mocks`, `test` (3.11),
`test` (3.12), `gnn-conformance` — chained by `needs:` and repeating the
uv/Python setup in four of them. It now runs three independent jobs and syncs
the environment once per job.

### Known red arm — `test-full`

`./run.sh test-full` is **not green on this host**, and it was not green when
the gate work merged as #25. Recorded rather than resolved:

- Run: `uv run pytest tests/` on 2026-11-12, macOS arm64, Python 3.11.
- Result: 97% complete, 1 failure —
  `tests/test_youtube_render.py::TestEnumeratePlaylistVideos::test_enumerate_known_playlist`
  with `yt_dlp.utils.DownloadError: ERROR: [youtube:tab] … Unable to download API
  page: HTTP Error 400: Bad Request`. Execution then blocked for more than two
  minutes in `tests/test_youtube_transcript_main.py` (caption download) and was
  interrupted at 2m16s.
- Cause shown by the run: live network dependency of the marked tests. These
  runs do not establish a code defect, and they do not establish that the arm
  passes anywhere.
- Not fixed. Making it green needs reachable network/API access, or a deliberate
  decision to make network tests self-skip when unreachable; neither was done.
- Consequence: the estate's "every arm green locally before landing" condition
  was violated when #25 merged. The next landing must either satisfy that arm or
  keep the PR open.

---

## Refreshing the generated facts

```bash
./run.sh test     # produces software/coverage.json for the coverage line
./run.sh metrics  # rewrites docs/_generated/GATE_METRICS.md and ARM_TIMINGS.md
./run.sh docs     # fails if GATE_METRICS.md is stale or a link is broken
```

`GATE_METRICS.md` is deterministic for a given tree; `ARM_TIMINGS.md` is a
record of measurements and reports a missing arm as `not measured` rather than
guessing.

---

## Troubleshooting

- **`uv: command not found`** — install uv; the arms assume it is on `PATH`.
- **WeasyPrint/PDF failures on macOS** — `export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"` before running the test arms.
- **GNN admission fails** — check the explicit mode, selected interpreter/import root, frozen bootstrap and full manifest. Do not install implicitly, change the pin, or fall back from failed installed admission to source mode.
- **`docs` arm reports a stale generated document** — run `./run.sh metrics`; never hand-edit `docs/_generated/`.
