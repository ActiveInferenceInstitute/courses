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

    @patch("generate_module_renderings.find_module_path")
    @patch("generate_module_renderings.process_module_by_type")
    def test_main_execution(self, mock_process, mock_find, script, temp_dir):
        # Setup mock
        module_path = temp_dir / "active_inference" / "01_philosophy" / "module-01-intro"
        module_path.mkdir(parents=True)
        (module_path / "lab.md").write_text("lab content", "utf-8")
        
        mock_find.return_value = module_path
        
        # Test main
        exit_code = script.main(["--course", "ai-philosophy", "--module", "1"])
        assert exit_code == 0
        
        # Verify process calls
        # 1. Module (Lecture)
        # 2. Lab (since lab.md exists)
        # 3. Questions (not called since questions.md doesn't exist)
        assert mock_process.call_count == 2
        
        # Check call arguments (path strings)
        args, _ = mock_process.call_args_list[0]
        assert str(module_path) == args[0]
        assert str(module_path / "output") == args[1]

    @patch("generate_module_renderings.find_module_path")
    def test_main_module_not_found(self, mock_find, script, capsys):
        mock_find.return_value = None
        
        exit_code = script.main(["--course", "ai-philosophy", "--module", "99"])
        assert exit_code == 1
        
        captured = capsys.readouterr()
        assert "Error: Module 99 not found" in captured.out
