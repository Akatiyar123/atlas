"""Version command."""

import typer

from atlas.version import __version__

app = typer.Typer(invoke_without_command=True)


@app.command()
def version() -> None:
    """Show the ATLAS version."""
    typer.echo(f"ATLAS {__version__}")


@app.callback()
def version_callback(ctx: typer.Context) -> None:
    """Show the version when no subcommand is specified."""
    if ctx.invoked_subcommand is None:
        version()
