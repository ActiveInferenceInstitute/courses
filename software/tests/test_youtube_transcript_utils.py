"""Tests for youtube_transcript utility functions."""

import json
from pathlib import Path

import pytest

from src.youtube_transcript.utils import (
    clean_vtt_text,
    ensure_output_directory,
    load_manifest,
    parse_vtt_to_text,
    save_manifest,
)


class TestCleanVttText:
    """Tests for VTT text cleaning (offline)."""

    def test_strips_webvtt_header(self) -> None:
        raw = "WEBVTT\n\nhello world"
        assert clean_vtt_text(raw) == "hello world"

    def test_strips_timestamps(self) -> None:
        raw = (
            "WEBVTT\n\n"
            "00:00:01.000 --> 00:00:03.000\n"
            "hello world\n\n"
            "00:00:03.000 --> 00:00:05.000\n"
            "goodbye world"
        )
        result = clean_vtt_text(raw)
        assert "00:00" not in result
        assert "-->" not in result
        assert "hello world" in result
        assert "goodbye world" in result

    def test_strips_html_tags(self) -> None:
        raw = "WEBVTT\n\n<c.colorCCCCCC>hello</c> <b>world</b>"
        result = clean_vtt_text(raw)
        assert "<" not in result
        assert ">" not in result
        assert "hello" in result
        assert "world" in result

    def test_deduplicates_overlapping_segments(self) -> None:
        raw = (
            "WEBVTT\n\n"
            "00:00:01.000 --> 00:00:03.000\n"
            "hello world\n\n"
            "00:00:02.000 --> 00:00:04.000\n"
            "hello world\n\n"
            "00:00:04.000 --> 00:00:06.000\n"
            "goodbye"
        )
        result = clean_vtt_text(raw)
        assert result.count("hello world") == 1
        assert "goodbye" in result

    def test_strips_numeric_cue_ids(self) -> None:
        raw = "WEBVTT\n\n1\n00:00:01.000 --> 00:00:03.000\nhello\n\n2\n00:00:03.000 --> 00:00:05.000\nworld"
        result = clean_vtt_text(raw)
        assert result == "hello world"

    def test_strips_position_metadata(self) -> None:
        raw = "WEBVTT\n\n00:00:01.000 --> 00:00:03.000 position:10% align:start\nhello world"
        result = clean_vtt_text(raw)
        assert "position" not in result
        assert "align" not in result
        assert "hello world" in result

    def test_empty_file(self) -> None:
        assert clean_vtt_text("") == ""

    def test_header_only(self) -> None:
        assert clean_vtt_text("WEBVTT\n\n") == ""

    def test_inline_position_metadata(self) -> None:
        raw = "WEBVTT\n\nhello align:start position:0% world"
        result = clean_vtt_text(raw)
        assert "align:" not in result
        assert "position:" not in result
        assert "hello" in result
        assert "world" in result


class TestParseVttToText:
    """Tests for VTT file parsing (offline)."""

    def test_reads_and_cleans_vtt_file(self, tmp_path: Path) -> None:
        vtt_content = (
            "WEBVTT\n\n"
            "00:00:01.000 --> 00:00:03.000\n"
            "hello world\n\n"
            "00:00:03.000 --> 00:00:05.000\n"
            "goodbye world"
        )
        vtt_file = tmp_path / "test.vtt"
        vtt_file.write_text(vtt_content, encoding="utf-8")
        result = parse_vtt_to_text(vtt_file)
        assert "hello world" in result
        assert "goodbye world" in result
        assert "-->" not in result


class TestManifestIO:
    """Tests for manifest load/save (offline)."""

    def test_load_nonexistent_returns_empty(self, tmp_path: Path) -> None:
        manifest = load_manifest(tmp_path / "missing.json")
        assert manifest["videos"] == {}
        assert manifest["total_videos"] == 0

    def test_roundtrip(self, tmp_path: Path) -> None:
        manifest = {
            "channel_url": "https://example.com",
            "last_updated": "2025-01-01T00:00:00Z",
            "total_videos": 2,
            "videos": {
                "abc123": {
                    "title": "Test Video",
                    "duration": 120,
                    "upload_date": "20250101",
                    "method": "auto_caption",
                    "status": "completed",
                    "transcript_path": "transcripts/abc123.txt",
                    "error": None,
                }
            },
        }
        path = tmp_path / "manifest.json"
        save_manifest(manifest, path)

        loaded = load_manifest(path)
        assert loaded["channel_url"] == "https://example.com"
        assert loaded["total_videos"] == 2
        assert loaded["videos"]["abc123"]["title"] == "Test Video"
        assert loaded["videos"]["abc123"]["status"] == "completed"

    def test_atomic_write_creates_valid_json(self, tmp_path: Path) -> None:
        path = tmp_path / "manifest.json"
        manifest = {"channel_url": "test", "last_updated": "", "total_videos": 0, "videos": {}}
        save_manifest(manifest, path)
        # Verify it's valid JSON
        raw = path.read_text(encoding="utf-8")
        parsed = json.loads(raw)
        assert parsed == manifest

    def test_save_overwrites_existing(self, tmp_path: Path) -> None:
        path = tmp_path / "manifest.json"
        save_manifest({"channel_url": "first", "last_updated": "", "total_videos": 0, "videos": {}}, path)
        save_manifest({"channel_url": "second", "last_updated": "", "total_videos": 0, "videos": {}}, path)
        loaded = load_manifest(path)
        assert loaded["channel_url"] == "second"


class TestEnsureOutputDirectory:
    """Tests for directory creation (offline)."""

    def test_creates_nested_dirs(self, tmp_path: Path) -> None:
        target = tmp_path / "a" / "b" / "c"
        ensure_output_directory(target)
        assert target.is_dir()

    def test_idempotent(self, tmp_path: Path) -> None:
        target = tmp_path / "existing"
        target.mkdir()
        ensure_output_directory(target)
        assert target.is_dir()


@pytest.mark.requires_internet
class TestEnumerateChannelVideos:
    """Tests for channel enumeration (requires internet)."""

    def test_enumerate_active_inference(self) -> None:
        from src.youtube_transcript.utils import enumerate_channel_videos

        videos = enumerate_channel_videos("https://www.youtube.com/@ActiveInference")
        assert len(videos) > 0
        first = videos[0]
        assert "id" in first
        assert "title" in first
        assert len(first["id"]) == 11  # YouTube video IDs are 11 chars


@pytest.mark.requires_internet
class TestDownloadAutoCaptions:
    """Tests for caption download (requires internet)."""

    def test_download_captions_for_known_video(self, tmp_path: Path) -> None:
        from src.youtube_transcript.utils import download_auto_captions

        # Use a well-known Active Inference video that has captions
        # "ActInf Livestream #001" - one of the earliest, likely to have auto-captions
        result = download_auto_captions("qUJK1IDxKzg", tmp_path)
        # May or may not have captions; just verify no crash
        if result is not None:
            assert result.exists()
            assert result.suffix == ".vtt"
