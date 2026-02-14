# 📺 YouTube Pipeline

> **Navigation**: [← Docs Index](README.md) | [Modules](MODULES.md) | [CLI Reference](CLI_REFERENCE.md)

Turn YouTube playlists into structured course materials.

---

## 🚀 Quick Start

```bash
cd software

# 1. Download transcripts (auto-caption or Whisper)
uv run python scripts/transcribe_youtube.py --video-id <ID>

# 2. Render playlists as courses
uv run python scripts/render_youtube_courses.py --course active-inference-textbook-group
```

---

## 🛠️ Components

| Script | Purpose |
| :--- | :--- |
| `transcribe_youtube.py` | Downloads audio/captions. Uses **Whisper** if needed. |
| `render_youtube_courses.py` | Scaffolds course structure from transcripts. |

---

## 🎧 Whisper Setup

For high-quality transcription (when auto-captions are bad/missing), you need `openai-whisper`.

```bash
# Install extra dependencies
uv sync --extra whisper

# usage
uv run python scripts/transcribe_youtube.py --whisper-model base
```

---

## 📊 Manifest

Tracking is stored in `course_development/youtube/manifest.json`. This prevents re-downloading videos you've already processed.

---
*Last Updated: 2026-02-14*
