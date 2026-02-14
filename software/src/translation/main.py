"""Main translation logic."""

import logging
from pathlib import Path
from typing import Optional

from ..llm import OllamaClient, prompts
from ..llm.utils import split_text_into_chunks
from .config import DEFAULT_CHUNK_SIZE, DEFAULT_SOURCE_LANG
from . import utils

logger = logging.getLogger(__name__)


def translate_text(
    text: str,
    target_lang: str,
    source_lang: str = DEFAULT_SOURCE_LANG,
    client: Optional[OllamaClient] = None,
) -> str:
    """Translate text using LLM.

    Args:
        text: Text to translate.
        target_lang: Target language code or name.
        source_lang: Source language name.
        client: Optional OllamaClient instance.

    Returns:
        Translated text.
    """
    if not client:
        client = OllamaClient()

    target_name = utils.get_language_name(target_lang)

    # Split long text if necessary, using configured chunk size
    chunks = list(split_text_into_chunks(text, max_tokens=DEFAULT_CHUNK_SIZE))
    translated_chunks = []

    for i, chunk in enumerate(chunks):
        logger.info(f"Translating chunk {i+1}/{len(chunks)} to {target_name}...")
        prompt = prompts.TRANSLATION_PROMPT.format(
            source_lang=source_lang,
            target_lang=target_name,
            text=chunk,
        )

        try:
            result = client.generate(prompt)
            translated_chunks.append(str(result))
        except Exception as e:
            logger.error(f"Translation failed for chunk {i+1}: {e}")
            # Fallback: keep original text for this chunk to avoid data loss
            translated_chunks.append(chunk)

    return "\n\n".join(translated_chunks)


def translate_file(
    input_path: str,
    target_lang: str,
    output_path: Optional[str] = None,
    client: Optional[OllamaClient] = None,
) -> str:
    """Translate a file.

    Args:
        input_path: Path to input file.
        target_lang: Target language code.
        output_path: Optional output path.
        client: Optional OllamaClient instance.

    Returns:
        Path to translated file.
    """
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if not utils.validate_file_extension(input_file):
        logger.warning(
            f"File '{input_file.name}' has non-translatable extension "
            f"'{input_file.suffix}', proceeding anyway"
        )

    if not output_path:
        output_file = utils.get_output_path(input_file, target_lang)
    else:
        output_file = Path(output_path)

    logger.info(f"Translating {input_file} -> {output_file}")

    content = input_file.read_text(encoding="utf-8")
    translated_content = translate_text(content, target_lang, client=client)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(translated_content, encoding="utf-8")
    logger.info(f"Translation saved to {output_file}")

    return str(output_file)
