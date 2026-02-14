# YouTube Transcript Archive — Agent Guidelines

> **Quick Navigation**: [Course Development AGENTS.md](../AGENTS.md) | [Root AGENTS.md](../../AGENTS.md) | [README](./README.md)

## Overview

This directory contains structured transcripts from **38 playlists** (~2,600 videos) from the Active Inference Institute YouTube channel. These are source materials — not hand-authored course content.

---

## Critical Rules

### 1. Transcripts Are Auto-Generated

Transcript files are produced by `scripts/transcribe_youtube.py`. They may contain transcription artifacts (misspellings, missing punctuation, speaker misattributions). When using transcripts as source material:

- Do not treat transcript text as authoritative for technical terms
- Cross-reference technical claims against published papers
- Use the course's `resources/glossary.md` for canonical terminology

### 2. Do Not Hand-Edit Transcripts

Transcripts should be regenerated via the transcription pipeline rather than manually corrected. Manual edits will be lost on the next transcription run.

### 3. Playlist Metadata

The `youtube_courses.json` file at this directory level contains playlist metadata and mappings. Do not modify this file unless updating playlist configurations.

### 4. Rendering

To render transcripts as course materials:

```bash
uv run python scripts/render_youtube_courses.py
```

Rendered outputs go to `published/youtube/`.

---

## Directory Structure

Each subdirectory corresponds to one YouTube playlist:

```text
youtube/
├── active-inference-livestreams-paper-discussions/
├── gueststreams/
├── mathstreams/
├── modelstreams/
├── artstream/
├── bookstreams/
├── ...  (38 playlist directories)
└── youtube_courses.json
```

---

> *"Minimize surprise. Maximize evidence."* — Active Inference Institute
