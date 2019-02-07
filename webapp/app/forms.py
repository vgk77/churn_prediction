from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DecimalField, BooleanField, FloatField
from wtforms.validators import DataRequired, InputRequired


class PredictionForm(FlaskForm):
    customer_id = StringField(
        'ID Клиента',
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    gender = SelectField(
        'Пол',
        validators=[InputRequired()],
        choices=[('Male', 'Мужчина'), ('Female', 'Женщина')],
        render_kw={"class": "form-control"},
    )
    senior_citizen = BooleanField(
        'Пожилой',
        default=False,
        render_kw={"class": "checkbox-inline"},
    )
    partner = BooleanField(
        'Партнер',
        default=False,
        render_kw={"class": "checkbox-inline"},
    )
    dependents = BooleanField(
        'Иждивенец',
        default=False,
        render_kw={"class": "checkbox-inline"},
    )
    tenure = IntegerField(
        'Срок пользования',
        validators=[InputRequired()],
        render_kw={"class": "form-control", "type": "number"},
    )
    phone_service = BooleanField(
        'Услуги телефонии',
        default=False,
        render_kw={"class": "checkbox-inline"},
    )
    multiplelines = SelectField(
        'Многоканальные линии',
        validators=[DataRequired()],
        choices=[
            ('NO_PHONE', 'Нет телефонных услуг'),
            ('Yes', 'Да'),
            ('No', 'Нет')
        ],
        render_kw={"class": "form-control"},
    )
    internet_service = SelectField(
        'Услуги  интернета',
        validators=[DataRequired()],
        choices=[
            ('Fiber optic', 'Оптоволокно'),
            ('DSL', 'DSL'),
            ('No', 'Нет')
        ],
        render_kw={"class": "form-control"},
    )
    online_security = SelectField(
        'Безопасность онлайн',
        validators=[DataRequired()],
        choices=[
            ('NO_INTERNET', 'Нет интернет услуг'),
            ('Yes', 'Да'),
            ('No', 'Нет')
        ],
        render_kw={"class": "form-control"},
    )
    streaming_tv = SelectField(
        'Потоковое ТВ',
        validators=[DataRequired()],
        choices=[
            ('NO_INTERNET', 'Нет интернет услуг'),
            ('Yes', 'Да'),
            ('No', 'Нет')
        ],
        render_kw={"class": "form-control"},
    )
    online_backup = SelectField(
        'Онлайн хранилище',
        validators=[DataRequired()],
        choices=[
            ('NO_INTERNET', 'Нет интернет услуг'),
            ('Yes', 'Да'),
            ('No', 'Нет')
        ],
        render_kw={"class": "form-control"},
    )
    streaming_movies = SelectField(
        'Потоковое кино',
        validators=[DataRequired()],
        choices=[
            ('NO_INTERNET', 'Нет интернет услуг'),
            ('Yes', 'Да'),
            ('No', 'Нет')
        ],
        render_kw={"class": "form-control"},
    )
    device_protection = SelectField(
        'Защита устройства',
        validators=[DataRequired()],
        choices=[
            ('NO_INTERNET', 'Нет интернет услуг'),
            ('Yes', 'Да'),
            ('No', 'Нет')
        ],
        render_kw={"class": "form-control"},
    )
    techsupport = SelectField(
        'Техподдержка',
        validators=[DataRequired()],
        choices=[
            ('NO_INTERNET', 'Нет интернет услуг'),
            ('Yes', 'Да'),
            ('No', 'Нет')
        ],
        render_kw={"class": "form-control"},
    )
    contract = SelectField(
        'Контракт',
        validators=[DataRequired()],
        choices=[
            ('Month-to-month', 'Ежемесячный'),
            ('One year', 'Годовой'),
            ('Two year', 'Двух годовой')
        ],
        render_kw={"class": "form-control"},
    )
    paperless = BooleanField(
        'Безбумажные чеки',
        default=False,
        render_kw={"class": "checkbox-inline"},
    )
    payment_method = SelectField(
        'Способ оплаты',
        validators=[DataRequired()],
        choices=[
            ('Electronic check', 'Электронный чек'),
            ('Bank transfer', 'Банковский перевод'),
            ('Mailed check', 'Почтовый перевод'),
            ('Credit card', 'Кредитная карта'),
        ],
        render_kw={"class": "form-control"},
    )
    monthly_charges = FloatField(
        'Ежемесячная оплата',
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    total_charges = FloatField(
        'Общая сумма оплат',
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    probability = FloatField(
        'Вероятность ухода',
        # validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    action = SubmitField(
        'Добавить в БД',
        render_kw={"class": "btn btn-primary btn-block"})

    # predict = SubmitField(
    #     'Прогноз вероятности ухода',
    #     render_kw={"class": "btn btn-primary btn-block", "name": "submit", "value": "Pr"})
