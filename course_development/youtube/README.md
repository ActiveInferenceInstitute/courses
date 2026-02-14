# YouTube Transcript Archive

> **Navigation**: [Course Development](../README.md) | [Root README](../../README.md) | [AGENTS.md](AGENTS.md)

## Overview

This directory contains structured transcripts from **38 playlists** covering the Active Inference Institute's [YouTube channel](https://www.youtube.com/@ActiveInference), totaling approximately **2,600 videos**.

---

## Playlist Categories

| Category | Playlists | Highlights |
|----------|-----------|------------|
| **Lecture Series** | Livestreams, FEP Lectures, Podcasts | 1,000+ paper discussions |
| **Guest Speakers** | GuestStreams | Invited experts across disciplines |
| **Textbook Groups** | Cohorts 1, 3, 4, 6, 7, 8, 9 | Parr et al. textbook deep dives |
| **Symposia** | Applied AI Symposia 2021–2025 | Annual applied research |
| **Specialized** | MathStreams, ModelStreams, ArtStream, BookStreams | Domain-specific sessions |
| **Community** | OrgStream, ReviewStreams, MorphStream | Organizational & review content |
| **Special Series** | Chris Fields (Physics as Info Processing), John Boik, Blockference | Invited lecture series |

---

## Directory Structure

Each playlist has its own subdirectory containing individual transcript files:

```text
youtube/
├── active-inference-livestreams-paper-discussions/
│   ├── transcript_001.md
│   ├── transcript_002.md
│   └── ...
├── gueststreams/
├── mathstreams/
├── ...
└── youtube_courses.json     # Playlist metadata
```

---

## Processing

Transcripts are downloaded and processed via the software pipeline:

```bash
# Download new transcripts
uv run python scripts/transcribe_youtube.py

# Translate transcripts
uv run python scripts/translate_youtube.py

# Render as course materials
uv run python scripts/render_youtube_courses.py
```

---

## Notes

- Transcripts are auto-generated and may contain transcription artifacts
- The `youtube_courses.json` file maps playlists to course structures
- Rendered outputs appear in `published/youtube/`

---

> *"Minimize surprise. Maximize evidence."* — Active Inference Institute
