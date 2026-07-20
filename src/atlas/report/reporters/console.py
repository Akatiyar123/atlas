from pathlib import Path

from rich.console import Console
from rich.table import Table

from atlas.report.base import Reporter
from atlas.report.evaluation import EvaluationReport


class ConsoleReporter(Reporter):
    """Render a report as a Rich terminal table."""

    def render(
        self,
        report: EvaluationReport,
        output: str | Path | None = None,
    ) -> None:
        console = Console()
        table = Table(title="ATLAS Evaluation Report", show_header=True, header_style="bold cyan")

        table.add_column("Metric")
        table.add_column("Score")
        table.add_column("Passed")

        for result in report.to_dict()["results"]:
            table.add_row(
                result["metric"],
                f"{result['score']:.2f}",
                "✅" if result["passed"] else "❌",
            )

        console.print(table)
        console.print()
        console.print(f"[bold]Overall Score:[/bold] {report.overall_score:.2f}")
