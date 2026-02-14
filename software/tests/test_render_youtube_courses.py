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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "render_youtube_courses.py"
spec = importlib.util.spec_from_file_location("render_youtube_courses", SCRIPT_PATH)
render_youtube_script = importlib.util.module_from_spec(spec)
sys.modules["render_youtube_courses"] = render_youtube_script
spec.loader.exec_module(render_youtube_script)


@pytest.fixture
def script():
    return render_youtube_script


class TestRenderYoutubeCourses:
    
    def test_parse_args(self, script):
        args = script.parse_args(["--limit", "5", "--formats", "pdf,txt", "--dry-run"])
        assert args.limit == 5
        assert args.formats == "pdf,txt"
        assert args.dry_run is True

    @patch("render_youtube_courses.load_youtube_manifest")
    def test_main_dry_run(self, mock_load, script, caplog):
        mock_load.return_value = {
            "total_playlists": 1,
            "playlists": {"test-slug": {"title": "Test Playlist", "video_count": 2}}
        }
        
        # Bypass filesystem checks for existing course directories
        with patch("render_youtube_courses.Path.exists", return_value=False):
            with caplog.at_level("INFO"):
                exit_code = script.main(["--dry-run"])
                assert exit_code == 0
            
        assert "Dry run - 1 playlists" in caplog.text

    @patch("render_youtube_courses.enumerate_and_map_playlists")
    @patch("render_youtube_courses.save_youtube_manifest")
    def test_main_list_playlists(self, mock_save, mock_enum, script, caplog):
        mock_enum.return_value = {
            "total_playlists": 2,
            "playlists": {
                "slug1": {"title": "Title 1", "video_count": 1},
                "slug2": {"title": "Title 2", "video_count": 2}
            }
        }
        
        with caplog.at_level("INFO"):
            exit_code = script.main(["--list-playlists", "--dry-run"])
            assert exit_code == 0
        
        assert "Playlists (2):" in caplog.text
        mock_save.assert_not_called() # because of --dry-run

    @patch("render_youtube_courses.load_youtube_manifest")
    @patch("render_youtube_courses.scaffold_course_directory")
    @patch("render_youtube_courses.render_all_youtube_courses")
    def test_main_execution(self, mock_render, mock_scaffold, mock_load, script):
        mock_load.return_value = {
            "playlists": {"slug1": {"title": "Title 1", "videos": []}}
        }
        mock_scaffold.return_value = {"created": 1, "skipped": 0, "failed": 0}
        mock_render.return_value = {"total_rendered": 1, "total_errors": []}
        
        # Bypass filesystem checks for directories
        with patch("render_youtube_courses.Path.mkdir"):
             with patch("render_youtube_courses.Path.exists", return_value=True):
                exit_code = script.main(["--skip-whisper"])
                assert exit_code == 0
                
        mock_scaffold.assert_called_once()
        mock_render.assert_called_once()
