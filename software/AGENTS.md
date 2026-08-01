# Software Technical Documentation

## Overview

Technical documentation for course management software utilities, including function signatures, module APIs, and code organization.

## Test Coverage

**Overall: 75%** (1,014 tests collected; CI-equivalent gate ~995 passing, 34 network/external/whisper tests deselected)

| Module | Coverage | Notes |
| ------ | -------- | ----- |
| `batch_processing` | 78% | Main processing functions |
| `canvas_integration` | 45% | External API |
| `file_validation` | 91-92% | Validation utilities |
| `format_conversion` | 80-98% | Format-specific converters |
| `html_website` | 92-100% | Website generation |
| `lab_manual` | 90-95% | Lab rendering |
| `markdown_to_pdf` | 90-92% | PDF generation |
| `module_organization` | 78-93% | Module structure |
| `publish` | 80-84% | Course publishing |
| `schedule` | 93% | Schedule processing |
| `speech_to_text` | 88-98% | Audio transcription |
| `text_to_speech` | 89-91% | Audio generation |
| `validation` | 31-64% | Output validation (syllabus, study guides) |
| `content_processing` | — | Content transformation |
| `course_config` | — | Layered TOML-based per-course config |
| `course_generator` | — | Schema-driven curriculum generation |
| `legacy_import` | — | Legacy format import |
| `youtube_transcript` | — | YouTube transcript processing |

## Modular Architecture

The software follows a modular architecture where each module is self-contained and can be used independently.

### Module Structure Standards

Every module follows a consistent structure:

```text
module_name/
├── __init__.py      # Exports public functions from main.py
├── main.py          # Public API (only way other modules should interact)
├── utils.py         # Internal helper functions (private to module)
└── config.py        # Constants and configuration
```

### Dependency Rules

Modules are organized in layers to minimize dependencies:

- **Layer 0 (Independent)**: No dependencies on other modules
  - `module_organization`, `file_validation`

- **Layer 1 (Core)**: Depend only on external libraries
  - `markdown_to_pdf`, `text_to_speech`, `speech_to_text`

- **Layer 2 (Format)**: Depend on Layer 1 modules
  - `format_conversion`

- **Layer 3 (Orchestration)**: Compose lower-layer modules
  - `batch_processing`, `html_website`, `schedule`

- **Layer 4 (Integration)**: Use validation and external services
  - `canvas_integration`, `publish`

### Interface Contracts

When modules interact, they do so through well-defined interfaces:

- **Public API**: Functions in `main.py` are the public interface
- **Type Hints**: All functions have complete type annotations
- **Return Values**: Consistent return types (dicts with known keys)
- **Error Handling**: Exceptions are documented and predictable
- **Side Effects**: File operations and external calls are explicit

### Module Independence

Each module entry below indicates:

- **Standalone**: Can be used without other modules (Yes/No)
- **Dependencies**: Required modules or libraries
- **Interface**: How other modules interact with it

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for detailed design principles.

## Software Modules

### Markdown to PDF Rendering

**Purpose**: Convert Markdown course materials to PDF format

**Location**: `src/markdown_to_pdf/`

**Standalone**: Yes - can be used independently

**Dependencies**: WeasyPrint (external library), Markdown parser

**Key Functions**:

- `render_markdown_to_pdf(input_path: str, output_path: str, css_content: Optional[str] = None, pdf_options: Optional[Dict[str, Any]] = None) -> None`
- `batch_render_markdown(directory: str, output_dir: str) -> List[str]`
- `configure_pdf_options(template: str, options: dict) -> dict`

**Used by**: `format_conversion`, `batch_processing`, `schedule`, `html_website`

### Text-to-Speech Generation

**Purpose**: Generate audio content from text materials

**Location**: `src/text_to_speech/`

**Standalone**: Yes - can be used independently (requires internet for gTTS)

**Dependencies**: gTTS (external library), audio file handling

**Key Functions**:

- `generate_speech(text: str, output_path: str, voice: str = "default", lang: Optional[str] = None, slow: bool = False) -> None`
- `batch_generate_speech(input_dir: str, output_dir: str) -> List[str]`
- `configure_voice_settings(voice: str, speed: float, pitch: float) -> dict`

