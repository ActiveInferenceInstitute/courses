# Testing Guide

> **Navigation**: [README](README.md) | [Architecture](ARCHITECTURE.md) | [Contributing](CONTRIBUTING.md) | [Quick Start](QUICKSTART.md)

Comprehensive guide to the test suite, conventions, and practices for the Active Inference Institute course pipeline.

---

## Overview

| Metric | Value |
|--------|-------|
| Framework | pytest |
| Test files | 65+ |
| Test location | `software/tests/` |
| Coverage tool | pytest-cov |
| Mock policy | **No mocks.** All tests use real implementations. |

---

## Running Tests

### All Tests

```bash
cd software

# Standard run
uv run pytest tests/ -v

# macOS (if DYLD_LIBRARY_PATH not in shell profile)
DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH" uv run pytest tests/ -v

# macOS wrapper script
./run_tests.sh
```

### Specific Tests

```bash
# Single file
uv run pytest tests/test_batch_processing_main.py -v

# Single test class
uv run pytest tests/test_batch_processing_main.py::TestProcessModuleByType -v

# Single test function
uv run pytest tests/test_batch_processing_main.py::TestProcessModuleByType::test_success -v

# By keyword
uv run pytest tests/ -k "test_pdf" -v

# By marker
uv run pytest tests/ -m "not requires_internet" -v
```

### Coverage

```bash
# Terminal report
uv run pytest tests/ --cov=src --cov-report=term-missing

# HTML report (opens in browser)
uv run pytest tests/ --cov=src --cov-report=html
open htmlcov/index.html

# Minimum threshold
uv run pytest tests/ --cov=src --cov-fail-under=70
```

---

## Test Organization

### Naming Convention

```
tests/test_{module_name}_{submodule}.py
```

Examples:
- `test_batch_processing_main.py` — Tests for `src/batch_processing/main.py`
- `test_batch_processing_utils.py` — Tests for `src/batch_processing/utils.py`
- `test_publish_main.py` — Tests for `src/publish/main.py`

### Test Categories

#### Module Tests

Test individual module functionality:

| Test File | Module | Focus |
|-----------|--------|-------|
| `test_batch_processing_main.py` | batch_processing | Core batch rendering |
| `test_batch_processing_utils.py` | batch_processing | Utility functions |
| `test_batch_processing_orchestration.py` | batch_processing | Course-level orchestration |
| `test_markdown_to_pdf_main.py` | markdown_to_pdf | PDF rendering |
| `test_text_to_speech_main.py` | text_to_speech | Audio generation |
| `test_speech_to_text_main.py` | speech_to_text | Audio transcription |
| `test_format_conversion_main.py` | format_conversion | Format conversion |
| `test_format_conversion_utils.py` | format_conversion | Conversion utilities |
| `test_html_website_utils.py` | html_website | Website generation |
| `test_html_website_features.py` | html_website | Feature configuration |
| `test_file_validation_main.py` | file_validation | File validation |
| `test_file_validation_utils.py` | file_validation | Validation utilities |
| `test_module_organization_main.py` | module_organization | Module scaffolding |
| `test_module_organization_utils.py` | module_organization | Organization utilities |
| `test_schedule_main.py` | schedule | Schedule processing |
| `test_schedule_utils.py` | schedule | Schedule utilities |
| `test_publish_main.py` | publish | Publishing |
| `test_publish_utils.py` | publish | Publish utilities |
| `test_validation_main.py` | validation | Output validation |
| `test_validation_utils.py` | validation | Validation utilities |
| `test_content_processing_main.py` | content_processing | Content transforms |
| `test_content_processing_utils.py` | content_processing | Content utilities |
| `test_lab_manual_main.py` | lab_manual | Lab rendering |
| `test_lab_manual_utils.py` | lab_manual | Lab utilities |
| `test_canvas_integration_main.py` | canvas_integration | Canvas upload |
| `test_canvas_integration_utils.py` | canvas_integration | Canvas utilities |
| `test_legacy_import_main.py` | legacy_import | Legacy import |
| `test_legacy_import_utils.py` | legacy_import | Import utilities |
| `test_course_generator_main.py` | course_generator | Curriculum generation |
| `test_course_generator_schema.py` | course_generator | Schema validation |
| `test_course_generator_scaffold.py` | course_generator | Scaffolding |
| `test_course_generator_content.py` | course_generator | Content generation |
| `test_course_generator_llm.py` | course_generator | LLM enrichment |
| `test_course_config.py` | course_config | Per-course config |
| `test_youtube_transcript_main.py` | youtube_transcript | YouTube transcription |
| `test_youtube_transcript_utils.py` | youtube_transcript | YouTube utilities |
| `test_danvas_main.py` | danvas | Danvas server |
| `test_danvas_utils.py` | danvas | Danvas utilities |
| `test_danvas_comprehensive.py` | danvas | Comprehensive Danvas tests |
| `test_llm.py` | llm | LLM client |
| `test_translation.py` | translation | Translation |

