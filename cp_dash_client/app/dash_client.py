# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div(
        "Left Div",
        className="left-pane",
        style={
            "background": "grey",
            # "float": "left",
            "width": "29%",
            "display": "inline-block",
            # "height": "100%",
        }
    ),
    html.Div([
        html.Div(
            "Data Result Div",
            className="data-resulte-pane",
            style={
                "background": "green",
            }
        )
        ],
        "Data Table Div",
        className="data-table-pane",
        style={
            "background": "red",
            "width": "71%",
            "display": "inline-block",
        }
    ),

    
    # html.Div(
    #     className="app-header",
    #     children=[
    #         html.Div('Plotly Dash', className="app-header--title")
    #     ]
    # ),
    # html.Div(
    #     children=html.Div([
    #         html.H5('Overview'),
    #         html.Div('''
    #             This is an example of a simple Dash app with
    #             local, customized CSS.
    #         ''')
    #     ])
    # )
])

if __name__ == '__main__':
    app.run_server(debug=True)
