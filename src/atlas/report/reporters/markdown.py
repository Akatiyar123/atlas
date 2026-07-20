from pathlib import Path

from atlas.report.base import Reporter
from atlas.report.evaluation import EvaluationReport


class MarkdownReporter(Reporter):
    """Write a report as a Markdown document."""

    file_extension = ".md"

    def render(
        self,
        report: EvaluationReport,
        output: str | Path | None = None,
    ) -> None:
        if output is None:
            raise ValueError("Markdown reports require an output path.")

        output = Path(output)
        data = report.to_dict()
        lines = [
            "# ATLAS Evaluation Report",
            "",
            f"Dataset: `{data['dataset_name']}`",
            "",
            "| Metric | Score | Passed |",
            "|--------|------:|:------:|",
        ]
        lines.extend(
            f"| {result['metric']} | {result['score']:.2f} | "
            f"{'✅' if result['passed'] else '❌'} |"
            for result in data["results"]
        )
        lines.extend(["", f"Overall Score: {data['overall_score']:.2f}", ""])

        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("\n".join(lines), encoding="utf-8")
