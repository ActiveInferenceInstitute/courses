"""Source-derived output validation with real authored/generated files."""
import pytest

from src.batch_processing.main import generate_selected_outputs, process_module_by_type
from src.batch_processing.utils import get_courses_to_process, plan_course, plan_generation
from src.publish.main import publish_course
from src.validation.main import (
    validate_outputs, validate_plan, validate_published,
    generate_validation_report, get_output_summary,
)
from src.validation.utils import check_lab_files


def _module(root):
    module = root / "course_development/active_inference/01_philosophy/01_systems"
    module.mkdir(parents=True)
    (module / "module.md").write_text("# Systems\n\nAuthored content.")
    return module


def test_module_md_requires_no_invented_study_guide(tmp_path):
    module = _module(tmp_path)
    generated = process_module_by_type(str(module), str(module / "output"), formats=["md", "txt"])
    assert generated["errors"] == []
    result = validate_outputs(str(module.parent), formats=["md", "txt"], generate_website=False)
    assert result["valid"] is True
    assert result["modules_valid"] == 1
    assert not (module / "output/study-guides").exists()
    (module / "output/lecture-content/01_systems-module.md").unlink()
    assert validate_outputs(str(module.parent), ["md", "txt"], generate_website=False)["valid"] is False


def test_requested_mp3_is_required_without_contacting_a_speech_service(tmp_path):
    module = _module(tmp_path)
    process_module_by_type(str(module), str(module / "output"), formats=["md"])
    result = validate_outputs(str(module.parent), ["md", "mp3"], generate_website=False)
    assert result["valid"] is False
    assert len(result["issues"]) == 1
    assert result["issues"][0].endswith("01_systems-module.mp3")


def test_only_selected_units_modules_and_website_are_required(tmp_path):
    first = _module(tmp_path)
    other = first.parents[1] / "02_cognitive_science/01_systems"
    other.mkdir(parents=True)
    (other / "module.md").write_text("# Systems\n\nOther unit.")
    plans = plan_generation(
        tmp_path, get_courses_to_process("active-inference"), ["md"],
        module_filter=1, unit_filter="01_philosophy", generate_website=False,
    )
    assert generate_selected_outputs(plans)["errors"] == []
    result = validate_plan(plans[0])
    assert result["valid"] is True
    assert [module["name"] for module in result["modules"]] == ["01_philosophy/01_systems"]
    assert not validate_outputs(str(first.parents[1]), ["md"], course_id="active-inference",
                                generate_website=False)["valid"]


def test_directory_syllabus_missing_output_invalidates_entire_course(tmp_path):
    course = tmp_path / "legacy"
    module = course / "module-1"
    module.mkdir(parents=True)
    (module / "module.md").write_text("# Module\n\nBody.")
    syllabus = course / "syllabus"
    syllabus.mkdir()
    (syllabus / "Syllabus.md").write_text("# Syllabus\n\nOverview.")
    plan = plan_course(course, "Legacy", ["md", "txt"], generate_website=False)
    assert generate_selected_outputs([plan])["errors"] == []
    assert validate_plan(plan)["valid"] is True
    (syllabus / "output/Syllabus.md").unlink()
    result = validate_plan(plan)
    assert result["modules_valid"] == 1
    assert result["syllabus_valid"] is False
    assert result["valid"] is False


def test_file_syllabus_is_not_a_generation_obligation(tmp_path):
    module = _module(tmp_path)
    (module.parent / "syllabus.md").write_text("# File syllabus")
    plans = plan_generation(tmp_path, get_courses_to_process("ai-philosophy"), ["md"],
                            generate_website=False)
    assert generate_selected_outputs(plans)["errors"] == []
    assert validate_plan(plans[0])["valid"] is True
    assert all(artifact["kind"] != "syllabus" for artifact in plans[0]["artifacts"])


def test_labs_report_every_missing_selected_format_and_respect_limits(tmp_path):
    labs = tmp_path / "course/labs"
    labs.mkdir(parents=True)
    for number in (1, 2):
        (labs / f"lab-{number}.md").write_text(f"# Lab {number}\n\nProtocol.")
    result = check_lab_files(tmp_path, max_lab=1, formats=["pdf", "html"])
    assert result["source_labs"] == 1
    assert {path.rsplit("/", 1)[-1] for path in result["missing_outputs"]} == {"lab-1.pdf", "lab-1.html"}
    assert not any("dashboard" in issue.lower() for issue in result["issues"])


