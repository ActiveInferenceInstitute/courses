"""Tests for the publish_course script.

Tests that publish to real course directories are marked with
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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "publish_course.py"
spec = importlib.util.spec_from_file_location("publish_course", SCRIPT_PATH)
publish_course_script = importlib.util.module_from_spec(spec)
sys.modules["publish_course"] = publish_course_script
spec.loader.exec_module(publish_course_script)


@pytest.fixture
def script():
    return publish_course_script


class TestPublishCourse:
    def test_parse_args(self, script):
        args = script.parse_args(["--course", "ai-math"])
        assert args.course == "ai-math"

    def test_main_invalid_course(self, script):
        with pytest.raises(SystemExit):
            script.main(["--course", "INVALID"])

    @pytest.mark.requires_api
    def test_main_execution(self, script, temp_dir, monkeypatch):
        """main() calls publish_course and returns 0 on success (requires real paths)."""
        fake_result = {
            "course": "Philosophy",
            "modules_published": 1,
            "syllabus_files": 1,
            "total_files": 2,
            "modules": [{"name": "module-01", "files": 2}],
        }

        monkeypatch.setattr(publish_course_script, "publish_course", lambda *a, **kw: fake_result)
        monkeypatch.setattr(Path, "exists", lambda self: True)

        exit_code = script.main(["--course", "ai-philosophy"])
        assert exit_code == 0

    @pytest.mark.requires_api
    def test_main_all(self, script, temp_dir, monkeypatch):
        """main() calls publish_course once per registered course (requires real paths)."""
        from src.batch_processing.config import COURSE_REGISTRY

        call_count = []

        def fake_publish(*args, **kwargs):
            call_count.append(1)
            return {
                "course": "Any",
                "modules_published": 0,
                "syllabus_files": 0,
                "total_files": 0,
                "modules": [],
            }

        monkeypatch.setattr(publish_course_script, "publish_course", fake_publish)
        monkeypatch.setattr(Path, "exists", lambda self: True)

        exit_code = script.main(["--course", "all"])
        assert exit_code == 0
        assert len(call_count) == len(COURSE_REGISTRY)
