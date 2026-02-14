"""Configuration for the LLM module."""

import os
from typing import Any, Dict

# Default Ollama settings
DEFAULT_BASE_URL = os.getenv("OLLAMA_HOST", "http://localhost:11434")
DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:4b")
DEFAULT_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "120"))
DEFAULT_TEMPERATURE = 0.7

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 1.0

# Context window settings (approximation)
DEFAULT_CONTEXT_WINDOW = 4096
CHARS_PER_TOKEN_ESTIMATE = 4.0
