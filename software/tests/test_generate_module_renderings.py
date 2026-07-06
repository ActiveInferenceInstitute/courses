"""Tests for the generate_module_renderings script.

Uses real function calls where possible; monkeypatch only for
path discovery so tests aren't tied to the real repo layout.
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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "generate_module_renderings.py"
spec = importlib.util.spec_from_file_location("generate_module_renderings", SCRIPT_PATH)
generate_module_renderings = importlib.util.module_from_spec(spec)
sys.modules["generate_module_renderings"] = generate_module_renderings
spec.loader.exec_module(generate_module_renderings)


@pytest.fixture
def script():
    return generate_module_renderings


class TestGenerateModuleRenderings:

    def test_parse_args(self, script):
        args = script.parse_args(["--course", "ai-philosophy", "--module", "2"])
        assert args.course == "ai-philosophy"
        assert args.module == 2

    def test_main_execution(self, script, temp_dir, monkeypatch):
        """main() calls process_module_by_type for each content type found."""
        # Build a module directory under temp_dir
        module_path = temp_dir / "active_inference" / "01_philosophy" / "module-01-intro"
        module_path.mkdir(parents=True)
        (module_path / "lab.md").write_text("lab content", "utf-8")

        calls = []

        def fake_process(mod_dir, out_dir, **kwargs):
            calls.append((mod_dir, out_dir))
            return {"by_type": {}, "summary": {}, "errors": [], "assignments": {}}

        def fake_find(course_path, module_num):
            return module_path

        monkeypatch.setattr(generate_module_renderings, "find_module_path", fake_find)
        monkeypatch.setattr(generate_module_renderings, "process_module_by_type", fake_process)

        exit_code = script.main(["--course", "ai-philosophy", "--module", "1"])
        assert exit_code == 0

        # Should have been called: 1 for module + 1 for lab (lab.md exists)
        assert len(calls) == 2

        # Check call arguments
        assert str(module_path) == calls[0][0]
        assert str(module_path / "output") == calls[0][1]

    def test_main_module_not_found(self, script, capsys, monkeypatch):
        def fake_find(course_path, module_num):
            return None

        monkeypatch.setattr(generate_module_renderings, "find_module_path", fake_find)

        exit_code = script.main(["--course", "ai-philosophy", "--module", "99"])
        assert exit_code == 1

        captured = capsys.readouterr()
        assert "Error: Module 99 not found" in captured.out
