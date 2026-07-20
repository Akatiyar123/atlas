from pathlib import Path

import typer

from atlas import Atlas
from atlas.core.config import MetricConfig

app = typer.Typer(invoke_without_command=True)


@app.callback()
def evaluate(
    dataset: str,
    formats: list[str] = typer.Option(
        ["console"],
        "--format",
        "-f",
        help="Report format; repeat to produce multiple reports.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output path when producing one file-based report.",
    ),
):
    """
    Evaluate a dataset.
    """

    Atlas().evaluate(
        dataset_path=dataset,
        metrics=["completeness"],
        configs={
            "completeness": MetricConfig(
                options={
                    "required_fields": [
                        "id",
                        "prompt",
                        "response",
                    ]
                }
            )
        },
        formats=formats,
        output=output,
    )
