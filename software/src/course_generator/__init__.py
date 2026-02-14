"""Course generator module for Active Inference curricula.

Provides schema-driven generation of complete curriculum structures
with optional LLM-powered content enrichment via Ollama.
"""

from .schema import (
    CurriculumConfig,
    CourseConfig,
    ModuleConfig,
    MODULE_TOPICS,
    MODULE_FILES,
    RESOURCE_FILES,
    ROOT_FILES,
    COURSE_FILES,
)
from .config import (
    ALL_CURRICULA,
    AGE_LEVEL_CURRICULA,
    DOMAIN_CURRICULA,
    CURRICULUM_ES,
    CURRICULUM_MS,
    CURRICULUM_FAMILY,
    CURRICULUM_101,
    CURRICULUM_401,
    CURRICULUM_EMBODIED,
    CURRICULUM_ROBOTICS,
    CURRICULUM_ORGANIZATIONS,
)
from .scaffold import generate_curriculum, generate_single_course
from .main import generate, generate_all, validate, list_curricula
from .llm import OllamaClient, enrich_module, enrich_curriculum

__all__ = [
    # Schema
    "CurriculumConfig",
    "CourseConfig",
    "ModuleConfig",
    "MODULE_TOPICS",
    "MODULE_FILES",
    "RESOURCE_FILES",
    "ROOT_FILES",
    "COURSE_FILES",
    # Config
    "ALL_CURRICULA",
    "AGE_LEVEL_CURRICULA",
    "DOMAIN_CURRICULA",
    "CURRICULUM_ES",
    "CURRICULUM_MS",
    "CURRICULUM_FAMILY",
    "CURRICULUM_101",
    "CURRICULUM_401",
    "CURRICULUM_EMBODIED",
    "CURRICULUM_ROBOTICS",
    "CURRICULUM_ORGANIZATIONS",
    # Scaffold
    "generate_curriculum",
    "generate_single_course",
    # Main
    "generate",
    "generate_all",
    "validate",
    "list_curricula",
    # LLM
    "OllamaClient",
    "enrich_module",
    "enrich_curriculum",
]
