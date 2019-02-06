import dash
import dash_html_components as html
from flask import render_template, url_for



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def create_app():
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    server = app.server

    app.layout = html.Div([
        html.H2('Hello Dash')
    ])

    @server.route('/main')
    def index():
        title = 'Churn Prediction'
        return render_template('index.html', page_title=title)

    return server
