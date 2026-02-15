# 📺 YouTube Pipeline

> **Navigation**: [← Docs Index](README.md) | [Modules](MODULES.md) | [CLI Reference](CLI_REFERENCE.md)

Turn YouTube playlists into structured course materials. The pipeline downloads transcripts (~2,600 videos in the archive), scaffolds them into the standard 4-unit × 8-module course structure, and renders them through the publishing engine.

---

## 🚀 Quick Start

```bash
cd software

# 1. Download transcripts (auto-caption or Whisper)
uv run python scripts/transcribe_youtube.py --video-id <ID>

# 2. Render playlists as courses
uv run python scripts/render_youtube_courses.py --course active-inference-textbook-group

# 3. Translate transcripts to another language
uv run python scripts/translate_youtube.py --lang ja
```

---

## 🛠️ Components

| Script | Purpose |
| :--- | :--- |
| `transcribe_youtube.py` | Downloads audio/captions. Uses **Whisper** if needed. |
| `render_youtube_courses.py` | Scaffolds course structure from transcripts. |
| `translate_youtube.py` | Translates transcript archives to target languages. |

---

## 📋 Workflow

```mermaid
graph LR
    A[YouTube Video] --> B[transcribe_youtube.py]
    B --> C[Raw Transcript .md]
    C --> D[render_youtube_courses.py]
    D --> E[Structured Course]
    E --> F[publish.py]
    F --> G[PDF / HTML / Audio]
```

1. **Transcription**: Downloads auto-captions or runs Whisper for higher accuracy.
2. **Scaffolding**: Injects real transcript content into the 4-unit × 8-module structure, replacing any template `module.md` files.
3. **Publishing**: The `publish.py` pipeline integrates this step automatically — see [ORCHESTRATION.md](ORCHESTRATION.md).

---

## 🎧 Whisper Setup

For high-quality transcription (when auto-captions are bad or missing), install Whisper:

```bash
# Install extra dependencies
uv sync --extra whisper

# Transcribe with Whisper
uv run python scripts/transcribe_youtube.py --whisper-model base

# Available models: tiny, base, small, medium, large
# Larger models = better accuracy, slower speed
```

**Tip**: Start with `base` for a good speed/accuracy tradeoff. Use `medium` or `large` for noisy audio or non-English content.

---

## 📊 Manifest

Tracking is stored in `course_development/youtube/manifest.json`. This file:

- Records every video ID that has been processed.
- Prevents re-downloading videos you've already transcribed.
- Stores metadata: title, channel, duration, transcript method (auto vs. Whisper).

```json
{
  "video_id": {
    "title": "ActInf Livestream 001.1",
    "channel": "Active Inference Institute",
    "duration_seconds": 3600,
    "method": "auto_caption",
    "processed_at": "2026-01-15T10:30:00Z"
  }
}
```

---

## 📂 Output Structure

```
course_development/youtube/
├── manifest.json
├── transcripts/
│   ├── <video_id_1>.md
│   ├── <video_id_2>.md
│   └── ...
└── rendered/
    └── active-inference-textbook-group/
        ├── 01_introduction/
        │   ├── 01_systems/module.md
        │   └── ...
        └── ...
```

---

## ⚠️ Known Limitations

- **Auto-captions** may have poor accuracy for technical terminology.
- **Rate limiting**: YouTube may throttle transcript downloads. Space out batch requests.
- **Whisper memory**: The `large` model requires ~10 GB VRAM.

---
*Last Updated: 2026-02-15*
