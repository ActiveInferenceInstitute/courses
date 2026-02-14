"""Configuration for module organization."""

from pathlib import Path
from typing import Dict, List

# Required files in each module
REQUIRED_FILES: List[str] = ["README.md", "AGENTS.md"]

# Required directories in each module
REQUIRED_DIRECTORIES: List[str] = ["assignments"]

# Template content for README.md
README_TEMPLATE: str = """# Module {module_number}

## Overview

Module {module_number} course materials.

## Contents

### Assignments

Assignments for this module are located in the [`assignments/`](assignments/) directory.

### Course Materials

This module includes:
- **Lecture Slides**: Presentation materials for module topics
- **Lab Protocols and Notes**: Laboratory instructions and documentation
- **Study Guides**: Student study materials
- **Quizzes**: Assessment materials

## Documentation

- **[AGENTS.md](AGENTS.md)**: Technical documentation for module structure and file management
"""

# Template content for AGENTS.md
AGENTS_TEMPLATE: str = """# Module {module_number} Technical Documentation

## Module Structure

### Directory Organization

```
module-{module_number}/
├── assignments/      # Assignment files
├── README.md         # Module overview
└── AGENTS.md         # This file
```

### File Types

- **Assignments**: Markdown or PDF files in `assignments/` directory
- **Lecture Slides**: PDF or PowerPoint files
- **Lab Protocols**: Markdown files
- **Study Guides**: Markdown or PDF files
- **Quizzes**: Markdown or PDF files

## File Naming Conventions

### Assignments
- Format: `module-{module_number}-assignment-[number]-[description].md`
- Example: `module-{module_number}-assignment-1-introduction.md`

### Lecture Materials
- Format: `module-{module_number}-lecture-[topic].pdf` or `.pptx`
- Example: `module-{module_number}-lecture-introduction.pdf`

### Lab Protocols
- Format: `module-{module_number}-lab-[number]-[topic].md`
- Example: `module-{module_number}-lab-1-safety.md`

### Study Guides
- Format: `module-{module_number}-study-guide.md`

### Quizzes
- Format: `module-{module_number}-quiz.md`

## File Management

### Assignment Organization
- All assignments stored in `assignments/` subdirectory
- Numbered sequentially
- Descriptive names for easy identification

### Material Updates
- Maintain version control for major revisions
- Update README.md when adding new materials
- Document file changes in this AGENTS.md

## Canvas Upload

### Preparation
- Verify all required files are present
- Check file naming conventions
- Ensure folder structure matches Canvas organization
- Validate that no private materials are included

### Upload Process
- Upload entire module folder to Canvas
- Maintain folder structure
- Update Canvas links after upload
"""

# Template content for assignments/README.md
ASSIGNMENTS_README_TEMPLATE: str = """# Module {module_number} Assignments

## Overview

This directory contains assignment files for Module {module_number}.

## Assignment Files

Assignment files will be added to this directory as they are created.

## File Naming

Assignments follow the naming convention: `module-{module_number}-assignment-[number]-[description].md`

## Documentation

- **[AGENTS.md](AGENTS.md)**: Technical documentation for assignment management processes
"""

# Template content for assignments/AGENTS.md
ASSIGNMENTS_AGENTS_TEMPLATE: str = """# Module {module_number} Assignments Technical Documentation

## Assignment Management

### File Organization

- All assignments stored in this directory
- Sequential numbering: `module-{module_number}-assignment-1`, `module-{module_number}-assignment-2`, etc.
- Descriptive suffixes for topic identification

### Naming Convention

- Format: `module-{module_number}-assignment-[number]-[description].md`
- Number: Sequential assignment number
- Description: Brief topic or title identifier

### File Structure

Assignment files should include:
- Assignment title
- Instructions
- Requirements
- Submission guidelines
- Due dates

## Workflow

### Creating Assignments

1. Create file with proper naming convention
2. Include standard assignment sections
3. Update parent module README.md with assignment reference
4. Document in this AGENTS.md file

### Updating Assignments

1. Maintain version history for major changes
2. Update assignment index in README.md
3. Document changes in this file

## Quality Checks

- Verify naming convention compliance
- Ensure all required sections are present
- Check for consistency across assignments
- Validate file format and structure
"""
