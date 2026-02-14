"""Main module for LLM interaction."""

import json
import logging
import time
from typing import Any, Dict, List, Optional, Union, Generator

import requests

from . import config, prompts

logger = logging.getLogger(__name__)


class OllamaClient:
    """Robust client for interacting with Ollama."""

    def __init__(
        self,
        base_url: str = config.DEFAULT_BASE_URL,
        model: str = config.DEFAULT_MODEL,
        timeout: int = config.DEFAULT_TIMEOUT,
    ):
        """Initialize the client.

        Args:
            base_url: Ollama API base URL.
            model: Default model to use.
            timeout: Request timeout in seconds.
        """
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout
        self._available: Optional[bool] = None

    def is_available(self, force_check: bool = False) -> bool:
        """Check if Ollama is reachable."""
        if self._available is not None and not force_check:
            return self._available

        try:
            resp = requests.get(f"{self.base_url}/api/tags", timeout=5)
            self._available = resp.status_code == 200
            if self._available:
                logger.debug(f"Ollama connected at {self.base_url}")
        except Exception as e:
            logger.debug(f"Ollama check failed: {e}")
            self._available = False

        return self._available

    def generate(
        self,
        prompt: str,
        system: str = prompts.SYSTEM_DEFAULT,
        model: Optional[str] = None,
        temperature: float = config.DEFAULT_TEMPERATURE,
        format: Optional[str] = None,
        stream: bool = False,
    ) -> Union[str, Generator[str, None, None]]:
        """Generate text completion.

        Args:
            prompt: User prompt.
            system: System prompt.
            model: Override default model.
            temperature: Sampling temperature.
            format: Optional format (e.g. "json").
            stream: Whether to stream details.

        Returns:
            Generated text string (if stream=False) or generator (if stream=True).
        """
        if not self.is_available():
            raise ConnectionError("Ollama is not available")

        url = f"{self.base_url}/api/generate"
        payload = {
            "model": model or self.model,
            "prompt": prompt,
            "system": system,
            "stream": stream,
            "options": {
                "temperature": temperature,
            },
        }

        if format:
            payload["format"] = format

        try:
            if stream:
                return self._stream_generation(url, payload)
            else:
                resp = requests.post(url, json=payload, timeout=self.timeout)
                resp.raise_for_status()
                return resp.json().get("response", "")
        except requests.RequestException as e:
            logger.error(f"Generation failed: {e}")
            raise RuntimeError(f"Ollama generation failed: {e}")

    def _stream_generation(self, url: str, payload: Dict[str, Any]) -> Generator[str, None, None]:
        """Yield generated chunks from stream."""
        with requests.post(url, json=payload, stream=True, timeout=self.timeout) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines():
                if line:
                    try:
                        chunk = json.loads(line)
                        if "response" in chunk:
                            yield chunk["response"]
                    except json.JSONDecodeError:
                        continue

    def generate_structured(
        self,
        prompt: str,
        schema: Optional[Dict[str, Any]] = None,
        model: Optional[str] = None,
        temperature: float = config.DEFAULT_TEMPERATURE,
    ) -> Dict[str, Any]:
        """Generate structured JSON output.

        Args:
            prompt: User prompt.
            schema: Optional JSON schema to enforce (if model supports it).
            model: Override default model.
            temperature: Sampling temperature.

        Returns:
            Parsed JSON dictionary.
        """
        # Note: minimal plumbing for now; fuller schema enforcement can be added later
        # or via guidance/structured generation libraries if needed.
        # For now, we rely on the generic JSON instruction.
        
        system_prompt = prompts.SYSTEM_JSON
        if schema:
            system_prompt += f"\nFollow this schema: {json.dumps(schema)}"

        response_text = self.generate(
            prompt=prompt,
            system=system_prompt,
            model=model,
            temperature=temperature,
            format="json",
            stream=False
        )

        try:
            return json.loads(str(response_text))
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {response_text[:200]}...")
            raise RuntimeError(f"Invalid JSON response from LLM: {e}")
