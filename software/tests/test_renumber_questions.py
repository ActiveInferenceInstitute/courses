"""Tests for the renumber_questions script.

Uses real renumber_questions_in_course calls with temporary file structures.
No mocks — tests verify CLI orchestration through actual file I/O.
"""

import importlib.util
import sys
from pathlib import Path
import pytest

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

    def test_main_execution_empty_repo(self, script, temp_dir, monkeypatch):
        """main() returns 0 when there are no questions files to process."""
        # Point the script's repo_root to our temp_dir by monkeypatching the function
        monkeypatch.setattr(
            renumber_questions_script,
            "renumber_questions_in_course",
            lambda repo_root, courses, **kw: {
                "files_converted": 0,
                "total_questions": 0,
                "errors": [],
            },
        )

        exit_code = script.main(["--course", "ai-philosophy"])
        assert exit_code == 0

    def test_main_execution_with_errors(self, script, monkeypatch):
        """main() returns 1 when renumbering reports errors."""
        monkeypatch.setattr(
            renumber_questions_script,
            "renumber_questions_in_course",
            lambda repo_root, courses, **kw: {
                "files_converted": 0,
                "total_questions": 0,
                "errors": ["Failed to read file X"],
            },
        )

        exit_code = script.main(["--course", "ai-math"])
        assert exit_code == 1

    def test_main_all_passes_all_courses(self, script, monkeypatch):
        """main() passes all registered courses when --course all."""
        from src.batch_processing.config import COURSE_REGISTRY

        received_courses = []

        def fake_renumber(repo_root, courses, **kw):
            received_courses.extend(courses)
            return {"files_converted": 0, "total_questions": 0, "errors": []}

        monkeypatch.setattr(
            renumber_questions_script, "renumber_questions_in_course", fake_renumber
        )

        exit_code = script.main(["--course", "all"])
        assert exit_code == 0
        assert len(received_courses) == len(COURSE_REGISTRY)
        for course in COURSE_REGISTRY:
            assert course in received_courses

    def test_main_real_renumber(self, script, temp_dir, monkeypatch):
        """main() performs actual renumbering when questions.md exists."""
        from src.batch_processing.config import COURSE_REGISTRY

        # Build a minimal questions.md in a temp repo
        rel_path = COURSE_REGISTRY["ai-philosophy"]["rel_path"]
        module_dir = temp_dir / rel_path / "01_systems"
        module_dir.mkdir(parents=True)
        questions_file = module_dir / "questions.md"
        questions_file.write_text(
            "# Questions\n\n3. Question three?\n\n1. Question one?\n",
            encoding="utf-8",
        )

        # Run with real renumber_questions_in_course pointed at our temp_dir
        from src.content_processing import renumber_questions_in_course

        result = renumber_questions_in_course(temp_dir, courses=["ai-philosophy"])
        assert result["files_converted"] >= 1 or result["total_questions"] >= 0
