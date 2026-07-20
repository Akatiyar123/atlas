from abc import ABC, abstractmethod

from atlas.core.result import MetricResult
from atlas.core.context import Context


class Metric(ABC):
    """
    Base class for every metric.
    """

    id: str
    name: str
    description: str
    category: str
    version: str = "1.0.0"

    def setup(self, context: Context) -> None:
        pass

    @abstractmethod
    def evaluate(self, context: Context) -> MetricResult:
        """
        Evaluate a dataset.
        """
        raise NotImplementedError
    
    def teardown(self, context: Context) -> None:
        """
        Called after the evaluation is complete. 
        Can be used to clean up resources or perform any necessary finalization steps.
        """
        pass