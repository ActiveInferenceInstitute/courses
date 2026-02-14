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

    @patch("publish_course.publish_course")
    def test_main_execution(self, mock_publish, script):
        mock_publish.return_value = {
            "course": "Philosophy",
            "modules_published": 1,
            "syllabus_files": 1,
            "total_files": 2,
            "modules": [{"name": "module-01", "files": 2}]
        }
        
        # Bypass filesystem checks
        with patch("publish_course.Path.exists", return_value=True):
            exit_code = script.main(["--course", "ai-philosophy"])
            assert exit_code == 0
            
        mock_publish.assert_called_once()

    @patch("publish_course.publish_course")
    def test_main_all(self, mock_publish, script):
        mock_publish.return_value = {
            "course": "Any", "modules_published": 0, "syllabus_files": 0, "total_files": 0, "modules": []
        }
        
        with patch("publish_course.Path.exists", return_value=True):
            exit_code = script.main(["--course", "all"])
            assert exit_code == 0
            
        # Should be called for each registered course
        from src.batch_processing.config import COURSE_REGISTRY
        assert mock_publish.call_count == len(COURSE_REGISTRY)

    def test_main_invalid_course(self, script):
        with pytest.raises(SystemExit):
            script.main(["--course", "INVALID"])
