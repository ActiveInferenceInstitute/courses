"""Main functions for Canvas integration."""

import time
from pathlib import Path
from typing import Any, Dict, List

import requests

from . import config
from .utils import (
    get_canvas_api_url,
    get_file_mime_type,
    make_canvas_request,
    validate_file_size,
)
from ..file_validation.main import validate_module_files


def upload_module_to_canvas(
    module_path: str, course_id: str, api_key: str, domain: str = "canvas.instructure.com"
) -> Dict[str, Any]:
    """Upload module materials to Canvas LMS.

    Args:
        module_path: Path to module directory
        course_id: Canvas course ID
        api_key: Canvas API key
        domain: Canvas domain (default: "canvas.instructure.com")

    Returns:
        Dictionary with upload results

    Raises:
        ValueError: If module path is invalid
        requests.RequestException: If API request fails
    """
    module_dir = Path(module_path)

    if not module_dir.exists():
        raise ValueError(f"Module path does not exist: {module_path}")

    # Validate module structure first
    validation = validate_module_files(module_path)
    if not validation["valid"]:
        raise ValueError(f"Module structure is invalid: {validation}")

    results = {
        "uploaded_files": [],
        "failed_files": [],
        "errors": [],
    }

    # Get or create module folder in Canvas
    folder_name = module_dir.name
    folder_id = _get_or_create_folder(course_id, api_key, domain, folder_name)

    # Upload files
    for file_path in module_dir.rglob("*"):
        if file_path.is_file() and file_path.name not in [".gitkeep"]:
            try:
                if not validate_file_size(file_path):
                    results["failed_files"].append(str(file_path))
                    results["errors"].append(
                        f"File too large: {file_path.name}"
                    )
                    continue

                upload_result = _upload_file_to_canvas(
                    file_path, folder_id, api_key, domain
                )
                results["uploaded_files"].append(
                    {
                        "file": str(file_path),
                        "canvas_url": upload_result.get("url", ""),
                    }
                )
            except Exception as e:
                results["failed_files"].append(str(file_path))
                results["errors"].append(f"Error uploading {file_path.name}: {e}")

    return results


def validate_upload_readiness(module_path: str) -> List[str]:
    """Validate module is ready for Canvas upload.

    Args:
        module_path: Path to module directory

    Returns:
        List of validation issues (empty if ready)
    """
    issues = []

    module_dir = Path(module_path)
    if not module_dir.exists():
        issues.append(f"Module path does not exist: {module_path}")
        return issues

    # Validate module structure
    validation = validate_module_files(module_path)
    if not validation["valid"]:
        if validation.get("missing_files"):
            issues.append(f"Missing required files: {validation['missing_files']}")
        if validation.get("missing_directories"):
            issues.append(
                f"Missing required directories: {validation['missing_directories']}"
            )
        if validation.get("naming_violations"):
            issues.append(
                f"File naming violations: {validation['naming_violations']}"
            )

    # Check for files that are too large
    for file_path in module_dir.rglob("*"):
        if file_path.is_file():
            if not validate_file_size(file_path):
                issues.append(f"File too large: {file_path}")

    return issues


def sync_module_structure(module_path: str, canvas_course_id: str, api_key: str, domain: str = "canvas.instructure.com") -> Dict[str, Any]:
    """Sync module structure with Canvas course.

    Args:
        module_path: Path to module directory
        canvas_course_id: Canvas course ID
        api_key: Canvas API key
        domain: Canvas domain (default: "canvas.instructure.com")

    Returns:
        Dictionary with sync results

    Raises:
        ValueError: If module path is invalid
        requests.RequestException: If API request fails
    """
    module_dir = Path(module_path)

    if not module_dir.exists():
        raise ValueError(f"Module path does not exist: {module_path}")

    # This is similar to upload_module_to_canvas but focuses on structure
    # For now, we'll use the upload function
    return upload_module_to_canvas(module_path, canvas_course_id, api_key, domain)


def _get_or_create_folder(
    course_id: str, api_key: str, domain: str, folder_name: str
) -> str:
    """Get existing folder or create new one in Canvas.

    Args:
        course_id: Canvas course ID
        api_key: Canvas API key
        domain: Canvas domain
        folder_name: Name of folder

    Returns:
        Folder ID
    """
    # List existing folders
    url = get_canvas_api_url(domain, config.ENDPOINTS["list_folders"], course_id=course_id)
    response = make_canvas_request("GET", url, api_key)

    folders = response.json()
    for folder in folders:
        if folder["name"] == folder_name:
            return str(folder["id"])

    # Create new folder if not found
    url = get_canvas_api_url(domain, config.ENDPOINTS["create_folder"], course_id=course_id)
    data = {"name": folder_name}
    response = make_canvas_request("POST", url, api_key, json=data)

    folder = response.json()
    return str(folder["id"])


def _upload_file_to_canvas(
    file_path: Path, folder_id: str, api_key: str, domain: str
) -> Dict[str, Any]:
    """Upload a single file to Canvas.

    Args:
        file_path: Path to file to upload
        folder_id: Canvas folder ID
        api_key: Canvas API key
        domain: Canvas domain

    Returns:
        Upload result dictionary
    """
    # Canvas file upload is a two-step process:
    # 1. Request upload URL
    # 2. Upload file to that URL

    url = get_canvas_api_url(domain, config.ENDPOINTS["upload_to_folder"], folder_id=folder_id)
    params = {
        "name": file_path.name,
        "size": file_path.stat().st_size,
        "content_type": get_file_mime_type(file_path),
    }

    response = make_canvas_request("POST", url, api_key, params=params)
    upload_data = response.json()

    # Upload file
    upload_url = upload_data["upload_url"]
    with open(file_path, "rb") as f:
        files = {"file": (file_path.name, f, get_file_mime_type(file_path))}
        upload_response = requests.post(upload_url, files=files)

    upload_response.raise_for_status()
    return upload_response.json()
