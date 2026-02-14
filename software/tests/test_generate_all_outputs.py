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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "generate_all_outputs.py"
spec = importlib.util.spec_from_file_location("generate_all_outputs", SCRIPT_PATH)
generate_all_outputs = importlib.util.module_from_spec(spec)
sys.modules["generate_all_outputs"] = generate_all_outputs
spec.loader.exec_module(generate_all_outputs)


@pytest.fixture
def script():
    return generate_all_outputs


class TestGenerateAllOutputs:
    
    def test_parse_args(self, script):
        args = script.parse_args(["--course", "ai-philosophy", "--formats", "pdf,mp3", "--dry-run"])
        assert args.course == "ai-philosophy"
        assert args.formats == "pdf,mp3"
        assert args.dry_run is True

    def test_parse_limits(self, script):
        limits = script.parse_limits(["ai-math:6", "ai-robotics:5", "invalid"])
        assert limits["ai-math"] == 6
        assert limits["ai-robotics"] == 5
        assert "invalid" not in limits

    @patch("generate_all_outputs.get_courses_to_process")
    @patch("generate_all_outputs.generate_dry_run_report")
    @patch("generate_all_outputs.logger")
    def test_main_dry_run(self, mock_logger, mock_report, mock_get_courses, script):
        mock_get_courses.return_value = [("active_inference/01_philosophy", "Philosophy", "ai-philosophy")]
        mock_report.return_value = "Dry run changes..."
        
        # Test main with dry-run
        script.main(["--dry-run", "--course", "ai-philosophy"])
            
        # Verify logger was called with dry run info
        mock_logger.info.assert_any_call("DRY RUN MODE - Checking what would be generated")

    @patch("generate_all_outputs.get_courses_to_process")
    @patch("generate_all_outputs.clear_all_outputs")
    @patch("generate_all_outputs.process_course_modules")
    @patch("generate_all_outputs.process_course_labs")
    @patch("generate_all_outputs.process_course_syllabus")
    @patch("generate_all_outputs.process_course_practice_tests")
    def test_main_execution(self, mock_tests, mock_syllabus, mock_labs, mock_modules, mock_clear, mock_get_courses, script):
        mock_get_courses.return_value = [("active_inference/01_philosophy", "Philosophy", "ai-philosophy")]
        
        # Call main directly with argv
        exit_code = script.main(["--course", "ai-philosophy", "--skip-clear"])
        assert exit_code == 0
            
        # Verify orchestration calls
        # skip-clear was passed, so clear_all_outputs should NOT be called
        mock_clear.assert_not_called()
        
        # Check if processing functions were called
        args, kwargs = mock_modules.call_args
        # args[0] is course_path, args[1] is course_name
        assert "Philosophy" == args[1]
        
        # labs and syllabus take course_id
        _, kwargs_labs = mock_labs.call_args
        assert kwargs_labs.get("course_id") == "ai-philosophy"
        
        _, kwargs_syllabus = mock_syllabus.call_args
        assert kwargs_syllabus.get("course_id") == "ai-philosophy"
        
        mock_tests.assert_called()