#### Script Tests

Test CLI script argument parsing and orchestration:

| Test File | Script |
|-----------|--------|
| `test_generate_all_outputs.py` | `generate_all_outputs.py` |
| `test_generate_module_renderings.py` | `generate_module_renderings.py` |
| `test_generate_module_website.py` | `generate_module_website.py` |
| `test_generate_syllabus_renderings.py` | `generate_syllabus_renderings.py` |
| `test_generate_dashboards.py` | `generate_dashboards.py` |
| `test_publish_all.py` | `publish_all.py` |
| `test_publish_course.py` | `publish_course.py` |
| `test_validate_outputs.py` | `validate_outputs.py` |
| `test_flatten_published.py` | `flatten_published.py` |
| `test_renumber_questions.py` | `renumber_questions.py` |
| `test_render_youtube_courses.py` | `render_youtube_courses.py` |
| `test_transcribe_youtube.py` | `transcribe_youtube.py` |
| `test_fix_stub_labs.py` | `fix_stub_labs.py` |
| `test_fix_stub_quizzes.py` | `fix_stub_quizzes.py` |
| `test_fix_stub_questions.py` | `fix_stub_questions.py` |
| `test_import_legacy_materials.py` | `import_legacy_materials.py` |

#### Integration and Verification Tests

| Test File | Purpose |
|-----------|---------|
| `test_imports.py` | Verify all modules import correctly |
| `test_dependencies.py` | Verify all dependencies are installed |
| `test_real_implementations.py` | Verify no mocks/stubs exist |
| `test_integration.py` | Cross-module integration |
| `test_orchestration.py` | Multi-module workflow patterns |
| `test_cli.py` | CLI argument parsing |

---

## Test Markers

| Marker | Description | Deselect |
|--------|-------------|----------|
| `requires_internet` | Tests needing internet (gTTS, etc.) | `-m "not requires_internet"` |
| `requires_api` | Tests needing external APIs | `-m "not requires_api"` |
| `requires_whisper` | Tests needing openai-whisper | `-m "not requires_whisper"` |

```bash
# Skip all external-dependency tests
uv run pytest tests/ -m "not (requires_internet or requires_api or requires_whisper)"
```

---

## Fixtures

Defined in `tests/conftest.py`:

| Fixture | Description |
|---------|-------------|
| `temp_dir` | Temporary directory, auto-cleaned |
| `sample_markdown_file` | Sample `.md` file for testing |
| `sample_text_file` | Sample `.txt` file for testing |
| `sample_module_structure` | Complete module directory with all content files |
| `sample_curriculum_files` | Files for each curriculum element type |

---

## Writing Tests

### AAA Pattern

```python
class TestFunctionName:
    """Tests for function_name."""

    def test_success(self, temp_dir):
        """Test normal operation."""
        # Arrange
        input_file = temp_dir / "input.md"
        input_file.write_text("# Test Content")

        # Act
        result = function_name(str(input_file))

        # Assert
        assert result["valid"] is True
        assert len(result["files"]) > 0

    def test_invalid_input(self, temp_dir):
        """Test error handling for invalid input."""
        with pytest.raises(ValueError, match="does not exist"):
            function_name("/nonexistent/path")
```

### Real Implementations Policy

**No mocks, stubs, or fakes.** All tests use:
- Real file operations (via `temp_dir` fixture)
- Real library calls (WeasyPrint, gTTS, etc.)
- Real validation logic

```python
# CORRECT: Use real files
def test_pdf_generation(self, temp_dir):
    md_file = temp_dir / "test.md"
    md_file.write_text("# Test\n\nContent here.")
    pdf_file = temp_dir / "output.pdf"
    render_markdown_to_pdf(str(md_file), str(pdf_file))
    assert pdf_file.exists()
    assert pdf_file.stat().st_size > 0

# WRONG: Never use mocks
def test_pdf_generation_mock(self):
    with patch("weasyprint.HTML") as mock:
        mock.return_value.write_pdf.return_value = b"fake"
        ...  # Don't do this
```

---

## Verification Tests

### Import Verification

Ensures all modules import without errors:

```bash
uv run pytest tests/test_imports.py -v
```

### Dependency Verification

Ensures all required libraries are installed:

```bash
uv run pytest tests/test_dependencies.py -v
```

### Real Implementation Verification

Scans for mock/stub patterns and fails if found:

```bash
uv run pytest tests/test_real_implementations.py -v
```

---

## Troubleshooting Tests

### WeasyPrint/PDF Failures

```bash
# Ensure system libraries are available
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
uv run pytest tests/test_markdown_to_pdf_main.py -v
```

### Skip Slow Tests

```bash
# Skip PDF and audio tests
uv run pytest tests/ -k "not (pdf or audio or mp3)" -v
```

### Run Only Fast Tests

```bash
# Text-based tests only
uv run pytest tests/ -m "not (requires_internet or requires_api)" -k "not pdf" -v
```

---

*Last Updated: 2026-02-14*
