"""Utility functions for Canvas integration."""

import time
from pathlib import Path
from typing import Dict, Optional

import requests

from . import config


def get_canvas_api_url(domain: str, endpoint: str, **kwargs) -> str:
    """Build Canvas API URL.

    Args:
        domain: Canvas domain (e.g., "canvas.instructure.com")
        endpoint: API endpoint path
        **kwargs: Variables to substitute in endpoint

    Returns:
        Complete API URL
    """
    base_url = config.CANVAS_API_BASE.format(domain=domain)
    endpoint_path = endpoint.format(**kwargs)
    return f"{base_url}{endpoint_path}"


def make_canvas_request(
    method: str,
    url: str,
    api_key: str,
    headers: Optional[Dict[str, str]] = None,
    **kwargs,
) -> requests.Response:
    """Make a request to Canvas API with rate limiting.

    Args:
        method: HTTP method (GET, POST, etc.)
        url: API URL
        api_key: Canvas API key
        headers: Optional additional headers
        **kwargs: Additional arguments for requests

    Returns:
        Response object

    Raises:
        requests.RequestException: If request fails
    """
    if headers is None:
        headers = {}

    headers["Authorization"] = f"Bearer {api_key}"

    # Rate limiting
    time.sleep(config.RATE_LIMIT_DELAY)

    response = requests.request(method, url, headers=headers, **kwargs)
    response.raise_for_status()

    return response


def validate_file_size(file_path: Path) -> bool:
    """Validate file size is within limits.

    Args:
        file_path: Path to file

    Returns:
        True if file size is valid, False otherwise
    """
    if not file_path.exists():
        return False

    file_size = file_path.stat().st_size
    return file_size <= config.MAX_FILE_SIZE


def get_file_mime_type(file_path: Path) -> str:
    """Get MIME type for file.

    Args:
        file_path: Path to file

    Returns:
        MIME type string
    """
    suffix = file_path.suffix.lower()
    mime_types = {
        ".pdf": "application/pdf",
        ".md": "text/markdown",
        ".html": "text/html",
        ".txt": "text/plain",
        ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    }
    return mime_types.get(suffix, "application/octet-stream")
