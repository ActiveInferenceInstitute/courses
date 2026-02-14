"""Standard prompt templates."""

SYSTEM_DEFAULT = "You are a helpful AI assistant."

SYSTEM_JSON = (
    "You are a helpful AI assistant. "
    "Respond ONLY with valid JSON. "
    "Do not include any explanation, markdown formatting, or code fences."
)

TRANSLATION_PROMPT = """
Translate the following text from {source_lang} to {target_lang}.
Maintain all markdown formatting, links, and code blocks exactly as they are.
Do not translate code blocks or URLs.
Translate headings, lists, and body text.

Text to translate:
{text}
"""

SUMMARIZATION_PROMPT = """
Summarize the following text in a concise manner.
Focus on the key concepts and main arguments.

Text:
{text}
"""