**Used by**: `format_conversion`, `batch_processing`, `schedule`

### Format Conversion

**Purpose**: Batch processing of file format conversions

**Location**: `src/format_conversion/`

**Standalone**: Yes - can be used independently (requires core converters)

**Dependencies**: Core converters (`markdown_to_pdf`, `text_to_speech`), python-docx, pypdf

**Key Functions**:

- `convert_file(input_path: str, output_format: str, output_path: str) -> None`
- `batch_convert(directory: str, input_format: str, output_format: str) -> List[str]`
- `get_supported_formats() -> dict`

**Used by**: `batch_processing`, `html_website`, `schedule`

### Module Organization

**Purpose**: Automated structure creation for new modules

**Location**: `src/module_organization/`

**Standalone**: Yes - no dependencies on other modules

**Dependencies**: None (file system operations only)

**Key Functions**:

- `create_module_structure(course_path: str, module_number: int) -> str`
- `create_next_module(course_path: str) -> str` - Create next module in sequence
- `validate_module_structure(module_path: str) -> bool`
- `initialize_module_files(module_path: str, template: str) -> None`
- `list_course_modules(course_path: str) -> List[str]` - List all modules in course
- `get_module_statistics(module_path: str) -> dict` - Get module statistics

**Utility Functions**:

- `get_module_number_from_path(module_path: Path) -> int` - Extract module number
- `list_all_modules(course_path: Path) -> List[Path]` - List all module directories
- `get_next_module_number(course_path: Path) -> int` - Get next available module number

**Used by**: Test orchestration, module creation scripts

### Canvas Integration

**Purpose**: Scripts for batch uploading module materials

**Location**: `src/canvas_integration/`

**Standalone**: Yes - can be used independently (requires file_validation)

**Dependencies**: `file_validation` (for validation), Canvas API client, requests library

**Key Functions**:

- `upload_module_to_canvas(module_path: str, course_id: str, api_key: str, domain: str = "canvas.instructure.com") -> dict`
- `validate_upload_readiness(module_path: str) -> List[str]`
- `sync_module_structure(module_path: str, canvas_course_id: str, api_key: str, domain: str = "canvas.instructure.com") -> dict`

**Used by**: Canvas upload scripts

### File Validation

**Purpose**: Checks for required files in each module

**Location**: `src/file_validation/`

**Standalone**: Yes - no dependencies on other modules

**Dependencies**: None (file system operations only)

**Key Functions**:

- `validate_module_files(module_path: str) -> dict`
- `check_naming_conventions(directory: str) -> List[str]`
- `verify_required_structure(module_path: str) -> bool`
- `validate_course_structure(course_path: str) -> dict` - Validate entire course
- `get_validation_report(module_path: str) -> dict` - Detailed validation report
- `find_missing_materials(module_path: str) -> dict` - Find missing materials
- `check_file_sizes(module_path: str, max_size: int) -> List[str]` - Check file sizes

**Utility Functions**:

- `get_file_type(file_name: str) -> str` - Determine file type (assignment, lecture, etc.)
- `extract_module_number_from_filename(file_name: str) -> int` - Extract module number from filename
- `validate_file_name_structure(file_name: str) -> dict` - Comprehensive file name validation

**Used by**: `batch_processing`, `canvas_integration`

### Speech-to-Text

**Purpose**: Transcribe audio files to text

**Location**: `src/speech_to_text/`

**Standalone**: Yes - can be used independently

**Dependencies**: SpeechRecognition (external library), pydub

**Key Functions**:

- `transcribe_audio(audio_path: str, output_path: str, language: str = "en") -> str`
- `batch_transcribe_audio(input_dir: str, output_dir: str) -> List[str]`
- `transcribe_from_markdown(markdown_path: str, output_path: str) -> str`

**Used by**: Format conversion workflows

### Batch Processing

**Purpose**: Process entire modules for multiple format conversions

**Location**: `src/batch_processing/`

**Standalone**: Yes - can be used independently (requires core/format modules)

