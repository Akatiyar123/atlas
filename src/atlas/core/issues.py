# core/issues.py

from dataclasses import dataclass


@dataclass(slots=True)
class ValidationIssue:
    record: int
    field: str
    reason: str