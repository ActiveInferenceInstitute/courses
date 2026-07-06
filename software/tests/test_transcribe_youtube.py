"""Tests for the transcribe_youtube script.

Tests that require real YouTube/network access are marked with
@pytest.mark.requires_api — run them with: pytest -m requires_api
"""

import importlib.util
import sys
from pathlib import Path
import pytest

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Load the script
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "transcribe_youtube.py"
spec = importlib.util.spec_from_file_location("transcribe_youtube", SCRIPT_PATH)
transcribe_youtube_script = importlib.util.module_from_spec(spec)
sys.modules["transcribe_youtube"] = transcribe_youtube_script
spec.loader.exec_module(transcribe_youtube_script)


@pytest.fixture
def script():
    return transcribe_youtube_script


class TestTranscribeYoutube:

    def test_parse_args(self, script):
        args = script.parse_args(["--video-id", "test123", "--limit", "10", "--dry-run"])
        assert args.video_id == "test123"
        assert args.limit == 10
        assert args.dry_run is True

    @pytest.mark.requires_api
    def test_main_single_video(self, script, temp_dir, monkeypatch):
        """main() calls transcribe_video for a single video-id (requires API)."""
        results = []

        def fake_transcribe(video_id, output_dir, **kwargs):
            results.append(video_id)
            return {
                "status": "completed",
                "method": "captions",
                "transcript_path": str(output_dir / "transcript.md"),
            }

        monkeypatch.setattr(transcribe_youtube_script, "transcribe_video", fake_transcribe)

        exit_code = script.main(["--video-id", "test123", "--output", str(temp_dir)])
        assert exit_code == 0
        assert len(results) == 1

    @pytest.mark.requires_api
    def test_main_list_only(self, script, temp_dir, caplog, monkeypatch):
        """main() lists videos and saves manifest without transcribing (requires API)."""
        fake_videos = [
            {"id": "v1", "title": "Video 1", "duration": 60, "upload_date": "2023-01-01"},
            {"id": "v2", "title": "Video 2", "duration": 120, "upload_date": "2023-01-02"},
        ]

        monkeypatch.setattr(
            transcribe_youtube_script, "get_channel_video_list", lambda **kw: fake_videos
        )

        with caplog.at_level("INFO"):
            exit_code = script.main(["--list-only", "--output", str(temp_dir)])
            assert exit_code == 0

        assert "Found 2 videos" in caplog.text
        assert "Manifest saved" in caplog.text
        assert (temp_dir / "manifest.json").exists()

    @pytest.mark.requires_api
    def test_main_dry_run(self, script, temp_dir, caplog, monkeypatch):
        """main() prints DRY RUN message without actually transcribing (requires API)."""
        monkeypatch.setattr(
            transcribe_youtube_script,
            "get_channel_video_list",
            lambda **kw: [{"id": "v1", "title": "V1"}],
        )

        with caplog.at_level("INFO"):
            exit_code = script.main(["--dry-run", "--output", str(temp_dir)])
            assert exit_code == 0

        assert "DRY RUN: Would transcribe" in caplog.text

    @pytest.mark.requires_api
    def test_main_full_transcription(self, script, temp_dir, monkeypatch):
        """main() delegates to transcribe_channel for full runs (requires API)."""
        result = {
            "total_enumerated": 2,
            "processed": 1,
            "completed": 1,
            "failed": 0,
            "manifest_path": str(temp_dir / "manifest.json"),
        }
        monkeypatch.setattr(
            transcribe_youtube_script, "transcribe_channel", lambda **kw: result
        )

        exit_code = script.main(["--limit", "1", "--output", str(temp_dir)])
        assert exit_code == 0
