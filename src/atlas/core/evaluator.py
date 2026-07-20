from atlas.registry import registry
from atlas.core.dataset import Dataset
from atlas.core.config import MetricConfig
from atlas.report.evaluation import EvaluationReport
from pathlib import Path
from atlas.core.context import Context


class Evaluator:

    def __init__(
        self,
        metrics: list[str],
        configs: dict[str, MetricConfig] | None = None,
    ):
        self.metrics = metrics
        self.configs = configs or {}

    def evaluate(self, dataset: Dataset):
        results = []
        for metric_name in self.metrics:
            metric_class = registry.get(metric_name)
            config = self.configs.get(
                metric_name,
                MetricConfig(),
            )
            metric = metric_class()
            context = Context(
                dataset=dataset,
                config=config,
            )
            metric.setup(context)
            result = metric.evaluate(context)
            metric.teardown(context)
            results.append(result)
        return EvaluationReport(
            dataset_name=Path(dataset.path).name,
            results=results,
        )
