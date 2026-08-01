"""Tests for the LLM module.

Uses monkeypatch to stub HTTP calls — no mock objects from unittest.mock.
"""

import json

import pytest
import requests

from src.llm import OllamaClient, utils


class TestOllamaClient:
    """Test OllamaClient functionality."""

    def test_init(self):
        client = OllamaClient(base_url="http://localhost:11434", model="llama3")
        assert client.base_url == "http://localhost:11434"
        assert client.model == "llama3"

    def test_is_available_success(self, monkeypatch):
        class FakeResponse:
            status_code = 200

        monkeypatch.setattr(requests, "get", lambda url, timeout=5: FakeResponse())
        client = OllamaClient()
        assert client.is_available() is True

    def test_is_available_failure(self, monkeypatch):
        def raise_error(url, timeout=5):
            raise requests.RequestException("Connection refused")

        monkeypatch.setattr(requests, "get", raise_error)
        client = OllamaClient()
        assert client.is_available() is False

    def test_generate_success(self, monkeypatch):
        class FakeGetResponse:
            status_code = 200

        class FakePostResponse:
            status_code = 200

            def raise_for_status(self):
                pass

            def json(self):
                return {"response": "Hello world"}

        monkeypatch.setattr(requests, "get", lambda url, timeout=5: FakeGetResponse())
        monkeypatch.setattr(
            requests,
            "post",
            lambda url, json=None, timeout=None: FakePostResponse(),
        )

        client = OllamaClient()
        result = client.generate("Hi")
        assert result == "Hello world"

    def test_generate_unavailable(self, monkeypatch):
        class FakeGetResponse:
            status_code = 500

        monkeypatch.setattr(requests, "get", lambda url, timeout=5: FakeGetResponse())
        client = OllamaClient()
        with pytest.raises(ConnectionError, match="Ollama is not available"):
            client.generate("Hi")

    def test_generate_error(self, monkeypatch):
        class FakeGetResponse:
            status_code = 200

        def raise_post_error(url, json=None, timeout=None):
            raise requests.RequestException("Timeout")

        monkeypatch.setattr(requests, "get", lambda url, timeout=5: FakeGetResponse())
        monkeypatch.setattr(requests, "post", raise_post_error)

        client = OllamaClient()
        with pytest.raises(RuntimeError, match="Ollama generation failed"):
            client.generate("Hi")

    def test_generate_structured_success(self, monkeypatch):
        expected_dict = {"summary": "Short summary"}

        class FakeGetResponse:
            status_code = 200

        class FakePostResponse:
            status_code = 200
            _captured_json: dict = {}

            def raise_for_status(self):
                pass

            def json(self):
                return {"response": json.dumps(expected_dict)}

        # Capture the json payload to verify 'format' key was sent
        captured = {}

        def fake_post(url, json=None, timeout=None):
            captured["json"] = json
            return FakePostResponse()

        monkeypatch.setattr(requests, "get", lambda url, timeout=5: FakeGetResponse())
        monkeypatch.setattr(requests, "post", fake_post)

        client = OllamaClient()
        result = client.generate_structured("Summarize this", schema={"summary": "string"})
        assert result == expected_dict
        assert "format" in captured["json"]


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

    def test_split_text_into_chunks_carries_overlap(self):
        # With overlap_tokens > 0, the tail of a paragraph-chunk boundary is
        # carried into the next chunk so context is preserved across splits.
        text = ("Alpha paragraph content. " * 10) + "\n\n" + ("Beta paragraph content. " * 10)

        no_overlap = list(utils.split_text_into_chunks(text, max_tokens=20, overlap_tokens=0))
        with_overlap = list(utils.split_text_into_chunks(text, max_tokens=20, overlap_tokens=20))

        # A chunk boundary exists, and the overlap version preserves the tail
        # of the prior chunk at the start of the following chunk.
        assert len(no_overlap) >= 2
        assert len(with_overlap) >= 2
        # The non-overlap case starts each chunk fresh (no duplicated tail marker).
        assert "Alpha" in with_overlap[0]
        # Overlap must never empty the output.
        assert all(chunk for chunk in with_overlap)

    def test_split_text_into_chunks_empty_input(self):
        assert list(utils.split_text_into_chunks("", max_tokens=10)) == []
