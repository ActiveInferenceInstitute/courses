"""Tests for the import_legacy_materials script.

Uses real function calls with temporary file structures where possible.
monkeypatch replaces only functions that touch external filesystem
paths that don't exist in CI.
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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "import_legacy_materials.py"
spec = importlib.util.spec_from_file_location("import_legacy_materials", SCRIPT_PATH)
import_legacy_materials = importlib.util.module_from_spec(spec)
sys.modules["import_legacy_materials"] = import_legacy_materials
spec.loader.exec_module(import_legacy_materials)


@pytest.fixture
def script():
    return import_legacy_materials


class TestImportLegacyMaterials:
    def test_parse_args(self, script):
        args = script.parse_args(["--course", "ai-math", "--dry-run", "--skip-questions"])
        assert args.course == "ai-math"
        assert args.dry_run is True
        assert args.skip_questions is True

    def test_main_dry_run(self, script, capsys, monkeypatch):
        """main() calls process_slides and process_chapter_questions in dry-run mode."""
        calls = {"slides": [], "questions": []}

        def fake_slides(src, dst, dry_run=False):
            calls["slides"].append((src, dst, dry_run))
            return True

        def fake_questions(src, dst, dry_run=False):
            calls["questions"].append((src, dst, dry_run))
            return True

        monkeypatch.setattr(import_legacy_materials, "process_slides", fake_slides)
        monkeypatch.setattr(import_legacy_materials, "process_chapter_questions", fake_questions)
        # Make the path-existence check pass
        monkeypatch.setattr(Path, "exists", lambda self: True)

        exit_code = script.main(["--dry-run", "--course", "ai-philosophy"])
        assert exit_code == 0

        assert len(calls["questions"]) == 1
        assert len(calls["slides"]) == 1
        # Verify dry_run was forwarded correctly
        assert calls["questions"][0][2] is True
        assert calls["slides"][0][2] is True

    def test_main_module_not_found(self, script):
        """main() raises SystemExit for invalid course (argparse choice validation)."""
        with pytest.raises(SystemExit):
            script.main(["--course", "INVALID"])

    def test_main_execution(self, script, monkeypatch):
        """main() calls both process functions with dry_run=False."""
        calls = {"slides": [], "questions": []}

        def fake_slides(src, dst, dry_run=False):
            calls["slides"].append((src, dst, dry_run))
            return True

        def fake_questions(src, dst, dry_run=False):
            calls["questions"].append((src, dst, dry_run))
            return True

        monkeypatch.setattr(import_legacy_materials, "process_slides", fake_slides)
        monkeypatch.setattr(import_legacy_materials, "process_chapter_questions", fake_questions)
        monkeypatch.setattr(Path, "exists", lambda self: True)

        exit_code = script.main(["--course", "ai-philosophy"])
        assert exit_code == 0

        assert calls["questions"][0][2] is False
        assert calls["slides"][0][2] is False
