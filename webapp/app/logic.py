from app.model import db, Predictions
import json


def preprocess_form_data(form_dict):
    del form_dict['csrf_token']
    del form_dict['action']
    del form_dict['probability']
    # form_dict['churn'] = 'No'
    result = json.dumps(form_dict)

    return result


def add_prediction(json_data):
    prediction_exists = Predictions.query.filter(
        Predictions.client_id == json_data.client_id).count()
    if not prediction_exists:
        new_prediction = Predictions()
        db.session.add(new_prediction)
        db.session.commit()
