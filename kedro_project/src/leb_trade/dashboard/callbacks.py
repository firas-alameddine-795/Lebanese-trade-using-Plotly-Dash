"""Dash callbacks: page routing and the interactive figures of the four dashboards."""
import pandas as pd
from dash import Input, Output, State, html

from . import figures
from .layout import build_userguide, dash_page, harmonized_system, home


def is_root(data):
    """True when nothing is selected, or the root of a treemap was clicked/hovered.

    Plotly omits 'percentRoot' for some points (e.g. the path bar), so don't assume it exists.
    """
    if not data or not data.get('points'):
        return True
    point = data['points'][0]
    return point.get('percentRoot') == 1 or not point.get('label')


def register_callbacks(app, df: pd.DataFrame) -> None:
    """Attach every callback to `app`; `df` is the master trade table."""
    userguide = build_userguide(df)

    # Local helpers keep the original call style (flow, ..., optional filtered dataframe).
    def create_time_series(flow, dff=None):
        return figures.create_time_series(df if dff is None else dff, flow)

    def create_products_treemap(flow, year, depth, dff=None):
        return figures.create_products_treemap(df if dff is None else dff, flow, year, depth)

    def create_countries_treemap(flow, year, dff=None):
        return figures.create_countries_treemap(df if dff is None else dff, flow, year)

    def build_diff_treemap_products(value, flow, dff=None):
        return figures.build_diff_treemap_products(df if dff is None else dff, value, flow)

    def build_diff_treemap_countries(value, flow, dff=None):
        return figures.build_diff_treemap_countries(df if dff is None else dff, value, flow)

    #Callbacks to render content

    @app.callback(
        [Output(f"page-{i}-link", "active") for i in range(1, 5)],
        [Input("url", "pathname")],
    )
    def toggle_active_links(pathname):
        if pathname == "/":
            # Treat page 1 as the homepage / index
            return True, False, False, False
        return [pathname == f"/page-{i}" for i in range(1, 5)]


    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname in ["/", "/page-1"]:
            return html.Div([home])
        elif pathname == "/page-2":
            return html.Div([harmonized_system])
        elif pathname == "/page-3":
            return html.Div([userguide])
        elif pathname == "/page-4":
            return html.Div([dash_page])


    #Callbacks to update figures
    @app.callback(Output('treemap 1_1','figure'),
                 [Input('submit 1','n_clicks')],
                 [State('flow 1','value'),
                  State('year 1','value'),
                  State('hs 1','value')])
    def update_countries_treemap(n_clicks, flow, year, depth):
        fig1 = create_products_treemap(flow, year, depth)
        return fig1

    @app.callback(Output('treemap 1_2','figure'),
                 [Input('treemap 1_1','clickData'),
                  Input('submit 1','n_clicks')],
                 [State('flow 1','value'),
                  State('year 1','value')])
    def update_countries_treemap(clickData, n_clicks, flow, year):
        if is_root(clickData):
            fig2 = create_countries_treemap(flow, year)
            return fig2
    
        product = clickData['points'][0]['label']
        dfff = df[(df['hs1_desc'] == product) | (df['hs2_desc'] == product) | 
                  (df['hs4_desc'] == product) | (df['hs6_desc'] == product)]
        fig2 = create_countries_treemap(flow, year, dfff)
        return fig2

    @app.callback(Output('time series 1','figure'),
                 [Input('treemap 1_1','clickData'),
                  Input('treemap 1_2','hoverData'),
                  Input('submit 1','n_clicks')],
                 [State('flow 1','value')])
    def update_time_series(clickData, hoverData, n_clicks, flow):
        if (is_root(clickData)) and (is_root(hoverData)):
            fig3 = create_time_series(flow)
            return fig3
        elif clickData != None and (is_root(hoverData)):
            product = clickData['points'][0]['label']
            dfff = df[(df['hs1_desc'] == product) | 
                      (df['hs2_desc'] == product) | 
                      (df['hs4_desc'] == product) | 
                      (df['hs6_desc'] == product)]
            fig3 = create_time_series(flow, dfff)
            return fig3
        elif (is_root(clickData)) and hoverData != None:
            place = hoverData['points'][0]['label']
            dfff = df[(df['region'] == place) | 
                      (df['country'] == place)]
            fig3 = create_time_series(flow, dfff)
            return fig3
        else:
            product = clickData['points'][0]['label']
            dfff = df[(df['hs1_desc'] == product) | 
                      (df['hs2_desc'] == product) | 
                      (df['hs4_desc'] == product) | 
                      (df['hs6_desc'] == product)]
        
            place = hoverData['points'][0]['label']
            dfff = dfff[(dfff['region'] == place) | 
                        (dfff['country'] == place)]
            fig3 = create_time_series(flow, dfff)
            return fig3

    @app.callback(Output('treemap 2_1','figure'),
                 [Input('submit 2','n_clicks')],
                 [State('flow 2','value'),
                  State('year 2','value')])
    def update_countries_treemap_2(n_clicks, flow, year):
        fig1 = create_countries_treemap(flow, year)
        return fig1

    @app.callback(Output('treemap 2_2','figure'),
                 [Input('treemap 2_1','clickData'),
                  Input('submit 2','n_clicks')],
                 [State('flow 2','value'),
                  State('year 2','value'),
                  State('hs 2','value')])
    def update_countries_treemap(clickData, n_clicks, flow, year, depth):
        if is_root(clickData):
            fig2 = create_products_treemap(flow, year, depth)
            return fig2
        place = clickData['points'][0]['label']
        dfff = df[(df['region'] == place) | 
                  (df['country'] == place)]
        fig2 = create_products_treemap(flow, year, depth, dfff)
        return fig2

    @app.callback(Output('time series 2','figure'),
                 [Input('treemap 2_1','clickData'),
                  Input('treemap 2_2','hoverData'),
                  Input('submit 2','n_clicks')],
                 [State('flow 2','value')])
    def update_time_series(clickData, hoverData, n_clicks, flow):
        if (is_root(clickData)) and (is_root(hoverData)):
            fig3 = create_time_series(flow)
            return fig3
        elif clickData != None and (is_root(hoverData)):
            place = clickData['points'][0]['label']
            dfff = df[(df['region'] == place) | 
                      (df['country'] == place)]
            fig3 = create_time_series(flow, dfff)
            return fig3
        elif (is_root(clickData)) and hoverData != None:
            product = hoverData['points'][0]['label']
            dfff = df[(df['hs1_desc'] == product) | 
                      (df['hs2_desc'] == product) | 
                      (df['hs4_desc'] == product) | 
                      (df['hs6_desc'] == product)]
            fig3 = create_time_series(flow, dfff)
            return fig3
        else:
            place = clickData['points'][0]['label']
            dfff = df[(df['region'] == place) | 
                      (df['country'] == place)]
        
            product = hoverData['points'][0]['label']
            dfff = dfff[(dfff['hs1_desc'] == product) | 
                        (dfff['hs2_desc'] == product) | 
                        (dfff['hs4_desc'] == product) | 
                        (dfff['hs6_desc'] == product)]
            fig3 = create_time_series(flow, dfff)
            return fig3

    @app.callback(Output('treemap 3_1','figure'),
                 [Input('submit 3','n_clicks')],
                 [State('slider 3','value'),
                  State('flow 3','value')])
    def update_treemap_diff_products(n_clicks, value, flow):
        return build_diff_treemap_products(value, flow)

    @app.callback(Output('treemap 3_2','figure'),
                 [Input('treemap 3_1','clickData'),
                  Input('submit 3','n_clicks')],
                 [State('slider 3','value'),
                  State('flow 3','value')])
    def update_treemap_diff_countries(clickData, n_clicks, value, flow):
        while is_root(clickData):
            return build_diff_treemap_countries(value, flow)
        product = clickData['points'][0]['label']
    
        dff = df[(df['hs1_desc']==product) |
                 (df['hs2_desc']==product) |
                 (df['hs4_desc']==product) |
                 (df['hs6_desc']==product)]
    
        return build_diff_treemap_countries(value, flow, dff)

    @app.callback(Output('time series 3','figure'),
                 [Input('treemap 3_1','clickData'),
                  Input('treemap 3_2','hoverData'),
                  Input('submit 3','n_clicks')],
                 [State('flow 3','value')])
    def update_time_series(clickData, hoverData, n_clicks, flow):
        if (is_root(clickData)) and (is_root(hoverData)):
            fig3 = create_time_series(flow)
            return fig3
        elif clickData != None and (is_root(hoverData)):
            place = clickData['points'][0]['label']
            dfff = df[(df['region'] == place) | 
                      (df['country'] == place)]
            fig3 = create_time_series(flow, dfff)
            return fig3
        elif (is_root(clickData)) and hoverData != None:
            product = hoverData['points'][0]['label']
            dfff = df[(df['hs1_desc'] == product) | 
                      (df['hs2_desc'] == product) | 
                      (df['hs4_desc'] == product) | 
                      (df['hs6_desc'] == product)]
            fig3 = create_time_series(flow, dfff)
            return fig3
        else:
            place = clickData['points'][0]['label']
            dfff = df[(df['region'] == place) | 
                      (df['country'] == place)]
        
            product = hoverData['points'][0]['label']
            dfff = dfff[(dfff['hs1_desc'] == product) | 
                        (dfff['hs2_desc'] == product) | 
                        (dfff['hs4_desc'] == product) | 
                        (dfff['hs6_desc'] == product)]
            fig3 = create_time_series(flow, dfff)
            return fig3

    @app.callback(Output('treemap 4_1','figure'),
                 [Input('submit 4','n_clicks')],
                 [State('slider 4','value'),
                  State('flow 4','value')])
    def update_treemap_diff_countries_(n_clicks, value, flow):
        return build_diff_treemap_countries(value, flow)

    @app.callback(Output('treemap 4_2','figure'),
                 [Input('treemap 4_1','clickData'),
                  Input('submit 4','n_clicks')],
                 [State('slider 4','value'),
                  State('flow 4','value')])
    def update_treemap_diff_products_(clickData, n_clicks, value, flow):
        while is_root(clickData):
            return build_diff_treemap_products(value, flow)
        place = clickData['points'][0]['label']
    
        dff = df[(df['region']==place) | 
                 (df['country']==place)]
    
        return build_diff_treemap_products(value, flow, dff)
    @app.callback(Output('time series 4','figure'),
                 [Input('treemap 4_1','clickData'),
                  Input('treemap 4_2','hoverData'),
                  Input('submit 4','n_clicks')],
                 [State('flow 4','value')])
    def update_time_series(clickData, hoverData, n_clicks, flow):
        if (is_root(clickData)) and (is_root(hoverData)):
            fig3 = create_time_series(flow)
            return fig3
        elif clickData != None and (is_root(hoverData)):
            place = clickData['points'][0]['label']
            dfff = df[(df['region'] == place) | 
                      (df['country'] == place)]
            fig3 = create_time_series(flow, dfff)
            return fig3
        elif (is_root(clickData)) and hoverData != None:
            product = hoverData['points'][0]['label']
            dfff = df[(df['hs1_desc'] == product) | 
                      (df['hs2_desc'] == product) | 
                      (df['hs4_desc'] == product) | 
                      (df['hs6_desc'] == product)]
            fig3 = create_time_series(flow, dfff)
            return fig3
        else:
            place = clickData['points'][0]['label']
            dfff = df[(df['region'] == place) | 
                      (df['country'] == place)]
        
            product = hoverData['points'][0]['label']
            dfff = dfff[(dfff['hs1_desc'] == product) | 
                        (dfff['hs2_desc'] == product) | 
                        (dfff['hs4_desc'] == product) | 
                        (dfff['hs6_desc'] == product)]
            fig3 = create_time_series(flow, dfff)
            return fig3
