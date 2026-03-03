"""Configuration for batch processing."""

from typing import Dict, List, Any

# File patterns to process
MARKDOWN_PATTERNS: List[str] = ["*.md", "*.markdown"]
AUDIO_PATTERNS: List[str] = ["*.mp3", "*.wav", "*.m4a"]

# Directories to skip
SKIP_DIRECTORIES: List[str] = [".git", "__pycache__", ".pytest_cache", ".venv"]

# Output directory names
OUTPUT_DIRECTORIES: Dict[str, str] = {
    "pdf": "pdf_output",
    "audio": "audio_output",
    "text": "text_output",
    "media": "media_output",
}

# =============================================================================
# Course Registry
# =============================================================================
# Each entry maps a course ID to its structural metadata.
# - rel_path: path from repo root to the course dir inside course_development/
# - display_name: human-readable name used in logs and CLI
# - module_glob: glob pattern to discover module directories inside the course
# - has_course_subdir: True if modules live under a "course/" subdirectory
# - content_files: list of markdown filenames to render per module
# - syllabus_location: where to find the syllabus (subdir name or filename)
# - module_prefix: prefix pattern for module directories

COURSE_REGISTRY: Dict[str, Dict[str, Any]] = {
    # --- Active Inference Institute courses ---
    # --- Active Inference Core (Consolidated) ---
    "active-inference": {
        "rel_path": "course_development/active_inference",
        "display_name": "Active Inference (Core)",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
        "static_dirs": [
            "04_computer_science/src/active_inference",
            "04_computer_science/tests",
            "resources",
        ],
    },
    # --- Legacy Individual Entries (Deprecated) ---
    "ai-philosophy": {
        "rel_path": "course_development/active_inference/01_philosophy",
        "display_name": "Active Inference: Philosophy",
        "module_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-cognitive-science": {
        "rel_path": "course_development/active_inference/02_cognitive_science",
        "display_name": "Active Inference: Cognitive Science",
        "module_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-math": {
        "rel_path": "course_development/active_inference/03_math",
        "display_name": "Active Inference: Mathematics",
        "module_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-computer-science": {
        "rel_path": "course_development/active_inference/04_computer_science",
        "display_name": "Active Inference: Computer Science",
        "module_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    # --- Level-Adapted Courses ---
    "ai-es": {
        "rel_path": "course_development/active_inference_es",
        "display_name": "Active Inference: Elementary School",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-family": {
        "rel_path": "course_development/active_inference_family",
        "display_name": "Active Inference: Family",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-ms": {
        "rel_path": "course_development/active_inference_ms",
        "display_name": "Active Inference: Middle School",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-hs": {
        "rel_path": "course_development/active_inference_hs",
        "display_name": "Active Inference: High School",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-101": {
        "rel_path": "course_development/active_inference_101",
        "display_name": "Active Inference: College 101",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-401": {
        "rel_path": "course_development/active_inference_401",
        "display_name": "Active Inference: Advanced 401",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    # --- Domain Courses ---
    "ai-embodied": {
        "rel_path": "course_development/domains/active_inference_embodied",
        "display_name": "Active Inference: Embodied",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-organizations": {
        "rel_path": "course_development/domains/active_inference_organizations",
        "display_name": "Active Inference: Organizations",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-robotics": {
        "rel_path": "course_development/domains/active_inference_robotics",
        "display_name": "Active Inference: Robotics",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-crochet": {
        "rel_path": "course_development/domains/active_inference_crochet",
        "display_name": "Active Inference: Crochet",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-inventions": {
        "rel_path": "course_development/domains/active_inference_inventions",
        "display_name": "Active Inference: Inventions",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-metallurgy": {
        "rel_path": "course_development/domains/active_inference_metallurgy",
        "display_name": "Active Inference: Metallurgy",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    "ai-comedy": {
        "rel_path": "course_development/domains/active_inference_comedy",
        "display_name": "Active Inference: Comedy",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "[0-9][0-9]_*",
        "has_course_subdir": False,
        "content_files": ["module.md", "questions.md", "practice_quiz.md", "lab.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
    # --- YouTube Transcript Archive ---
    "youtube": {
        "rel_path": "course_development/youtube",
        "display_name": "YouTube Transcripts",
        "module_glob": "[0-9][0-9]_*",
        "unit_glob": "*",
        "has_course_subdir": False,
        "content_files": ["module.md"],
        "syllabus_location": "syllabus.md",
        "module_prefix": "",
    },
}

# Available output formats
AVAILABLE_FORMATS: List[str] = ["pdf", "mp3", "docx", "html", "txt", "md"]

# File selection patterns for batch processing
SAMPLE_FILE_PREFIX: str = "sample_"

# Content type patterns that map filenames to study-guide output subdirectory
CONTENT_TYPE_PATTERNS: List[str] = ["keys-to-success", "comprehension-questions"]
QUESTIONS_FILENAME: str = "questions.md"
