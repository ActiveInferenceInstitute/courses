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

    @patch("generate_module_website.find_module_path")
    @patch("generate_module_website.process_module_website")
    def test_main_execution(self, mock_process, mock_find, script, temp_dir):
        # Setup mock module path
        module_path = temp_dir / "active_inference" / "01_philosophy" / "module-01-intro"
        module_path.mkdir(parents=True)
        
        mock_find.return_value = module_path
        
        # Test main
        exit_code = script.main(["--course", "ai-philosophy", "--module", "1"])
        assert exit_code == 0
        
        # Verify process call
        mock_process.assert_called_once_with(str(module_path))

    @patch("generate_module_website.find_module_path")
    def test_main_module_not_found(self, mock_find, script, capsys):
        mock_find.return_value = None
        
        exit_code = script.main(["--course", "ai-philosophy", "--module", "99"])
        assert exit_code == 1
        
        captured = capsys.readouterr()
        assert "Error: Module 99 not found" in captured.out
