from flask import Flask
from flask import request
# import dash_core_components as dcc
# import dash_html_components as html

from app.logic import churn_prediction, preprocess_data


# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
# ])


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Welcome to Predict App !'

    @app.route('/predict', methods=['POST'])
    def predict():
        # TODO: Обработать исключения при не правильном json запросе
        result = str(churn_prediction(
            preprocess_data(request.get_json()), 
            'model_data/model.joblib'),
        )
        return result

    return app

