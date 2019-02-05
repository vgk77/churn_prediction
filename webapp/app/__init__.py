import dash


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def create_app():
    app = dash.Dash(__name__)  # , external_stylesheets=external_stylesheets)
    server = app.server

    @server.route('/')
    def index():
        return 'Welcome to Churn Prediction WebApp !'

    return app