**Dependencies**: `markdown_to_pdf`, `text_to_speech`, `format_conversion`, `file_validation`

**Key Functions**:

- `process_module_to_pdf(module_path: str, output_dir: str) -> List[str]`
- `process_module_to_audio(module_path: str, output_dir: str) -> List[str]`
- `process_module_to_text(module_path: str, output_dir: str) -> List[str]`
- `generate_module_media(module_path: str, output_dir: str) -> dict`
- `process_module_by_type(module_path: str, output_dir: str) -> dict` - Process by curriculum element type
- `process_syllabus(syllabus_path: str, output_dir: str) -> dict` - Process syllabus files
- `clear_all_outputs(repo_root: Path) -> dict` - Clear all output directories
- `process_module_website(module_path: str, output_dir: Optional[str] = None) -> str` - Generate module website

**Used by**: `html_website`, generation scripts

### HTML Website Generation

**Purpose**: Generate HTML websites for modules with audio, quizzes, and interactive features

**Location**: `src/html_website/`

**Standalone**: Yes - can be used independently (requires batch_processing, format_conversion)

**Dependencies**: `batch_processing`, `format_conversion`, markdown2

**Key Functions**:

- `generate_module_website(module_path: str, output_dir: Optional[str] = None, course_name: Optional[str] = None) -> str`

**Features**:

- Dark mode toggle with localStorage persistence
- Back to top button
- Collapsible sections
- Interactive quizzes (multiple choice, true/false, matching, free response)
- Embedded audio players
- Print-friendly layout
- Mobile responsive design

**Used by**: Website generation scripts

### Lab Manual Rendering

**Purpose**: Render rich lab manuals from Markdown with data tables, measurement exercises, and fillable worksheets

**Location**: `src/lab_manual/`

**Standalone**: Yes - can be used independently

**Dependencies**: `markdown`, `weasyprint`

**Key Functions**:

- `render_lab_manual(input_path: str, output_path: str, output_format: str = "pdf", lab_title: Optional[str] = None, course_name: Optional[str] = None, include_header: bool = True) -> str`
- `parse_lab_elements(markdown_content: str) -> List[LabElement]`
- `generate_data_table(rows: int = 5, columns: Optional[List[str]] = None, title: Optional[str] = None) -> str`
- `generate_measurement_table(rows: int = 5, aspects: Optional[List[str]] = None, include_device: bool = True, include_unit: bool = True, include_value: bool = False) -> str`
- `batch_render_lab_manuals(directory: str, output_dir: str, output_format: str = "pdf", course_name: Optional[str] = None) -> List[str]`
- `get_lab_template(template_name: str = "basic") -> str`

**Lab Directive Syntax**:

- `<!-- lab:data-table rows=N title="Title" -->` - Fillable data tables
- `<!-- lab:object-selection -->` - Object selection fields
- `<!-- lab:measurement-feasibility -->` - Feasibility analysis sections
- `<!-- lab:reflection -->` - Reflection boxes

**Fillable Fields**:

- `{fill}` - Basic fillable cell
- `{fill:text}` - Inline text input
- `{fill:textarea rows=N}` - Multi-line text area

**Used by**: Lab generation scripts

### Schedule Processing

**Purpose**: Parse schedule markdown files and generate outputs in multiple formats

**Location**: `src/schedule/`

**Standalone**: Yes - can be used independently (requires core/format modules)

**Dependencies**: `markdown_to_pdf`, `text_to_speech`, `format_conversion`

**Key Functions**:

- `parse_schedule_markdown(schedule_path: str) -> Dict[str, Any]`
- `process_schedule(schedule_path: str, output_dir: str, formats: Optional[List[str]] = None) -> Dict[str, Any]`
- `generate_schedule_outputs(schedule_data: Dict[str, Any], output_dir: Path, base_name: str, formats: List[str]) -> Dict[str, List[str]]`
- `batch_process_schedules(directory: str, output_dir: str, formats: Optional[List[str]] = None) -> Dict[str, Any]`

**Used by**: Schedule generation scripts

### Publish Module

