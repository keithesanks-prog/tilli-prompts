"""Schema definitions for intervention and curriculum data."""

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
    # Base schemas
    "EMTScores",
    "ClassMetadata",
    "InterventionRequest",
    "InterventionStrategy",
    "SuccessMetrics",
    "InterventionPlan",
    "HealthResponse",
    # Curriculum schemas
    "SkillArea",
    "GradeLevel",
    "Implementation",
    "CurriculumIntervention",
    "CurriculumRequest",
    "CurriculumResponse",
]

