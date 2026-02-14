"""Configuration for Canvas integration."""

from typing import Dict

# Canvas API base URL template
CANVAS_API_BASE: str = "https://{domain}/api/v1"

# Default API endpoints
ENDPOINTS: Dict[str, str] = {
    "upload_file": "/courses/{course_id}/files",
    "create_folder": "/courses/{course_id}/folders",
    "list_folders": "/courses/{course_id}/folders",
    "upload_to_folder": "/folders/{folder_id}/files",
}

# Maximum file size for upload (in bytes)
MAX_FILE_SIZE: int = 50 * 1024 * 1024  # 50 MB

# Rate limiting settings
RATE_LIMIT_DELAY: float = 0.5  # seconds between requests
