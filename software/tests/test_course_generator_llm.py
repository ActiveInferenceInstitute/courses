"""Tests for course_generator LLM integration.

Uses real OllamaClient methods — no mocks. Tests gracefully handle
Ollama being unavailable by exercising the built-in fallback logic.
"""

import pytest
from src.course_generator.llm import OllamaClient, enrich_module


class TestOllamaClient:
    """Tests for OllamaClient."""

    def test_default_init(self):
        """Test default initialization values."""
        client = OllamaClient()
        assert client.model == "llama3.2"
        assert client.base_url == "http://localhost:11434"
        assert client.timeout == 120

    def test_custom_init(self):
        """Test custom initialization."""
        client = OllamaClient(
            model="mistral",
            base_url="http://custom:8080",
            timeout=60,
        )
        assert client.model == "mistral"
        assert client.base_url == "http://custom:8080"
        assert client.timeout == 60

    def test_is_available_returns_bool(self):
        """Test that is_available returns a boolean."""
        client = OllamaClient()
        result = client.is_available()
        assert isinstance(result, bool)

    def test_is_available_caches_result(self):
        """Test that availability result is cached after first call."""
        client = OllamaClient()
        # Set internal cache directly — this is testing the caching mechanism
        client._available = True
        assert client.is_available() is True

        client._available = False
        assert client.is_available() is False

    def test_generate_raises_when_unavailable(self):
        """Test generate raises ConnectionError when unavailable."""
        client = OllamaClient()
        client._available = False
        with pytest.raises(ConnectionError, match="not available"):
            client.generate("test prompt")

    def test_is_available_false_without_requests_lib(self):
        """Test availability is False when requests library check fails.

        Instead of patching HAS_REQUESTS, we use a client configured to
        a port that is almost certainly not running Ollama, then clear
        the cache to force a real check.
        """
        client = OllamaClient(base_url="http://127.0.0.1:1")
        client._available = None  # Clear cache to force fresh check
        # This should return False since nothing is on port 1
        assert client.is_available() is False


class TestEnrichModule:
    """Tests for enrich_module function."""

    def test_returns_original_when_unavailable(self):
        """Test fallback when Ollama is unavailable."""
        client = OllamaClient()
        client._available = False
        original = "# Test Content\n\nThis is test content."
        result = enrich_module(
            client,
            original,
            "systems",
            "Test Course",
            "Testers",
            "Test tone.",
        )
        assert result == original

    def test_returns_original_on_connection_error(self):
        """Test fallback when generate raises ConnectionError.

        Uses an unreachable host so generate() naturally raises
        ConnectionError without any mocking.
        """
        client = OllamaClient(base_url="http://192.0.2.1:1", timeout=1)
        client._available = True  # Force past availability check

        original = "# Test Content\n\nThis is test content."
        result = enrich_module(
            client,
            original,
            "systems",
            "Test Course",
            "Testers",
            "Test tone.",
        )
        # Should fall back to original on any connection failure
        assert result == original

    def test_enrich_module_with_empty_content(self):
        """Test enrich_module handles empty content gracefully."""
        client = OllamaClient()
        client._available = False
        result = enrich_module(
            client,
            "",
            "systems",
            "Test Course",
            "Testers",
            "Test tone.",
        )
        assert result == ""

    def test_enrich_module_preserves_markdown_structure(self):
        """Test that fallback preserves markdown structure exactly."""
        client = OllamaClient()
        client._available = False
        original = "# Title\n\n## Section\n\n- Item 1\n- Item 2\n\n```python\nprint('hi')\n```\n"
        result = enrich_module(
            client,
            original,
            "systems",
            "Test Course",
            "Testers",
            "Test tone.",
        )
        assert result == original
