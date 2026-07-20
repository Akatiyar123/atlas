import csv
from pathlib import Path

from atlas.report.base import Reporter
from atlas.report.evaluation import EvaluationReport


class CsvReporter(Reporter):
    """Write one CSV row per metric result."""

    file_extension = ".csv"

    def render(
        self,
        report: EvaluationReport,
        output: str | Path | None = None,
    ) -> None:
        if output is None:
            raise ValueError("CSV reports require an output path.")

        output = Path(output)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["metric", "score", "passed"])
            writer.writeheader()
            writer.writerows(
                {
                    "metric": result["metric"],
                    "score": result["score"],
                    "passed": result["passed"],
                }
                for result in report.to_dict()["results"]
            )
