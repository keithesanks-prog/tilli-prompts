"""Tilli Prompts - Shared prompt templates and schemas for SEAL and Prompt-Eval-Tool."""

__version__ = "1.0.0"

from tilli_prompts.prompts.intervention import InterventionPrompt
from tilli_prompts.prompts.curriculum import CurriculumPrompt
from tilli_prompts.schemas.base import (
    EMTScores,
    ClassMetadata,
    InterventionRequest,
    InterventionStrategy,
    SuccessMetrics,
    InterventionPlan,
    HealthResponse,
)
from tilli_prompts.schemas.curriculum import (
    SkillArea,
    GradeLevel,
    Implementation,
    CurriculumIntervention,
    CurriculumRequest,
    CurriculumResponse,
)

__all__ = [
    # Prompts
    "InterventionPrompt",
    "CurriculumPrompt",
    # Base Schemas
    "EMTScores",
    "ClassMetadata",
    "InterventionRequest",
    "InterventionStrategy",
    "SuccessMetrics",
    "InterventionPlan",
    "HealthResponse",
    # Curriculum Schemas
    "SkillArea",
    "GradeLevel",
    "Implementation",
    "CurriculumIntervention",
    "CurriculumRequest",
    "CurriculumResponse",
]

