# ActiveInferAnt Stream 017.1 — "Of Course I Can": Active Inference Courses for All

> **Date**: 2026-02-14  
> **Host**: Daniel Ari Friedman ([@docxology](https://github.com/docxology))  
> **Repo**: [ActiveInferenceInstitute/courses](https://github.com/ActiveInferenceInstitute/courses)

---

## 🎯 Stream Agenda: Comprehensive Repository Walk-through

### Opening (5 min)

- Start with a Github push
- Welcome & stream context
- Write comments and questions in the livechat, we will make and publish courses for whatever people suggest.
- What is this repo? — A single open-source home for **10 courses**, **320 modules**, **3,400+ content files**, a full **publishing engine**, and a **YouTube transcript archive**
- This is intended as a first pass on course material; an opening gambit. From here, please email <blanket@activeinference.institute> with subject [EDUCATION] if you would like to get involved. There are directions ranging from course polishing, curating, and presenting, credentialing, DeSchooling, translation and localization
- Goals for today: walk through every layer of the repository, explore existing courses, make new courses, get excited about Active Inference education today and tomorrow!

---

### 1. Repository Architecture (10 min)

- Configuration with top-level publish.toml and publish.py
- **Root structure overview**
  - `course_development/` — All source curricula (authoring space)
  - `published/` — Rendered outputs for distribution
  - `software/` — The Python engine that powers everything
  - `publish.py` + `publish.toml` — Top-level pipeline entry point & configuration
  - `summaries/` — Generated course summaries
  - `AGENTS.md` / `README.md` — Documentation & agent guidelines at every level
- **Design philosophy**
  - Development ↔ Published separation (source vs. artifact)
  - Shared 8-topic spine across all courses
  - Modular software with layered dependencies
  - Configuration-driven publishing (`publish.toml`)

---

### 2. Course Development — The 10-Course Curriculum Portfolio (20 min)

#### 2a. The 8-Topic Spine

- Every course follows the same conceptual dependency chain:
  1. **Systems** — What exists? Markov blankets, boundaries
  2. **Agents** — Which systems act? Agency, autonomy
  3. **Perception** — How agents sense: generative models, prediction error
  4. **Cognition** — How agents think: belief updating, precision weighting
  5. **Action** — How agents do: policy selection, active inference
  6. **Learning** — How agents improve: model updating, structure learning
  7. **Communication** — How agents coordinate: shared models, social inference
  8. **Planning** — How agents plan: expected free energy, temporal depth
- Spiral learning: same spine at increasing formalism from K-5 to PhD

#### 2b. Active Inference Core Curriculum (`active_inference/`)

- 4 disciplinary tracks, 8 modules each = 32 modules
  - `01_philosophy/` — Philosophical argumentation, thought experiments
  - `02_cognitive_science/` — Neural correlates, clinical case studies
  - `03_math/` — Formal derivations, proofs, notation
  - `04_computer_science/` — Custom Python `active_inference` library, coding labs
- Each module contains: `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`, `dashboard.html`, `README.md`, `AGENTS.md`
- Shared resources: `notation_table.md`, `glossary.md`, `references.md`, `cross_course_map.md`

#### 2c. Level-Adapted Curricula (6 courses)

| Course | Audience | Units × Modules | Key Style |
|--------|----------|-----------------|-----------|
| `active_inference_es/` | Grades K-5 | 4 × 8 = 32 | Stories, drawing, play |
| `active_inference_family/` | Families & young children | 4 × 8 = 32 | Parent-child activities, nurturing |
| `active_inference_ms/` | Grades 6-8 | 4 × 8 = 32 | Group challenges, Scratch/blocks |
| `active_inference_hs/` | Grades 9-12 | 4 × 8 = 32 | Guided labs, Python basics |
| `active_inference_101/` | Undergraduates | 4 × 8 = 32 | Full notation, simulations, essays |
| `active_inference_401/` | PhD/Graduate | 4 × 8 = 32 | Research seminars, paper reviews, proofs |

- Walk through one module at each level to show tone adaptation
- Color identity system for dashboards

#### 2d. Domain Curricula (3 courses)

| Course | Domain | Units × Modules | Key Style |
|--------|--------|-----------------|-----------|
| `active_inference_embodied/` | Body & Movement | 4 × 8 = 32 | Somatic exercises, mindfulness |
| `active_inference_organizations/` | Systems & Strategy | 4 × 8 = 32 | Case studies, workshops |
| `active_inference_robotics/` | Engineering | 4 × 8 = 32 | ROS2, hardware labs, control theory |

- Live walkthrough of a domain module

---

### 3. YouTube Transcript Archive (`course_development/youtube/`) (10 min)

- **38 playlists** covering the full Active Inference Institute YouTube presence
  - `active-inference-livestreams-paper-discussions/` — 1,065 files, main lecture series
  - `gueststreams/` — 925 files, invited experts
  - `active-inference-free-energy-principle-lectures-podcasts/` — 497 files
  - `active-inferant-stream/` — 169 files, this very stream series!
  - `modelstreams/`, `mathstreams/`, `bookstreams/`, `artstream/`
  - Multiple textbook group cohorts (1, 3, 4, 6, 7, 8, 9)
  - Applied Active Inference Symposia (2021–2025)
  - `physics-as-information-processing-chris-fields-2023/`
  - And more...
- `youtube_courses.json` — Structured metadata for all playlists
- Transcription pipeline: `scripts/transcribe_youtube.py`, `scripts/render_youtube_courses.py`
- Translation pipeline: `scripts/translate_youtube.py`

---

### 4. Software Engine (`software/`) (15 min)

#### 4a. Source Modules (`src/`)

- **21 Python modules**, layered architecture (L0–L4):
  - **L0 (Independent)**: `module_organization`, `file_validation`
  - **L1 (Core)**: `markdown_to_pdf`, `text_to_speech`, `speech_to_text`
  - **L2 (Format)**: `format_conversion`
  - **L3 (Orchestration)**: `batch_processing`, `html_website`, `schedule`, `lab_manual`
  - **L4 (Integration)**: `canvas_integration`, `publish`, `validation`
  - **Content**: `content_processing`, `course_config`, `course_generator`, `llm`
  - **External**: `youtube_transcript`, `translation`, `legacy_import`, `danvas`
- Each module: `__init__.py`, `main.py`, `utils.py`, `config.py`, `AGENTS.md`
- Real methods policy: no mocks, no stubs, no fakes

#### 4b. CLI Scripts (`scripts/`)

- **23 scripts** for the full development workflow:
  - `generate_all_outputs.py` — Master rendering (course → formats)
  - `generate_dashboards.py` — Interactive HTML dashboards
  - `generate_module_website.py` — Per-module websites
  - `publish_all.py` / `publish_course.py` — Publishing pipeline
  - `transcribe_youtube.py` / `translate_youtube.py` — YouTube workflows
  - `translate_course.py` — Multi-language course translation
  - `scan_modules.py`, `validate_outputs.py` — Quality assurance
  - `fix_structural_issues.py`, `fix_stub_*` — Structural remediation
  - And more...

#### 4c. Documentation (`docs/`)

- **18 documentation files** covering every aspect:
  - `QUICKSTART.md` — Installation & setup
  - `ARCHITECTURE.md` — System design & module layers
  - `ORCHESTRATION.md` — Multi-module workflow patterns
  - `CLI_REFERENCE.md` — Complete CLI documentation
  - `CONFIGURATION.md` — Config system reference
  - `CONTENT_AUTHORING.md` — How to write course content
  - `COURSE_CATALOG.md` — All courses at a glance
  - `COURSE_GENERATOR.md` — Schema-driven curriculum generation
  - `TRANSLATION.md` — Multi-language support
  - `YOUTUBE.md` — YouTube integration guide
  - `DANVAS.md` — Dashboard canvas system
  - `MODULES.md`, `TESTING.md`, `TROUBLESHOOTING.md`, `CONTRIBUTING.md`

#### 4d. Testing

- 822 tests, all passing
- Coverage across all modules
- All tests use real methods — no mocks or stubs

---

### 5. Publishing Pipeline (10 min)

- **Entry point**: `python publish.py` at repo root
- **Configuration**: `publish.toml` — toggle courses, formats, options
- **Supported formats**: PDF, DOCX, HTML, TXT, MD, MP3
- **Generated outputs**:
  - `published/active-inference/` — Consolidated core course
  - `published/ai-101/`, `ai-401/`, `ai-es/`, `ai-family/`, `ai-ms/`, `ai-hs/`
  - `published/ai-embodied/`, `ai-organizations/`, `ai-robotics/`
  - `published/translations/` — Multi-language versions
  - `published/youtube/` — Rendered YouTube transcripts
- **Live demo**: Run `python publish.py --dry-run` to show what gets generated
- **Per-module outputs**: Each module produces ~5-6 files across formats + dashboard + website

---

### 6. Published Outputs & Translations (5 min)

- Walk through `published/` directory structure
- Show a rendered module across formats (PDF, HTML, DOCX, TXT)
- **Translations**: Multi-language course delivery
  - Organized under `published/translations/{LANGUAGE_NAME}/courses/`
  - `translate_course.py` — Automated pipeline
- **YouTube rendered**: `published/youtube/` — Transcripts rendered into clean formats

---

### 7. Documentation & Agent Architecture (10 min)

- **AGENTS.md hierarchy** — 66+ files across every directory level
  - Root `AGENTS.md` — Top-level repo guidelines
  - `course_development/AGENTS.md` — Master curriculum agent guidelines
  - `software/AGENTS.md` — Full software technical reference (517 lines)
  - Per-course, per-unit, per-module AGENTS.md files
- **README.md hierarchy** — GitHub landing pages at every level
- **Purpose**: Enable AI agents to work effectively anywhere in the repo
- **Real methods policy**: All code uses real implementations, no mocks/stubs
- **Quality checklist**: Universal standards for every module

---

### 8. Key Metrics & Statistics (5 min)

- **10 courses** spanning K-5 through PhD
- **40 units**, **320 modules**
- **3,400+ content files** (module.md, questions.md, practice_quiz.md, lab.md, dashboard.html, README.md, AGENTS.md)
- **38 YouTube playlists**, ~2,600 video transcripts
- **21 software modules**, **23 CLI scripts**, **18 documentation files**
- **822 tests**, all passing with real methods
- **6 output formats**: PDF, DOCX, HTML, TXT, MD, MP3
- **Multi-language** translation support

---

### 9. Q&A & Discussion (10 min)

- Open questions from the audience
- How to contribute: `CONTRIBUTING.md`
- Roadmap & future directions
  - Additional domain courses
  - More language translations
  - Enhanced interactive dashboards
  - LMS integration expansion
- Community resources & links

---

### Closing (5 min)

- Recap key takeaways
- Links & resources
  - **Repository**: <https://github.com/ActiveInferenceInstitute/courses>
  - **Active Inference Institute**: <https://activeinference.org>
  - **Documentation**: `software/docs/README.md`
- Thank you & see you next stream!

---

> *"Minimize surprise. Maximize evidence."* — Active Inference Institute
