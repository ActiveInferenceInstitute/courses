# specialized-agent: youtube_transcript

> **Purpose**: Download and process YouTube transcripts for course generation.
> **Key Function**: `transcribe_channel()`

## Overview

The `youtube_transcript` module automates the retrieval of transcripts from YouTube videos and channels. It supports:

1. **Auto-captions**: Downloading and parsing VTT files.
2. **Whisper Fallback**: Downloding audio and transcribing locally using OpenAI Whisper if captions are missing.
3. **Channel Enumeration**: Listing all videos in a channel.
4. **Course Scaffolding**: Converting playlists into course directory structures (`render_all_youtube_courses`).

## Public API

### Transcription

#### `transcribe_channel(...)`

Transcribe all videos from a YouTube channel.

- **Args**: `channel_url`, `output_dir`, `whisper_model`, `skip_whisper`, `limit`, `resume`.
- **Returns**: Summary dict with counts and manifest path.

#### `transcribe_video(...)`

Transcribe a single YouTube video.

- **Args**: `video_id`, `output_dir`, `whisper_model`.
- **Returns**: Dict with status, method (`auto_caption` or `whisper`), and transcript path.

### Enumeration

#### `get_channel_video_list(channel_url) -> List[Dict]`

List video metadata (ID, title, duration) without transcribing.

#### `enumerate_channel_playlists(channel_url) -> List[Dict]`

List all playlists in a channel.

#### `enumerate_playlist_videos(playlist_url) -> List[Dict]`

List all videos in a specific playlist.

### Rendering

#### `render_all_youtube_courses(youtube_courses_dir, ...)`

Scaffold and render active inference courses from YouTube playlists.

- **Process**:
  1. Enumerates playlists.
  2. Creates course directories based on playlist names.
  3. Creates `module.md` files from transcripts.
  4. Runs the standard `batch_processing` pipeline to generate PDFs, etc.

## Usage

```python
from src.youtube_transcript.main import transcribe_channel

# Transcribe an entire channel
summary = transcribe_channel(
    channel_url="https://www.youtube.com/@ActiveInference",
    whisper_model="base"
)
```

## Dependencies

- **External**: `yt-dlp` (video/caption download), `openai-whisper` (optional, for fallback).
- **Internal**: `batch_processing` (for rendering courses).
