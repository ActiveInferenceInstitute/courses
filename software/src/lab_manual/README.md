# Lab Manual Module

Tools for rendering rich lab manuals from Markdown with interactive data tables, measurement recording, and fillable worksheets.

## Installation

The lab_manual module is part of the cr-bio software package. Ensure dependencies are installed:

```bash
cd /Users/4d/Documents/GitHub/cr-bio/software
uv sync
```

## Quick Start

### Render a Lab Manual

```python
from src.lab_manual import render_lab_manual

# Render to PDF
output = render_lab_manual(
    "resources/lab-1-measurement-methods.md",
    "output/lab-1.pdf",
    output_format="pdf",
    course_name="BIOL-1: Introduction to Biology"
)

# Render to HTML (interactive)
output = render_lab_manual(
    "resources/lab-1-measurement-methods.md",
    "output/lab-1.html",
    output_format="html"
)
```

### Generate Tables Programmatically

```python
from src.lab_manual import generate_measurement_table, generate_data_table

# Measurement table with custom aspects
table_html = generate_measurement_table(
    rows=5,
    aspects=["Length", "Mass", "Volume"],
    include_device=True,
    include_unit=True
)

# Generic data table
table_html = generate_data_table(
    rows=10,
    columns=["Time", "Observation", "Notes"],
    title="Observation Log"
)
```

### Batch Rendering

```python
from src.lab_manual import batch_render_lab_manuals

# Render all labs in a directory
outputs = batch_render_lab_manuals(
    "course/module-1/labs",
    "output/module-1-labs",
    output_format="pdf",
    course_name="BIOL-1"
)
```

## Markdown Syntax

### Data Tables

Create fillable data tables:

```markdown
<!-- lab:data-table rows=5 title="Observation Log" -->
| Time | Observation | Notes |
|------|-------------|-------|
| {fill} | {fill} | {fill} |
<!-- /lab:data-table -->
```

### Object Selection

Create paired object selection fields:

```markdown
<!-- lab:object-selection -->
Object in room: {fill:text}
Object NOT in room: {fill:text}
<!-- /lab:object-selection -->
```

### Measurement Feasibility

Create feasibility analysis sections:

```markdown
<!-- lab:measurement-feasibility -->
Which aspects can we measure tonight?
{fill:textarea rows=3}

What resources are needed?
- [ ] Internet access
- [ ] Equipment purchase
- [ ] Other: {fill:text}
<!-- /lab:measurement-feasibility -->
```

### Reflection Boxes

Create reflection sections:

```markdown
<!-- lab:reflection -->
Summarize your findings:
{fill:textarea rows=5}
<!-- /lab:reflection -->
```

## Fillable Fields

| Syntax | Description | Output |
|--------|-------------|--------|
| `{fill}` | Basic fillable | Empty cell or inline input |
| `{fill:text}` | Text input | Inline text field |
| `{fill:textarea rows=N}` | Text area | Multi-line text box |

## Templates

Get pre-built lab templates:

```python
from src.lab_manual import get_lab_template

# Available templates: "basic", "measurement", "observation"
template = get_lab_template("measurement")
print(template)
```

## Output Formats

### PDF

- Print-friendly layout
- Letter size with 0.75" margins
- Fillable areas highlighted in yellow
- Tables with row numbers

### HTML

- Interactive fillable fields
- Auto-save to localStorage
- Dark mode (inherited from website module)
- Print button

## Example Lab

See `course_development/biol-1/course/module-1/resources/lab-1-measurement-methods.md` for a complete example using all features.

## API Reference

See [AGENTS.md](./AGENTS.md) for complete function signatures and technical documentation.
