# HTML Website Generation Technical Documentation

## Overview

HTML website generation utilities for creating comprehensive, accessible module websites with embedded audio, text content, and interactive quizzes.

## Module Purpose

Generate single-page HTML websites for course modules that combine all module materials (lecture content, lab protocols, study guides, assignments) with audio files, text versions, and interactive quiz elements in a simple grayscale design.

## Function Signatures

### Main Functions

**File**: `src/html_website/main.py`

#### `generate_module_website(module_path: str, output_dir: Optional[str] = None, course_name: Optional[str] = None) -> str`

Generate HTML website for a module.

**Args**:
- `module_path`: Path to module directory
- `output_dir`: Output directory (defaults to `module_path/output/website`)
- `course_name`: Course name for display (optional, defaults to "BIOL-1")

**Returns**:
- Path to generated HTML file (index.html)

**Raises**:
- `ValueError`: If module path doesn't exist
- `OSError`: If website generation fails

**Process**:
1. Reads markdown source files from module directory
2. Finds corresponding audio and text files from output directory
3. Converts markdown to HTML
4. Reads questions from `questions/questions.json` if available
5. Generates complete HTML website with embedded content, resizable components, collapsible sections, and interactive questions
6. Outputs to `output/website/index.html`

**Dependencies**:
- `markdown` library for markdown to HTML conversion
- `json` library for parsing question JSON files
- `utils.read_markdown_file`
- `utils.markdown_to_html`
- `utils.find_audio_file`
- `utils.find_text_file`
- `utils.find_questions_file`
- `utils.parse_questions_json`

### Utility Functions

**File**: `src/html_website/utils.py`

#### `read_markdown_file(file_path: Path) -> str`

Read markdown file content.

**Args**:
- `file_path`: Path to markdown file

**Returns**:
- File content as string

**Raises**:
- `FileNotFoundError`: If file doesn't exist

#### `markdown_to_html(markdown_content: str) -> str`

Convert markdown content to HTML.

**Args**:
- `markdown_content`: Markdown text content

**Returns**:
- HTML content

**Dependencies**:
- `markdown` library with extensions: "extra", "codehilite", "tables"

#### `find_audio_file(base_name: str, output_dir: Path, curriculum_type: str) -> Optional[Path]`

Find audio file for a given base name and curriculum type.

**Args**:
- `base_name`: Base filename without extension
- `output_dir`: Output directory to search
- `curriculum_type`: Type of curriculum element (assignments, lecture-content, etc.)

**Returns**:
- Path to audio file if found, None otherwise

#### `find_text_file(base_name: str, output_dir: Path, curriculum_type: str) -> Optional[Path]`

Find text file for a given base name and curriculum type.

**Args**:
- `base_name`: Base filename without extension
- `output_dir`: Output directory to search
- `curriculum_type`: Type of curriculum element

**Returns**:
- Path to text file if found, None otherwise

#### `parse_questions_json(questions_file: Path) -> List[Dict]`

Parse questions from JSON file.

**Args**:
- `questions_file`: Path to questions JSON file

**Returns**:
- List of question dictionaries

**Raises**:
- `FileNotFoundError`: If questions file doesn't exist
- `json.JSONDecodeError`: If JSON is invalid

#### `find_questions_file(module_dir: Path) -> Optional[Path]`

Find questions JSON file in module directory.

**Args**:
- `module_dir`: Path to module directory

**Returns**:
- Path to questions file if found, None otherwise

#### `get_relative_path(target: Path, base: Path) -> str`

Get relative path from base to target.

**Args**:
- `target`: Target file path
- `base`: Base directory path

**Returns**:
- Relative path string

#### `extract_quiz_questions(markdown_content: str) -> List[dict]`

Extract quiz questions from markdown content.

Looks for sections with "Review Questions" or "Practice Problems".

**Args**:
- `markdown_content`: Markdown content to parse

**Returns**:
- List of question dictionaries with 'question' and 'options' keys

#### `ensure_output_directory(directory: Path) -> None`

Ensure output directory exists.

