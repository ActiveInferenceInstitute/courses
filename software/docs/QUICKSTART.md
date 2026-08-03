# ⚡ Quick Start Guide

> **Navigation**: [← Docs Index](README.md) | [Troubleshooting](TROUBLESHOOTING.md)

Get the Active Inference Institute course publishing pipeline running in minutes.

---

## 1. Prerequisites

- **Python 3.11+**
- **[uv](https://docs.astral.sh/uv/)** (recommended for dependency management)

### System Libraries (for PDF generation)

The pipeline uses **WeasyPrint**, which requires system-level libraries:

- **macOS**: `brew install cairo pango gdk-pixbuf glib`
- **Linux**: `apt-get install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0`
- **Windows**: [Follow WeasyPrint guides](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)

---

## 2. Installation

```bash
# Clone the repository
git clone https://github.com/ActiveInferenceInstitute/courses.git
cd courses/software

# Install dependencies (creates a virtualenv automatically)
uv sync

# Verify installation
uv run python -c "import src; print('Setup complete!')"
```

---

## 3. Rendering Your First Course

The pipeline works by transforming Markdown source files (in `course_development/`) into outputs (in `published/`).

### Render "Active Inference: Philosophy"

This will generate **Text** and **Markdown** versions (fastest).

```bash
uv run python scripts/generate_all_outputs.py --course ai-philosophy --formats txt,md
```

### Preview the Full Pipeline

See what would happen without actually writing files.

```bash
cd ..  # Return to repo root
python publish.py --dry-run
```

---

## 4. Key Commands

All commands are run from the `software/` directory using `uv run`.

| Task | Command |
| :--- | :--- |
| **Render Course** | `uv run python scripts/generate_all_outputs.py --course <ID>` |
| **Run Tests** | `uv run pytest tests/` |
| **Validate pipeline** | `uv run python scripts/validate_outputs.py` |
| **Generate Dashboard** | `uv run python scripts/generate_dashboards.py` |

### Available Course IDs

- `ai-philosophy`, `ai-cognitive-science`, `ai-math`, `ai-computer-science`
- `active-inference` (The consolidated core)
- `ai-es`, `ai-family`, `ai-ms`, `ai-hs`, `ai-101`, `ai-401`
- `ai-embodied`, `ai-organizations`, `ai-robotics`, `ai-crochet`, `ai-inventions`, `ai-metallurgy`, `ai-comedy`
- `youtube` (transcript archive)

---

## 5. Next Steps

- **[Architecture](ARCHITECTURE.md)**: Understand how it works.
- **[Contributing](CONTRIBUTING.md)**: Learn how to modify the code.
- **[Content Authoring](CONTENT_AUTHORING.md)**: Learn how to write course modules.

---
*Last Updated: 2026-08-02*
