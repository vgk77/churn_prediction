import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from flask import flash, redirect, request, render_template, url_for


from app.logic import preprocess_form_data, get_probability
from app.model import db, Predictions
from app.forms import PredictionForm
from app.analytics import get_columns, get_statistics

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
        result_churned = get_statistics(value, query=True)
        result_not_churned = get_statistics(value, query=False)
        return {

            'data': [{'x': list(map(lambda x: x[0], result_churned)), 'y': list(map(lambda x: x[1], result_churned)), 'type': 'bar', 'name': 'Churn'},
                     {'x': list(map(lambda x: x[0], result_not_churned)), 'y': list(map(lambda x: x[1], result_not_churned)), 'type': 'bar', 'name': 'Not Churn'}, ],
            'layout': {
                'title': 'Churn by ' + value
            }}

    @server.route('/', methods=['GET'])
    def homepage():
        return render_template('index.html', title='Welcome')

    @server.route('/prediction', methods=['GET', 'POST'])
    def prediction():
        title = 'Введите данные клиента'
        form = PredictionForm()
        if form.validate_on_submit():
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
            )
            db.session.add(new_prediction)
            db.session.commit()
            flash('Клиент добавлен.')
            return redirect('/')

        return render_template('prediction.html', form=form)

        # if request.method == 'GET':
        #     return render_template('prediction.html', page_title=title, form=form)
        # elif request.method == 'POST':
        #     if form.validate_on_submit():
        #         # return str(form.data)
        #         json_data = preprocess_form_data(form.data)
        #         proba = get_probability(json_data)
        #         # print(str(json_data))
        #         if proba:
        #             form.probability.data = proba
        #             # print(type(proba))
        #             rez = round(float(proba[1:-1]), 3) * 100
        #             return render_template('prediction.html', result=rez, form=form)
        #             # return f'Вероятность ухода: {proba} %'
        #             # return render_template('prediction.html', page_title=title, form=form)
        #         else:
        #             return 'Служба прогноза не доступна'
        #     else:
                # return 'Передаваемые данные не валидны'

    return server
