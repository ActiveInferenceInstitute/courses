import importlib.util
import sys
from pathlib import Path
import pytest

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Load the script
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "fix_stub_quizzes.py"
spec = importlib.util.spec_from_file_location("fix_stub_quizzes", SCRIPT_PATH)
fix_stub_quizzes = importlib.util.module_from_spec(spec)
sys.modules["fix_stub_quizzes"] = fix_stub_quizzes
spec.loader.exec_module(fix_stub_quizzes)


@pytest.fixture
def script():
    return fix_stub_quizzes


@pytest.fixture
def course_structure(temp_dir):
    """Create a mock course structure."""
    base = temp_dir / "course_development"
    base.mkdir()
    
    # ai-philosophy (Core/Flat)
    course_dir = base / "active_inference" / "01_philosophy"
    course_dir.mkdir(parents=True)
    module_dir = course_dir / "01_intro"
    module_dir.mkdir()
    
    (module_dir / "module.md").write_text(
        "# Intro to Active Inference\n\n## Overview\nOverview here.\n\n## Key Concepts\n- **Free Energy Principle** - A mathematical principle for adaptive systems.\n\n## Learning Objectives\n1. Explain the FEP.\n",
        encoding="utf-8"
    )
    (module_dir / "practice_quiz.md").write_text(
        "# Practice Quiz\n\n**1.** Which of the following is true?\nA) A core concept in\nB) An unrelated idea\nC) None of the above\nD) All of the above\n",
        encoding="utf-8"
    )
    
    return base


class TestFixStubQuizzes:
    
    def test_parse_args(self, script, course_structure):
        args = script.parse_args(["--base", str(course_structure), "--dry-run", "--course", "ai-philosophy"])
        assert args.base == course_structure
        assert args.dry_run is True
        assert args.course == "ai-philosophy"

    def test_find_stub_quizzes(self, script, course_structure):
        stubs = script.find_stub_quizzes(course_structure)
        assert len(stubs) == 1
        assert stubs[0].name == "practice_quiz.md"

    def test_main_dry_run(self, script, course_structure, capsys):
        quiz_path = course_structure / "active_inference" / "01_philosophy" / "01_intro" / "practice_quiz.md"
        original = quiz_path.read_text("utf-8")
        
        script.main(["--base", str(course_structure), "--dry-run"])
        
        captured = capsys.readouterr()
        assert "Found 1 stub quizzes" in captured.out
        assert "Would fix" in captured.out
        assert quiz_path.read_text("utf-8") == original

    def test_main_execution(self, script, course_structure, capsys):
        quiz_path = course_structure / "active_inference" / "01_philosophy" / "01_intro" / "practice_quiz.md"
        
        script.main(["--base", str(course_structure)])
        
        captured = capsys.readouterr()
        assert "Fixed:" in captured.out
        
        new_content = quiz_path.read_text("utf-8")
        assert "A core concept in" not in new_content
        assert "Free Energy Principle" in new_content
        assert "Answer Key" in new_content

    def test_course_filter(self, script, course_structure, capsys):
        # Add another course
        other = course_structure / "courses" / "other" / "01_mod"
        other.mkdir(parents=True)
        (other / "practice_quiz.md").write_text("A core concept in...", "utf-8")
        
        script.main(["--base", str(course_structure), "--course", "ai-philosophy", "--dry-run"])
        
        captured = capsys.readouterr()
        assert "Found 2 stub quizzes" in captured.out
        assert "active_inference/01_philosophy" in captured.out
        assert "courses/other" not in captured.out
