"""CSV logging utilities shared across SEAL and Prompt-Eval-Tool."""

from __future__ import annotations

import csv
import os
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional


DEFAULT_FIELDNAMES: List[str] = [
    "timestamp",
    "batch_id",
    "row_type",
    "model",
    "temperature",
    "question",
    "answer",
    "judge_feedback",
    "judge_prompt",
    "total_rating",
    "validation_status",
    "relevance_score",
    "clarity_score",
    "consistency_score",
    "creativity_score",
]


@dataclass
class CSVLogger:
    """Shared CSV logging utility for evaluation results."""

    filepath: str = "evaluations.csv"
    fieldnames: Optional[Iterable[str]] = None
    append_headers: bool = True

    def __post_init__(self) -> None:
        if isinstance(self.fieldnames, Iterable):
            self._fieldnames: List[str] = list(self.fieldnames)
        else:
            self._fieldnames = list(DEFAULT_FIELDNAMES)
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Create CSV file with headers if it doesn't exist."""
        if not os.path.exists(self.filepath):
            os.makedirs(os.path.dirname(self.filepath) or ".", exist_ok=True)
            with open(self.filepath, "w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=self._fieldnames)
                writer.writeheader()

    def log(self, data: Dict[str, Any]) -> None:
        """Log a single evaluation row."""
        row = {key: data.get(key, "") for key in self._fieldnames}
        if not row.get("timestamp"):
            row["timestamp"] = datetime.utcnow().isoformat()

        with open(self.filepath, "a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=self._fieldnames)
            writer.writerow(row)


def log_evaluation(logger: CSVLogger, data: Dict[str, Any]) -> None:
    """Convenience wrapper to log a single evaluation row."""
    enriched = {"row_type": data.get("row_type", "evaluation"), **data}
    logger.log(enriched)


def log_batch_summary(logger: CSVLogger, summary: Dict[str, Any]) -> None:
    """Log aggregated metrics for a batch run (e.g., averages, totals)."""
    enriched = {"row_type": summary.get("row_type", "batch_summary"), **summary}
    logger.log(enriched)


def get_evaluation_history(filepath: str) -> List[Dict[str, str]]:
    """Load the CSV history for downstream analytics."""
    if not os.path.exists(filepath):
        return []

    with open(filepath, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader)

