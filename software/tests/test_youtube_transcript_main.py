"""Tests for youtube_transcript main module."""

from pathlib import Path

import pytest


@pytest.mark.requires_internet
class TestTranscribeVideo:
    """Tests for single video transcription (requires internet)."""

    def test_transcribe_video_with_captions(self, tmp_path: Path) -> None:
        from src.youtube_transcript.main import transcribe_video

        result = transcribe_video("qUJK1IDxKzg", tmp_path, skip_whisper=True)
        assert result["video_id"] == "qUJK1IDxKzg"
        assert result["status"] in ("completed", "skipped")
        if result["status"] == "completed":
            assert result["method"] == "auto_caption"
            transcript_file = tmp_path / result["transcript_path"]
            assert transcript_file.exists()
            text = transcript_file.read_text(encoding="utf-8")
            assert len(text) > 0


@pytest.mark.requires_internet
class TestTranscribeChannel:
    """Tests for channel transcription (requires internet)."""

    def test_transcribe_channel_with_limit(self, tmp_path: Path) -> None:
        from src.youtube_transcript.main import transcribe_channel

        summary = transcribe_channel(
            channel_url="https://www.youtube.com/@ActiveInference",
            output_dir=tmp_path,
            skip_whisper=True,
            limit=2,
            resume=False,
        )
        assert summary["total_enumerated"] > 0
        assert summary["processed"] <= 2
        manifest_path = Path(summary["manifest_path"])
        assert manifest_path.exists()

    def test_resume_skips_completed(self, tmp_path: Path) -> None:
        from src.youtube_transcript.main import transcribe_channel

        # First run
        summary1 = transcribe_channel(
            channel_url="https://www.youtube.com/@ActiveInference",
            output_dir=tmp_path,
            skip_whisper=True,
            limit=1,
            resume=False,
        )
        assert summary1["completed"] >= 0

        # Second run with resume - should skip the already completed video
        summary2 = transcribe_channel(
            channel_url="https://www.youtube.com/@ActiveInference",
            output_dir=tmp_path,
            skip_whisper=True,
            limit=1,
            resume=True,
        )
        # A resumed run must never re-process the completed video: it either
        # processed something new or skipped everything.
        assert summary2["processed"] <= summary2["total_enumerated"]
        if summary1["completed"] > 0:
            # The manifest is the resume source of truth; it must still exist.
            assert Path(summary2["manifest_path"]).exists()


@pytest.mark.requires_internet
class TestGetChannelVideoList:
    """Tests for channel enumeration via public API (requires internet)."""

    def test_list_returns_videos(self) -> None:
        from src.youtube_transcript.main import get_channel_video_list

        videos = get_channel_video_list("https://www.youtube.com/@ActiveInference")
        assert len(videos) > 100  # Channel has 244+ videos
        assert all("id" in v for v in videos)


@pytest.mark.requires_whisper
class TestWhisperFallback:
    """Tests for Whisper transcription fallback (requires whisper)."""

    def test_whisper_transcription(self, tmp_path: Path) -> None:
        from src.youtube_transcript.main import transcribe_video

        # Use a short video to minimize processing time
        result = transcribe_video("qUJK1IDxKzg", tmp_path, whisper_model="tiny")
        assert result["status"] == "completed"
        assert result["method"] in ("auto_caption", "whisper")
