import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from dash import Input, Output, callback


Card_left_top = dbc.Card(
    dbc.CardBody([
        html.H1("Home"),
        dcc.Graph(figure={})
    ], className="home")
)

Card_left_bottom = dbc.Card(
    dbc.CardBody([
        dcc.Dropdown(
            [],
            multi=False,
            searchable=True,
            id="left_country_dropdown"
            ),
        dcc.Dropdown(
            [],
            multi=False,
            searchable=True,
            id="left_league_dropdown"
            ),
        dcc.Dropdown(
            [],
            multi=False,
            searchable=True,
            id="left_team_dropdown"
            ),
    ])
)


Card_right_top = dbc.Card(
    dbc.CardBody([
        html.H1("Away"),
        dcc.Graph(figure={})
    ], className="away")
)

Card_right_bottom = dbc.Card(
    dbc.CardBody([
        dcc.Dropdown(
            [],
            multi=False,
            searchable=True,
            id="right_country_dropdown"
            ),
        dcc.Dropdown(
            [],
            multi=False,
            searchable=True,
            id="right_league_dropdown"
            ),
        dcc.Dropdown(
            [],
            multi=False,
            searchable=True,
            id="right_team_dropdown"
            ),
    ])
)

Card_below_fold = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={})
    ])
)

main_content = html.Div([
    html.Div([

        html.Div([
            Card_left_top,
            Card_left_bottom,
        ], className="flex_baby_left flex_daddy"),

        html.Div([
            Card_right_top,
            Card_right_bottom,
        ], className="flex_baby_right flex_daddy"),

    ], className="flex_daddy"),
    Card_below_fold
])


lyt = html.Div([
    main_content
], fluid=True)