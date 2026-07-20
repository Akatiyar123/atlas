from pathlib import Path
from collections.abc import Sequence

from atlas.core import Evaluator
from atlas.core.config import MetricConfig
from atlas.io import DatasetLoader
from atlas.report import EvaluationReport, registry as reporter_registry


class Atlas:
    """High-level entry point for evaluating datasets."""

    def evaluate(
        self,
        dataset_path: str | Path,
        metrics: list[str],
        configs: dict[str, MetricConfig] | None = None,
        formats: Sequence[str] = ("console",),
        output: str | Path | None = None,
    ) -> EvaluationReport:
        """Load, evaluate, render in one or more formats, and return a report."""
        dataset = DatasetLoader.load(dataset_path)

        report = Evaluator(
            metrics=metrics,
            configs=configs,
        ).evaluate(dataset)

        self.render(report, formats=formats, output=output)
        return report

    def render(
        self,
        report: EvaluationReport,
        formats: Sequence[str] = ("console",),
        output: str | Path | None = None,
    ) -> None:
        """Render one report without re-running its evaluation."""
        if output is not None and len(formats) != 1:
            raise ValueError("--output can only be used with a single report format.")

        for name in formats:
            reporter = reporter_registry.get(name)()
            target = Path(output) if output is not None else self._default_output(reporter)
            reporter.render(report, target)

    @staticmethod
    def _default_output(reporter) -> Path | None:
        if reporter.file_extension is None:
            return None

        return Path(f"report{reporter.file_extension}")
