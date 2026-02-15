# Course Management Software

## Overview

This directory contains executable code and utilities for managing course materials, including tools for content generation, format conversion, and course management automation.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and environment setup.

### Installation

1. Install uv (if not already installed):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install system dependencies (macOS):

   ```bash
   brew install cairo pango gdk-pixbuf glib
   ```

   These are required for WeasyPrint (PDF generation). On Linux, install via your package manager:

   ```bash
   # Ubuntu/Debian
   sudo apt-get install python3-cairo python3-pango libgdk-pixbuf2.0-dev libffi-dev
   
   # Fedora/RHEL
   sudo dnf install cairo pango gdk-pixbuf2 glib2 libffi
   ```

3. Install Python dependencies:

   ```bash
   uv sync --extra dev
   ```

4. Set library path (macOS only):

   ```bash
   export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
   ```

   Add this to your `~/.zshrc` or `~/.bash_profile` to make it permanent:

   ```bash
   echo 'export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

   **Note**: You may need to restart your terminal or run `source ~/.zshrc` for the change to take effect.

5. Verify installation:

   ```bash
   export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
   uv run python -c "from weasyprint import HTML; print('✓ WeasyPrint: OK')"
   uv run python -c "from src.format_conversion.main import convert_file; print('✓ Format conversion: OK')"
   uv run pytest tests/test_imports.py -v
   ```

### Running Tests

**Note**: On macOS, ensure `DYLD_LIBRARY_PATH` is set (see Installation step 4).

**Important**: Always use `uv run pytest` to ensure tests run in the correct environment with all dependencies.

Run all tests:

```bash
# macOS (with library path)
DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH" uv run pytest

# Or if already in your shell environment
uv run pytest
```

Run tests with coverage:

```bash
DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH" uv run pytest --cov=src --cov-report=html
```

Run specific test modules:

```bash
DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH" uv run pytest tests/test_module_organization_main.py -v
```

Run import verification tests:

```bash
uv run pytest tests/test_imports.py -v
```

Run dependency verification tests:

```bash
uv run pytest tests/test_dependencies.py -v
```

Run real implementation verification tests:

```bash
uv run pytest tests/test_real_implementations.py -v
```

### Dependencies

All required dependencies are specified in `pyproject.toml`:

- `gtts>=2.5.0` - Google Text-to-Speech
- `speechrecognition>=3.10.0` - Speech recognition
- `pydub>=0.25.1` - Audio processing
- `markdown>=3.5.0` - Markdown processing
- `weasyprint>=60.0` - PDF generation
- `python-docx>=1.1.0` - DOCX generation
- `pypdf>=4.0.0` - PDF processing
- `markdown2>=2.4.0` - Additional markdown support

Install all dependencies:

```bash
uv sync --extra dev
```

Verify dependencies are installed:

```bash
uv run pytest tests/test_dependencies.py -v
```

### Development

Activate the virtual environment:

```bash
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

Or use uv to run commands directly:

```bash
uv run python -m src.markdown_to_pdf.main
```

## Structure

- **[src/](src/)**: Source code for all software modules
- **[tests/](tests/)**: Test files for software validation
- **[docs/](docs/)**: Technical documentation for software modules

## Modular Design

The software follows a modular architecture where each module is:

- **Self-contained**: Each module contains all code, configuration, and logic needed for its purpose
- **Independently usable**: Modules can be imported and used without other modules
- **Clearly bounded**: Public API (`main.py`) is separate from internal implementation (`utils.py`)
- **Minimally dependent**: Only essential inter-module dependencies exist
- **Composable**: Modules can be combined in various workflows

### Module Structure

Every module follows a consistent structure:

- `main.py`: Public API (imported by users and other modules)
- `utils.py`: Internal helper functions (private to module)
- `config.py`: Constants and configuration
- `__init__.py`: Exports public functions

### Using Modules Independently

All modules can be used independently:

```python
# Use any module independently
from src.markdown_to_pdf.main import render_markdown_to_pdf
from src.text_to_speech.main import generate_speech
from src.file_validation.main import validate_module_files
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for design principles and [docs/ORCHESTRATION.md](docs/ORCHESTRATION.md) for composition patterns.

## Utilities

### Content Generation

- **Markdown to PDF**: Convert course materials from Markdown to PDF format
- **Text-to-Speech**: Generate audio content from text materials
- **Speech-to-Text**: Transcribe audio files to text
- **Format Conversion**: Convert files between formats (MD, PDF, DOCX, HTML, TXT, Audio)
- **Batch Processing**: Process entire modules for multiple format conversions
- **HTML Website**: Generate comprehensive HTML websites for modules with audio, quizzes, and interactive features
- **Schedule Processing**: Parse and generate schedule outputs in multiple formats
- **Publishing**: Export generated course materials to `published/` folder
- **Course Generator**: Schema-driven curriculum generation with optional LLM enrichment via Ollama
- **Course Config**: Layered TOML-based per-course configuration
- **YouTube Transcript**: Download and process YouTube channel transcripts

### Course Management

- **Module Organization**: Automated structure creation for new modules
- **Canvas Integration**: Scripts for batch uploading module materials
- **File Validation**: Comprehensive validation of module files and structure

## Course Content Files

Each Active Inference module in `course_development/` contains:

| File | Purpose |
|------|---------|
| `module.md` | Main lecture content |
| `questions.md` | Study questions |
| `practice_quiz.md` | Practice quiz |
| `lab.md` | Lab protocol |
| `dashboard.html` | Interactive dashboard |

These files are rendered into all configured output formats (PDF, DOCX, HTML, TXT, MD, MP3) by the pipeline.

## Real Methods Policy

All code in this software uses real methods and implementations. No mocks, stubs, or fake methods are used. Tests use real file operations, real library calls, and real validation logic. External API integrations use real API clients with proper error handling.

## Test Coverage

- **1,021 tests collected** (verify with `uv run pytest --collect-only`)
- Tests cover all major functionality across 21 modules
- Run tests with: `uv run pytest tests/ -v`
- Measure coverage with: `uv run pytest --cov=src --cov-report=html`

## Documentation

- **[AGENTS.md](AGENTS.md)**: Technical documentation for all software modules, function signatures, and APIs
- **[docs/](docs/)**: Detailed documentation including quickstart guide and orchestration patterns