**Purpose**: Export finalized course materials to the public `PUBLISHED/` directory

**Location**: `src/publish/`

**Standalone**: Yes - no dependencies on other modules

**Dependencies**: None (shutil, pathlib only)

**Key Functions**:

- `publish_course(course_path: str, publish_root: str = None) -> Dict[str, Any]` - Main publishing logic
- `get_course_config(course_name: str) -> Dict[str, str]` - Get course-specific configuration
- `copy_directory_contents(src: Path, dst: Path, exclude_patterns: Optional[List[str]] = None) -> int` - Intelligent copy

**Used by**: Publishing scripts

### Validation Module

**Purpose**: Validate output files and directory structure for published courses

**Location**: `src/validation/`

**Standalone**: Yes - no dependencies on other modules

**Dependencies**: None (pathlib only)

**Key Functions**:

- `validate_module_outputs(module_dir: Path) -> Dict[str, Any]` - Validate a module's output directory
- `validate_syllabus_outputs(course_dir: Path) -> Dict[str, Any]` - Validate syllabus outputs (flat structure)
- `validate_published_directory(published_dir: Path, course: str) -> Dict[str, Any]` - Validate published directory
- `run_validation(course: str, published_dir: Path) -> Dict[str, Any]` - Run full validation suite

**Configuration** (`config.py`):

- `EXPECTED_FORMATS`: Required output formats (`["pdf", "docx", "html", "txt"]`)
- `EXPECTED_STUDY_GUIDE_FILES`: Required study guide files per module
- `OPTIONAL_STUDY_GUIDE_FILES`: Optional files (e.g., MP3 audio narration)
- `SYLLABUS_REQUIRED_FORMATS` / `SYLLABUS_OPTIONAL_FORMATS`: Format requirements for syllabus

**Utility Functions** (`utils.py`):

- `count_files_by_extension(directory: Path) -> Dict[str, int]` - Count files by extension
- `get_module_directories(course_dir: Path) -> List[Path]` - Get all module directories
- `check_study_guide_files(module_path: Path) -> Dict[str, bool]` - Check study guide files exist
- `check_output_directory_structure(module_path: Path) -> Dict[str, Any]` - Validate output structure
- `check_lab_outputs(labs_dir: Path) -> Dict[str, Any]` - Validate lab outputs

**Used by**: `scripts/validate_outputs.py`, `scripts/publish_all.py`

### LLM Integration (Ollama)

**Purpose**: Client for interacting with local Ollama LLM instances for text generation and structured output

**Location**: `src/llm/`

**Standalone**: Yes - can be used independently (requires running Ollama)

**Dependencies**: `requests`, Ollama (external service)

**Key Functions** (`OllamaClient` class):

- `OllamaClient(base_url: str = DEFAULT_BASE_URL, model: str = DEFAULT_MODEL, timeout: int = DEFAULT_TIMEOUT)` - Initialize client
- `is_available(force_check: bool = False) -> bool` - Check if Ollama is reachable
- `generate(prompt: str, system: str = SYSTEM_DEFAULT, model: Optional[str] = None, temperature: float = DEFAULT_TEMPERATURE, format: Optional[str] = None, stream: bool = False) -> Union[str, Generator]` - Generate text completion
- `generate_structured(prompt: str, schema: Optional[Dict] = None, model: Optional[str] = None, temperature: float = DEFAULT_TEMPERATURE) -> Dict` - Generate structured JSON output

**Used by**: `translation`, `course_generator`

### Danvas (Course Management Server)

**Purpose**: Lightweight HTTP server for browsing courses, managing enrollments, gradebook, announcements, and calendar

**Location**: `src/danvas/`

**Standalone**: Yes - zero external framework dependencies (built on `http.server`)

**Dependencies**: None (stdlib only), optional `batch_processing` for logging

**Key Functions**:

- `start_server(repo_root: Path, port: int = DANVAS_PORT, host: str = DANVAS_HOST, data_dir: Optional[Path] = None) -> HTTPServer` - Start the Danvas HTTP server
- `DanvasHandler` class - HTTP request handler with routing, HTML/JSON responses, form handling

