import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from flask import flash, redirect, request, render_template, url_for


from app.logic import preprocess_form_data, get_probability
from app.model import db
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
        result_churned = get_statistics(value, query = True)
        result_not_churned= get_statistics(value, query = False)
        return {
           
           'data': [{'x': list(map(lambda x: x[0],result_churned)), 'y': list(map(lambda x: x[1],result_churned)), 'type': 'bar', 'name': 'Churn'},
                   {'x': list(map(lambda x: x[0],result_not_churned)), 'y': list(map(lambda x: x[1],result_not_churned)), 'type': 'bar', 'name': 'Not Churn'},],
            'layout':{
                'title': 'Churn by '+value
                } }

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
