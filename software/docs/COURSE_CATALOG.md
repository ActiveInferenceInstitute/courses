# Course Catalog

> **Navigation**: [README](README.md) | [Quick Start](QUICKSTART.md) | [Content Authoring](CONTENT_AUTHORING.md) | [Architecture](ARCHITECTURE.md)

Complete catalog of all courses managed by the Active Inference Institute publishing pipeline. Every course listed here has a corresponding entry in [`COURSE_REGISTRY`](../src/batch_processing/config.py).

---

## Course Categories

| Category | Courses | Description |
|----------|---------|-------------|
| [Core](#core-consolidated) | 1 consolidated + 4 legacy individual | The primary Active Inference textbook |
| [Level-Adapted](#level-adapted-courses) | 6 | Same curriculum adapted for different audiences |
| [Domain-Specific](#domain-specific-courses) | 7 | Active Inference applied to specific fields |
| [Archive](#youtube-transcript-archive) | 1 | 38 playlists / ~821 YouTube video transcripts |

---

## Core (Consolidated)

### `active-inference` — Active Inference (Core)

The primary consolidated course combining all four units of the Active Inference textbook. This is the recommended course for full rendering.

| Field | Value |
|-------|-------|
| **Registry ID** | `active-inference` |
| **Display name** | Active Inference (Core) |
| **Path** | `course_development/active_inference/` |
| **Structure** | 4 units x 8 modules = 32 modules |
| **Content files** | `module.md`, `questions.md`, `practice_quiz.md`, `lab.md` |
| **Static dirs** | `04_computer_science/src/active_inference`, `04_computer_science/tests`, `resources` |

#### Units

| Unit | Directory | Topic | Modules |
|------|-----------|-------|---------|
| 1 | `01_philosophy/` | Philosophy of Active Inference | 8 |
| 2 | `02_cognitive_science/` | Cognitive Science of Active Inference | 8 |
| 3 | `03_math/` | Mathematics of Active Inference | 8 |
| 4 | `04_computer_science/` | Computer Science of Active Inference | 8 |

#### Module Topics (per unit)

| # | Philosophy | Cognitive Science | Mathematics | Computer Science |
|---|-----------|-------------------|-------------|------------------|
| 1 | Systems | Systems | Systems | Systems |
| 2 | Agents | Agents | Agents | Agents |
| 3 | Perception | Perception | Perception | Perception |
| 4 | Cognition | Cognition | Cognition | Cognition |
| 5 | Action | Action | Action | Action |
| 6 | Learning | Learning | Learning | Learning |
| 7 | Communication | Communication | Communication | Communication |
| 8 | Planning | Planning | Planning | Planning |

Each module covers the same topic from a different disciplinary perspective, enabling cross-course comparison.

#### Cross-Course Navigation

Modules link to their counterparts via README files:

```markdown
| [Philosophy](../../01_philosophy/01_systems/) | Boundaries, Markov Blankets |
| [Cognitive Science](../../02_cognitive_science/01_systems/) | Neural Assemblies |
| [Mathematics](../../03_math/01_systems/) | Matrices, Probability |
| [Computer Science](../../04_computer_science/01_systems/) | Generative Models |
```

#### Shared Resources

| Resource | Path | Description |
|----------|------|-------------|
| Notation Table | `resources/notation_table.md` | Symbol definitions used across all units |
| Glossary | `resources/glossary.md` | Term definitions |
| References | `resources/references.md` | Bibliographic citations |

```bash
# Render the full consolidated core course
uv run python scripts/generate_all_outputs.py --course active-inference --formats txt,md
```

---

### Legacy Individual Courses (Deprecated)

These entries allow rendering individual units separately. They are deprecated in favor of `active-inference`:

| ID | Unit | Path |
|----|------|------|
| `ai-philosophy` | Philosophy | `course_development/active_inference/01_philosophy` |
| `ai-cognitive-science` | Cognitive Science | `course_development/active_inference/02_cognitive_science` |
| `ai-math` | Mathematics | `course_development/active_inference/03_math` |
| `ai-computer-science` | Computer Science | `course_development/active_inference/04_computer_science` |

```bash
# Render only the philosophy unit
uv run python scripts/generate_all_outputs.py --course ai-philosophy --formats txt,md
```

---

## Level-Adapted Courses

These courses adapt the Active Inference curriculum for different educational levels and audiences. Each uses the same 4-unit x 8-module structure with content tailored for its audience.

| ID | Display Name | Audience | Path |
|----|-------------|----------|------|
| `ai-es` | Elementary School | Ages 6-10 | `course_development/active_inference_es/` |
| `ai-family` | Family | Multi-generational, ages 5+ | `course_development/active_inference_family/` |
| `ai-ms` | Middle School | Ages 11-13 | `course_development/active_inference_ms/` |
| `ai-hs` | High School | Ages 14-18 | `course_development/active_inference_hs/` |
| `ai-101` | College Introductory | Undergraduate | `course_development/active_inference_101/` |
| `ai-401` | Advanced PhD Seminar | Graduate/PhD | `course_development/active_inference_401/` |

### Common Structure

All level-adapted courses share:

- **Unit/module glob**: `[0-9][0-9]_*` at both unit and module level
- **Content files**: `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`
- **Syllabus**: `syllabus.md` per unit

### Audience Differences

| Level | Language | Depth | Lab Style |
|-------|----------|-------|-----------|
| Elementary | Simple, concrete metaphors | Introductory concepts | Hands-on activities |
| Family | Accessible, multi-age | Shared exploration | Group activities |
| Middle School | Age-appropriate academic | Foundational | Guided experiments |
| High School | Academic with scaffolding | Intermediate | Structured labs |
| College 101 | University-level prose | Standard textbook depth | Research-oriented |
| Advanced 401 | Graduate-level academic | Full mathematical rigor | Research proposals |

```bash
# Render all level-adapted courses
for course in ai-es ai-family ai-ms ai-hs ai-101 ai-401; do
  uv run python scripts/generate_all_outputs.py --course $course --formats txt,md
done
```

---

## Domain-Specific Courses

These courses apply Active Inference to specific professional and research domains.

| ID | Display Name | Focus Area | Path |
|----|-------------|-----------|------|
| `ai-embodied` | Embodied Active Inference | Robotics, morphological computation, sensorimotor coupling | `course_development/domains/active_inference_embodied/` |
| `ai-organizations` | Organizations | Management, governance, collective intelligence | `course_development/domains/active_inference_organizations/` |
| `ai-robotics` | Robotics Applications | Practical robotics implementations | `course_development/domains/active_inference_robotics/` |
| `ai-crochet` | Active Inference & Crochet | Fiber arts, stitch patterns, morphological computation through craft | `course_development/domains/active_inference_crochet/` |
| `ai-inventions` | Active Inference & Inventions | Creative engineering, design thinking, innovation processes | `course_development/domains/active_inference_inventions/` |
| `ai-metallurgy` | Active Inference & Metallurgy | Materials science, alloy design, phase transformations | `course_development/domains/active_inference_metallurgy/` |
| `ai-comedy` | Active Inference & Comedy | Comedic structure, timing dynamics, crowd reading, improvisation | `course_development/domains/active_inference_comedy/` |

### Structure

Same 4-unit x 8-module pattern, adapted for domain context:

- **Unit/module glob**: `[0-9][0-9]_*`
- **Content files**: `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`
- **Syllabus**: `syllabus.md`

```bash
# Render a domain course
uv run python scripts/generate_all_outputs.py --course ai-embodied --formats txt,md
```

---

## YouTube Transcript Archive

### `youtube` — YouTube Transcripts

An archive of transcripts from the Active Inference Institute YouTube channel (38 playlists, ~821 videos per playlist metadata).

| Field | Value |
|-------|-------|
| **Registry ID** | `youtube` |
| **Display name** | YouTube Transcripts |
| **Path** | `course_development/youtube/` |
| **Unit glob** | `*` (playlist directories) |
| **Module glob** | `[0-9][0-9]_*` (video directories within playlists) |
| **Content files** | `module.md` only |

### YouTube Pipeline

The YouTube archive has a dedicated multi-stage pipeline:

1. **Enumerate** playlists from the channel
2. **Scaffold** course directory structures per playlist
3. **Transcribe** videos (auto-captions, then Whisper fallback)
4. **Render** through the standard batch processing pipeline

```bash
# List playlists
uv run python scripts/render_youtube_courses.py --list-playlists

# Scaffold and render a single playlist
uv run python scripts/render_youtube_courses.py --course active-inference-textbook-group --formats txt,md

# Full archive render
uv run python scripts/render_youtube_courses.py --formats txt,md
```

See [YOUTUBE.md](YOUTUBE.md) for the full YouTube processing guide.

---

## Module File Reference

Every Active Inference module (across all course types) contains:

| File | Purpose | Rendering Category | Output Formats |
|------|---------|-------------------|----------------|
| `module.md` | Main lecture content | `lecture-content/` | PDF, HTML, DOCX, TXT, MD, MP3 |
| `questions.md` | 20 study questions | `study-guides/` | PDF, HTML, DOCX, TXT, MD, MP3 |
| `practice_quiz.md` | 7 MC + 3 FR quiz | `study-guides/` | PDF, HTML, DOCX, TXT, MD, MP3 |
| `lab.md` | Lab protocol/activity | `lab-protocols/` | PDF, HTML, DOCX, TXT, MD, MP3 |
| `dashboard.html` | Interactive dashboard | (copied as-is) | HTML |
| `README.md` | Module overview & navigation | (not rendered) | -- |
| `AGENTS.md` | Agent/contributor guidelines | (not rendered) | -- |

### Dashboard Features

Each `dashboard.html` is a standalone interactive page with:

- Concept cards with expandable detail sections
- Self-assessment quiz with scoring
- Study checklist with progress tracking
- Module navigation links
- Dark theme UI

---

## Course Registry Configuration

All courses are registered in `COURSE_REGISTRY` inside `software/src/batch_processing/config.py`. Key fields:

| Field | Type | Description |
|-------|------|-------------|
| `rel_path` | `str` | Path from repo root to course directory |
| `display_name` | `str` | Human-readable name for logs/CLI |
| `module_glob` | `str` | Glob pattern for module directories |
| `unit_glob` | `str` | Glob pattern for unit directories (multi-level courses) |
| `content_files` | `list[str]` | Files to render per module |
| `syllabus_location` | `str` | Where to find the syllabus |
| `static_dirs` | `list[str]` | Additional directories to copy during publish |

### Adding a New Course

1. Add an entry to `COURSE_REGISTRY` in `software/src/batch_processing/config.py`
2. Create the directory structure under `course_development/`
3. Add the course to `publish.toml` at the repo root
4. Run: `uv run python scripts/generate_all_outputs.py --course YOUR_ID --dry-run`

---

## Quick Commands

```bash
# List all registered course IDs
uv run python -c "from src.batch_processing.config import COURSE_REGISTRY; print('\n'.join(COURSE_REGISTRY.keys()))"

# Count modules for a course
uv run python -c "
from pathlib import Path
from src.batch_processing.utils import find_modules_for_course
from src.batch_processing.config import COURSE_REGISTRY
reg = COURSE_REGISTRY['active-inference']
modules = find_modules_for_course(Path(reg['rel_path']), 'active-inference')
print(f'{len(modules)} modules')
"

# Dry-run preview for all enabled courses
python publish.py --dry-run
```

---

*Last Updated: 2026-08-02*
