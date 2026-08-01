"""Utilities for text processing and context management."""

import re
from typing import Generator

from .config import CHARS_PER_TOKEN_ESTIMATE, DEFAULT_CONTEXT_WINDOW


def estimate_tokens(text: str) -> int:
    """Estimate the number of tokens in a text string.

    Args:
        text: Input text.

    Returns:
        Estimated token count.
    """
    return int(len(text) / CHARS_PER_TOKEN_ESTIMATE)


def split_text_into_chunks(
    text: str,
    max_tokens: int = DEFAULT_CONTEXT_WINDOW,
    overlap_tokens: int = 100,
) -> Generator[str, None, None]:
    """Split text into chunks that fit within the context window.

    Tries to split on paragraph boundaries first, then sentences.  Only the
    tail of the previous chunk (up to ``overlap_tokens``) is carried forward
    un-emitted as context overlap --- it is prepended to the next chunk so
    context is preserved across boundaries.  The overlap is accounted for in
    the size budget of the new chunk.

    Args:
        text: Input text to split.
        max_tokens: Maximum tokens per chunk.
        overlap_tokens: Number of tokens to retain as overlap between chunks.

    Yields:
        Text chunks.
    """
    if not text:
        return

    max_chars = int(max_tokens * CHARS_PER_TOKEN_ESTIMATE)
    overlap_chars = int(overlap_tokens * CHARS_PER_TOKEN_ESTIMATE)

    # Split by paragraphs (double newline)
    paragraphs = re.split(r"\n\s*\n", text)

    # Overlap tail carried from the previously emitted chunk.
    pending_overlap = ""

    def emit(chunk: list[str]) -> str:
        """Join a chunk, update the pending overlap tail, return the text."""
        nonlocal pending_overlap
        text_out = "\n\n".join(chunk)
        if overlap_chars > 0:
            pending_overlap = text_out[-overlap_chars:]
        return text_out

    current_chunk: list[str] = []
    current_len = 0

    def seed_with_overlap(paragraph: str) -> None:
        """Start a fresh chunk, prepending the pending overlap tail."""
        nonlocal current_chunk, current_len
        current_chunk = [paragraph]
        current_len = len(paragraph)
        if pending_overlap and overlap_chars > 0:
            current_chunk = [pending_overlap, paragraph]
            current_len += len(pending_overlap)

    for paragraph in paragraphs:
        para_len = len(paragraph)
        # Account for the overlap tail that will accompany this paragraph.
        budget = para_len + (len(pending_overlap) if pending_overlap else 0)

        # If a single paragraph is too long, split it by sentence.
        if para_len > max_chars:
            # Flush any accumulated content first.
            if current_chunk:
                yield emit(current_chunk)
                current_chunk = []
                current_len = 0
            # Split the long paragraph by sentence.
            sentences = re.split(r"(?<=[.!?])\s+", paragraph)
            for sentence in sentences:
                sent_len = len(sentence)
                if current_len + sent_len > max_chars:
                    yield emit(current_chunk)
                    current_chunk = []
                    current_len = 0
                    if pending_overlap:
                        current_chunk.append(pending_overlap)
                        current_len += len(pending_overlap)
                current_chunk.append(sentence)
                current_len += sent_len

        elif current_len + budget > max_chars:
            yield emit(current_chunk)
            seed_with_overlap(paragraph)
        else:
            if pending_overlap and not current_chunk:
                seed_with_overlap(paragraph)
            else:
                current_chunk.append(paragraph)
                current_len += para_len

    if current_chunk:
        yield "\n\n".join(current_chunk)
