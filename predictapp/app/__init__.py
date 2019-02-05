from flask import Flask
from flask import request

from app.logic import churn_prediction, preprocess_data


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
            'model_data/rf_model.joblib'),
        )
        return result

    return app

