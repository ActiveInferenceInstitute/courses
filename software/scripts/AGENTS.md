# specialized-agent: scripts

> **Purpose**: CLI orchestration for course generation, publishing, and maintenance.
> **Pattern**: Thin Orchestrator (CLI parsing -> `src` module invocation).

## Overview

Scripts in this directory are entry points for manual or automated workflows. They contain **no complex business logic**, delegating instead to the `software/src` modules.

## Script Reference

### Core Pipeline

| Script | Purpose | Underlying Module |
|--------|---------|-------------------|
| `publish_all.py` | Full generation & publishing pipeline | `src.publish`, `batch_processing` |
| `generate_all_outputs.py` | Generate PDFs, HTML, MP3 for a course | `src.batch_processing` |
| `validate_outputs.py` | Verify file existence and quality | `src.validation` |

### Content Maintenance

| Script | Purpose | Underlying Module |
|--------|---------|-------------------|
| `fix_stub_labs.py` | Replace template labs with generated content | `src.content_processing.labs` |
| `fix_stub_questions.py` | Generate study questions | `src.content_processing.questions` |
| `fix_stub_quizzes.py` | Generate quizzes | `src.content_processing.quizzes` |
| `renumber_questions.py` | Continuous numbering for questions | `src.content_processing` |

### AI & LLM Features (New)

| Script | Purpose | Underlying Module |
|--------|---------|-------------------|
| `summarize_courses.py` | Generate 1-page summary using LLM | `src.llm` |
| `translate_course.py` | Translate entire course directory | `src.translation` |

### Utilities

| Script | Purpose | Underlying Module |
|--------|---------|-------------------|
| `flatten_published.py` | Flatten output directory structure | `src.publish` |
| `import_legacy_materials.py` | Import from old format | `src.legacy_import` |
| `generate_dashboards.py` | Create interactive HTML dashboards | `src.content_processing.dashboards` |

## Usage Examples

### Summary Generation

```bash
# Summarize AI 101
python scripts/summarize_courses.py --course ai-101
```

### Course Translation

```bash
# Translate to Spanish (creates active_inference_es/)
python scripts/translate_course.py --course ai-philosophy --lang es
```

### Dashboard Generation

```bash
# Dry run check
python scripts/generate_dashboards.py --course ai-401 --dry-run
```
