from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class MetricConfig:
    """
    Configuration passed to metrics.
    """

    options: dict[str, Any] = field(default_factory=dict)