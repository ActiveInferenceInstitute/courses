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

The `gnn` arm is the exception: it creates its own seeded virtual environment
(`software/.venv-gnn`, git-ignored) and installs the parser pinned in
[`.github/gnn-pin.json`](../.github/gnn-pin.json). Every other arm runs inside
the single `software/` environment.

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
| `gnn` | `software/.venv-gnn/bin/python software/scripts/verify_gnn_conformance.py --install` | The installed GNN parser matches the pinned tag, and all five exemplars parse and type-check. |
| `metrics` | `uv run python scripts/generate_gate_metrics.py` | Rewrites `docs/_generated/` from the current tree. Not a check. |
| `all` | `lint`, `types`, `no-mocks`, `test`, `docs` in order | The offline gate in one command. |

`test-full` is an investigation arm, not a gate arm. It runs the 34 tests marked
`requires_internet`, `requires_api`, or `requires_whisper`; on a host without
reachable YouTube/gTTS/Ollama it fails or blocks, by design. The gate is
`./run.sh test`.

---

## CI mapping

| Job key | Display name | Arms |
| --- | --- | --- |
| `static` | Static checks (lint, types, no-mocks, docs) | `lint`, `types`, `no-mocks`, `docs` |
| `test` | Tests (Python 3.11 / 3.12) | `test` |
| `gnn-conformance` | gnn conformance (pinned) | `gnn` |

Jobs are independent — there is no `needs:` chain, so one slow arm cannot delay
another, and each job syncs the environment once for all of its arms. The
former standalone `verify-no-mocks` job is now the `no-mocks` arm inside
`static`: it used to run `python scripts/verify_no_mocks.py` with no interpreter
step, which fails on a runner that has only `python3`.

---

## Measurements

Wall time per arm, one run each, on the host and commit named in
[`_generated/ARM_TIMINGS.md`](_generated/ARM_TIMINGS.md). That table is
generated: `./run.sh` appends a receipt per arm to
`docs/_generated/arm-timings.jsonl` when `CI` is unset, and `./run.sh metrics`
rewrites the table. Do not retype a timing into prose.

Coverage (last `./run.sh test` run) is reported in the same generated table.

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
| Full tests | `uv run pytest tests/` | `./run.sh test-full` | not completed here: 1 failure at 97% (`test_enumerate_known_playlist`, YouTube `HTTP 400`), then blocked > 2 min on caption download |
| Docs | no check existed | `./run.sh docs`, 1.6–1.8 s | 59 files, 0 broken relative links, generated facts current |
| GNN conformance | two heredocs inside `ci.yml`, not runnable outside Actions | `./run.sh gnn`, 29.8 s first run (installs the pin) / 0.4 s after | pass, parser 5.0.3, 5 parsed, 5 type-checked |

Two changes account for the offline-test difference: the arm writes `xml` and
`json` coverage reports for CI and the generator, and `--cov-report=html` was
removed from `addopts`, so the HTML tree is no longer written on every run
(ask for it with `--cov-report=html`).

The old workflow ran five jobs — `lint`, `verify-no-mocks`, `test` (3.11),
`test` (3.12), `gnn-conformance` — chained by `needs:` and repeating the
uv/Python setup in four of them. It now runs three independent jobs and syncs
the environment once per job.

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
- **`gnn` arm fails with "the pinned GNN parser is not importable"** — the install step needs network access to GitHub; re-run `./run.sh gnn`.
- **`docs` arm reports a stale generated document** — run `./run.sh metrics`; never hand-edit `docs/_generated/`.
