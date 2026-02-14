# 🌍 Translation Guide

> **Navigation**: [← Docs Index](README.md) | [Modules](MODULES.md) | [CLI Reference](CLI_REFERENCE.md)

Translate course content into **11 languages** using local LLMs (Ollama).

---

## 🚀 Quick Start

```bash
cd software

# Translate Core Course to Spanish
uv run python scripts/translate_course.py active-inference es

# Dry run (preview)
uv run python scripts/translate_course.py active-inference fr --dry-run
```

---

## 🌐 Supported Languages

| Code | Language |
| :--- | :--- |
| `ar` | Arabic |
| `de` | German |
| `es` | Spanish |
| `fr` | French |
| `hi` | Hindi |
| `it` | Italian |
| `ja` | Japanese |
| `ko` | Korean |
| `pt` | Portuguese |
| `ru` | Russian |
| `zh` | Chinese |

---

## ⚙️ How It Works

1. **Chunking**: Splits large documents into manageable context windows.
2. **Translation**: Sends chunks to **Ollama** (default model: `gemma3:4b` or `llama3.2`).
3. **Reassembly**: Stitches chunks back together, preserving Markdown formatting.

---
*Last Updated: 2026-02-14*
