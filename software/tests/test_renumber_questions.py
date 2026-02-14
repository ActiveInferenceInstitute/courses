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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "renumber_questions.py"
spec = importlib.util.spec_from_file_location("renumber_questions", SCRIPT_PATH)
renumber_questions_script = importlib.util.module_from_spec(spec)
sys.modules["renumber_questions"] = renumber_questions_script
spec.loader.exec_module(renumber_questions_script)


@pytest.fixture
def script():
    return renumber_questions_script


class TestRenumberQuestions:
    
    def test_parse_args(self, script):
        args = script.parse_args(["--course", "ai-math", "--dry-run", "--verbose"])
        assert args.course == "ai-math"
        assert args.dry_run is True
        assert args.verbose is True

    @patch("renumber_questions.renumber_questions_in_course")
    def test_main_execution(self, mock_renumber, script):
        mock_renumber.return_value = {
            "files_converted": 5,
            "total_questions": 25,
            "errors": []
        }
        
        exit_code = script.main(["--course", "ai-philosophy"])
        assert exit_code == 0
        mock_renumber.assert_called_once()

    @patch("renumber_questions.renumber_questions_in_course")
    def test_main_all(self, mock_renumber, script):
        mock_renumber.return_value = {
            "files_converted": 10,
            "total_questions": 100,
            "errors": []
        }
        
        exit_code = script.main(["--course", "all"])
        assert exit_code == 0
        
        # Verify it passed all recognized courses
        from src.batch_processing.config import COURSE_REGISTRY
        courses_passed = mock_renumber.call_args[1]["courses"]
        assert len(courses_passed) == len(COURSE_REGISTRY)

    @patch("renumber_questions.renumber_questions_in_course")
    def test_main_failure(self, mock_renumber, script):
        mock_renumber.return_value = {
            "files_converted": 0,
            "total_questions": 0,
            "errors": ["Failed to read file X"]
        }
        
        exit_code = script.main(["--course", "ai-math"])
        assert exit_code == 1
