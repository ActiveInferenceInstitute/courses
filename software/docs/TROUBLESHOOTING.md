# 🔧 Troubleshooting

> **Navigation**: [← Docs Index](README.md) | [Quick Start](QUICKSTART.md) | [Testing](TESTING.md)

Common solutions for the Active Inference course pipeline.

---

## 🚨 Diagnostics

Run these sanity checks first:

```bash
cd software
uv run pytest tests/test_imports.py         # Check environment
uv run pytest tests/test_dependencies.py    # Check libs
uv run pytest tests/test_real_implementations.py  # Verify no mocks
```

| Symptom | Likely Cause | See Section |
| :--- | :--- | :--- |
| `OSError: cannot load library 'pango'` | Missing system libs | [PDF Generation](#-pdf-generation) |
| `gTTSError: 429` | Rate limiting | [Audio Generation](#-audio-generation) |
| `uv: command not found` | uv not installed | [Python / uv](#-python--uv) |
| `Connection refused` on translate | Ollama not running | [LLM / Ollama](#-llm--ollama) |
| Tests failing in CI | Missing env vars | [Test Failures](#-test-failures) |

---

## 📄 PDF Generation

**Error**: `OSError: cannot load library 'pango'` / `cairo`

**Fix**: You are missing system libraries for WeasyPrint.

```bash
# macOS
brew install cairo pango gdk-pixbuf glib
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"

# Ubuntu
sudo apt-get install python3-cairo python3-pango libgdk-pixbuf2.0-dev libffi-dev
```

**Note**: On macOS, add the `DYLD_LIBRARY_PATH` export to your `~/.zshrc` for persistence.

---

## 🔊 Audio Generation

**Error**: `gTTSError: 429 (Too Many Requests)`

**Fix**: Google TTS is rate-limiting you.

1. Wait 10 minutes.
2. Or skip audio: `--override-formats pdf,html,txt,md`

---

## 🐍 Python / uv

**Error**: `uv: command not found`

**Fix**: Install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Error**: `ModuleNotFoundError: No module named 'src'`

**Fix**: Always run from the `software/` directory!

```bash
cd software
uv run ...
```

**Error**: `No matching version found` for a dependency

**Fix**: Update the lockfile:

```bash
uv lock
uv sync --extra dev
```

---

## 🤖 LLM / Ollama

**Error**: `Connection refused` when running translation or course generation

**Fix**: Ensure Ollama is running:

```bash
ollama serve
```

**Error**: Translation timeout on large files

**Fix**: Increase timeout or use a faster/smaller model:

```bash
export OLLAMA_TIMEOUT=300
export OLLAMA_MODEL=llama3.2:1b
```

---

## 🧪 Test Failures

**Error**: PDF-related tests fail on macOS

**Fix**: Ensure `DYLD_LIBRARY_PATH` is set:

```bash
DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH" uv run pytest tests/ -v
```

**Error**: Tests marked `requires_internet` fail

**Fix**: These tests need network access. Skip them in offline environments:

```bash
uv run pytest tests/ -v -m "not requires_internet"
```

**Error**: `test_real_implementations.py` fails

**Fix**: This test verifies the No Mocks policy. If it fails, a dependency may have introduced mock objects. Check recent changes to `conftest.py` and module imports.

---

## 📦 Publishing Pipeline

**Error**: `publish.py` fails with `FileNotFoundError`

**Fix**: Ensure `publish.toml` exists at the repo root and the listed course paths are valid:

```bash
# Verify config
python publish.py --dry-run
```

**Error**: Stale outputs in `published/`

**Fix**: Enable clean output in `publish.toml`:

```toml
[options]
clean_output = true
```

Or manually clear:

```bash
rm -rf published/*
python publish.py
```

---
*Last Updated: 2026-02-15*
