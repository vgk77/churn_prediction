import dash
import dash_html_components as html
from flask import render_template, url_for, flash, redirect

from app.logic import preprocess_form_data
from app.model import db
from app.forms import PredictionForm


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
        html.H2('Hello Dash')
    ])

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

    # @server.route('/dash')
    # def show_dash():
    #    app.layout = html.Div([
    #        html.H2('Hello Dash')
    #    ])
