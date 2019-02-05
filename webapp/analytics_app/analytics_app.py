import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from app import app

db_string = "postgres://db_admin:12345@localhost/churn_db"
db = create_engine(db_string)

# get column_names for dropdown
result_columns = list(db.execute(
"""select column_name
from information_schema.columns 
where table_name = 'churn_table';"""
))
columns = map(lambda x: x[0],result_columns)

#get grouped by churn
query_string =  """select {0}, count(*) FILTER (WHERE churn = 'Yes') as churned, count(*) FILTER (WHERE churn = 'No') as not_churned
from churn_table
group by {0};"""


layout = html.Div([
    html.H1('Churn prediction analysis'),
 
    dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in columns],
                value='gender'
            ),

    dcc.Graph(id='example-graph'),

])


@app.callback(Output('example-graph', 'figure'),
              [Input('xaxis-column', 'value')])
def display_graph(value):
    result = list(db.execute(query_string.format(str(value))))
    return {
    'data': [{'x': map(lambda x: x[0],result), 'y': map(lambda x: x[1],result), 'type': 'bar', 'name': 'Churn'},
             {'x': map(lambda x: x[0],result), 'y': map(lambda x: x[2],result), 'type': 'bar', 'name': 'Not Churn'},],
    'layout':{
                'title': 'Churn by '+value
        }
        
    }