"""Shared model configuration presets."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class ModelConfig:
    """Standardized model configuration for LLM generation."""

    temperature: float = 0.45
    top_p: float = 0.9
    top_k: int = 50
    max_output_tokens: int = 4096

    def to_dict(self) -> dict[str, float | int]:
        """Return configuration as dictionary compatible with generation APIs."""
        return {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "max_output_tokens": self.max_output_tokens,
        }

    @classmethod
    def conservative(cls) -> "ModelConfig":
        """Conservative settings for highly structured responses."""
        return cls(temperature=0.3, top_p=0.8, top_k=40, max_output_tokens=2048)

    @classmethod
    def enhanced(cls) -> "ModelConfig":
        """Balanced settings recommended for production."""
        return cls(temperature=0.45, top_p=0.9, top_k=50, max_output_tokens=4096)

    @classmethod
    def creative(cls) -> "ModelConfig":
        """Creative settings for brainstorming and ideation."""
        return cls(temperature=0.6, top_p=0.95, top_k=60, max_output_tokens=4096)


@dataclass
class EvaluationConfig:
    """Standardized evaluation configuration for LLM-as-a-judge."""

    judge_model: str = "gemini-2.5-flash"
    judge_temperature: float = 0.5
    evaluation_dimensions: Optional[List[str]] = None

    def __post_init__(self) -> None:
        if self.evaluation_dimensions is None:
            self.evaluation_dimensions = [
                "relevance",
                "clarity",
                "consistency",
                "creativity",
            ]

    def to_dict(self) -> dict[str, float | str | List[str]]:
        """Return configuration as dictionary for downstream consumers."""
        return {
            "judge_model": self.judge_model,
            "judge_temperature": self.judge_temperature,
            "evaluation_dimensions": list(self.evaluation_dimensions or []),
        }

