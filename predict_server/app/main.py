from flask import Flask
from flask import request
from logic import churn_prediction, preprocess_data

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcom to Churn Prediction!"


@app.route('/predict', methods=['POST'])
def predict():
    result = churn_prediction(preprocess_data(
        request.get_json()), 'model_data/rf_model.joblib')
    return result


if __name__ == "__main__":
    app.run(debug=True) #, host="0.0.0.0")
