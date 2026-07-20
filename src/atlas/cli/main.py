"""ATLAS command-line application."""

import typer

from atlas.cli.evaluate import app as evaluate_app
from atlas.cli.metrics import app as metrics_app
from atlas.cli.version import app as version_app

app = typer.Typer(
    help="ATLAS - Automated Toolkit for Language Data Assessment and Scoring"
)

app.add_typer(evaluate_app, name="evaluate")
app.add_typer(metrics_app, name="metrics")
app.add_typer(version_app, name="version")


def main() -> None:
    """Run the ATLAS command-line application."""
    app()


if __name__ == "__main__":
    main()
