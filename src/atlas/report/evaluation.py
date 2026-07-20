from dataclasses import dataclass, field

from atlas.core.result import MetricResult


@dataclass(slots=True)
class EvaluationReport:
    """
    Represents the complete evaluation of a dataset.
    """

    dataset_name: str

    results: list[MetricResult] = field(default_factory=list)

    @property
    def overall_score(self) -> float:
        if not self.results:
            return 0.0

        return sum(r.score for r in self.results) / len(self.results)

    @property
    def passed(self) -> bool:
        return all(result.passed for result in self.results)

    def to_dict(self) -> dict:
        """Return a stable, serializable representation of this report."""
        return {
            "dataset_name": self.dataset_name,
            "results": [
                {
                    "metric": result.metric,
                    "score": result.score,
                    "passed": result.passed,
                    "issues": [
                        {
                            "record": issue.record,
                            "field": issue.field,
                            "reason": issue.reason,
                        }
                        for issue in result.issues
                    ],
                    "metadata": result.metadata,
                }
                for result in self.results
            ],
            "overall_score": self.overall_score,
            "passed": self.passed,
        }
