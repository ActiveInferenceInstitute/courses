# Contributing to the Active Inference Institute — Courses

Welcome! We're glad you want to contribute.

**The full contribution guide** — including the no-mocks policy, code standards, testing patterns, and module architecture — lives in:

👉 [`software/docs/CONTRIBUTING.md`](software/docs/CONTRIBUTING.md)

---

## Quick start

```bash
# 1. Install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install dependencies
cd software
uv sync --extra dev

# 3. Install pre-commit hooks
cd ..
pre-commit install

# 4. Verify everything works
cd software
uv run pytest tests/ -v -m "not requires_internet and not requires_api and not requires_whisper"
```

## Key rules (short version)

| Rule | Summary |
|------|---------|
| **No mocks** | All tests use real implementations — no `unittest.mock`, `MonkeyPatch`, or stubs. |
| **Real coverage** | New features require tests; 100% coverage for new code. |
| **Module structure** | `main.py` (public API) · `utils.py` (helpers) · `config.py` (constants) |
| **8-topic spine** | Course units follow the fixed order: Systems → Agents → Perception → Cognition → Action → Learning → Communication → Planning |
| **No generated edits** | Never hand-edit files under `published/` — re-run the pipeline. |

See [`software/docs/CONTRIBUTING.md`](software/docs/CONTRIBUTING.md) for the complete guide.
