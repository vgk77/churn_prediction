import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

data_dict = {'gender': {'male': (12,5), 'female':(14,12)}, 'phone_service': {'yes': (12,1), 'no':(10,9)}, 'contract': {'month-to-month':(9,2), 'year':(12,13)}}


layout = html.Div([
    html.H1('churn'),
 
    dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in data_dict.keys()],
                value='gender'
            ),

    dcc.Graph(id='example-graph'),
    html.Br(),
    dcc.Link('Go to table input', href='apps/prediction'),
    html.Br(),
    dcc.Link('Go home', href='/'),

])


@app.callback(Output('example-graph', 'figure'),
              [Input('xaxis-column', 'value')])
def display_graph(value):
        return {
        'data': [{'x': data_dict[value].keys(), 'y': map(lambda x: x[0],data_dict[value].values()), 'type': 'bar', 'name': 'Churn'},
                {'x': data_dict[value].keys(), 'y': map(lambda x: x[1],data_dict[value].values()),'type': 'bar', 'name': 'Not Churn'},],
        'layout':{
                'title': 'Churn by '+value
            }
        
    }