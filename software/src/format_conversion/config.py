"""Configuration for format conversion."""

from typing import Dict

# Supported format conversions
SUPPORTED_CONVERSIONS: Dict[str, list] = {
    "md": ["pdf", "html", "docx"],
    "markdown": ["pdf", "html", "docx"],
    "html": ["pdf"],
    "txt": ["pdf", "html"],
    "pdf": ["txt"],
    "mp3": ["txt"],
    "wav": ["txt"],
    "m4a": ["txt"],
}

# Conversion handlers (module:function mapping)
CONVERSION_HANDLERS: Dict[str, str] = {
    "md->pdf": "markdown_to_pdf",
    "markdown->pdf": "markdown_to_pdf",
    "md->html": "markdown_to_html",
    "markdown->html": "markdown_to_html",
    "html->pdf": "html_to_pdf",
    "txt->pdf": "text_to_pdf",
    "txt->html": "text_to_html",
}
