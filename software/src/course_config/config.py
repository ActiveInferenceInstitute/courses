"""Configuration defaults for per-course configuration."""

from typing import Any, Dict, List

CONFIG_FILENAME: str = "course.toml"

VALID_SECTIONS: List[str] = [
    "metadata",
    "audience",
    "localization",
    "rendering",
    "assessment",
    "custom",
]

DEFAULT_CONFIG: Dict[str, Any] = {
    "metadata": {
        "title": "",
        "description": "",
        "version": "",
        "authors": [],
        "institution": "",
        "license": "",
        "created_date": "",
        "updated_date": "",
        "tags": [],
        "visibility": "public",
    },
    "audience": {
        "level": "",
        "prerequisites": [],
        "difficulty": "",
        "estimated_hours": 0,
    },
    "localization": {
        "language": "en",
        "locale": "en-US",
        "date_format": "%Y-%m-%d",
        "rtl": False,
    },
    "rendering": {
        "pdf": {
            "enabled": True,
            "page_size": "letter",
            "margins": {"top": "1in", "right": "1in", "bottom": "1in", "left": "1in"},
            "fonts": [],
            "css_file": "",
        },
        "html": {
            "enabled": True,
            "theme": "default",
            "css_file": "",
            "generate_website": True,
        },
        "audio": {
            "enabled": True,
            "voice": "",
            "lang": "en",
            "speed": 1.0,
            "slow": False,
        },
        "docx": {
            "enabled": True,
        },
        "txt": {
            "enabled": True,
        },
        "md": {
            "enabled": True,
        },
    },
    "assessment": {
        "quiz_shuffle": False,
        "show_answers": False,
        "grading_weights": {},
    },
    "custom": {},
}
