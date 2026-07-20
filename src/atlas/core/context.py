from dataclasses import dataclass, field
from typing import Any

from atlas.core.config import MetricConfig
from atlas.core.dataset import Dataset


@dataclass(slots=True)
class Context:
    """
    Shared execution context passed to every metric.
    """

    dataset: Dataset
    config: MetricConfig = field(default_factory=MetricConfig)
    metadata: dict[str, Any] = field(default_factory=dict)