**Args**:
- `directory`: Directory path to create

## Configuration

**File**: `src/html_website/config.py`

- `DEFAULT_CSS`: Complete CSS stylesheet for grayscale website design
- `HTML_TEMPLATE`: HTML template structure with placeholders for content, CSS, and JavaScript

## Website Features

### Content Sections

1. **Lecture Content**: Full lecture materials with embedded audio player
2. **Lab Protocol**: Laboratory instructions and procedures
3. **Study Guide**: Study materials and review content
4. **Assignments**: All assignment files with audio versions
5. **Interactive Questions**: Questions from `questions/questions.json` with full interactivity

### Design Features

- **Grayscale color scheme**: Simple, professional design
- **Responsive layout**: Flexbox-based split view with sidebar
- **Audio integration**: Embedded HTML5 audio players
- **Text accessibility**: Plain text versions available
- **Resizable Layout**: Draggable handle between sidebar and content
- **Collapsible sections**: Toggle buttons to expand/collapse sections
- **State persistence**: Preferences saved in localStorage

### Interactive Features

**Sidebar Navigation**:
- Auto-generated links for all module sections
- Active state highlighting based on scroll position (ScrollSpy)
- Mobile-friendly toggle menu
- Fixed position with scrollable content

**Resizable Layout**:
- Global resize handle between sidebar and main content
- Drag to adjust width (min/max constraints applied)
- Double-click to reset defaults
- Width preference persists across sessions

**Collapsible Sections**:
- Toggle buttons in section headers
- Smooth expand/collapse animations
- Collapsed state persists across sessions
- Visual indicators (▼/▶) for state

**Interactive Questions**:
- Multiple choice: Radio buttons with answer validation
- Free response: Text areas with character counting
- True/False: Toggle buttons with validation
- Matching: Select-based matching with validation
- Progress tracking: Visual progress bar
- Answer feedback: Correct/incorrect indicators with explanations
- State persistence: Answers and progress saved

### Question Processing

**Source**: Questions are read from `questions/questions.json` in the module directory

**Question Format**: JSON structure with question objects containing:
- `id`: Unique question identifier
- `type`: Question type (multiple_choice, free_response, true_false, matching)
- `question`: Question text
- Type-specific fields (options, correct answer, explanation, etc.)

**Question Types**:

1. **Multiple Choice**:
   - Radio button selection
   - Correct answer validation
   - Visual feedback (correct/incorrect highlighting)
   - Explanation display

2. **Free Response**:
   - Textarea input
   - Character counting
   - Optional max length
   - Submission tracking for progress

3. **True/False**:
   - Toggle button selection
   - Correct answer validation
   - Visual feedback
   - Explanation display

4. **Matching**:
   - Select dropdowns for matching
   - Term-definition pairing
   - Individual item validation
   - Visual feedback per match

**Progress Tracking**:
- Completed questions counter
- Visual progress bar
- Percentage completion
- State saved in localStorage

## Output Structure

```
module-X/output/website/
└── index.html          # Complete module website
```

The website includes relative links to:
- Audio files in `output/[curriculum-type]/`
- Text files in `output/[curriculum-type]/`

## Integration Points

### Dependencies on Other Modules

- **batch_processing**: Assumes output files have been generated
- **text_to_speech**: Uses generated MP3 audio files
- **format_conversion**: Uses generated TXT text files

### Used By

- Module processing scripts
- Course material generation pipelines
- Batch website generation workflows

## Error Handling

- Missing source files are skipped (does not fail)
- Missing audio/text files are handled gracefully (sections created without them)
- File reading errors are raised as OSError
- Invalid paths raise ValueError

## Example Usage

```python
from src.html_website.main import generate_module_website

# Generate website for module-1
html_file = generate_module_website(
    "biol-1/course/module-1",
    course_name="BIOL-1"
)

print(f"Website generated: {html_file}")
```

## File Processing

- Reads markdown source files from module directory
- Locates corresponding output files (audio, text) from output directory
- Generates single HTML file with all content
- Uses relative paths for embedded resources
- Maintains module structure and organization
