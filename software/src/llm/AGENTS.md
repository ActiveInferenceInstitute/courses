# specialized-agent: llm

> **Purpose**: Provides a robust, flexible interface to local LLMs via Ollama.
> **Key Class**: `OllamaClient`

## Overview

The `llm` module abstracts interactions with local Large Language Models. It provides a unified client for text generation, structured JSON output, and streaming, along with utilities for context window management.

## Public API

### `OllamaClient`

Main entry point for LLM interactions.

#### `__init__(base_url, model, timeout)`

- **base_url**: Defaults to `http://localhost:11434`.
- **model**: Defaults to `gemma3:4b` (configurable via `OLLAMA_MODEL`).
- **timeout**: Defaults to 120s.

#### `generate(prompt, system, ...)`

Generate text completion.

- **Args**:
  - `prompt`: The user input.
  - `system`: System instruction (default: "You are a helpful AI assistant").
  - `format`: Optional output format (e.g. "json").
  - `stream`: If True, returns a generator.
- **Returns**: String or Generator.

#### `generate_structured(prompt, schema, ...)`

Generate and parse JSON output.

- **Args**:
  - `prompt`: Input prompt.
  - `schema`: Optional JSON schema to guide generation.
- **Returns**: Dictionary.

### Utilities

- `estimate_tokens(text)`: Approximate token count.
- `split_text_into_chunks(text, max_tokens)`: Smart text splitting respecting paragraph/sentence boundaries.

## Usage

```python
from src.llm import OllamaClient

client = OllamaClient()

# Simple generation
try:
    text = client.generate("Why is the sky blue?")
except ConnectionError:
    print("Is Ollama running?")

# Structured output
data = client.generate_structured(
    "List 3 distinct colors",
    schema={"type": "array", "items": {"type": "string"}}
)
# data might be: ["red", "green", "blue"]

# Streaming
for chunk in client.generate("Tell me a story", stream=True):
    print(chunk, end="", flush=True)
```

## Error Handling

The client raises specific exceptions for different failure modes:

- **`ConnectionError`**: Raised when the Ollama server cannot be reached (check if `ollama serve` is running).
- **`RuntimeError`**: Raised when generation fails (e.g. invalid model, server error, or JSON parsing failure).

Best practice is to wrap calls in a try/except block or check `client.is_available()` before critical operations.

## Configuration

Defaults can be overridden via environment variables:

- `OLLAMA_HOST`
- `OLLAMA_MODEL`
- `OLLAMA_TIMEOUT`
