# specialized-agent: translation

> **Purpose**: Translates course content using local LLMs.
> **Key Function**: `translate_file()`

## Overview

The `translation` module provides automated translation of text files (specifically Markdown) using the `llm` module. It handles text chunking to ensure large files fit within the LLM's context window.

## Public API

### `translate_text(text, target_lang, source_lang="English", client=None) -> str`

Translate a string of text.

- **Args**:
  - `text`: Input text.
  - `target_lang`: Target language code (e.g. "es") or name.
  - `source_lang`: Source language (default: "English").
  - `client`: Optional `OllamaClient` instance.
- **Returns**: Translated string.

### `translate_file(input_path, target_lang, output_path=None, client=None) -> str`

Translate a file and save to disk.

- **Args**:
  - `input_path`: Path to source file.
  - `target_lang`: Target language code.
  - `output_path`: Optional specific output path. (Default: `filename_lang.ext`)
- **Returns**: Path to the generated file.

### `validate_file_extension(file_path) -> bool`

Check if a file has a translatable extension (`.md`, `.txt`).

- **Args**:
  - `file_path`: `Path` to the file.
- **Returns**: `True` if the extension is translatable.

## Configuration

All constants live in `config.py`:

| Constant | Default | Purpose |
|----------|---------|---------|
| `SUPPORTED_LANGUAGES` | 11 languages | Language code → name mapping |
| `DEFAULT_SOURCE_LANG` | `"English"` | Source language for translation |
| `DEFAULT_CHUNK_SIZE` | `4096` | Max tokens per LLM chunk |
| `TRANSLATABLE_EXTENSIONS` | `[".md", ".txt"]` | Eligible file extensions |

## Usage

```python
from src.translation import translate_file, translate_text

# Translate a file to Spanish
try:
    output_path = translate_file("module.md", "es")
    print(f"Translated file: {output_path}")
except FileNotFoundError:
    print("Input file missing")
except Exception as e:
    print(f"Translation failed: {e}")

# Translate text with custom client
from src.llm import OllamaClient
client = OllamaClient(model="mistral")
text = translate_text("Hello", "fr", client=client)
```

## CLI Scripts

- **`scripts/translate_youtube.py`**: Translates YouTube playlist transcripts.

  ```bash
  python software/scripts/translate_youtube.py --lang ru
  python software/scripts/translate_youtube.py --lang es --dry-run
  ```

## Error Handling

- **Chunking**: Large files are automatically split to fit context windows.
- **Partial Failures**: If a chunk fails to translate, the original text is preserved in the output to prevent data loss. Check logs for warnings.
- **File I/O**: Raises `FileNotFoundError` if input is missing.
- **Extension Warning**: Non-translatable extensions log a warning but still proceed.

## Dependencies

- **Internal**: `llm` (OllamaClient, prompts, split_text_into_chunks).