**Features**:

- Course browsing and navigation
- Enrollment management
- Gradebook tracking
- Announcements and calendar
- URL-encoded POST form processing
- Built-in logging

**Used by**: CLI entry point (`python -m src.danvas.main`)

### Translation

**Purpose**: Translate course content files to other languages using LLM

**Location**: `src/translation/`

**Standalone**: No - depends on `llm` module

**Dependencies**: `llm` (OllamaClient), Ollama (external service)

**Key Functions**:

- `translate_text(text: str, target_lang: str, source_lang: str = DEFAULT_SOURCE_LANG, client: Optional[OllamaClient] = None) -> str` - Translate text using LLM
- `translate_file(input_path: str, target_lang: str, output_path: Optional[str] = None, client: Optional[OllamaClient] = None) -> str` - Translate a file

**Features**:

- Automatic text chunking for long documents
- Graceful fallback (keeps original text on chunk failure)
- Language name resolution from codes
- File extension validation

**Used by**: `scripts/translate_course.py`, `scripts/translate_youtube.py`

## Code Organization

### Directory Structure

```text
software/
├── src/              # Source code
│   ├── batch_processing/
│   ├── canvas_integration/
│   ├── content_processing/
│   ├── course_config/
│   ├── course_generator/
│   ├── danvas/
│   ├── file_validation/
│   ├── format_conversion/
│   ├── html_website/
│   ├── lab_manual/
│   ├── legacy_import/
│   ├── llm/
│   ├── markdown_to_pdf/
│   ├── module_organization/
│   ├── publish/
│   ├── schedule/
│   ├── speech_to_text/
│   ├── text_to_speech/
│   ├── translation/
│   ├── validation/
│   └── youtube_transcript/
├── tests/            # Test files
│   └── [mirrors src/ structure]
├── scripts/          # Generation scripts
└── docs/             # Documentation
    └── [module-specific docs]
```

### Module Structure

Each module in `src/` follows this structure:

- `__init__.py`: Module initialization and exports
- `main.py` or `[module_name].py`: Core functionality
- `utils.py`: Utility functions
- `config.py`: Configuration management

### Testing Structure

Test files in `tests/` mirror the source structure:

- `test_[module_name].py`: Unit tests for each module
- `test_integration.py`: Integration tests
- `test_utils.py`: Utility function tests

## Real Methods Policy

### Core Principle

**All code uses real methods and implementations - no mocks, stubs, or fake methods.**

### Implementation Standards

- All functions use real library implementations (weasyprint, gTTS, requests, etc.)
- All file operations use real file system operations
- All validation uses real validation logic
- All API integrations use real API clients (with proper error handling)

### Testing Standards

- Tests use real file operations and real library calls
- No mocks or stubs in test code
- External API tests validate structure/logic, not actual API calls
- Integration tests that require external services are clearly marked

### External Dependencies

- Real library calls for all functionality
- Proper error handling for network operations
- Graceful degradation when external services are unavailable
- Clear documentation of external service requirements

## Development Workflow

### Adding New Modules

1. Create module directory in `src/`
2. Implement core functionality following module structure using real methods
3. Write tests in `tests/` mirroring source structure using real implementations
4. Document in module-specific docs
5. Update this AGENTS.md with function signatures

### Testing

1. Run unit tests: `pytest tests/`
2. Run integration tests: `pytest tests/test_integration.py`
3. Validate code coverage: `pytest --cov=src tests/`
4. All tests must use real methods - no mocks or stubs

### Documentation

1. Update module README.md with usage examples
2. Document function signatures in module AGENTS.md
3. Update main software AGENTS.md with new module information

## Dependencies

### Core Dependencies

- Python 3.x
- Markdown parser
- PDF generation library
- Text-to-speech engine
- Canvas API client

### Development Dependencies

- pytest: Testing framework
- pytest-cov: Code coverage
- black: Code formatting
- mypy: Type checking

## Build and Deployment

### Build Process

- Automated compilation and packaging
- Dependency management
- Version control

### Deployment

- Package distribution
- Installation scripts
- Configuration management
