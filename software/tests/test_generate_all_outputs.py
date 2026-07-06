"""Tests for the generate_all_outputs script.

Tests that orchestrate the full output-generation pipeline are marked
with @pytest.mark.requires_api.
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

    @pytest.mark.requires_api
    def test_main_dry_run(self, script, monkeypatch):
        """main() logs DRY RUN message and returns without generating files (requires API)."""
        log_calls = []

        class FakeLogger:
            def info(self, msg, *a, **kw):
                log_calls.append(msg)
            def warning(self, *a, **kw):
                pass
            def error(self, *a, **kw):
                pass
            def debug(self, *a, **kw):
                pass

        monkeypatch.setattr(
            generate_all_outputs,
            "get_courses_to_process",
            lambda *a, **kw: [("active_inference/01_philosophy", "Philosophy", "ai-philosophy")],
        )
        monkeypatch.setattr(
            generate_all_outputs, "generate_dry_run_report", lambda *a, **kw: "Dry run changes..."
        )
        monkeypatch.setattr(generate_all_outputs, "logger", FakeLogger())

        script.main(["--dry-run", "--course", "ai-philosophy"])

        assert any("DRY RUN MODE" in msg for msg in log_calls)

    @pytest.mark.requires_api
    def test_main_execution(self, script, monkeypatch):
        """main() runs the full module/lab/syllabus pipeline (requires API)."""
        modules_calls = []
        labs_calls = []
        syllabus_calls = []

        monkeypatch.setattr(
            generate_all_outputs,
            "get_courses_to_process",
            lambda *a, **kw: [("active_inference/01_philosophy", "Philosophy", "ai-philosophy")],
        )
        monkeypatch.setattr(generate_all_outputs, "clear_all_outputs", lambda *a, **kw: None)
        monkeypatch.setattr(
            generate_all_outputs,
            "process_course_modules",
            lambda course_path, course_name, **kw: modules_calls.append((course_path, course_name)),
        )
        monkeypatch.setattr(
            generate_all_outputs,
            "process_course_labs",
            lambda course_path, course_name, **kw: labs_calls.append(course_name),
        )
        monkeypatch.setattr(
            generate_all_outputs,
            "process_course_syllabus",
            lambda course_path, course_name, **kw: syllabus_calls.append(course_name),
        )
        monkeypatch.setattr(
            generate_all_outputs, "process_course_practice_tests", lambda *a, **kw: None
        )

        exit_code = script.main(["--course", "ai-philosophy", "--skip-clear"])
        assert exit_code == 0

        assert len(modules_calls) == 1
        assert modules_calls[0][1] == "Philosophy"

        assert len(labs_calls) == 1
        assert labs_calls[0] == "ai-philosophy"

        assert len(syllabus_calls) == 1
        assert syllabus_calls[0] == "ai-philosophy"