def test_lab_failure_sets_overall_valid_false(tmp_path):
    module = _module(tmp_path)
    lab = module.parent / "labs/lab-1.md"
    lab.parent.mkdir()
    lab.write_text("# Lab\n\nProtocol.")
    plan = plan_course(module.parent, "Philosophy", ["html"], course_id="ai-philosophy",
                       generate_website=False)
    module_plan = {**plan, "artifacts": [a for a in plan["artifacts"] if a["kind"] == "module"]}
    assert generate_selected_outputs([module_plan])["errors"] == []
    result = validate_plan(plan)
    assert result["modules_valid"] == 1
    assert result["valid"] is False
    assert result["labs"]["missing_outputs"] == [str(lab.parent / "output/html/lab-1.html")]


def test_published_current_unit_identity_and_empty_failure(tmp_path):
    module = _module(tmp_path)
    other = module.parents[1] / "02_cognitive_science/01_systems"
    other.mkdir(parents=True)
    (other / "module.md").write_text("# Other\n\nContent.")
    plans = plan_generation(tmp_path, get_courses_to_process("active-inference"), ["md"],
                            generate_website=False)
    assert generate_selected_outputs(plans)["errors"] == []
    published = tmp_path / "published"
    assert publish_course(str(module.parents[1]), str(published), plan=plans[0])["errors"] == []
    report = validate_published(str(published), ["active-inference"])
    assert report["valid"] is True
    assert {entry["name"] for entry in report["courses"]["active-inference"]["modules"]} == {
        "01_philosophy/01_systems", "02_cognitive_science/01_systems",
    }
    assert validate_published(str(tmp_path / "missing"), ["active-inference"])["valid"] is False
    assert validate_published(str(published), ["unknown"])["valid"] is False
    empty = tmp_path / "empty-publication/active-inference"
    empty.mkdir(parents=True)
    assert validate_published(str(empty.parent), ["active-inference"])["valid"] is False

class TestGetOutputSummary:
    """Tests for get_output_summary function."""

    def test_empty_course(self, temp_dir):
        """Empty course directory returns empty summary."""
        course_dir = temp_dir / "test-course"
        course_dir.mkdir()
        (course_dir / "course").mkdir()

        result = get_output_summary(str(course_dir))

        assert result["course"] == "test-course"
        assert result["totals"]["modules"] == 0
        assert result["totals"]["files"] == 0

    def test_course_with_modules(self, temp_dir):
        """Course with modules counts outputs correctly."""
        course_dir = temp_dir / "test-course"
        course_dir.mkdir()
        (course_dir / "course").mkdir()

        # Create two modules with outputs
        for i in range(1, 3):
            module_dir = course_dir / "course" / f"module-{i:02d}"
            output_dir = module_dir / "output"
            output_dir.mkdir(parents=True)

            (output_dir / "study-guide.pdf").write_text("PDF", encoding="utf-8")
            (output_dir / "study-guide.docx").write_text("DOCX", encoding="utf-8")

        result = get_output_summary(str(course_dir))

        assert result["totals"]["modules"] == 2
        assert result["totals"]["files"] == 4  # 2 files per module
        assert result["by_format"]["pdf"] == 2
        assert result["by_format"]["docx"] == 2

    def test_course_with_various_formats(self, temp_dir):
        """Course with various output formats."""
        course_dir = temp_dir / "test-course"
        course_dir.mkdir()
        (course_dir / "course").mkdir()

        module_dir = course_dir / "course" / "module-01"
        output_dir = module_dir / "output"
        output_dir.mkdir(parents=True)

        # Create various format files
        for ext in ["pdf", "docx", "html", "mp3", "txt"]:
            (output_dir / f"study-guide.{ext}").write_text(f"{ext}", encoding="utf-8")

        result = get_output_summary(str(course_dir))

        assert result["by_format"]["pdf"] == 1
        assert result["by_format"]["docx"] == 1
        assert result["by_format"]["html"] == 1
        assert result["by_format"]["mp3"] == 1
        assert result["by_format"]["txt"] == 1
        assert result["totals"]["files"] == 5


class TestGenerateValidationReport:
    def test_unknown_course_is_rejected(self, temp_dir):
        with pytest.raises(ValueError):
            generate_validation_report("nonexistent-course", str(temp_dir))

    def test_report_uses_registry_path_and_selected_publication(self, temp_dir):
        module = _module(temp_dir)
        result = generate_validation_report("ai-philosophy", str(temp_dir))
        assert result["source_validation"]["modules_checked"] == 1
        assert result["source_validation"]["valid"] is False
        assert result["published_validation"]["valid"] is False
        assert any("01_systems-module" in issue for issue in result["source_validation"]["issues"])
