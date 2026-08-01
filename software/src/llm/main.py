"""Main module for LLM interaction."""

import json
import logging
import time
from typing import Any, Dict, Optional, Union, Generator, cast

import requests  # type: ignore[import-untyped]

from . import config, prompts

logger = logging.getLogger(__name__)

# Re-check availability after this many seconds so a transient failure
# (startup ordering, Ollama restart) is not cached forever.
_AVAILABILITY_TTL = 30.0


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
        self._last_check: Optional[float] = None

    def is_available(self, force_check: bool = False) -> bool:
        """Check if Ollama is reachable.

        The result is cached for a short TTL so transient failures are
        re-probed on subsequent calls instead of being cached forever.
        """
        if (
            not force_check
            and self._available is not None
            and self._last_check is not None
            and (time.monotonic() - self._last_check) < _AVAILABILITY_TTL
        ):
            return self._available

        try:
            resp = requests.get(f"{self.base_url}/api/tags", timeout=max(5, self.timeout))
            self._available = resp.status_code == 200
            if self._available:
                logger.debug(f"Ollama connected at {self.base_url}")
        except Exception as e:
            logger.debug(f"Ollama check failed: {e}")
            self._available = False

        self._last_check = time.monotonic()
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

        Raises:
            ConnectionError: If Ollama is not available.
            RuntimeError: If generation failed after retries.
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

        last_exc: Optional[Exception] = None
        for attempt in range(config.MAX_RETRIES):
            try:
                if stream:
                    return self._stream_generation(url, payload)
                resp = requests.post(url, json=payload, timeout=self.timeout)
                resp.raise_for_status()
                return str(resp.json().get("response", ""))
            except requests.RequestException as e:
                last_exc = e
                logger.warning(
                    "Generation failed (attempt %d/%d): %s",
                    attempt + 1,
                    config.MAX_RETRIES,
                    e,
                )
                if attempt < config.MAX_RETRIES - 1:
                    self._available = None  # force availability re-probe next time
                    self.is_available(force_check=True)
                    time.sleep(config.RETRY_DELAY)

        raise RuntimeError(f"Ollama generation failed: {last_exc}")

    def _stream_generation(self, url: str, payload: Dict[str, Any]) -> Generator[str, None, None]:
        """Yield generated chunks from stream.

        Errors are wrapped in ``RuntimeError`` (matching the non-streaming
        path's contract) rather than leaking raw ``requests`` exceptions, and
        malformed stream lines are counted and surfaced as a warning instead of
        being silently dropped (which could truncate output with no signal).
        """
        bad_lines = 0
        try:
            with requests.post(url, json=payload, stream=True, timeout=self.timeout) as resp:
                resp.raise_for_status()
                for line in resp.iter_lines():
                    if not line:
                        continue
                    try:
                        chunk = json.loads(line)
                        if "response" in chunk:
                            yield chunk["response"]
                    except json.JSONDecodeError:
                        bad_lines += 1
                        if bad_lines <= 5:
                            logger.warning("Skipping malformed stream line: %r", line[:120])
        except requests.RequestException as e:
            raise RuntimeError(f"Ollama stream generation failed: {e}") from e
        if bad_lines:
            logger.warning("Streaming: %d malformed line(s) skipped", bad_lines)

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
            stream=False,
        )

        try:
            return cast(Dict[str, Any], json.loads(str(response_text)))
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {str(response_text)[:200]}...")
            raise RuntimeError(f"Invalid JSON response from LLM: {e}")
