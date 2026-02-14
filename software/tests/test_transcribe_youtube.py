import importlib.util
import sys
from pathlib import Path
import pytest
from unittest.mock import MagicMock, patch

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

    @patch("transcribe_youtube.transcribe_video")
    def test_main_single_video(self, mock_transcribe, script, temp_dir):
        mock_transcribe.return_value = {
            "status": "completed",
            "method": "captions",
            "transcript_path": "transcript.md"
        }
        
        exit_code = script.main(["--video-id", "test123", "--output", str(temp_dir)])
        assert exit_code == 0
        mock_transcribe.assert_called_once()

    @patch("transcribe_youtube.get_channel_video_list")
    def test_main_list_only(self, mock_get_list, script, temp_dir, caplog):
        mock_get_list.return_value = [
            {"id": "v1", "title": "Video 1", "duration": 60, "upload_date": "2023-01-01"},
            {"id": "v2", "title": "Video 2", "duration": 120, "upload_date": "2023-01-02"}
        ]
        
        with caplog.at_level("INFO"):
            exit_code = script.main(["--list-only", "--output", str(temp_dir)])
            assert exit_code == 0
            
        assert "Found 2 videos" in caplog.text
        assert "Manifest saved" in caplog.text
        assert (temp_dir / "manifest.json").exists()

    @patch("transcribe_youtube.get_channel_video_list")
    def test_main_dry_run(self, mock_get_list, script, temp_dir, caplog):
        mock_get_list.return_value = [{"id": "v1", "title": "V1"}]
        
        with caplog.at_level("INFO"):
            exit_code = script.main(["--dry-run", "--output", str(temp_dir)])
            assert exit_code == 0
            
        assert "DRY RUN: Would transcribe" in caplog.text

    @patch("transcribe_youtube.transcribe_channel")
    def test_main_full_transcription(self, mock_transcribe_channel, script, temp_dir):
        mock_transcribe_channel.return_value = {
            "total_enumerated": 2,
            "processed": 1,
            "completed": 1,
            "failed": 0,
            "manifest_path": "manifest.json"
        }
        
        exit_code = script.main(["--limit", "1", "--output", str(temp_dir)])
        assert exit_code == 0
        mock_transcribe_channel.assert_called_once()
