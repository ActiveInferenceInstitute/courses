"""LLM module initialization."""

from .main import OllamaClient
from .config import DEFAULT_MODEL

__all__ = ["OllamaClient", "DEFAULT_MODEL"]
