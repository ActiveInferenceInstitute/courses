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
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "publish_all.py"
spec = importlib.util.spec_from_file_location("publish_all", SCRIPT_PATH)
publish_all = importlib.util.module_from_spec(spec)
sys.modules["publish_all"] = publish_all
spec.loader.exec_module(publish_all)


@pytest.fixture
def script():
    return publish_all


class TestPublishAll:
    
    def test_parse_args(self, script):
        args = script.parse_args(["--clean", "--skip-mp3", "--formats", "pdf,html"])
        assert args.clean is True
        assert args.skip_mp3 is True
        assert args.formats == "pdf,html"

    @patch("publish_all.run_script")
    @patch("publish_all.clean_published")
    @patch("publish_all.copy_labs_and_dashboards")
    @patch("publish_all.copy_slides")
    @patch("publish_all.copy_slides_to_modules")
    @patch("publish_all.copy_practice_tests")
    @patch("publish_all.flatten_published")
    @patch("publish_all.reorganize_to_categories")
    def test_main_execution(self, mock_reorg, mock_flatten, mock_cp_pt, mock_cp_sm, mock_cp_s, mock_cp_ld, mock_clean, mock_run, script, temp_dir):
        # Setup mocks
        mock_run.return_value = True
        mock_cp_ld.return_value = 5
        mock_cp_s.return_value = 2
        mock_cp_sm.return_value = 2
        mock_cp_pt.return_value = 1
        mock_flatten.return_value = 10
        mock_reorg.return_value = 10
        
        # Bypass filesystem checks for the summary print
        published_dir = temp_dir / "PUBLISHED"
        published_dir.mkdir()
        
        with patch("publish_all.get_repo_root") as mock_root:
            mock_root.return_value = temp_dir
            
            # Test main with skip-mp3
            exit_code = script.main(["--skip-mp3"])
            assert exit_code == 0
        
        # Verify orchestration
        assert mock_clean.call_count == 0 # --clean not passed
        
        # Check generation call
        gen_call = mock_run.call_args_list[0]
        assert gen_call[0][0] == "generate_all_outputs.py"
        assert "--formats" in gen_call[0][1]
        
        # Check publish call
        pub_call = mock_run.call_args_list[1]
        assert pub_call[0][0] == "publish_course.py"
        
        # Check validate call
        val_call = mock_run.call_args_list[2]
        assert val_call[0][0] == "validate_outputs.py"

    @patch("publish_all.run_script")
    def test_main_failure(self, mock_run, script, temp_dir):
        mock_run.return_value = False
        
        with patch("publish_all.get_repo_root") as mock_root:
            mock_root.return_value = temp_dir
            exit_code = script.main([])
            assert exit_code == 1
