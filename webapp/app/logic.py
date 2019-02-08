import json
import requests

from app.model import db, Predictions
from app.config import PREDICTAPP_URL


def preprocess_form_data(form_dict):
    del form_dict['csrf_token']
    del form_dict['action']
    del form_dict['probability']
    # form_dict['churn'] = 'No'
    # result = json.dumps(form_dict)

    return form_dict

def get_probability(json_data):
    response = requests.post(PREDICTAPP_URL, json=json_data)
    if response.status_code == 200:
        return response.text
    else:
        return False

def add_prediction(form):
    prediction_exists = Predictions.query.filter(
        Predictions.customer_id == form.customer_id).count()
    if not prediction_exists:
        new_prediction = Predictions(
            customer_id = form.customer_id.data,
            gender=form.gender.data,
            senior_citizen=form.senior_citizen.data,
            partner=form.partner.data,
            dependents=form.dependents.data,
            tenure=form.tenure.data,
            phone_service=form.phone_service.data,
            multiplelines=form.multiplelines.data,
            internet_service=form.internet_service.data,
            online_security=form.online_security.data,
            streaming_tv=form.streaming_tv.data,
            online_backup=form.online_backup.data,
            streaming_movies=form.streaming_movies.data,
            device_protection=form.device_protection.data,
            techsupport=form.techsupport.data,
            contract=form.contract.data,
            paperless=form.paperless.data,
            payment_method=form.payment_method.data,
            monthly_charges=form.monthly_charges.data,
            total_charges=form.total_charges.data,
            probability=form.probability.data,
            churn = 'null'
        )
        try:
            db.session.add(new_prediction)
            db.session.commit()
            return 'DATA ADD'
        except Exception as e:
            return(str(e))
    else:
        return 'data exists'
