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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "validate_outputs.py"
spec = importlib.util.spec_from_file_location("validate_outputs", SCRIPT_PATH)
validate_outputs_script = importlib.util.module_from_spec(spec)
sys.modules["validate_outputs"] = validate_outputs_script
spec.loader.exec_module(validate_outputs_script)


@pytest.fixture
def script():
    return validate_outputs_script


class TestValidateOutputs:
    
    def test_parse_args(self, script):
        args = script.parse_args(["--course", "ai-philosophy", "--formats", "pdf,html", "--json"])
        assert args.course == "ai-philosophy"
        assert args.formats == "pdf,html"
        assert args.json is True

    @patch("validate_outputs.validate_outputs")
    def test_main_execution_success(self, mock_validate, script, tmp_path):
        mock_validate.return_value = {
            "course": "ai-philosophy",
            "valid": True,
            "modules_checked": 8,
            "modules_valid": 8,
            "issues": []
        }
        
        # Setup repo structure: tmp_path is software_dir, tmp_path.parent is repo_root
        repo_root = tmp_path.parent
        (repo_root / "course_development" / "ai-philosophy").mkdir(parents=True, exist_ok=True)
        
        with patch("validate_outputs.software_dir", tmp_path):
            exit_code = script.main(["--course", "ai-philosophy"])
            assert exit_code == 0
        mock_validate.assert_called_once()

    @patch("validate_outputs.validate_outputs")
    def test_main_execution_failure(self, mock_validate, script, tmp_path):
        mock_validate.return_value = {
            "course": "ai-math",
            "valid": False,
            "modules_checked": 8,
            "modules_valid": 7,
            "issues": ["Missing file X"]
        }
        
        # Setup repo structure
        repo_root = tmp_path.parent
        (repo_root / "course_development" / "ai-math").mkdir(parents=True, exist_ok=True)
        
        with patch("validate_outputs.software_dir", tmp_path):
            exit_code = script.main(["--course", "ai-math"])
            assert exit_code == 1

    @patch("validate_outputs.validate_outputs")
    def test_main_all(self, mock_validate, script, tmp_path):
        mock_validate.return_value = {
            "course": "any",
            "valid": True,
            "modules_checked": 1,
            "modules_valid": 1,
            "issues": []
        }
        
        # Setup repo structure for all courses
        from src.batch_processing.config import COURSE_REGISTRY
        repo_root = tmp_path.parent
        for course in COURSE_REGISTRY:
            (repo_root / "course_development" / course).mkdir(parents=True, exist_ok=True)
            
        with patch("validate_outputs.software_dir", tmp_path):
            exit_code = script.main(["--course", "all"])
            assert exit_code == 0
            
        assert mock_validate.call_count == len(COURSE_REGISTRY)

    def test_parse_formats(self, script):
        assert script.parse_formats("pdf,docx") == ["pdf", "docx"]
        assert script.parse_formats(None) is None
        # Should handle unknown formats gracefully
        from src.validation.config import ALL_SUPPORTED_FORMATS
        valid_format = ALL_SUPPORTED_FORMATS[0]
        assert script.parse_formats(f"{valid_format},invalid") == [valid_format]
