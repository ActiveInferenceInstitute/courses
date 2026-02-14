# Text-to-Speech Technical Documentation

## Overview

Text-to-speech generation utilities using real TTS libraries.

## Module Purpose

Generate audio content from text materials, supporting batch processing and Markdown text extraction.

## Function Signatures

### Main Functions

**File**: `src/text_to_speech/main.py`

#### `generate_speech(text: str, output_path: str, voice: str = "default", lang: Optional[str] = None, slow: bool = False) -> None`

Generate speech audio from text.

**Args**:
- `text`: Text content to convert
- `output_path`: Path for output audio file
- `voice`: Voice identifier (default: "default", currently not used with gTTS)
- `lang`: Language code (default: "en")
- `slow`: Whether to speak slowly (default: False)

**Raises**:
- `OSError`: If audio generation fails

**Dependencies**:
- gTTS (Google Text-to-Speech) library

#### `batch_generate_speech(input_dir: str, output_dir: str) -> List[str]`

Batch generate speech from text files in a directory.

**Args**:
- `input_dir`: Directory containing text files
- `output_dir`: Output directory for audio files

**Returns**:
- List of output file paths

**Raises**:
- `ValueError`: If directory doesn't exist
- `OSError`: If audio generation fails for any file

**Processes**:
- Text files (.txt)
- Markdown files (.md, .markdown) - extracts text first

#### `configure_voice_settings(voice: str, speed: float, pitch: float) -> Dict[str, Any]`

Configure voice settings for speech generation.

**Args**:
- `voice`: Voice identifier (currently not used with gTTS)
- `speed`: Speech speed (0.5-2.0, currently not used with gTTS)
- `pitch`: Speech pitch adjustment (currently not used with gTTS)

**Returns**:
- Configuration dictionary

**Note**:
- gTTS doesn't support speed/pitch adjustment directly
- Parameters are stored for potential future use with other TTS engines

### Utility Functions

**File**: `src/text_to_speech/utils.py`

#### `text_to_speech_audio(text: str, output_path: Path, lang: str = "en", slow: bool = False) -> None`

Generate speech audio from text using gTTS.

#### `read_text_file(file_path: Path) -> str`

Read text file content.

#### `extract_text_from_markdown(markdown_content: str) -> str`

Extract plain text from Markdown content, removing formatting.

#### `ensure_output_directory(output_path: Path) -> None`

Ensure output directory exists.

#### `get_output_path(input_file: Path, output_dir: Path) -> Path`

Generate output audio path from input text file.

## Configuration

**File**: `src/text_to_speech/config.py`

- `DEFAULT_VOICE_SETTINGS`: Dictionary of default voice settings:
  - `lang`: "en" (language code)
  - `voice`: "default"
  - `speed`: 1.0
  - `pitch`: 1.0

## Integration Points

### Dependencies on Other Modules

- None (standalone module)

### Used By

- **batch_processing**: Batch audio generation for modules
- **format_conversion**: Text to audio conversion
- Test orchestration workflows

### External Dependencies

- **gTTS**: Google Text-to-Speech library
- **pydub**: Audio file handling (for format conversion if needed)

## Error Handling

- Validates input file existence
- Creates output directories automatically
- Continues batch processing after individual file errors
- Handles network errors for gTTS API calls

## Generation Process

1. Read text content (from string or file)
2. Extract plain text from Markdown if needed
3. Generate speech using gTTS
4. Save audio file (MP3 format)

## Supported Input Formats

- Plain text (.txt)
- Markdown (.md, .markdown) - text is extracted first

## Output Format

- MP3 audio files

## Language Support

Supports all languages supported by gTTS. Default is English ("en").
