"""Tests for lab_manual utils module functions."""

import tempfile
from pathlib import Path

import pytest

from src.lab_manual.utils import (
    LabElement,
    TableConfig,
    create_data_table_html,
    create_feasibility_html,
    create_lab_header_html,
    create_measurement_table_html,
    create_object_selection_html,
    create_reflection_html,
    ensure_output_directory,
    expand_fillable_fields,
    get_output_path,
    markdown_to_html,
    parse_object_selection,
    parse_reflection,
    parse_table_directive,
    read_markdown_file,
)


class TestTableConfig:
    """Tests for TableConfig dataclass."""

    def test_default_values(self):
        """Default values are set correctly."""
        config = TableConfig()
        
        assert config.rows == 5
        assert config.fillable is True
        assert config.title is None
        assert len(config.columns) == 3

    def test_custom_values(self):
        """Custom values are set correctly."""
        config = TableConfig(
            rows=10,
            columns=["A", "B"],
            fillable=False,
            title="Test Table"
        )
        
        assert config.rows == 10
        assert config.columns == ["A", "B"]
        assert config.fillable is False
        assert config.title == "Test Table"


class TestParseTableDirective:
    """Tests for parse_table_directive function."""

    def test_parse_basic_table(self):
        """Parse basic table directive."""
        content = """<!-- lab:data-table rows=3 -->
| A | B |
|---|---|
<!-- /lab:data-table -->"""
        
        config, remaining = parse_table_directive(content)
        
        assert config.rows == 3
        assert config.columns == ["A", "B"]

    def test_parse_table_with_title(self):
        """Parse table with title."""
        content = '''<!-- lab:data-table rows=5 title="My Table" -->
| X | Y | Z |
<!-- /lab:data-table -->'''
        
        config, _ = parse_table_directive(content)
        
        assert config.title == "My Table"

    def test_no_table_directive(self):
        """Return default config when no directive found."""
        content = "Regular markdown content"
        
        config, remaining = parse_table_directive(content)
        
        assert config.rows == 5  # Default
        assert remaining == content


class TestParseObjectSelection:
    """Tests for parse_object_selection function."""

    def test_parse_selection(self):
        """Parse object selection section."""
        content = """<!-- lab:object-selection -->
Object in room: test
<!-- /lab:object-selection -->"""
        
        config, _ = parse_object_selection(content)
        
        assert config["in_room"] is True
        assert config["not_in_room"] is True
        assert "Object in room" in config["content"]

    def test_no_selection(self):
        """Return empty dict when no directive."""
        config, remaining = parse_object_selection("No directive here")
        
        assert config == {}


class TestParseReflection:
    """Tests for parse_reflection function."""

    def test_parse_reflection(self):
        """Parse reflection section."""
        content = """<!-- lab:reflection -->
Reflect on this.
<!-- /lab:reflection -->"""
        
        config, _ = parse_reflection(content)
        
        assert "Reflect on this" in config["content"]


class TestExpandFillableFields:
    """Tests for expand_fillable_fields function."""

    def test_expand_text_input(self):
        """Expand {fill:text} to input element."""
        html = "Name: {fill:text}"
        
        result = expand_fillable_fields(html)
        
        assert '<input type="text" class="fill-text" />' in result

    def test_expand_textarea(self):
        """Expand {fill:textarea} to textarea element."""
        html = "{fill:textarea rows=5}"
        
        result = expand_fillable_fields(html)
        
        assert '<textarea class="fill-textarea" rows="5"></textarea>' in result

    def test_expand_table_cell(self):
        """Expand {fill} in table cells."""
        html = "<td> {fill} </td>"
        
        result = expand_fillable_fields(html)
        
        assert '<td class="fillable">' in result

    def test_expand_number_input(self):
        """Expand {fill:number} to number input element."""
        html = "Count: {fill:number}"

        result = expand_fillable_fields(html)

        assert '<input type="number" class="fill-number" />' in result

    def test_expand_standalone_fill(self):
        """Expand standalone {fill}."""
        html = "Value: {fill}"
        
        result = expand_fillable_fields(html)
        
        assert '<input type="text" class="fill-text" />' in result


class TestCreateDataTableHtml:
    """Tests for create_data_table_html function."""

    def test_basic_table(self):
        """Create basic data table."""
        config = TableConfig(rows=3, columns=["A", "B"])
        
        html = create_data_table_html(config)
        
        assert '<table class="lab-table">' in html
        assert "<th>A</th>" in html
        assert "<th>B</th>" in html
        assert html.count("<tr>") == 4  # 1 header + 3 data rows

    def test_fillable_cells(self):
        """Fillable cells have correct class."""
        config = TableConfig(rows=2, columns=["X"], fillable=True)
        
        html = create_data_table_html(config)
        
        assert 'class="fillable"' in html

    def test_with_title(self):
        """Table with title."""
        config = TableConfig(rows=1, columns=["A"], title="Test Title")
        
        html = create_data_table_html(config)
        
        assert "<h3>Test Title</h3>" in html


