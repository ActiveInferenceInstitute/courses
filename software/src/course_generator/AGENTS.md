# Course Generator Module

> **Quick Navigation**: [Software README](../README.md) | [Software AGENTS](../AGENTS.md)

## Purpose

Schema-driven generation of Active Inference curriculum structures with optional
LLM-powered content enrichment via Ollama.

## Architecture

| File | Responsibility |
| --- | --- |
| `schema.py` | Dataclasses: `CurriculumConfig`, `CourseConfig`, `ModuleConfig` |
| `config.py` | All 8 curriculum definitions (ES, MS, Family, 101, 401, Embodied, Robotics, Organizations) |
| `scaffold.py` | Deterministic directory + file creation from schema |
| `content.py` | Template-based content rendering (no LLM) |
| `llm.py` | Optional Ollama integration for structured content generation |
| `main.py` | CLI interface and orchestration |
| `utils.py` | Helpers (path resolution, validation, markdown formatting) |
| `logging_config.py` | Structured logging |

## Usage

```bash
# List available curricula
python -m src.course_generator.main list

# Generate a single curriculum
python -m src.course_generator.main generate active_inference_es

# Generate all curricula
python -m src.course_generator.main generate all

# Generate with LLM enrichment
python -m src.course_generator.main generate active_inference_es --llm --model llama3.2

# Validate a generated curriculum
python -m src.course_generator.main validate ./course_development/active_inference_es
```

## Conventions

- All content must contain zero placeholders (no `[TODO]`, `[PLACEHOLDER]`, `TBD`)
- Every file uses proper MD060-compliant table formatting
- Cross-references use relative paths from the file location
- The 8-module topic spine is shared across ALL curricula
