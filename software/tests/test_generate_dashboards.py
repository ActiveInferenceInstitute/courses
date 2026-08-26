import importlib.util
import sys
from pathlib import Path
import pytest

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Load the script
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "generate_dashboards.py"
spec = importlib.util.spec_from_file_location("generate_dashboards", SCRIPT_PATH)
generate_dashboards = importlib.util.module_from_spec(spec)
sys.modules["generate_dashboards"] = generate_dashboards
spec.loader.exec_module(generate_dashboards)


@pytest.fixture
def script():
    return generate_dashboards


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
        "# Intro to Active Inference\n\n## Overview\nOverview here.\n\n## Key Concepts\n- **Concept A** - Description A\n\n## Learning Objectives\n1. Objective A\n",
        encoding="utf-8",
    )
    (module_dir / "practice_quiz.md").write_text(
        "# Practice Quiz\n\n**1.** Question?\nA) Answer A\nB) Answer B\nC) Answer C\nD) Answer D\n",
        encoding="utf-8",
    )

    return base


class TestGenerateDashboards:
    def test_parse_args(self, script, course_structure):
        args = script.parse_args(
            ["--base", str(course_structure), "--course", "ai-philosophy", "--dry-run"]
        )
        assert args.base == course_structure
        assert args.course == "ai-philosophy"
        assert args.dry_run is True

    def test_main_dry_run(self, script, course_structure, capsys):
        script.main(["--base", str(course_structure), "--dry-run", "--include-core"])

        captured = capsys.readouterr()
        # Should find our mock ai-philosophy module
        assert "Would generate" in captured.out
        assert "active_inference/01_philosophy/01_intro/dashboard.html" in captured.out

        # Verify no file written
        db_path = (
            course_structure / "active_inference" / "01_philosophy" / "01_intro" / "dashboard.html"
        )
        assert not db_path.exists()

    def test_main_execution(self, script, course_structure, capsys):
        script.main(["--base", str(course_structure), "--include-core"])

        captured = capsys.readouterr()
        assert "Generated:" in captured.out

        db_path = (
            course_structure / "active_inference" / "01_philosophy" / "01_intro" / "dashboard.html"
        )
        assert db_path.exists()

        html = db_path.read_text("utf-8")
        assert "Intro to Active Inference" in html
        assert "Concept A" in html
        assert "Active Inference: Philosophy" in html
        assert "Core" in html

    def test_theme_lookup(self, script):
        # ai-philosophy should have its specific theme
        theme = script.get_theme("ai-philosophy")
        assert theme["accent"] == "#38bdf8"

        # ai-101 should have its specific theme
        theme_101 = script.get_theme("ai-101")
        assert theme_101["accent"] == "#22d3ee"

        # Unknown should use default
        theme_unk = script.get_theme("unknown-course")
        assert theme_unk == script.DEFAULT_THEME

    def test_course_filter(self, script, course_structure, capsys):
        # Create another course
        other = course_structure / "courses" / "other" / "01_mod"
        other.mkdir(parents=True)
        (other / "module.md").write_text("# Other", "utf-8")

        script.main(
            [
                "--base",
                str(course_structure),
                "--course",
                "ai-philosophy",
                "--dry-run",
                "--include-core",
            ]
        )

        captured = capsys.readouterr()
        assert "active_inference/01_philosophy" in captured.out
        assert "courses/other" not in captured.out
