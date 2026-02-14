"""Tests for the LLM module."""

import json
from unittest.mock import MagicMock, patch

import pytest
import requests

from src.llm import OllamaClient, config, prompts, utils


@pytest.fixture
def mock_requests_get():
    with patch("requests.get") as mock:
        yield mock


@pytest.fixture
def mock_requests_post():
    with patch("requests.post") as mock:
        yield mock


class TestOllamaClient:
    """Test OllamaClient functionality."""

    def test_init(self):
        client = OllamaClient(base_url="http://localhost:11434", model="llama3")
        assert client.base_url == "http://localhost:11434"
        assert client.model == "llama3"

    def test_is_available_success(self, mock_requests_get):
        mock_requests_get.return_value.status_code = 200
        client = OllamaClient()
        assert client.is_available() is True
        mock_requests_get.assert_called_with(f"{config.DEFAULT_BASE_URL}/api/tags", timeout=5)

    def test_is_available_failure(self, mock_requests_get):
        mock_requests_get.side_effect = requests.RequestException("Connection refused")
        client = OllamaClient()
        assert client.is_available() is False

    def test_generate_success(self, mock_requests_post, mock_requests_get):
        # Mock availability check
        mock_requests_get.return_value.status_code = 200
        
        # Mock generation response
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "Hello world"}
        mock_response.status_code = 200
        mock_requests_post.return_value = mock_response

        client = OllamaClient()
        result = client.generate("Hi")
        assert result == "Hello world"
        
        mock_requests_post.assert_called_once()
        args, kwargs = mock_requests_post.call_args
        assert kwargs["json"]["prompt"] == "Hi"
        assert kwargs["json"]["stream"] is False

    def test_generate_unavailable(self, mock_requests_get):
        mock_requests_get.return_value.status_code = 500
        client = OllamaClient()
        with pytest.raises(ConnectionError, match="Ollama is not available"):
            client.generate("Hi")

    def test_generate_error(self, mock_requests_post, mock_requests_get):
        mock_requests_get.return_value.status_code = 200
        mock_requests_post.side_effect = requests.RequestException("Timeout")
        
        client = OllamaClient()
        with pytest.raises(RuntimeError, match="Ollama generation failed"):
            client.generate("Hi")

    def test_generate_structured_success(self, mock_requests_post, mock_requests_get):
        mock_requests_get.return_value.status_code = 200
        
        expected_dict = {"summary": "Short summary"}
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": json.dumps(expected_dict)}
        mock_requests_post.return_value = mock_response

        client = OllamaClient()
        result = client.generate_structured("Summarize this", schema={"summary": "string"})
        assert result == expected_dict
        assert "format" in mock_requests_post.call_args[1]["json"]


class TestLLMUtils:
    """Test LLM utility functions."""

    def test_estimate_tokens(self):
        text = "Hello world"
        # 11 chars / 4 = 2.75 -> 2
        assert utils.estimate_tokens(text) == 2

    def test_split_text_into_chunks(self):
        # Create text that forces a split
        # estimate: 1 char = 0.25 tokens. 
        # max_tokens=10 -> 40 chars.
        text = "This is paragraph one.\n\nThis is paragraph two that is quite long."
        
        chunks = list(utils.split_text_into_chunks(text, max_tokens=10, overlap_tokens=0))
        assert len(chunks) >= 2
        assert "paragraph one" in chunks[0]
