"""Tests for the generate_syllabus_renderings script.

Uses real process_syllabus calls with temporary file structures.
monkeypatch replaces only the repo_root discovery so tests aren't
tied to the real repository layout on disk.
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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "generate_syllabus_renderings.py"
spec = importlib.util.spec_from_file_location("generate_syllabus_renderings", SCRIPT_PATH)
generate_syllabus_renderings = importlib.util.module_from_spec(spec)
sys.modules["generate_syllabus_renderings"] = generate_syllabus_renderings
spec.loader.exec_module(generate_syllabus_renderings)


@pytest.fixture
def script():
    return generate_syllabus_renderings


class TestGenerateSyllabusRenderings:

    def test_parse_args(self, script):
        args = script.parse_args(["--course", "ai-math"])
        assert args.course == "ai-math"

    def test_main_simplified(self, script, monkeypatch):
        """main() calls process_syllabus and exits 0 when it finds the syllabus dir."""
        calls = []

        def fake_process(syllabus_dir, output_dir, **kwargs):
            calls.append(syllabus_dir)
            return {
                "summary": {"pdf": 1, "mp3": 0, "docx": 0, "html": 0, "txt": 0, "md": 0},
                "by_format": {"pdf": ["test.pdf"], "mp3": [], "docx": [], "html": [], "txt": [], "md": []},
                "errors": [],
            }

        monkeypatch.setattr(generate_syllabus_renderings, "process_syllabus", fake_process)
        monkeypatch.setattr(Path, "exists", lambda self: True)

        exit_code = script.main(["--course", "ai-philosophy"])
        assert exit_code == 0
        assert len(calls) == 1

    def test_main_with_real_syllabus_dir(self, script, temp_dir, monkeypatch):
        """main() succeeds when a real syllabus directory is present."""
        from src.batch_processing.config import COURSE_REGISTRY

        # Build a temp repo structure matching the registry rel_path for ai-philosophy
        rel_path = COURSE_REGISTRY["ai-philosophy"]["rel_path"]
        syllabus_path = temp_dir / rel_path / "syllabus"
        syllabus_path.mkdir(parents=True)
        (syllabus_path / "Syllabus.md").write_text("# Syllabus\n\nOverview.", encoding="utf-8")

        # Redirect the script's repo_root resolution to our temp_dir
        calls = []

        def fake_process(syllabus_dir, output_dir, **kwargs):
            calls.append(str(syllabus_dir))
            return {
                "summary": {"pdf": 0, "mp3": 0, "docx": 0, "html": 0, "txt": 1, "md": 0},
                "by_format": {"pdf": [], "mp3": [], "docx": [], "html": [], "txt": ["file.txt"], "md": []},
                "errors": [],
            }

        monkeypatch.setattr(generate_syllabus_renderings, "process_syllabus", fake_process)

        # Redirect the module's COURSE_REGISTRY reference
        monkeypatch.setattr(generate_syllabus_renderings, "COURSE_REGISTRY", COURSE_REGISTRY)
        # Use Path.exists to pass the syllabus_path check
        real_exists = Path.exists

        def patched_exists(self):
            if "syllabus" in str(self):
                return True
            return real_exists(self)

        monkeypatch.setattr(Path, "exists", patched_exists)

        exit_code = script.main(["--course", "ai-philosophy"])
        assert exit_code == 0
