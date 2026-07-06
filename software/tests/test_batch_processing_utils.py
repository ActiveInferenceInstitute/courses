"""Tests for batch processing utility functions."""

from pathlib import Path
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
    """Test course selection logic using the real COURSE_REGISTRY."""
    # Use the real COURSE_REGISTRY — no patching
    all_courses = get_courses_to_process("all")
    
    # Should return all registered courses
    assert len(all_courses) == len(config.COURSE_REGISTRY)
    
    # Each entry should be (rel_path, display_name, course_id)
    course_names = {name for _, name, _ in all_courses}
    assert "Active Inference: Philosophy" in course_names
    
    # Test selecting a specific known course
    ai_phil = get_courses_to_process("ai-philosophy")
    assert len(ai_phil) == 1
    assert ai_phil[0][0] == config.COURSE_REGISTRY["ai-philosophy"]["rel_path"]
    assert ai_phil[0][2] == "ai-philosophy"
    
    # Test selecting a non-existent course returns empty
    assert get_courses_to_process("nonexistent-course") == []


def test_get_formats_to_process(caplog):
    """Test format parsing logic using real AVAILABLE_FORMATS."""
    # "all" should return all available formats
    all_formats = get_formats_to_process("all")
    assert set(all_formats) == set(config.AVAILABLE_FORMATS)
    
    # Single known format
    assert get_formats_to_process("pdf") == ["pdf"]
    
    # Multiple comma-separated formats
    result = get_formats_to_process("pdf, html")
    assert set(result) == {"pdf", "html"}
    
    # Invalid format should be filtered out, valid kept
    result = get_formats_to_process("pdf, invalid_format_xyz")
    assert "pdf" in result
    assert "invalid_format_xyz" not in result
    assert "Unknown formats will be ignored" in caplog.text


def test_generate_dry_run_report(temp_dir):
    """Test dry run report generation with flat module structure (AIF convention)."""
    repo_root = temp_dir
    course_path = repo_root / "course_development/ai-philosophy"
    course_path.mkdir(parents=True)
    
    # Create flat module structure
    module_dir = course_path / "module-01"
    module_dir.mkdir()
    (module_dir / "module.md").touch()
    
    # Assignments
    (module_dir / "assignments").mkdir()
    (module_dir / "assignments" / "assign.md").touch()
    
    # Syllabus as file
    (course_path / "syllabus.md").touch()
    
    # Labs
    labs_dir = course_path / "labs"
    labs_dir.mkdir(parents=True)
    (labs_dir / "lab-1.md").touch()
    
    courses = [("course_development/ai-philosophy", "Active Inference: Philosophy", "ai-philosophy")]
    formats = ["pdf", "html"]
    
    report = generate_dry_run_report(
        repo_root, 
        courses, 
        formats,
        module_filter=None,
        generate_website=True,
        skip_labs=False
    )
        
    assert "DRY RUN" in report
    assert "Active Inference" in report
    assert "module-01" in report
    assert "1 root files" in report
    assert "1 assignments" in report
    assert "website/index.html" in report
    assert "Labs: 1 files" in report
    assert "pdf, html" in report


def test_generate_dry_run_report_filter(temp_dir):
    """Test dry run report with module filter using real matches_module_number."""
    repo_root = temp_dir
    course_path = repo_root / "course_development/biol-1"
    course_path.mkdir(parents=True)
    (course_path / "course" / "module-01").mkdir(parents=True)
    
    courses = [("course_development/biol-1", "BIOL-1")]
    formats = ["pdf"]
    
    # Use real matches_module_number — module 99 should not match module-01
    report = generate_dry_run_report(
        repo_root, 
        courses, 
        formats,
        module_filter=99
    )
        
    # Should not show any modules since 99 doesn't match module-01
    assert "module-01" not in report
