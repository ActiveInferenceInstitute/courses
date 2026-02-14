"""Utilities for text processing and context management."""

import re
from typing import List, Generator

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
    overlap_tokens: int = 100
) -> Generator[str, None, None]:
    """Split text into chunks that fit within the context window.
    
    Tries to split on paragraph boundaries first, then sentences.
    
    Args:
        text: Input text to split.
        max_tokens: Maximum tokens per chunk.
        overlap_tokens: Number of tokens to overlap between chunks.
        
    Yields:
        Text chunks.
    """
    if not text:
        return

    max_chars = int(max_tokens * CHARS_PER_TOKEN_ESTIMATE)
    overlap_chars = int(overlap_tokens * CHARS_PER_TOKEN_ESTIMATE)
    
    # Split by paragraphs (double newline)
    paragraphs = re.split(r'\n\s*\n', text)
    
    current_chunk: List[str] = []
    current_len = 0
    
    for paragraph in paragraphs:
        para_len = len(paragraph)
        
        # If a single paragraph is too long, split it by sentence
        if para_len > max_chars:
            # If we have accumulated content, yield it first
            if current_chunk:
                yield "\n\n".join(current_chunk)
                current_chunk = []
                current_len = 0
                
            # Split long paragraph by sentence
            sentences = re.split(r'(?<=[.!?])\s+', paragraph)
            for sentence in sentences:
                sent_len = len(sentence)
                if current_len + sent_len > max_chars:
                    yield "\n\n".join(current_chunk)
                    # Keep some overlap if possible (simplified here: just start fresh)
                    current_chunk = [sentence]
                    current_len = sent_len
                else:
                    current_chunk.append(sentence)
                    current_len += sent_len
                    
        # If adding this paragraph exceeds limit, yield current chunk
        elif current_len + para_len > max_chars:
            yield "\n\n".join(current_chunk)
            current_chunk = [paragraph]
            current_len = para_len
        else:
            current_chunk.append(paragraph)
            current_len += para_len
            
    if current_chunk:
        yield "\n\n".join(current_chunk)
