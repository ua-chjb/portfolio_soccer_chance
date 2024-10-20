import dash_bootstrap_components as dbc
from dash import html, dcc

from read_data import home, away, cols

########################## left #########################3
    # top left graph

Card_left_top = dbc.Card(
    dbc.CardBody([
        html.Div([
            html.H1("Home"),
        ], className="headercenter"),
        dcc.Dropdown(
            options=[j for j in home["country_name"].unique()],
            value=home["country_name"].unique()[0],
            multi=False,
            searchable=True,
            id="left_ct_dd",
            className="dropdown",
            ),
        dcc.Dropdown(
            # options=[],
            options=[f for f in home["league_name"].unique()],
            value=home["league_name"].unique()[0],
            multi=False,
            searchable=True,
            id="left_lg_dd",
            className="dropdown",
            ),
        dcc.Dropdown(
            # options=[],
            options=[k for k in home["team_long_name"].unique()],
            value=home["team_long_name"].unique()[0],
            multi=False,
            searchable=True,
            id="left_tm_dd",
            className="dropdown",
            ),
    ], className="knucklepuck centerflex")
)
    # bottom left graph

Card_left_bottom = dbc.Card(
    dbc.CardBody([
        dcc.Graph(id="leftpolar", figure={})
    ], className="knucklepuck home")
)
########################## right #########################3
    # top right graph
Card_right_top = dbc.Card(
    dbc.CardBody([
        html.Div([
            html.H1("Away"),
        ], className="headercenter"),
        dcc.Dropdown(
            options=[j for j in away["country_name"].unique()],
            value=away["country_name"].unique()[0],
            multi=False,
            searchable=True,
            clearable=False,
            id="right_ct_dd",
            className="dropdown"
            ),
        dcc.Dropdown(
            # options=[],
            options=[j for j in away["league_name"].unique()],
            value=away["league_name"].unique()[0],
            multi=False,
            searchable=True,
            clearable=False,
            id="right_lg_dd",
            className="dropdown"
            ),
        dcc.Dropdown(
            # options=[],
            options=[j for j in away["team_long_name"].unique()],
            value=away["team_long_name"].unique()[0],
            multi=False,
            searchable=True,
            clearable=False,
            id="right_tm_dd",
            className="dropdown"
            ),
    ], className="knucklepuck centerflex")
)

    # bottom right graph

Card_right_bottom = dbc.Card(
    dbc.CardBody([
        dcc.Graph(id="rightpolar", figure={})
    ], className="knucklepuck away")
)


########################## graph at bottom #########################3


Card_below_fold = dbc.Card(
    dbc.CardBody([
        html.Div([
            html.Button("Play", n_clicks=0, id="thebutton"),
        ]),
        html.Div([
            dcc.Graph(id="win_lose", figure={})
        ])
    ], className="knucklepuck blow_fold_flex"),
)

########################## summary #########################3


main_content = html.Div([
    html.Div([

        html.Div([
            Card_left_top,
            Card_left_bottom,
        ], className="inner_fd"),

        html.Div([
            Card_right_top,
            Card_right_bottom,
        ], className="inner_fd"),

    ], className="flex_daddy above"),

    html.Div([
        Card_below_fold
    ])

])
########################## exec summary #########################3

lyt = dbc.Container([
    main_content,
])