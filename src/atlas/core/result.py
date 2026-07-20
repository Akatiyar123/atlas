from dataclasses import dataclass, field
from typing import Any
from atlas.core.issues import ValidationIssue


@dataclass(slots=True)
class MetricResult:
    """
    Result returned by every metric.
    """

    metric: str
    score: float
    passed: bool
    issues: list[ValidationIssue] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)