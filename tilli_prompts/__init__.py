"""Tilli Prompts - Shared prompt templates and schemas for SEAL and Prompt-Eval-Tool."""

__version__ = "1.1.0"

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
from tilli_prompts.logging import (
    CSVLogger,
    get_evaluation_history,
    log_batch_summary,
    log_evaluation,
)
from tilli_prompts.config import ModelConfig, EvaluationConfig

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
    # Logging
    "CSVLogger",
    "log_evaluation",
    "log_batch_summary",
    "get_evaluation_history",
    # Config
    "ModelConfig",
    "EvaluationConfig",
]



