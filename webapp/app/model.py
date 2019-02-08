from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import ChoiceType

db = SQLAlchemy()


class Predictions(db.Model):
    GENDER_CHOICES = [
        ('Male', 'Мужчина'),
        ('Female', 'Женщина')
    ],

    NO_PHONE_CHOICES = [
        ('NO_PHONE', 'Нет телефонных услуг'),
        ('Yes', 'Да'),
        ('No', 'Нет')
    ],

    INTERNET_SERVICE_CHOICES = [
        ('Fiber optic', 'Оптоволокно'),
        ('DSL', 'DSL'),
        ('No', 'Нет')
    ],

    NO_INTERNET_CHOICES = [
        ('NO_INTERNET', 'No internet service'),
        ('Yes', 'Да'),
        ('No', 'Нет')
    ]

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String, unique=True, nullable=False)
    gender = db.Column(db.String, nullable=False)
    senior_citizen = db.Column(db.Boolean, nullable=False)
    partner = db.Column(db.Boolean, nullable=False)
    dependents = db.Column(db.Boolean, nullable=False)
    tenure = db.Column(db.Integer, nullable=False)
    phone_service = db.Column(db.Boolean, nullable=False)
    multiplelines = db.Column(db.String, nullable=False)
    internet_service = db.Column(db.String, nullable=False)
    online_security = db.Column(db.String, nullable=False)
    streaming_tv = db.Column(db.String, nullable=False)
    online_backup = db.Column(db.String, nullable=False)
    streaming_movies = db.Column(db.String, nullable=False)
    device_protection = db.Column(db.String, nullable=False)
    techsupport = db.Column(db.String, nullable=False)
    contract = db.Column(db.String, nullable=False)
    paperless = db.Column(db.Boolean, nullable=False)
    payment_method = db.Column(db.String, nullable=False)
    monthly_charges = db.Column(db.Float, nullable=False)
    total_charges = db.Column(db.Float, nullable=False)
    churn = db.Column(db.Boolean, nullable=True)
    probability = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '{} {}'.format(self.client_id, self.probability)
