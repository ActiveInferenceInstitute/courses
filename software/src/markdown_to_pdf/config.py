"""Configuration for Markdown to PDF conversion."""

from typing import Any, Dict

# Default PDF options
DEFAULT_PDF_OPTIONS: Dict[str, Any] = {
    "page_size": "letter",
    "margin_top": "1in",
    "margin_bottom": "1in",
    "margin_left": "1in",
    "margin_right": "1in",
    "encoding": "utf-8",
}

# Default CSS template for PDF styling
DEFAULT_CSS: str = """@page {
    size: letter;
    margin: 1in;
}

body {
    font-family: "Times New Roman", serif;
    font-size: 12pt;
    line-height: 1.6;
    color: #000;
}

h1, h2, h3, h4, h5, h6 {
    font-family: "Arial", sans-serif;
    margin-top: 1em;
    margin-bottom: 0.5em;
}

h1 {
    font-size: 18pt;
    page-break-after: avoid;
}

h2 {
    font-size: 16pt;
    page-break-after: avoid;
}

h3 {
    font-size: 14pt;
    page-break-after: avoid;
}

code {
    font-family: "Courier New", monospace;
    background-color: #f5f5f5;
    padding: 2px 4px;
    border-radius: 3px;
}

pre {
    background-color: #f5f5f5;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
    page-break-inside: avoid;
}

img {
    max-width: 100%;
    height: auto;
    page-break-inside: avoid;
}

table {
    border-collapse: collapse;
    width: 100%;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f2f2f2;
}
"""
