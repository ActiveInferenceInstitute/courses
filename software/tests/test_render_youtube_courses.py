"""Tests for the render_youtube_courses script.

Tests that scaffold/render real YouTube course directories are
marked with @pytest.mark.requires_api.
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

    @pytest.mark.requires_api
    def test_main_dry_run(self, script, caplog, monkeypatch):
        """main() reports dry-run summary without touching filesystem (requires API)."""
        fake_manifest = {
            "total_playlists": 1,
            "playlists": {"test-slug": {"title": "Test Playlist", "video_count": 2}},
        }
        monkeypatch.setattr(render_youtube_script, "load_youtube_manifest", lambda p: fake_manifest)
        monkeypatch.setattr(Path, "exists", lambda self: False)

        with caplog.at_level("INFO"):
            exit_code = script.main(["--dry-run"])
            assert exit_code == 0

        assert "Dry run - 1 playlists" in caplog.text

    @pytest.mark.requires_api
    def test_main_list_playlists(self, script, caplog, monkeypatch):
        """main() lists playlists without scaffolding (requires API)."""
        fake_result = {
            "total_playlists": 2,
            "playlists": {
                "slug1": {"title": "Title 1", "video_count": 1},
                "slug2": {"title": "Title 2", "video_count": 2},
            },
        }
        save_calls = []
        monkeypatch.setattr(
            render_youtube_script, "enumerate_and_map_playlists", lambda **kw: fake_result
        )
        monkeypatch.setattr(
            render_youtube_script, "save_youtube_manifest", lambda m, p: save_calls.append(m)
        )

        with caplog.at_level("INFO"):
            exit_code = script.main(["--list-playlists", "--dry-run"])
            assert exit_code == 0

        assert "Playlists (2):" in caplog.text
        assert len(save_calls) == 0  # --dry-run suppresses save

    @pytest.mark.requires_api
    def test_main_execution(self, script, monkeypatch):
        """main() scaffolds and renders courses (requires API)."""
        fake_manifest = {
            "playlists": {"slug1": {"title": "Title 1", "videos": []}}
        }
        scaffold_calls = []
        render_calls = []

        monkeypatch.setattr(render_youtube_script, "load_youtube_manifest", lambda p: fake_manifest)
        monkeypatch.setattr(
            render_youtube_script,
            "scaffold_course_directory",
            lambda *a, **kw: scaffold_calls.append(1) or {"created": 1, "skipped": 0, "failed": 0},
        )
        monkeypatch.setattr(
            render_youtube_script,
            "render_all_youtube_courses",
            lambda *a, **kw: render_calls.append(1) or {"total_rendered": 1, "total_errors": []},
        )
        monkeypatch.setattr(Path, "mkdir", lambda self, **kw: None)
        monkeypatch.setattr(Path, "exists", lambda self: True)

        exit_code = script.main(["--skip-whisper"])
        assert exit_code == 0

        assert len(scaffold_calls) == 1
        assert len(render_calls) == 1
