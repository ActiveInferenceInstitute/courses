"""Tests for batch processing utility functions."""

from pathlib import Path

import pytest

from src.batch_processing.utils import (
    find_markdown_files,
    find_audio_files,
    should_process_file,
    ensure_output_directory,
    get_relative_output_path,
    get_courses_to_process,
    get_formats_to_process,
    generate_dry_run_report,
    extract_course_info_from_path,
    prettify_name,
)
from src.batch_processing import config


def test_prettify_name():
    """Test name prettification."""
    assert prettify_name("01_intro") == "Intro"
    assert prettify_name("intro_to_ai") == "Intro To Ai"
    assert prettify_name("123_module") == "Module"


def test_extract_course_info_from_path(temp_dir):
    """Test course extraction using real COURSE_REGISTRY."""
    base = temp_dir / "course_development"
    base.mkdir()

    # Case 1: Active Inference Philosophy (Core, Flat)
    # Path: active_inference/01_philosophy/01_intro/questions.md
    c_path = base / "active_inference" / "01_philosophy"
    c_path.mkdir(parents=True)
    m_path = c_path / "01_intro"
    m_path.mkdir()
    f_path = m_path / "questions.md"

    info = extract_course_info_from_path(f_path, base)
    assert info["course"] == "ai-philosophy"
    assert info["course_name"] == "Active Inference: Philosophy"
    assert info["unit"] == "Core"
    assert info["module_topic"] == "Intro"
    assert info["module_num"] == "01"

    # Case 2: Active Inference 101 (Unit-based)
    # Path: active_inference_101/01_cogsci/01_intro/questions.md
    # Registry: "ai-101"
    c_path_2 = base / "active_inference_101"
    c_path_2.mkdir()
    u_path = c_path_2 / "01_cogsci"
    u_path.mkdir()
    m_path_2 = u_path / "01_intro"
    m_path_2.mkdir()
    f_path_2 = m_path_2 / "questions.md"

    info_2 = extract_course_info_from_path(f_path_2, base)
    assert info_2["course"] == "ai-101"
    assert info_2["course_name"] == "Active Inference: College 101"
    assert info_2["unit"] == "Cogsci"
    assert info_2["module_topic"] == "Intro"

    # Case 3: Unknown course (Fallback)
    # Path: courses/my_course/01_mod/questions.md
    c_path_3 = base / "courses" / "my_course"
    c_path_3.mkdir(parents=True)
    m_path_3 = c_path_3 / "01_mod"
    m_path_3.mkdir()
    f_path_3 = m_path_3 / "questions.md"

    info_3 = extract_course_info_from_path(f_path_3, base)
    assert info_3["course"] == "courses"
    assert info_3["unit"] == "My Course"
    assert info_3["module_topic"] == "Mod"
    # Fallback logic might vary depending on exact path structure, but this tests it returns something.


def test_find_markdown_files(temp_dir):
    """Test finding markdown files."""
    (temp_dir / "test.md").touch()
    (temp_dir / "test.markdown").touch()
    (temp_dir / "test.txt").touch()
    subdir = temp_dir / "subdir"
    subdir.mkdir()
    (subdir / "sub.md").touch()

    files = find_markdown_files(temp_dir)
    filenames = [f.name for f in files]

    assert "test.md" in filenames
    assert "test.markdown" in filenames
    assert "sub.md" in filenames
    assert "test.txt" not in filenames


def test_find_audio_files(temp_dir):
    """Test finding audio files."""
    (temp_dir / "test.mp3").touch()
    (temp_dir / "test.wav").touch()
    (temp_dir / "test.txt").touch()

    files = find_audio_files(temp_dir)
    filenames = [f.name for f in files]

    assert "test.mp3" in filenames
    assert "test.wav" in filenames
    assert "test.txt" not in filenames


def test_should_process_file():
    """Test skipping logic."""
    skip_dirs = ["skip_me", "output"]

    assert should_process_file(Path("a/b/c.md"), skip_dirs) is True
    assert should_process_file(Path("a/skip_me/c.md"), skip_dirs) is False
    assert should_process_file(Path("output/c.md"), skip_dirs) is False


def test_ensure_output_directory(temp_dir):
    """Test creating output directory."""
    out_dir = temp_dir / "new_dir" / "subdir"
    ensure_output_directory(out_dir)
    assert out_dir.exists()


def test_get_relative_output_path():
    """Test relative path calculation."""
    source_dir = Path("/src")
    out_dir = Path("/out")

    # /src/a/file.md -> /out/a/file.md
    source_file = Path("/src/a/file.md")
    result = get_relative_output_path(source_file, source_dir, out_dir)

    assert result == Path("/out/a/file.md")


def test_get_courses_to_process():
    entries = get_courses_to_process("all")
    paths = [Path(relative) for relative, _, _ in entries]
    assert all(not left.is_relative_to(right) for left in paths for right in paths if left != right)
    assert any(identity == "active-inference" for _, _, identity in entries)
    assert get_courses_to_process("ai-philosophy")[0][0] == config.COURSE_REGISTRY["ai-philosophy"]["rel_path"]
    with pytest.raises(ValueError):
        get_courses_to_process("nonexistent-course")


@pytest.mark.parametrize("formats", ["", "pdf,unknown", "pdf,", ",", "xyz"])
def test_rejects_every_invalid_format(formats):
    with pytest.raises(ValueError):
        get_formats_to_process(formats)


def test_format_selection_is_explicit_and_deduplicated():
    assert get_formats_to_process("md, txt,md") == ["md", "txt"]
    assert set(get_formats_to_process("all")) == set(config.AVAILABLE_FORMATS)


def test_generate_dry_run_report(temp_dir):
    course = temp_dir / config.COURSE_REGISTRY["ai-philosophy"]["rel_path"]
    module = course / "01_systems"
    module.mkdir(parents=True)
    (module / "module.md").write_text("# Systems\n\nExplanation.")
    (course / "syllabus.md").write_text("# File syllabus")
    report = generate_dry_run_report(temp_dir, get_courses_to_process("ai-philosophy"),
                                     ["md"], generate_website=False)
    assert str(module / "output/lecture-content/01_systems-module.md") in report
    assert "syllabus/output" not in report
    assert not (module / "output").exists()


def test_generate_dry_run_report_filter(temp_dir):
    course = temp_dir / config.COURSE_REGISTRY["ai-philosophy"]["rel_path"]
    (course / "01_systems").mkdir(parents=True)
    with pytest.raises(ValueError, match="No modules"):
        generate_dry_run_report(temp_dir, get_courses_to_process("ai-philosophy"),
                                ["md"], module_filter=99)
