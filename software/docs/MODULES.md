# Module API Reference

> **Navigation**: [README](README.md) | [Architecture](ARCHITECTURE.md) | [Orchestration](ORCHESTRATION.md) | [CLI Reference](CLI_REFERENCE.md)

Detailed reference for all 21 Python modules in `software/src/`. Each module follows the standard structure: `main.py` (public API), `utils.py` (internals), `config.py` (constants).

---

## Module Index

| Layer | Module | Primary Function | Purpose |
|-------|--------|-----------------|---------|
| **0** | [module_organization](#module_organization) | `create_module_structure()` | Scaffold module directories |
| **0** | [file_validation](#file_validation) | `validate_module_files()` | Validate module structure |
| **0** | [content_processing](#content_processing) | `renumber_questions_in_course()` | Content transformations |
| **0** | [publish](#publish) | `publish_course()` | Copy outputs to published/ |
| **0** | [validation](#validation) | `validate_published_directory()` | Validate published outputs |
| **0** | [lab_manual](#lab_manual) | `render_lab_manual()` | Lab worksheet rendering |
| **0** | [legacy_import](#legacy_import) | `import_legacy_course()` | Import legacy formats |
| **0** | [course_config](#course_config) | `load_course_config()` | Per-course TOML config |
| **1** | [markdown_to_pdf](#markdown_to_pdf) | `render_markdown_to_pdf()` | Markdown to PDF |
| **1** | [text_to_speech](#text_to_speech) | `generate_speech()` | Text to MP3 audio |
| **1** | [speech_to_text](#speech_to_text) | `transcribe_audio()` | Audio to text |
| **1** | [llm](#llm) | `OllamaClient.generate()` | Ollama LLM client |
| **2** | [format_conversion](#format_conversion) | `convert_file()` | Multi-format conversion |
| **2** | [translation](#translation) | `translate_file()` | LLM-based translation |
| **3** | [batch_processing](#batch_processing) | `process_module_by_type()` | Batch rendering + `COURSE_REGISTRY` |
| **3** | [html_website](#html_website) | `generate_module_website()` | Interactive HTML sites |
| **3** | [schedule](#schedule) | `process_schedule()` | Schedule rendering |
| **3** | [course_generator](#course_generator) | `generate()` | Curriculum generation |
| **3** | [youtube_transcript](#youtube_transcript) | `transcribe_video()` | YouTube transcription |
| **3** | [danvas](#danvas) | `start_server()` | Self-hosted course management |
| **4** | [canvas_integration](#canvas_integration) | `upload_module_to_canvas()` | Canvas LMS upload |

---

## Layer 0 — Independent

### module_organization

Create and manage module directory structures.

```python
from src.module_organization.main import create_module_structure
```

**`create_module_structure(base_path, module_name, template=None)`** — Creates a standardized module directory with placeholder content files.

---

### file_validation

Validate module directory structure and content completeness.

```python
from src.file_validation.main import validate_module_files
```

**`validate_module_files(module_path)`** — Returns `{"valid": bool, "missing": [...], "present": [...]}`.

---

### content_processing

Content transformations: question renumbering, dashboard generation, stub detection.

```python
from src.content_processing.main import renumber_questions_in_course
```

**`renumber_questions_in_course(course_path, dry_run=False)`** — Converts section-based numbering to continuous numbering across all questions.md files.

Additional sub-modules:
- `src.content_processing.dashboards` — Generate `dashboard.html` files
- `src.content_processing.labs` — Parse module content for lab generation
- `src.content_processing.structure_scan` — Structural analysis of course modules

---

### publish

Copy rendered outputs to the `published/` directory.

```python
from src.publish.main import publish_course
```

**`publish_course(course_path, publish_root)`** — Copies output directories from modules to the publish root, organized by course ID.

---

### validation

Validate published output completeness and quality.

```python
from src.validation.main import validate_published_directory
```

**`validate_published_directory(published_path)`** — Returns `{"valid": bool, "total_files": N, "missing": [...]}`.

---

### lab_manual

Render lab manual markdown files with special formatting (fill-in boxes, procedure sections).

```python
from src.lab_manual.main import render_lab_manual, batch_render_lab_manuals
```

**`render_lab_manual(input_path, output_path, output_format="pdf")`** — Renders a lab markdown file with `{fill:textarea}` directives expanded to interactive form fields.

**`batch_render_lab_manuals(labs_dir, output_dir, output_format="pdf")`** — Render all lab files in a directory.

---

### legacy_import

Import materials from legacy course formats (bio_1_2025 structure).

```python
from src.legacy_import.main import (
    process_chapter_questions,
    process_slides,
    create_for_upload_files,
)
```

---

### course_config

Layered TOML-based per-course configuration. Merges `course.toml` files from module up to curriculum level.

```python
from src.course_config.main import (
    load_course_config,     # Load merged config for a course path
    get_rendering_config,   # Extract rendering section
    is_format_enabled,      # Check if format is enabled
    get_metadata,           # Extract metadata section
    get_localization,       # Extract localization section
    get_tts_settings,       # Extract TTS settings
    get_pdf_css,            # Get custom PDF CSS path
    get_enabled_formats,    # List enabled format names
)
```

**`load_course_config(course_path, repo_root)`** — Walks from `course_path` up to `course_development/` boundary, collecting `course.toml` files. Merges bottom-up: `DEFAULT_CONFIG <- curriculum <- course <- module`.

See [CONFIGURATION.md](CONFIGURATION.md) for the full `course.toml` schema.

---

## Layer 1 — Core Converters

### markdown_to_pdf

Convert Markdown files to PDF using WeasyPrint.

```python
from src.markdown_to_pdf.main import render_markdown_to_pdf
```

**`render_markdown_to_pdf(input_path, output_path, css_file=None)`** — Converts Markdown to styled PDF.

**System dependency**: Requires `cairo`, `pango`, `gdk-pixbuf`, `glib` (install via `brew install cairo pango gdk-pixbuf glib` on macOS).

---

### text_to_speech

Generate audio narration from text using Google TTS.

```python
from src.text_to_speech.main import generate_speech
from src.text_to_speech.utils import extract_text_from_markdown, read_text_file
```

**`generate_speech(text, output_path, lang="en", slow=False)`** — Generates MP3 audio from text.

**`extract_text_from_markdown(content)`** — Strips Markdown formatting to plain text suitable for TTS.

**Requires**: Internet connection. Subject to rate limiting (429 errors). Pipeline adds 2-second delays between files.

---

### speech_to_text

Transcribe audio files to text using SpeechRecognition.

```python
from src.speech_to_text.main import transcribe_audio
```

**`transcribe_audio(audio_path, output_path)`** — Transcribes an audio file to text.

---

### llm

Ollama LLM client for content generation and enrichment.

```python
from src.llm import OllamaClient
```

**`OllamaClient(base_url, model, timeout)`**

| Method | Description |
|--------|-------------|
| `is_available()` | Check if Ollama is reachable |
| `generate(prompt, system, model, temperature, format, stream)` | Text completion |
| `generate_structured(prompt, schema, model, temperature)` | JSON-structured output |

**Configuration** (environment variables):

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama API URL |
| `OLLAMA_MODEL` | `gemma3:4b` | Default model |
| `OLLAMA_TIMEOUT` | `120` | Request timeout (seconds) |

```python
client = OllamaClient(model="llama3.2")
if client.is_available():
    response = client.generate("Explain Active Inference in one paragraph.")
```

---

## Layer 2 — Extended

### format_conversion

Convert files between Markdown, HTML, DOCX, TXT, and other formats.

```python
from src.format_conversion.main import convert_file
```

**`convert_file(input_path, target_format, output_path)`** — Converts a file to the target format. Supported targets: `html`, `docx`, `txt`, `md`.

---

### translation

LLM-based content translation supporting 11 languages.

```python
from src.translation import translate_file, translate_text
```

**`translate_text(text, target_lang, source_lang="English", client=None)`** — Translates text using Ollama. Automatically chunks long text.

**`translate_file(input_path, target_lang, output_path=None, client=None)`** — Translates a file, writing output to `{basename}_{lang}.{ext}`.

**Supported languages**: Arabic, German, Spanish, French, Hindi, Italian, Japanese, Korean, Portuguese, Russian, Chinese (Simplified).

See [TRANSLATION.md](TRANSLATION.md) for the full translation guide.

---

## Layer 3 — Orchestration

### batch_processing

Central orchestration module and home of `COURSE_REGISTRY`.

```python
from src.batch_processing.main import (
    process_module_by_type,      # Render a single module to all formats
    process_module_to_pdf,       # Module -> PDF
    process_module_to_audio,     # Module -> MP3
    process_syllabus,            # Render syllabus files
    process_course_modules,      # Render all modules for a course
    process_course_syllabus,     # Render course syllabus
    process_course_labs,         # Render lab manuals
    process_course_practice_tests,  # Render practice tests
    process_module_website,      # Generate module website
    clear_all_outputs,           # Clear output directories
    generate_module_media,       # Generate all media for a module
)
from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.utils import find_modules_for_course
```

**Key function**: `process_module_by_type(module_path, output_dir, formats=None)`

- Renders all content files in a module to the specified formats
- Organizes outputs by curriculum type: `lecture-content/`, `study-guides/`, `lab-protocols/`, `assignments/`
- Returns `{"by_type": {...}, "summary": {"pdf": N, ...}, "errors": [...]}`

```python
result = process_module_by_type(
    "/path/to/01_systems",
    "/path/to/01_systems/output",
    formats=["pdf", "html", "txt", "md"]
)
print(f"Generated {sum(result['summary'].values())} files")
```

---

### html_website

Generate interactive HTML websites for course modules.

```python
from src.html_website.main import generate_module_website
```

**`generate_module_website(module_path, output_dir=None)`** — Generates a standalone HTML website with sidebar navigation, embedded audio players, interactive quizzes, dark mode toggle, and progress tracking.

---

### schedule

Process syllabus/schedule files into multiple output formats.

```python
from src.schedule.main import process_schedule
```

**`process_schedule(schedule_path, output_dir, formats=None)`** — Renders schedule markdown files to PDF, HTML, DOCX, TXT.

---

### course_generator

Schema-driven curriculum generation with optional LLM enrichment.

```python
from src.course_generator.main import (
    generate,          # Generate a single curriculum
    generate_all,      # Generate all registered curricula
    validate,          # Validate curriculum structure
    list_curricula,    # List available configurations
)
```

**`generate(curriculum_id, output_dir=None, use_llm=False, model="llama3.2")`** — Generates a curriculum from schema-defined templates. Optionally enriches content using Ollama.

See [COURSE_GENERATOR.md](COURSE_GENERATOR.md) for the full generation guide.

---

### youtube_transcript

Download and process YouTube channel transcripts.

```python
from src.youtube_transcript.main import (
    transcribe_video,          # Single video transcription
    transcribe_channel,        # Full channel transcription
    get_channel_video_list,    # Enumerate videos without transcribing
)
```

**`transcribe_video(video_id, output_dir, whisper_model="base", skip_whisper=False)`** — Tries auto-captions first, falls back to Whisper.

**`transcribe_channel(channel_url, output_dir=None, limit=None, resume=True)`** — Full channel transcription with manifest tracking and crash recovery.

See [YOUTUBE.md](YOUTUBE.md) for the full YouTube guide.

---

### danvas

Self-hosted lightweight Canvas-like course management system. Zero-dependency HTTP server (built on `http.server`).

```python
from src.danvas import start_server
```

**`start_server(repo_root, port=8420, host="127.0.0.1", data_dir=None)`** — Starts the Danvas web server.

**Features**: Course browsing, enrollment management, gradebook, announcements, calendar, role-based permissions.

**Data layer modules**: `store`, `discovery`, `enrollment`, `gradebook`, `announcements`, `calendar_events`.

See [DANVAS.md](DANVAS.md) for the full Danvas guide.

---

## Layer 4 — Pipeline

### canvas_integration

Upload course materials to Canvas LMS.

```python
from src.canvas_integration.main import upload_module_to_canvas
```

**`upload_module_to_canvas(module_path, canvas_url, api_token, course_id)`** — Batch upload rendered module files to Canvas.

---

## Import Patterns

### Standard import

```python
from src.module_name.main import function_name
```

### Using `__init__.py` exports

```python
from src.llm import OllamaClient
from src.translation import translate_file
from src.danvas import start_server, discover_courses
```

### Composition

```python
from src.file_validation.main import validate_module_files
from src.batch_processing.main import process_module_by_type

# Validate then process
validation = validate_module_files(module_path)
if validation["valid"]:
    result = process_module_by_type(module_path, output_dir, formats=["txt", "md"])
```

---

## Module Dependencies Matrix

```
batch_processing -> markdown_to_pdf, text_to_speech, format_conversion, html_website
html_website     -> format_conversion
format_conversion -> markdown_to_pdf, text_to_speech
translation      -> llm
course_generator -> (standalone, optional llm)
publish          -> batch_processing (config), validation
danvas           -> batch_processing (config, discovery)
```

---

*Last Updated: 2026-02-14*
