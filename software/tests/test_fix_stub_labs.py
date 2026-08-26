import importlib.util
import sys
from pathlib import Path
import pytest

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Load the script
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "fix_stub_labs.py"
spec = importlib.util.spec_from_file_location("fix_stub_labs", SCRIPT_PATH)
fix_stub_labs = importlib.util.module_from_spec(spec)
sys.modules["fix_stub_labs"] = fix_stub_labs
spec.loader.exec_module(fix_stub_labs)


@pytest.fixture
def script():
    return fix_stub_labs


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
    (module_dir / "lab.md").write_text(
        "# Lab: Title\n\nexplore active inference through hands-on engagement\n", encoding="utf-8"
    )

    return base


class TestFixStubLabs:
    def test_parse_args(self, script, course_structure):
        args = script.parse_args(
            ["--base", str(course_structure), "--dry-run", "--course", "ai-philosophy"]
        )
        assert args.base == course_structure
        assert args.dry_run is True
        assert args.course == "ai-philosophy"

    def test_find_stub_labs(self, script, course_structure):
        stubs = script.find_stub_labs(course_structure)
        assert len(stubs) == 1
        assert stubs[0].name == "lab.md"

    def test_main_dry_run(self, script, course_structure, capsys):
        lab_path = course_structure / "active_inference" / "01_philosophy" / "01_intro" / "lab.md"
        original = lab_path.read_text("utf-8")

        script.main(["--base", str(course_structure), "--dry-run"])

        captured = capsys.readouterr()
        assert "Found 1 stub labs" in captured.out
        assert "Would fix" in captured.out
        assert lab_path.read_text("utf-8") == original

    def test_main_execution(self, script, course_structure, capsys):
        lab_path = course_structure / "active_inference" / "01_philosophy" / "01_intro" / "lab.md"

        script.main(["--base", str(course_structure)])

        captured = capsys.readouterr()
        assert "Fixed:" in captured.out

        new_content = lab_path.read_text("utf-8")
        assert "hands-on engagement" not in new_content
        assert "Lab: Intro to Active Inference" in new_content
        assert "Core" in new_content
        assert "Active Inference: Philosophy" in new_content

    def test_course_filter(self, script, course_structure, capsys):
        # Add another course
        other = course_structure / "courses" / "other" / "01_mod"
        other.mkdir(parents=True)
        (other / "lab.md").write_text("explore other through hands-on engagement", "utf-8")

        script.main(["--base", str(course_structure), "--course", "ai-philosophy", "--dry-run"])

        captured = capsys.readouterr()
        assert "Found 2 stub labs" in captured.out
        assert "active_inference/01_philosophy" in captured.out
        assert "courses/other" not in captured.out
