from abc import ABC, abstractmethod
from pathlib import Path

from atlas.report.evaluation import EvaluationReport


class Reporter(ABC):
    """Present an evaluation report in a particular output format."""

    file_extension: str | None = None

    @abstractmethod
    def render(
        self,
        report: EvaluationReport,
        output: str | Path | None = None,
    ) -> None:
        """Render ``report`` to the terminal or an optional output file."""
