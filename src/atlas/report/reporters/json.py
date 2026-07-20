import json
from pathlib import Path

from atlas.report.base import Reporter
from atlas.report.evaluation import EvaluationReport


class JsonReporter(Reporter):
    """Write a report's serialized representation as JSON."""

    file_extension = ".json"

    def render(
        self,
        report: EvaluationReport,
        output: str | Path | None = None,
    ) -> None:
        if output is None:
            raise ValueError("JSON reports require an output path.")

        output = Path(output)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8") as file:
            json.dump(report.to_dict(), file, indent=2)
            file.write("\n")
