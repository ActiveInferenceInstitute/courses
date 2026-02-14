"""Tests for lab_manual main module functions."""

import tempfile
from pathlib import Path

import pytest

from src.lab_manual.main import (
    batch_render_lab_manuals,
    generate_data_table,
    generate_measurement_table,
    get_lab_template,
    parse_lab_elements,
    render_lab_manual,
)


class TestParseLabElements:
    """Tests for parse_lab_elements function."""

    def test_parse_empty_content(self):
        """Empty content returns empty list."""
        result = parse_lab_elements("")
        assert result == []

    def test_parse_data_table(self):
        """Parse data table directive."""
        content = """# Test
<!-- lab:data-table rows=3 -->
| Col1 | Col2 |
|------|------|
| {fill} | {fill} |
<!-- /lab:data-table -->
More content"""
        
        elements = parse_lab_elements(content)
        
        assert len(elements) == 1
        assert elements[0].element_type == "data-table"
        assert elements[0].config["rows"] == 3
        assert elements[0].config["columns"] == ["Col1", "Col2"]

    def test_parse_data_table_with_title(self):
        """Parse data table with title attribute."""
        content = """<!-- lab:data-table rows=5 title="My Table" -->
| A | B | C |
|---|---|---|
<!-- /lab:data-table -->"""
        
        elements = parse_lab_elements(content)
        
        assert len(elements) == 1
        assert elements[0].config["title"] == "My Table"
        assert elements[0].config["columns"] == ["A", "B", "C"]

    def test_parse_object_selection(self):
        """Parse object selection directive."""
        content = """<!-- lab:object-selection -->
Object in room: {fill:text}
Object NOT in room: {fill:text}
<!-- /lab:object-selection -->"""
        
        elements = parse_lab_elements(content)
        
        assert len(elements) == 1
        assert elements[0].element_type == "object-selection"
        assert elements[0].config["in_room"] is True
        assert elements[0].config["not_in_room"] is True

    def test_parse_measurement_feasibility(self):
        """Parse measurement feasibility directive."""
        content = """<!-- lab:measurement-feasibility -->
What can we measure?
{fill:textarea rows=3}
<!-- /lab:measurement-feasibility -->"""
        
        elements = parse_lab_elements(content)
        
        assert len(elements) == 1
        assert elements[0].element_type == "measurement-feasibility"
        assert "What can we measure?" in elements[0].content

    def test_parse_reflection(self):
        """Parse reflection directive."""
        content = """<!-- lab:reflection -->
Reflect on your findings.
<!-- /lab:reflection -->"""
        
        elements = parse_lab_elements(content)
        
        assert len(elements) == 1
        assert elements[0].element_type == "reflection"

    def test_parse_calculation(self):
        """Parse calculation directive."""
        content = """<!-- lab:calculation -->
**Show your work:**

P(Heads) = {fill:number} / 20 = {fill:number}
<!-- /lab:calculation -->"""

        elements = parse_lab_elements(content)

        assert len(elements) == 1
        assert elements[0].element_type == "calculation"
        assert "Show your work" in elements[0].content

    def test_parse_multiple_elements(self):
        """Parse multiple different elements."""
        content = """<!-- lab:object-selection -->
Object: {fill:text}
<!-- /lab:object-selection -->

<!-- lab:data-table rows=2 -->
| A | B |
|---|---|
<!-- /lab:data-table -->

<!-- lab:reflection -->
Notes
<!-- /lab:reflection -->"""
        
        elements = parse_lab_elements(content)
        
        assert len(elements) == 3
        assert elements[0].element_type == "object-selection"
        assert elements[1].element_type == "data-table"
        assert elements[2].element_type == "reflection"
        # Should be sorted by position
        assert elements[0].start_pos < elements[1].start_pos < elements[2].start_pos


class TestGenerateDataTable:
    """Tests for generate_data_table function."""

    def test_default_table(self):
        """Generate table with default settings."""
        html = generate_data_table()
        
        assert '<table class="lab-table">' in html
        assert "<thead>" in html
        assert "<tbody>" in html
        assert 'class="row-number"' in html

    def test_custom_rows(self):
        """Generate table with custom row count."""
        html = generate_data_table(rows=3)
        
        # Should have 3 data rows
        assert html.count('<td class="row-number">') == 3

    def test_custom_columns(self):
        """Generate table with custom columns."""
        columns = ["Time", "Temp", "Notes"]
        html = generate_data_table(columns=columns)
        
        for col in columns:
            assert f"<th>{col}</th>" in html

    def test_with_title(self):
        """Generate table with title."""
        html = generate_data_table(title="My Data Table")
        
        assert "<h3>My Data Table</h3>" in html


