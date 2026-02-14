"""Per-course configuration module.

Provides layered TOML-based configuration for courses.  A ``course.toml``
file can live at any level of the directory hierarchy under
``course_development/``.  Layers merge bottom-up so that omitted fields
inherit from the level above, and the pipeline works identically when no
TOML files exist at all.
"""

from .main import (
    get_enabled_formats,
    get_localization,
    get_metadata,
    get_pdf_css,
    get_rendering_config,
    get_tts_settings,
    is_format_enabled,
    load_course_config,
)

__all__ = [
    "get_enabled_formats",
    "get_localization",
    "get_metadata",
    "get_pdf_css",
    "get_rendering_config",
    "get_tts_settings",
    "is_format_enabled",
    "load_course_config",
]
