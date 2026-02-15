# 🌐 Translation

> **Navigation**: [← Docs Index](README.md) | [CLI Reference](CLI_REFERENCE.md) | [Configuration](CONFIGURATION.md)

Translate course materials and YouTube transcripts into multiple languages using local LLMs via [Ollama](https://ollama.com).

---

## 🚀 Quick Start

```bash
cd software

# Translate a course to Spanish
uv run python scripts/translate_course.py --course ai-philosophy --lang es

# Translate pre-published outputs to Russian
uv run python scripts/translate_published.py --course active-inference --lang ru

# Translate YouTube transcripts to Japanese
uv run python scripts/translate_youtube.py --lang ja
```

---

## 🌍 Supported Languages

| Code | Language | Code | Language |
| :--- | :--- | :--- | :--- |
| `es` | Spanish | `ja` | Japanese |
| `fr` | French | `ko` | Korean |
| `de` | German | `hi` | Hindi |
| `zh` | Chinese (Simplified) | `ar` | Arabic |
| `pt` | Portuguese | `ru` | Russian |
| `it` | Italian | | |

---

## 🛠️ Translation Scripts

### `translate_course.py`

Translates source course content from `course_development/`. Use this for translating source materials before rendering.

```bash
uv run python scripts/translate_course.py --course ai-101 --lang fr
```

### `translate_published.py`

Translates pre-rendered outputs in `published/`. Processes all Markdown (`.md`) files within a published course directory and writes translations to `published/translations/{LANGUAGE}/courses/`.

```bash
uv run python scripts/translate_published.py --course active-inference --lang ru
```

### `translate_youtube.py`

Translates YouTube transcript archives.

```bash
uv run python scripts/translate_youtube.py --lang ja
```

---

## ⚙️ How It Works

1. **Chunking**: Long documents are split into chunks (default ~2,000 tokens) to fit within the LLM context window.
2. **LLM Translation**: Each chunk is sent to Ollama with a system prompt preserving Markdown formatting.
3. **Reassembly**: Translated chunks are reassembled into the final document.
4. **Formatting Preservation**: Headers, code blocks, tables, and lists are preserved.

### Configuration

| Environment Variable | Default | Description |
| :--- | :--- | :--- |
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama server URL |
| `OLLAMA_MODEL` | `llama3.2` | Model to use for translation |
| `OLLAMA_TIMEOUT` | `120` | Timeout per chunk (seconds) |

---

## 📂 Output Structure

Translated files are organized under `published/translations/`:

```
published/
└── translations/
    ├── Russian/
    │   └── courses/
    │       └── active-inference/
    │           ├── philosophy/...
    │           └── cognitive_science/...
    ├── Japanese/
    │   └── courses/...
    └── Hindi/
        └── courses/...
```

---

## 🔧 Troubleshooting

**Error**: `Connection refused` on translation

**Fix**: Ensure Ollama is running:

```bash
ollama serve
```

**Error**: Timeout on large files

**Fix**: Increase the timeout or use a faster model:

```bash
export OLLAMA_TIMEOUT=300
export OLLAMA_MODEL=llama3.2:1b
```

**Error**: Formatting lost in translation

**Fix**: The chunking algorithm preserves Markdown boundaries. If formatting is broken, try reducing chunk size or using a larger model.

---

## 📊 Requirements

- **Ollama** installed and running locally
- A compatible LLM model downloaded (e.g., `ollama pull llama3.2`)
- Sufficient disk space for translated outputs (~1x source size per language)

---
*Last Updated: 2026-02-15*
