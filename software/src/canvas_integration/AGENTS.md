# Canvas Integration Technical Documentation

## Overview

Canvas LMS integration utilities for uploading course module materials to Canvas courses.

## Module Purpose

Upload module materials to Canvas LMS, validate upload readiness, and sync module structure with Canvas courses.

## Function Signatures

### Main Functions

**File**: `src/canvas_integration/main.py`

#### `upload_module_to_canvas(module_path: str, course_id: str, api_key: str, domain: str = "canvas.instructure.com") -> Dict[str, Any]`

Upload module materials to Canvas LMS.

**Args**:
- `module_path`: Path to module directory
- `course_id`: Canvas course ID
- `api_key`: Canvas API key
- `domain`: Canvas domain (default: "canvas.instructure.com")

**Returns**:
- Dictionary with upload results:
  - `uploaded_files`: List of successfully uploaded files with Canvas URLs
  - `failed_files`: List of files that failed to upload
  - `errors`: List of error messages

**Raises**:
- `ValueError`: If module path is invalid or module structure is invalid
- `requests.RequestException`: If API request fails

**Dependencies**:
- `file_validation.main.validate_module_files`
- Canvas API (external service)

#### `validate_upload_readiness(module_path: str) -> List[str]`

Validate module is ready for Canvas upload.

**Args**:
- `module_path`: Path to module directory

**Returns**:
- List of validation issues (empty list if ready)

**Dependencies**:
- `file_validation.main.validate_module_files`
- `utils.validate_file_size`

#### `sync_module_structure(module_path: str, canvas_course_id: str, api_key: str, domain: str = "canvas.instructure.com") -> Dict[str, Any]`

Sync module structure with Canvas course.

**Args**:
- `module_path`: Path to module directory
- `canvas_course_id`: Canvas course ID
- `api_key`: Canvas API key
- `domain`: Canvas domain (default: "canvas.instructure.com")

**Returns**:
- Dictionary with sync results (same structure as `upload_module_to_canvas`)

**Raises**:
- `ValueError`: If module path is invalid
- `requests.RequestException`: If API request fails

**Dependencies**:
- `upload_module_to_canvas`

### Private Functions

#### `_get_or_create_folder(course_id: str, api_key: str, domain: str, folder_name: str) -> str`

Get existing folder or create new one in Canvas.

**Returns**:
- Folder ID as string

#### `_upload_file_to_canvas(file_path: Path, folder_id: str, api_key: str, domain: str) -> Dict[str, Any]`

Upload a single file to Canvas using two-step upload process.

**Returns**:
- Upload result dictionary with file information

### Utility Functions

**File**: `src/canvas_integration/utils.py`

#### `get_canvas_api_url(domain: str, endpoint: str, **kwargs) -> str`

Construct Canvas API URL from domain and endpoint template.

**Args**:
- `domain`: Canvas domain
- `endpoint`: Endpoint template with placeholders
- `**kwargs`: Values to substitute in endpoint template

**Returns**:
- Complete Canvas API URL

#### `make_canvas_request(method: str, url: str, api_key: str, **kwargs) -> requests.Response`

Make authenticated Canvas API request.

**Args**:
- `method`: HTTP method (GET, POST, etc.)
- `url`: Request URL
- `api_key`: Canvas API key for authentication
- `**kwargs`: Additional arguments for requests (json, params, etc.)

**Returns**:
- Response object

**Raises**:
- `requests.RequestException`: If request fails

#### `validate_file_size(file_path: Path) -> bool`

Validate file size is within Canvas upload limits.

**Args**:
- `file_path`: Path to file

**Returns**:
- True if file size is valid, False otherwise

#### `get_file_mime_type(file_path: Path) -> str`

Get MIME type for a file.

**Args**:
- `file_path`: Path to file

**Returns**:
- MIME type string

## Configuration

**File**: `src/canvas_integration/config.py`

- `CANVAS_API_BASE`: Canvas API base URL template (`"https://{domain}/api/v1"`)
- `ENDPOINTS`: Dictionary of API endpoint templates:
  - `upload_file`: `/courses/{course_id}/files`
  - `create_folder`: `/courses/{course_id}/folders`
  - `list_folders`: `/courses/{course_id}/folders`
  - `upload_to_folder`: `/folders/{folder_id}/files`
- `MAX_FILE_SIZE`: Maximum file size for upload in bytes (50 MB)
- `RATE_LIMIT_DELAY`: Delay between requests in seconds (0.5)

## Integration Points

### Dependencies on Other Modules

- **file_validation**: Module structure validation before upload

### External Dependencies

- **requests**: HTTP library for API calls
- **Canvas API**: External Canvas LMS service

## Error Handling

- Validates module structure before upload
- Validates file sizes before upload
- Collects errors for individual file failures
- Continues processing remaining files after errors
- Raises exceptions for critical failures (invalid module, API errors)

## Upload Process

1. Validates module structure
2. Gets or creates Canvas folder for module
3. For each file:
   - Validates file size
   - Requests upload URL from Canvas
   - Uploads file to Canvas
   - Records result
4. Returns summary of uploads and errors

## Rate Limiting

Includes rate limiting delay between requests to avoid overwhelming Canvas API.
