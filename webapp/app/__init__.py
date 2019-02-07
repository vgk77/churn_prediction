import dash
import dash_html_components as html
from flask import flash, redirect, request, render_template, url_for


from app.logic import preprocess_form_data, get_probability
from app.model import db
from app.forms import PredictionForm


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def create_app():
    app = dash.Dash(
        __name__,
        external_stylesheets=external_stylesheets,
        url_base_pathname='/analytic/',
    )

    server = app.server
    server.config.from_pyfile('config.py')
    db.init_app(server)

    app.layout = html.Div([
        html.H2('Hello Dash')
    ])

    @server.route('/prediction', methods=['GET', 'POST'])
    def prediction():
        title = 'Введите данные клиента'
        form = PredictionForm()
        if request.method == 'GET':
            return render_template('prediction.html', page_title=title, form=form)
        elif request.method == 'POST':
            if form.validate_on_submit():
                # return str(form.data)
                json_data = preprocess_form_data(form.data)
                proba = get_probability(json_data)
                # print(str(json_data))
                if proba:
                    form.probability.data = proba
                    # print(type(proba))
                    rez = round(float(proba[1:-1]), 3) * 100
                    return render_template('prediction.html', result=rez, form=form)
                    # return f'Вероятность ухода: {proba} %'
                    # return render_template('prediction.html', page_title=title, form=form)
                else:
                    return 'Служба прогноза не доступна'
            else:
                return 'Передаваемые данные не валидны'

    return server
