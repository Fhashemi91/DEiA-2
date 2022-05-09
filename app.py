# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ["https://unpkg.com/purecss@2.1.0/build/pure-min.css"]
app = Dash(__name__, external_stylesheets=external_stylesheets)


attributes = ["A1", "A2", "A3"]
default_weight = 5
default_percentile = 5


app.layout = html.Div(children=[
    html.Label("Treshold"),
    dcc.Slider(
        min=0,
        max=10,
        marks={i: str(i) for i in range(1, 10)},
        value=5
    ),


    html.Label("Attribute"),
    dcc.Dropdown(attributes),

    html.Label("Manual Inputs"),
    html.Div(children=[
        html.Label("Percentile"),
        dcc.Slider(
            id='percentile',
            min=0,
            max=10,
            marks={i: str(i) for i in range(1, 10)},
            value=default_percentile
        ),

        html.Label("Weight"),
        dcc.Input(id='weight', value=default_weight, type='number'),

        html.Br(),
        html.Button(id='reset', children='Reset', className="pure-button pure-button-primary")
    ], style={'border': '1px solid black', 'padding': 10})
], className='pure-form')

@app.callback(
    Output(component_id='weight', component_property='value'),
    Input(component_id='reset', component_property='n_clicks')
)
def reset_weight(n_clicks):
    return default_weight


@app.callback(
    Output(component_id='percentile', component_property='value'),
    Input(component_id='reset', component_property='n_clicks')
)
def reset_percentile(n_clicks):
    return default_percentile


if __name__ == '__main__':
    app.run_server(debug=True)
