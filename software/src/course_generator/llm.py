"""Optional Ollama LLM integration for enriched content generation.

This module provides a client for the Ollama API that can be used
to generate richer module content. It gracefully falls back to
template-based content when Ollama is unavailable.
"""

import json
import logging
from typing import Any, Optional, cast

logger = logging.getLogger("course_generator")

try:
    import requests  # type: ignore[import-untyped]

    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    logger.debug("requests library not available; LLM features disabled")


class OllamaClient:
    """Client for interacting with a local Ollama instance.

    Attributes:
        model: The Ollama model name to use.
        base_url: Base URL for the Ollama API.
        timeout: Request timeout in seconds.
    """

    def __init__(
        self,
        model: str = "llama3.2",
        base_url: str = "http://localhost:11434",
        timeout: int = 120,
    ) -> None:
        """Initialize the Ollama client.

        Args:
            model: Model name (default: llama3.2).
            base_url: Ollama API base URL.
            timeout: HTTP timeout in seconds.
        """
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._available: Optional[bool] = None

    def is_available(self) -> bool:
        """Check if the Ollama server is reachable.

        Returns:
            True if the server responds, False otherwise.
        """
        if not HAS_REQUESTS:
            logger.warning("requests library not installed; Ollama unavailable")
            return False

        if self._available is not None:
            return self._available

        try:
            resp = requests.get(f"{self.base_url}/api/tags", timeout=5)
            self._available = resp.status_code == 200
            if self._available:
                logger.info(f"Ollama available at {self.base_url} (model: {self.model})")
            else:
                logger.warning(f"Ollama returned status {resp.status_code}")
        except Exception as exc:
            logger.warning(f"Ollama not available: {exc}")
            self._available = False

        return self._available

    def generate(
        self,
        prompt: str,
        system_prompt: str = "",
        temperature: float = 0.7,
    ) -> str:
        """Generate text from the Ollama model.

        Args:
            prompt: The user prompt.
            system_prompt: Optional system prompt for context.
            temperature: Sampling temperature.

        Returns:
            Generated text string.

        Raises:
            ConnectionError: If Ollama is not available.
            RuntimeError: If generation fails.
        """
        if not self.is_available():
            raise ConnectionError("Ollama is not available")

        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system_prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
            },
        }

        try:
            resp = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=self.timeout,
            )
            resp.raise_for_status()
            data = resp.json()
            response_text = data.get("response", "")
            return response_text if isinstance(response_text, str) else str(response_text)
        except requests.RequestException as exc:
            raise RuntimeError(f"Ollama generation failed: {exc}") from exc

    def generate_structured(
        self,
        prompt: str,
        system_prompt: str = "",
        temperature: float = 0.7,
    ) -> dict[str, Any]:
        """Generate structured JSON output from the Ollama model.

        Args:
            prompt: Prompt requesting JSON output.
            system_prompt: System prompt setting up JSON mode.
            temperature: Sampling temperature.

        Returns:
            Parsed dictionary from the JSON response.

        Raises:
            ConnectionError: If Ollama is not available.
            RuntimeError: If generation or parsing fails.
        """
        json_prompt = (
            f"{prompt}\n\nRespond ONLY with valid JSON. No explanation, no markdown fences."
        )

        raw = self.generate(json_prompt, system_prompt, temperature)

        # Try to extract JSON from the response
        try:
            return cast(dict[str, Any], json.loads(raw))
        except json.JSONDecodeError:
            # Try to find JSON in the response
            start = raw.find("{")
            end = raw.rfind("}") + 1
            if start >= 0 and end > start:
                try:
                    return cast(dict[str, Any], json.loads(raw[start:end]))
                except json.JSONDecodeError:
                    pass
            raise RuntimeError(f"Could not parse JSON from Ollama response: {raw[:200]}")


def enrich_module(
    client: OllamaClient,
    module_content: str,
    topic: str,
    course_title: str,
    audience: str,
    tone: str,
) -> str:
    """Enrich template-generated module content using an LLM.

    Takes the scaffold-generated content and asks the LLM to
    expand it with more detailed explanations and examples.

    Args:
        client: An OllamaClient instance.
        module_content: The template-generated content.
        topic: Module topic name.
        course_title: Parent course title.
        audience: Target audience description.
        tone: Tone guidance.

    Returns:
        Enhanced content string, or the original if LLM fails.
    """
    if not client.is_available():
        logger.info("Ollama unavailable, returning template content")
        return module_content

    system_prompt = (
        f"You are an expert Active Inference educator writing for {audience}. "
        f"Tone: {tone}. Course: {course_title}. "
        "Enhance the following lesson content with deeper explanations, "
        "concrete examples, and engaging language. "
        "Keep all markdown formatting. Do not add new sections."
    )

    try:
        enhanced = client.generate(
            prompt=f"Enhance this lesson about {topic}:\n\n{module_content}",
            system_prompt=system_prompt,
            temperature=0.7,
        )
        if enhanced and len(enhanced) > len(module_content) * 0.5:
            logger.info(f"Successfully enriched module: {topic}")
            return enhanced
        else:
            logger.warning(f"LLM output too short for {topic}, using template")
            return module_content
    except (ConnectionError, RuntimeError) as exc:
        logger.warning(f"LLM enrichment failed for {topic}: {exc}")
        return module_content


def enrich_curriculum(
    client: OllamaClient,
    curriculum_dir: str,
    config: Any,
) -> dict[str, int]:
    """Batch-enrich all module.md files in a curriculum directory.

    Args:
        client: An OllamaClient instance.
        curriculum_dir: Path to the curriculum directory.
        config: CurriculumConfig instance.

    Returns:
        Dictionary with counts: enriched, skipped, errors.
    """
    from pathlib import Path

    stats = {"enriched": 0, "skipped": 0, "errors": 0}
    base = Path(curriculum_dir)

    if not client.is_available():
        logger.warning("Ollama unavailable, skipping all enrichment")
        return stats

    for course in config.courses:
        for module in course.modules:
            module_path = base / course.dir_name / module.dir_name / "module.md"
            if not module_path.exists():
                stats["skipped"] += 1
                continue

            try:
                original = module_path.read_text(encoding="utf-8")
                enriched = enrich_module(
                    client,
                    original,
                    module.topic,
                    course.title,
                    config.audience,
                    config.tone,
                )
                if enriched != original:
                    module_path.write_text(enriched, encoding="utf-8")
                    stats["enriched"] += 1
                else:
                    stats["skipped"] += 1
            except Exception as exc:
                logger.error(f"Error enriching {module_path}: {exc}")
                stats["errors"] += 1

    logger.info(
        f"Enrichment complete: {stats['enriched']} enriched, "
        f"{stats['skipped']} skipped, {stats['errors']} errors"
    )
    return stats
