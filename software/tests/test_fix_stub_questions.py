import importlib.util
import sys
from pathlib import Path
import pytest

# Add project root to sys.path to allow imports from src
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Load the script as a module
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "fix_stub_questions.py"
spec = importlib.util.spec_from_file_location("fix_stub_questions", SCRIPT_PATH)
fix_stub_questions = importlib.util.module_from_spec(spec)
sys.modules["fix_stub_questions"] = fix_stub_questions
spec.loader.exec_module(fix_stub_questions)


@pytest.fixture
def script():
    """Return the loaded script module."""
    return fix_stub_questions


@pytest.fixture
def course_structure(temp_dir):
    """Create a mock course structure matching COURSE_REGISTRY pattern."""
    # Pattern: course_development/active_inference/01_philosophy
    base = temp_dir / "course_development"
    base.mkdir()
    
    # Create ai-philosophy structure
    course_dir = base / "active_inference" / "01_philosophy"
    course_dir.mkdir(parents=True)
    
    module_dir = course_dir / "01_systems"
    module_dir.mkdir()
    
    # Stub content
    (module_dir / "module.md").write_text(
        "# Module 1: Systems\n\n## Overview\n\nOverview content.\n\n## Key Concepts\n- **System** - A set of things.\n\n## Learning Objectives\n1. **Define** a system.\n", 
        encoding="utf-8"
    )
    (module_dir / "questions.md").write_text(
        "# Questions\n\n... and why does it matter ...", 
        encoding="utf-8"
    )
    
    return base


class TestFixStubQuestions:
    
    def test_parse_args(self, script, course_structure):
        """Test argument parsing."""
        args = script.parse_args(["--base", str(course_structure), "--dry-run", "--course", "ai-philosophy"])
        assert args.base == course_structure
        assert args.dry_run is True
        assert args.course == "ai-philosophy"

    def test_find_stub_questions(self, script, course_structure):
        """Test finding stub files."""
        stubs = script.find_stub_questions(course_structure)
        assert len(stubs) == 1
        assert stubs[0].name == "questions.md"

    def test_extract_course_info_function(self, script):
        """Verify the script uses the shared utility."""
        # Just check that script.extract_course_info is a function
        assert callable(script.extract_course_info)
        # And check it corresponds to the imported one
        from src.batch_processing.utils import extract_course_info_from_path
        assert script.extract_course_info == extract_course_info_from_path

    def test_main_dry_run(self, script, course_structure, capsys):
        """Test dry run does not modify files."""
        qf_path = course_structure / "active_inference" / "01_philosophy" / "01_systems" / "questions.md"
        original_content = qf_path.read_text("utf-8")
        
        # Run main with dry-run
        script.main(["--base", str(course_structure), "--dry-run"])
        
        captured = capsys.readouterr()
        assert "Found 1 stub questions files" in captured.out
        # "Would fix" should appear because it found a match
        assert "Would fix" in captured.out
        assert qf_path.read_text("utf-8") == original_content

    def test_main_execution(self, script, course_structure, capsys):
        """Test execution modifies files."""
        qf_path = course_structure / "active_inference" / "01_philosophy" / "01_systems" / "questions.md"
        
        # Run main
        script.main(["--base", str(course_structure)])
        
        captured = capsys.readouterr()
        assert "Fixed:" in captured.out
        
        new_content = qf_path.read_text("utf-8")
        assert "and why does it matter" not in new_content
        assert "Recall and Define" in new_content
        # Check for Core unit labeling if applicable
        assert "Core" in new_content or "Active Inference: Philosophy" in new_content

    def test_course_filter(self, script, course_structure, capsys):
        """Test --course filter."""
        # Create another course that shouldn't be touched
        # Using a fallback structure: courses/other_course/01_mod
        other_course = course_structure / "courses" / "other_course" / "01_module"
        other_course.mkdir(parents=True)
        (other_course / "questions.md").write_text("... and why does it matter ...", "utf-8")
        
        script.main(["--base", str(course_structure), "--course", "ai-philosophy", "--dry-run"])
        
        captured = capsys.readouterr()
        
        # It should find 2 potential stubs, but filter one out.
        # "Found 2 stub questions files"
        assert "Found 2 stub questions files" in captured.out
        
        # Should verify that the OTHER file is NOT in the "Would fix" list
        # We need to capture the output and check lines.
        # "Would fix: .../active_inference/..." should be present.
        # "Would fix: .../courses/other_course/..." should NOT be present.
        
        output = captured.out
        target_path_part = "active_inference/01_philosophy"
        other_path_part = "courses/other_course"
        
        assert target_path_part in output
        assert other_path_part not in output
