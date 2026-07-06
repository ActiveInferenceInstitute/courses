"""Tests for the publish_all script.

Tests that orchestrate the full publish pipeline are marked with
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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "publish_all.py"
spec = importlib.util.spec_from_file_location("publish_all", SCRIPT_PATH)
publish_all = importlib.util.module_from_spec(spec)
sys.modules["publish_all"] = publish_all
spec.loader.exec_module(publish_all)


@pytest.fixture
def script():
    return publish_all


class TestPublishAll:

    def test_parse_args(self, script):
        args = script.parse_args(["--clean", "--skip-mp3", "--formats", "pdf,html"])
        assert args.clean is True
        assert args.skip_mp3 is True
        assert args.formats == "pdf,html"

    @pytest.mark.requires_api
    def test_main_execution(self, script, temp_dir, monkeypatch):
        """main() orchestrates generate → publish → validate pipeline (requires API)."""
        run_calls = []

        def fake_run(script_name, *args, **kwargs):
            run_calls.append(script_name)
            return True

        monkeypatch.setattr(publish_all, "run_script", fake_run)
        monkeypatch.setattr(publish_all, "clean_published", lambda *a, **kw: None)
        monkeypatch.setattr(publish_all, "copy_labs_and_dashboards", lambda *a, **kw: 5)
        monkeypatch.setattr(publish_all, "copy_slides", lambda *a, **kw: 2)
        monkeypatch.setattr(publish_all, "copy_slides_to_modules", lambda *a, **kw: 2)
        monkeypatch.setattr(publish_all, "copy_practice_tests", lambda *a, **kw: 1)
        monkeypatch.setattr(publish_all, "flatten_published", lambda *a, **kw: 10)
        monkeypatch.setattr(publish_all, "reorganize_to_categories", lambda *a, **kw: 10)
        monkeypatch.setattr(publish_all, "get_repo_root", lambda: temp_dir)

        # Create PUBLISHED dir so the summary print doesn't crash
        (temp_dir / "PUBLISHED").mkdir()

        exit_code = script.main(["--skip-mp3"])
        assert exit_code == 0

        # --clean was NOT passed, so clean_published should not be called
        # Verify orchestration order
        assert run_calls[0] == "generate_all_outputs.py"
        assert run_calls[1] == "publish_course.py"
        assert run_calls[2] == "validate_outputs.py"

    @pytest.mark.requires_api
    def test_main_failure(self, script, temp_dir, monkeypatch):
        """main() returns 1 when a script in the pipeline fails (requires API)."""
        monkeypatch.setattr(publish_all, "run_script", lambda *a, **kw: False)
        monkeypatch.setattr(publish_all, "get_repo_root", lambda: temp_dir)

        exit_code = script.main([])
        assert exit_code == 1
