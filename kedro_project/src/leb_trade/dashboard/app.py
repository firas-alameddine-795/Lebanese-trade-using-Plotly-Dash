"""Application factory: wires layout and callbacks around a trade dataframe."""
from pathlib import Path

import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, dcc, html

from .callbacks import register_callbacks
from .layout import content, sidebar

EXTERNAL_STYLESHEETS = ["https://codepen.io/chriddyp/pen/bWLwgP.css", dbc.themes.BOOTSTRAP]


def create_app(df: pd.DataFrame) -> Dash:
    app = Dash(
        __name__,
        external_stylesheets=EXTERNAL_STYLESHEETS,
        assets_folder=str(Path(__file__).parent / "assets"),
    )
    app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
    register_callbacks(app, df)
    return app
