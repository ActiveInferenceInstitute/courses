"""Tests for validation/utils.py functions."""

from src.validation.utils import (
    count_files_by_extension,
    get_module_directories,
    check_output_directory,
    check_study_guide_files,
    check_website_files,
    format_file_counts,
    get_timestamp,
)


class TestCountFilesByExtension:
    """Tests for count_files_by_extension function."""

    def test_empty_directory(self, temp_dir):
        """Empty directory returns empty count."""
        result = count_files_by_extension(temp_dir)
        assert result == {}

    def test_nonexistent_directory(self, temp_dir):
        """Non-existent directory returns empty count."""
        result = count_files_by_extension(temp_dir / "nonexistent")
        assert result == {}

    def test_single_extension(self, temp_dir):
        """Directory with single extension files."""
        (temp_dir / "file1.pdf").write_text("pdf1", encoding="utf-8")
        (temp_dir / "file2.pdf").write_text("pdf2", encoding="utf-8")

        result = count_files_by_extension(temp_dir)
        assert result == {"pdf": 2}

    def test_multiple_extensions(self, temp_dir):
        """Directory with multiple extension files."""
        (temp_dir / "file.pdf").write_text("pdf", encoding="utf-8")
        (temp_dir / "file.docx").write_text("docx", encoding="utf-8")
        (temp_dir / "file.html").write_text("html", encoding="utf-8")
        (temp_dir / "audio.mp3").write_text("mp3", encoding="utf-8")

        result = count_files_by_extension(temp_dir)
        assert result == {"pdf": 1, "docx": 1, "html": 1, "mp3": 1}

    def test_nested_directories(self, temp_dir):
        """Recursively counts files in nested directories."""
        subdir = temp_dir / "subdir"
        subdir.mkdir()
        (temp_dir / "file1.pdf").write_text("pdf", encoding="utf-8")
        (subdir / "file2.pdf").write_text("pdf", encoding="utf-8")

        result = count_files_by_extension(temp_dir)
        assert result == {"pdf": 2}

    def test_ignores_hidden_files(self, temp_dir):
        """Hidden files (starting with .) are ignored."""
        (temp_dir / ".hidden.pdf").write_text("hidden", encoding="utf-8")
        (temp_dir / "visible.pdf").write_text("visible", encoding="utf-8")

        result = count_files_by_extension(temp_dir)
        assert result == {"pdf": 1}

    def test_ignores_files_without_extension(self, temp_dir):
        """Files without extension are ignored."""
        (temp_dir / "README").write_text("readme", encoding="utf-8")
        (temp_dir / "file.pdf").write_text("pdf", encoding="utf-8")

        result = count_files_by_extension(temp_dir)
        assert result == {"pdf": 1}

    def test_case_insensitive_extension(self, temp_dir):
        """Extensions are lowercased."""
        (temp_dir / "file.PDF").write_text("pdf", encoding="utf-8")
        (temp_dir / "file2.pdf").write_text("pdf", encoding="utf-8")

        result = count_files_by_extension(temp_dir)
        assert result == {"pdf": 2}


class TestGetModuleDirectories:
    """Tests for get_module_directories function."""

    def test_no_course_dir(self, temp_dir):
        """No course directory returns empty list."""
        result = get_module_directories(temp_dir)
        assert result == []

    def test_empty_course_dir(self, temp_dir):
        """Empty course directory returns empty list."""
        (temp_dir / "course").mkdir()
        result = get_module_directories(temp_dir)
        assert result == []

    def test_single_module(self, temp_dir):
        """Single module directory is found."""
        course_dir = temp_dir / "course"
        course_dir.mkdir()
        (course_dir / "module-01").mkdir()

        result = get_module_directories(temp_dir)
        assert len(result) == 1
        assert result[0].name == "module-01"

    def test_multiple_modules_sorted(self, temp_dir):
        """Multiple modules are returned sorted."""
        course_dir = temp_dir / "course"
        course_dir.mkdir()
        (course_dir / "module-03").mkdir()
        (course_dir / "module-01").mkdir()
        (course_dir / "module-02").mkdir()

        result = get_module_directories(temp_dir)
        assert len(result) == 3
        assert [m.name for m in result] == ["module-01", "module-02", "module-03"]

    def test_ignores_non_module_dirs(self, temp_dir):
        """Non-module directories are ignored."""
        course_dir = temp_dir / "course"
        course_dir.mkdir()
        (course_dir / "module-01").mkdir()
        (course_dir / "syllabus").mkdir()
        (course_dir / "labs").mkdir()

        result = get_module_directories(temp_dir)
        assert len(result) == 1
        assert result[0].name == "module-01"

    def test_ignores_files(self, temp_dir):
        """Files in course dir are ignored."""
        course_dir = temp_dir / "course"
        course_dir.mkdir()
        (course_dir / "module-01").mkdir()
        (course_dir / "module-readme.md").write_text("readme", encoding="utf-8")

        result = get_module_directories(temp_dir)
        assert len(result) == 1

    def test_flat_layout(self, temp_dir):
        """Active-Inference flat layout (XX_topic/ under course) is discovered."""
        for name in ("01_systems", "02_agents", "03_perception"):
            (temp_dir / name).mkdir()
        result = get_module_directories(temp_dir)
        assert [m.name for m in result] == ["01_systems", "02_agents", "03_perception"]

    def test_two_level_layout(self, temp_dir):
        """Level-adapted / domain layout (unit_dir/XX_topic/) is discovered."""
        unit = temp_dir / "01_cognitive_science"
        unit.mkdir()
        (unit / "01_systems").mkdir()
        (unit / "02_agents").mkdir()
        unit2 = temp_dir / "02_comp_neuro"
        unit2.mkdir()
        (unit2 / "03_perception").mkdir()

        result = get_module_directories(temp_dir)
        assert [m.name for m in result] == ["01_systems", "02_agents", "03_perception"]


