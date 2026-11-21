"""Project-specific Kedro commands (`kedro dashboard`)."""
from pathlib import Path

import click
from kedro.framework.session import KedroSession


@click.group(name="leb_trade")
def cli():
    """Command line tools for leb_trade."""


@cli.command()
@click.option("--port", default=4400, show_default=True, help="Port to serve the dashboard on.")
@click.option("--debug", is_flag=True, help="Run Dash in debug (auto-reload) mode.")
@click.option("--dataset", default="trade_master", show_default=True, help="Catalog entry holding the trade table.")
def dashboard(port: int, debug: bool, dataset: str):
    """Serve the Dash app on top of the pipeline output (run `kedro run` first)."""
    from leb_trade.dashboard import create_app

    with KedroSession.create(project_path=Path.cwd()) as session:
        df = session.load_context().catalog.load(dataset)
    click.echo(f"Loaded {len(df):,} rows from '{dataset}'. Serving on http://127.0.0.1:{port}")
    create_app(df).run(port=port, debug=debug)
