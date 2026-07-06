"""Tests for the generate_module_website script.

Uses real function calls with temporary file structures.
monkeypatch replaces only path discovery so tests aren't tied
to the real repository layout.
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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "generate_module_website.py"
spec = importlib.util.spec_from_file_location("generate_module_website", SCRIPT_PATH)
generate_module_website = importlib.util.module_from_spec(spec)
sys.modules["generate_module_website"] = generate_module_website
spec.loader.exec_module(generate_module_website)


@pytest.fixture
def script():
    return generate_module_website


class TestGenerateModuleWebsite:

    def test_parse_args(self, script):
        args = script.parse_args(["--course", "ai-philosophy", "--module", "3"])
        assert args.course == "ai-philosophy"
        assert args.module == 3

    def test_main_execution(self, script, temp_dir, monkeypatch):
        """main() calls process_module_website for the resolved module path."""
        module_path = temp_dir / "active_inference" / "01_philosophy" / "module-01-intro"
        module_path.mkdir(parents=True)

        process_calls = []

        def fake_find(course_path, module_num):
            return module_path

        def fake_process(mod_dir, output_dir=None):
            process_calls.append(mod_dir)
            return str(module_path / "output" / "website" / "index.html")

        monkeypatch.setattr(generate_module_website, "find_module_path", fake_find)
        monkeypatch.setattr(generate_module_website, "process_module_website", fake_process)

        exit_code = script.main(["--course", "ai-philosophy", "--module", "1"])
        assert exit_code == 0

        assert len(process_calls) == 1
        assert process_calls[0] == str(module_path)

    def test_main_module_not_found(self, script, capsys, monkeypatch):
        monkeypatch.setattr(generate_module_website, "find_module_path", lambda cp, n: None)

        exit_code = script.main(["--course", "ai-philosophy", "--module", "99"])
        assert exit_code == 1

        captured = capsys.readouterr()
        assert "Error: Module 99 not found" in captured.out