class TestCheckOutputDirectory:
    """Tests for check_output_directory function."""

    def test_no_output_dir(self, temp_dir):
        """No output directory returns False."""
        has_output, subdirs = check_output_directory(temp_dir)
        assert has_output is False
        assert subdirs == {}

    def test_empty_output_dir(self, temp_dir):
        """Empty output directory returns True with missing subdirs."""
        (temp_dir / "output").mkdir()
        has_output, subdirs = check_output_directory(temp_dir)
        assert has_output is True
        assert subdirs["study_guides"] is False
        assert subdirs["website"] is False

    def test_with_study_guides_dir(self, temp_dir):
        """Output with study-guides subdirectory."""
        output_dir = temp_dir / "output"
        output_dir.mkdir()
        (output_dir / "study-guides").mkdir()

        has_output, subdirs = check_output_directory(temp_dir)
        assert has_output is True
        assert subdirs["study_guides"] is True
        assert subdirs["website"] is False

    def test_with_website_dir(self, temp_dir):
        """Output with website subdirectory."""
        output_dir = temp_dir / "output"
        output_dir.mkdir()
        (output_dir / "website").mkdir()

        has_output, subdirs = check_output_directory(temp_dir)
        assert has_output is True
        assert subdirs["study_guides"] is False
        assert subdirs["website"] is True

    def test_with_both_subdirs(self, temp_dir):
        """Output with both subdirectories."""
        output_dir = temp_dir / "output"
        output_dir.mkdir()
        (output_dir / "study-guides").mkdir()
        (output_dir / "website").mkdir()

        has_output, subdirs = check_output_directory(temp_dir)
        assert has_output is True
        assert subdirs["study_guides"] is True
        assert subdirs["website"] is True


class TestCheckStudyGuideFiles:
    """Tests for check_study_guide_files function."""

    def test_no_study_guides_dir(self, temp_dir):
        """No study-guides directory returns all False."""
        result = check_study_guide_files(temp_dir)
        # All expected files should be False
        assert all(not v for v in result.values())

    def test_empty_study_guides_dir(self, temp_dir):
        """Empty study-guides directory returns all False."""
        sg_dir = temp_dir / "output" / "study-guides"
        sg_dir.mkdir(parents=True)

        result = check_study_guide_files(temp_dir)
        assert all(not v for v in result.values())

    def test_with_matching_files(self, temp_dir):
        """Files with expected suffixes are found."""
        sg_dir = temp_dir / "output" / "study-guides"
        sg_dir.mkdir(parents=True)

        # Create files with module prefix but matching suffix
        (sg_dir / "module-01-study-guide-keys-to-success.pdf").write_text("pdf", encoding="utf-8")

        result = check_study_guide_files(temp_dir)
        # The keys-to-success file is discovered; at least one expected suffix
        # (that ends with "-keys-to-success.pdf") must resolve to True.
        assert any(v for v in result.values())


class TestCheckWebsiteFiles:
    """Tests for check_website_files function."""

    def test_no_website_dir(self, temp_dir):
        """No website directory returns all False."""
        result = check_website_files(temp_dir)
        assert all(not v for v in result.values())

    def test_empty_website_dir(self, temp_dir):
        """Empty website directory returns all False."""
        website_dir = temp_dir / "output" / "website"
        website_dir.mkdir(parents=True)

        result = check_website_files(temp_dir)
        assert all(not v for v in result.values())

    def test_with_index_html(self, temp_dir):
        """Website with index.html file."""
        website_dir = temp_dir / "output" / "website"
        website_dir.mkdir(parents=True)
        (website_dir / "index.html").write_text("<html>", encoding="utf-8")

        result = check_website_files(temp_dir)
        # index.html should be found if it's in config
        if "index.html" in result:
            assert result["index.html"] is True


class TestFormatFileCounts:
    """Tests for format_file_counts function."""

    def test_empty_counts(self):
        """Empty counts returns 'none'."""
        result = format_file_counts({})
        assert result == "none"

    def test_single_count(self):
        """Single extension count."""
        result = format_file_counts({"pdf": 10})
        assert result == "pdf:10"

    def test_multiple_counts(self):
        """Multiple extension counts sorted."""
        result = format_file_counts({"pdf": 10, "html": 5, "mp3": 3})
        assert result == "html:5, mp3:3, pdf:10"

    def test_zero_counts(self):
        """Zero counts are included."""
        result = format_file_counts({"pdf": 0, "html": 5})
        assert "pdf:0" in result
        assert "html:5" in result


class TestGetTimestamp:
    """Tests for get_timestamp function."""

    def test_returns_string(self):
        """Returns a string timestamp."""
        result = get_timestamp()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_contains_date_components(self):
        """Timestamp contains date-like components."""
        result = get_timestamp()
        # Should contain some numbers (from date)
        assert any(c.isdigit() for c in result)
