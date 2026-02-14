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

    @patch("import_legacy_materials.process_chapter_questions")
    @patch("import_legacy_materials.process_slides")
    def test_main_dry_run(self, mock_slides, mock_questions, script, capsys):
        # We need to bypass the path existence checks
        with patch("import_legacy_materials.Path.exists", return_value=True):
            exit_code = script.main(["--dry-run", "--course", "ai-philosophy"])
            assert exit_code == 0
            
        mock_questions.assert_called_once()
        mock_slides.assert_called_once()
        
        captured = capsys.readouterr()
        # setup_logging uses stream handler, so info logs might show up in capsys
        # but the script uses logger.info which we haven't mocked here.
        # However, setup_logging is called at module level in the script.
        pass

    @patch("import_legacy_materials.process_chapter_questions")
    @patch("import_legacy_materials.process_slides")
    def test_main_module_not_found(self, mock_slides, mock_questions, script):
        # Test with invalid course
        # The choices in parse_args will actually raise SystemExit if we use a real parser,
        # but we can test the logic in main if it gets past parsing somehow (or if choice validation is off).
        # Actually parse_args is called first.
        
        with pytest.raises(SystemExit):
            script.main(["--course", "INVALID"])

    @patch("import_legacy_materials.process_chapter_questions")
    @patch("import_legacy_materials.process_slides")
    def test_main_execution(self, mock_slides, mock_questions, script):
        from unittest.mock import ANY
        mock_questions.return_value = True
        mock_slides.return_value = True
        
        with patch("import_legacy_materials.Path.exists", return_value=True):
            exit_code = script.main(["--course", "ai-philosophy"])
            assert exit_code == 0
            
        mock_questions.assert_called_with(ANY, ANY, dry_run=False)
        mock_slides.assert_called_with(ANY, ANY, dry_run=False)