class TestCreateMeasurementTableHtml:
    """Tests for create_measurement_table_html function."""

    def test_default_columns(self):
        """Default measurement table has standard columns."""
        html = create_measurement_table_html()
        
        assert "Physical Aspect" in html
        assert "Measurement Device" in html
        assert "Measurement Unit" in html

    def test_with_aspects(self):
        """Pre-filled aspects appear in table."""
        aspects = ["Length", "Mass"]
        
        html = create_measurement_table_html(rows=3, aspects=aspects)
        
        assert "<td>Length</td>" in html
        assert "<td>Mass</td>" in html

    def test_without_device(self):
        """Exclude device column."""
        html = create_measurement_table_html(include_device=False)
        
        assert "Measurement Device" not in html

    def test_with_value(self):
        """Include value column."""
        html = create_measurement_table_html(include_value=True)
        
        assert "Measured Value" in html


class TestCreateObjectSelectionHtml:
    """Tests for create_object_selection_html function."""

    def test_both_fields(self):
        """Create section with both fields."""
        html = create_object_selection_html(in_room=True, not_in_room=True)
        
        assert "Object in room:" in html
        assert "Object NOT in room:" in html

    def test_only_in_room(self):
        """Create section with only in-room field."""
        html = create_object_selection_html(in_room=True, not_in_room=False)
        
        assert "Object in room:" in html
        assert "Object NOT in room:" not in html


class TestCreateFeasibilityHtml:
    """Tests for create_feasibility_html function."""

    def test_with_options(self):
        """Create feasibility section with checkbox options."""
        options = ["Option A", "Option B", "Option C"]
        
        html = create_feasibility_html("Test question?", options)
        
        assert "Test question?" in html
        assert 'type="checkbox"' in html
        assert "Option A" in html
        assert "Option B" in html
        assert "Option C" in html


class TestCreateReflectionHtml:
    """Tests for create_reflection_html function."""

    def test_with_prompt(self):
        """Create reflection box with prompt."""
        html = create_reflection_html(prompt="Reflect here")
        
        assert "Reflect here" in html
        assert 'class="reflection-box"' in html
        assert "textarea" in html


class TestCreateLabHeaderHtml:
    """Tests for create_lab_header_html function."""

    def test_full_header(self):
        """Create full header with all fields."""
        html = create_lab_header_html(
            lab_title="Test Lab",
            course_name="BIOL-1",
            include_name=True,
            include_date=True,
            include_section=True
        )
        
        assert "<h1>Test Lab</h1>" in html
        assert "BIOL-1" in html
        assert "Name:" in html
        assert "Date:" in html
        assert "Section:" in html

    def test_minimal_header(self):
        """Create header with minimal fields."""
        html = create_lab_header_html(
            lab_title="Lab",
            include_name=False,
            include_date=False,
            include_section=False
        )
        
        assert "<h1>Lab</h1>" in html
        assert "Name:" not in html


class TestMarkdownToHtml:
    """Tests for markdown_to_html function."""

    def test_basic_conversion(self):
        """Convert basic markdown to HTML."""
        md = "# Heading\n\nParagraph."
        
        html = markdown_to_html(md)
        
        assert "<h1>Heading</h1>" in html
        assert "<p>Paragraph.</p>" in html

    def test_tables(self):
        """Convert markdown tables."""
        md = """| A | B |
|---|---|
| 1 | 2 |"""
        
        html = markdown_to_html(md)
        
        assert "<table>" in html
        assert "<th>A</th>" in html


class TestFileOperations:
    """Tests for file I/O utility functions."""

    def test_read_markdown_file(self, temp_dir):
        """Read markdown file contents."""
        md_file = temp_dir / "test.md"
        md_file.write_text("# Test Content", encoding="utf-8")
        
        content = read_markdown_file(md_file)
        
        assert content == "# Test Content"

    def test_read_nonexistent_file(self, temp_dir):
        """Raise error for nonexistent file."""
        with pytest.raises(FileNotFoundError):
            read_markdown_file(temp_dir / "nonexistent.md")

    def test_ensure_output_directory(self, temp_dir):
        """Create output directory if needed."""
        output_path = temp_dir / "new_dir" / "output.pdf"
        
        ensure_output_directory(output_path)
        
        assert output_path.parent.exists()

    def test_get_output_path(self, temp_dir):
        """Generate correct output path."""
        input_path = temp_dir / "test.md"
        output_dir = temp_dir / "output"
        
        result = get_output_path(input_path, output_dir, ".pdf")
        
        assert result == output_dir / "test.pdf"


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)
