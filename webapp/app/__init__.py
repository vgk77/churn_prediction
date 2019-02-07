import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from flask import render_template, url_for, flash, redirect

from app.logic import preprocess_form_data
from app.model import db
from app.forms import PredictionForm
from app.analytics import get_columns, get_statistics

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def create_app():
    app = dash.Dash(
        __name__,
        external_stylesheets=external_stylesheets,
        url_base_pathname='/dash/',
    )

    server = app.server
    server.config.from_pyfile('config.py')
    db.init_app(server)

    app.layout = html.Div([
            html.H1('Churn prediction analysis'),
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in get_columns()],
                value='gender'
                        ),
            dcc.Graph(id='example-graph')])
    
    @app.callback(Output('example-graph', 'figure'),
                [Input('xaxis-column', 'value')])
    def display_graph(value):
        result_churned = get_statistics(value, query = True)
        result_not_churned= get_statistics(value, query = False)
        return {
           
           'data': [{'x': list(map(lambda x: x[0],result_churned)), 'y': list(map(lambda x: x[1],result_churned)), 'type': 'bar', 'name': 'Churn'},
                   {'x': list(map(lambda x: x[0],result_not_churned)), 'y': list(map(lambda x: x[1],result_not_churned)), 'type': 'bar', 'name': 'Not Churn'},],
            'layout':{
                'title': 'Churn by '+value
                } }

    @server.route('/prediction')
    def prediction():
        title = 'Churn Prediction'
        prediction_form = PredictionForm()
        return render_template('prediction.html', page_title=title, form=prediction_form)

    @server.route('/process-prediction', methods=['POST'])
    def process_prediction():
        form = PredictionForm()
        if form.validate_on_submit():
            result = preprocess_form_data(form.data)
        else:
            result = 'qq'

        return result

    return server