class TestGenerateMeasurementTable:
    """Tests for generate_measurement_table function."""

    def test_default_measurement_table(self):
        """Generate measurement table with defaults."""
        html = generate_measurement_table()
        
        assert '<table class="measurement-table">' in html
        assert "Physical Aspect" in html
        assert "Measurement Device" in html
        assert "Measurement Unit" in html

    def test_with_prefilled_aspects(self):
        """Generate table with pre-filled aspects."""
        aspects = ["Length", "Mass", "Volume"]
        html = generate_measurement_table(rows=5, aspects=aspects)
        
        for aspect in aspects:
            assert f"<td>{aspect}</td>" in html

    def test_exclude_device_column(self):
        """Exclude device column."""
        html = generate_measurement_table(include_device=False)
        
        assert "Measurement Device" not in html
        assert "Physical Aspect" in html
        assert "Measurement Unit" in html

    def test_include_value_column(self):
        """Include value column."""
        html = generate_measurement_table(include_value=True)
        
        assert "Measured Value" in html


class TestRenderLabManual:
    """Tests for render_lab_manual function."""

    def test_render_to_html(self, temp_dir):
        """Render lab manual to HTML."""
        # Create input file
        input_file = temp_dir / "test-lab.md"
        input_file.write_text("""# Test Lab

## Objective
Test objective.

<!-- lab:data-table rows=2 -->
| A | B |
|---|---|
<!-- /lab:data-table -->
""", encoding="utf-8")
        
        output_file = temp_dir / "output" / "test-lab.html"
        
        result = render_lab_manual(
            str(input_file),
            str(output_file),
            output_format="html",
            course_name="Test Course"
        )
        
        assert Path(result).exists()
        content = Path(result).read_text(encoding="utf-8")
        assert "<title>Test Lab</title>" in content
        assert "Test Course" in content
        assert '<table class="lab-table">' in content

    def test_render_to_pdf(self, temp_dir):
        """Render lab manual to PDF."""
        input_file = temp_dir / "test-lab.md"
        input_file.write_text("""# Test Lab

Basic content.
""", encoding="utf-8")
        
        output_file = temp_dir / "output" / "test-lab.pdf"
        
        result = render_lab_manual(
            str(input_file),
            str(output_file),
            output_format="pdf"
        )
        
        assert Path(result).exists()
        # PDF should be non-empty
        assert Path(result).stat().st_size > 0

    def test_file_not_found(self, temp_dir):
        """Raise error for missing input file."""
        with pytest.raises(FileNotFoundError):
            render_lab_manual(
                str(temp_dir / "nonexistent.md"),
                str(temp_dir / "output.pdf")
            )

    def test_invalid_format(self, temp_dir):
        """Raise error for invalid output format."""
        input_file = temp_dir / "test.md"
        input_file.write_text("# Test", encoding="utf-8")
        
        with pytest.raises(ValueError, match="Invalid output format"):
            render_lab_manual(
                str(input_file),
                str(temp_dir / "output.doc"),
                output_format="doc"
            )

    def test_auto_extract_title(self, temp_dir):
        """Auto-extract title from first heading."""
        input_file = temp_dir / "test.md"
        input_file.write_text("# My Custom Lab Title\n\nContent.", encoding="utf-8")
        
        output_file = temp_dir / "output.html"
        
        render_lab_manual(str(input_file), str(output_file), output_format="html")
        
        content = output_file.read_text(encoding="utf-8")
        assert "<title>My Custom Lab Title</title>" in content


class TestBatchRenderLabManuals:
    """Tests for batch_render_lab_manuals function."""

    def test_batch_render(self, temp_dir):
        """Batch render multiple lab files."""
        # Create lab files
        (temp_dir / "lab-1.md").write_text("# Lab 1\nContent.", encoding="utf-8")
        (temp_dir / "lab-2.md").write_text("# Lab 2\nContent.", encoding="utf-8")
        
        output_dir = temp_dir / "output"
        
        results = batch_render_lab_manuals(
            str(temp_dir),
            str(output_dir),
            output_format="html"
        )
        
        assert len(results) == 2
        for result in results:
            assert Path(result).exists()

    def test_batch_empty_directory(self, temp_dir):
        """Handle directory with no markdown files."""
        output_dir = temp_dir / "output"
        
        results = batch_render_lab_manuals(
            str(temp_dir),
            str(output_dir)
        )
        
        assert results == []

    def test_batch_invalid_directory(self, temp_dir):
        """Raise error for invalid directory."""
        with pytest.raises(ValueError, match="does not exist"):
            batch_render_lab_manuals(
                str(temp_dir / "nonexistent"),
                str(temp_dir / "output")
            )


class TestGetLabTemplate:
    """Tests for get_lab_template function."""

    def test_basic_template(self):
        """Get basic template."""
        template = get_lab_template("basic")
        
        assert "# Lab Title" in template
        assert "## Objectives" in template
        assert "<!-- lab:data-table" in template

    def test_measurement_template(self):
        """Get measurement template."""
        template = get_lab_template("measurement")
        
        assert "# Measurement Lab" in template
        assert "<!-- lab:object-selection -->" in template
        assert "Physical Aspect" in template

    def test_observation_template(self):
        """Get observation template."""
        template = get_lab_template("observation")
        
        assert "# Observation Lab" in template
        assert "Observation Log" in template

    def test_invalid_template(self):
        """Raise error for invalid template name."""
        with pytest.raises(ValueError, match="Unknown template"):
            get_lab_template("nonexistent")


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)
