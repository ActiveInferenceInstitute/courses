# Speech-to-Text Technical Documentation

## Overview

Speech-to-text transcription utilities using real speech recognition libraries.

## Module Purpose

Transcribe audio files to text using speech recognition, supporting batch processing and multiple audio formats.

## Function Signatures

### Main Functions

**File**: `src/speech_to_text/main.py`

#### `transcribe_audio(audio_path: str, output_path: str, language: str = "en") -> str`

Transcribe audio file to text using real speech recognition.

**Args**:
- `audio_path`: Path to input audio file
- `output_path`: Path for output text file
- `language`: Language code (default: "en")

**Returns**:
- Transcribed text content

**Raises**:
- `FileNotFoundError`: If audio file doesn't exist
- `OSError`: If transcription fails

**Dependencies**:
- Speech recognition library (speech_recognition)
- Audio processing library (pydub)

#### `batch_transcribe_audio(input_dir: str, output_dir: str) -> List[str]`

Batch transcribe audio files in a directory.

**Args**:
- `input_dir`: Directory containing audio files
- `output_dir`: Output directory for text files

**Returns**:
- List of output file paths

**Raises**:
- `ValueError`: If directory doesn't exist
- `OSError`: If transcription fails for any file

#### `transcribe_from_markdown(markdown_path: str, output_path: str) -> str`

Extract text from Markdown and transcribe (if audio is referenced).

Currently extracts text content from Markdown files. Future enhancement could transcribe referenced audio files.

**Args**:
- `markdown_path`: Path to Markdown file
- `output_path`: Path for output text file

**Returns**:
- Extracted text content

**Raises**:
- `FileNotFoundError`: If Markdown file doesn't exist
- `OSError`: If processing fails

**Dependencies**:
- `text_to_speech.utils.extract_text_from_markdown`
- `text_to_speech.utils.read_text_file`

### Utility Functions

**File**: `src/speech_to_text/utils.py`

#### `read_audio_file(audio_path: Path) -> AudioSegment`

Read audio file using pydub.

#### `convert_audio_to_wav(audio: AudioSegment, output_path: Path) -> None`

Convert audio to WAV format for speech recognition.

#### `transcribe_audio_segment(audio_path: Path, language: str = "en") -> str`

Transcribe audio segment using speech recognition.

#### `is_audio_file(file_path: Path) -> bool`

Check if file is an audio file.

#### `ensure_output_directory(output_path: Path) -> None`

Ensure output directory exists.

#### `get_output_path(input_file: Path, output_dir: Path) -> Path`

Generate output text path from input audio file.

## Configuration

**File**: `src/speech_to_text/config.py`

- Audio format support: MP3, WAV, M4A, FLAC, OGG
- Language codes for speech recognition
- Audio processing settings

## Integration Points

### Dependencies on Other Modules

- **text_to_speech**: Text extraction utilities for Markdown processing

### Used By

- **format_conversion**: Audio to text conversion
- **batch_processing**: Batch transcription of module audio files
- Test orchestration workflows

### External Dependencies

- **speech_recognition**: Speech recognition library
- **pydub**: Audio file processing

## Error Handling

- Validates audio file existence
- Handles audio format conversion errors
- Continues batch processing after individual file errors
- Cleans up temporary files

## Transcription Process

1. Read audio file
2. Convert to WAV format (if needed)
3. Use speech recognition to transcribe
4. Write transcribed text to output file
5. Clean up temporary files

## Supported Audio Formats

- MP3
- WAV
- M4A
- FLAC
- OGG

All formats are converted to WAV for speech recognition processing.
