# Source Code

> **Navigation**: [← README](../README.md) | [AGENTS.md](AGENTS.md) | [docs/](../docs/) | [scripts/](../scripts/)

Source code for course management software utilities.

---

## Statistics

- **21 Modules** across 5 layers
- **1001 Tests**
- **6 Output Formats**: PDF, DOCX, HTML, TXT, MD, MP3

---

## Module Architecture

### Layered Design

Modules are organized in layers by dependency:

```
Layer 4: Management (canvas_integration, danvas)
              ↑
Layer 3: Orchestration (batch_processing, html_website, schedule,
         course_generator, youtube_transcript)
              ↑
Layer 2: Extended (format_conversion, translation)
              ↑
Layer 1: Core (markdown_to_pdf, text_to_speech, speech_to_text, llm)
              ↑
Layer 0: Independent (module_organization, file_validation, publish, 
         content_processing, validation, lab_manual, legacy_import,
         course_config)
```

### Module Reference

| Module | Layer | Purpose | Key Function |
|--------|-------|---------|--------------|
| `batch_processing` | 3 | Multi-format batch generation | `process_module_by_type()` |
| `canvas_integration` | 4 | Canvas LMS upload | `upload_module_to_canvas()` |
| `content_processing` | 0 | Content transformation | `renumber_questions_in_course()` |
| `file_validation` | 0 | Structure validation | `validate_module_files()` |
| `format_conversion` | 2 | File format conversion | `convert_file()` |
| `html_website` | 3 | Website generation | `generate_module_website()` |
| `lab_manual` | 0 | Lab worksheet rendering | `render_lab_manual()` |
| `legacy_import` | 0 | Legacy format import | `import_legacy_course()` |
| `markdown_to_pdf` | 1 | PDF generation | `render_markdown_to_pdf()` |
| `module_organization` | 0 | Module structure creation | `create_module_structure()` |
| `publish` | 0 | Publishing to PUBLISHED/ | `publish_course()` |
| `schedule` | 3 | Schedule processing | `process_schedule()` |
| `speech_to_text` | 1 | Audio transcription | `transcribe_audio()` |
| `text_to_speech` | 1 | Audio generation | `generate_speech()` |
| `validation` | 0 | Output validation | `validate_published_directory()` |
| `course_config` | 0 | Per-course TOML config | `load_course_config()` |
| `course_generator` | 3 | Curriculum generation | `generate()` |
| `youtube_transcript` | 3 | YouTube transcript processing | `transcribe_video()` |
| `danvas` | 4 | Self-hosted Canvas LMS clone | `start_server()` |
| `llm` | 1 | Ollama LLM client | `OllamaClient.generate()` |
| `translation` | 2 | LLM-based content translation | `translate_file()` |

---

## Module Structure

Each module follows a consistent structure:

```
[module_name]/
├── __init__.py      # Public exports
├── main.py          # Public API functions
├── utils.py         # Internal helper functions
├── config.py        # Constants and configuration
└── AGENTS.md        # Technical documentation
```

### Clear Boundaries

- **Public Interface**: Only functions in `main.py` should be imported by other modules
- **Internal Implementation**: Functions in `utils.py` are private and not imported externally
- **Configuration**: `config.py` exposes constants but not implementation details

---

## Independent Usage

All modules can be used independently:

```python
# Use any module directly
from src.markdown_to_pdf.main import render_markdown_to_pdf
from src.file_validation.main import validate_module_files
from src.publish.main import publish_course

# Example: Single file conversion
render_markdown_to_pdf("input.md", "output.pdf")

# Example: Validate a module
result = validate_module_files("/path/to/module")
print(f"Valid: {result['valid']}")
```

### Module Import Pattern

```python
from src.[module_name].main import [function_name]
```

---

## Composable Design

Modules can be combined in various patterns:

### Sequential Composition

```python
from src.file_validation.main import validate_module_files
from src.batch_processing.main import process_module_by_type

# Validate first, then process
validation = validate_module_files(module_path)
if validation["valid"]:
    results = process_module_by_type(module_path, output_dir)
```

### Parallel Composition

```python
from src.markdown_to_pdf.main import render_markdown_to_pdf
from src.format_conversion.main import convert_file
from src.text_to_speech.main import generate_speech

# All can run independently
render_markdown_to_pdf("file.md", "file.pdf")
convert_file("file.md", "html", "file.html")
generate_speech("text", "file.mp3")
```

See [../docs/ORCHESTRATION.md](../docs/ORCHESTRATION.md) for detailed composition patterns.

---

## Detailed Module Documentation

Each module has its own AGENTS.md with:

- Module boundaries (what it does / doesn't do)
- Dependencies (internal and external)
- Public API documentation
- Usage examples

| Module | Documentation |
|--------|---------------|
| batch_processing | [AGENTS.md](batch_processing/AGENTS.md) |
| canvas_integration | [AGENTS.md](canvas_integration/AGENTS.md) |
| content_processing | [AGENTS.md](content_processing/AGENTS.md) |
| file_validation | [AGENTS.md](file_validation/AGENTS.md) |
| format_conversion | [AGENTS.md](format_conversion/AGENTS.md) |
| html_website | [AGENTS.md](html_website/AGENTS.md) |
| lab_manual | [AGENTS.md](lab_manual/AGENTS.md) |
| legacy_import | [AGENTS.md](legacy_import/AGENTS.md) |
| markdown_to_pdf | [AGENTS.md](markdown_to_pdf/AGENTS.md) |
| module_organization | [AGENTS.md](module_organization/AGENTS.md) |
| publish | [AGENTS.md](publish/AGENTS.md) |
| schedule | [AGENTS.md](schedule/AGENTS.md) |
| speech_to_text | [AGENTS.md](speech_to_text/AGENTS.md) |
| text_to_speech | [AGENTS.md](text_to_speech/AGENTS.md) |
| validation | [AGENTS.md](validation/AGENTS.md) |
| course_config | [AGENTS.md](course_config/AGENTS.md) |
| course_generator | [AGENTS.md](course_generator/AGENTS.md) |
| youtube_transcript | [AGENTS.md](youtube_transcript/AGENTS.md) |
| llm | [AGENTS.md](llm/AGENTS.md) |
| translation | [AGENTS.md](translation/AGENTS.md) |

---

## Code Standards

- **Python PEP 8**: Style guidelines followed
- **Type Hints**: All functions have type annotations
- **Docstrings**: All public functions documented
- **Real Methods**: No mocks or stubs (see [.cursorrules](.cursorrules))
- **Modular**: Self-contained, reusable modules
- **Logged**: Operations logged for debugging

---

## Related Documentation

| Document | Description |
|----------|-------------|
| [AGENTS.md](AGENTS.md) | Detailed API reference |
| [../docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md) | System architecture |
| [../docs/ORCHESTRATION.md](../docs/ORCHESTRATION.md) | Multi-module workflows |
| [../docs/QUICKSTART.md](../docs/QUICKSTART.md) | Quick start guide |
| [../scripts/README.md](../scripts/README.md) | CLI scripts documentation |
