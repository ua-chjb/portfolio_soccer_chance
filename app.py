import dash
import dash_bootstrap_components as dbc

# from server import server_var, app_var
from index import layout

app = dash.Dash(__name__)

server = app.server

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True, 
        # host='0.0.0.0'
        port='8080'
        )