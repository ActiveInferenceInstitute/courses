# 🔧 Troubleshooting

> **Navigation**: [← Docs Index](README.md) | [Quick Start](QUICKSTART.md) | [Testing](TESTING.md)

Common solutions for the Active Inference course pipeline.

---

## 🚨 Diagnostics

Run this sanity check first:

```bash
cd software
uv run pytest tests/test_imports.py         # Check environment
uv run pytest tests/test_dependencies.py    # Check libs
```

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

---
*Last Updated: 2026-02-14*
