from dash import Input, Output, State

from app import app
from charts import home, away, star_chart, score_output, scattersimple


@app.callback(
        Output(component_id="win_lose", component_property="figure"),
        Input(component_id="SIMPLE", component_property="value")
)
def away_polar(value):
    print("hello")
    return scattersimple(home)

# below here is trash
# @app.callback(
#         Output(component_id="away_polar", component_property="figure"),
#         Input(component_id="right_team_dropdown", component_property="value")
# )
# def away_polar(value):
#     mask_team = ( home["team_long_name"]==value )
#     home1 = home[mask_team].copy()
#     return star_chart(home1, "Belgium", "Belgium Jupiler League", value)

# below here is good

# @app.callback(
#     Output(component_id="lg_dd", component_property="options"),
#     Input(component_id="ct_dd", component_property="options"),
# )
# def polarcoords_left(country_value):
#     mask_country = ( home["country_name"]==country_value )
#     home1 = home[mask_country].copy()
#     print(home1["league_name"].unique())
#     return [{"label": j, "value": j} for j in home1["league_name"].unique()]

# @app.callback(
#     Output(component_id="tm_dd", component_property="options"),
#     Input(component_id="lg_dd", component_property="options"),
# )
# def polarcoords_left(league_value):
#     mask_league = ( home["league_name"]==league_value )
#     home2 = home[mask_league].copy()
#     return [{"label": j, "value": j} for j in home2["team_long_name"].unique()]



# above here should work fine

    # mask2 = ( df2["league_name"]==value2 )
    # df3 = df2[mask2]
    # mask3 =  (df3["team_long_name"]==value3 )
    # df_final = df3[mask3]

    # return star_chart(df_final, value1, value2, value3)

# @callback(
#     Output(component_id="graph_left", component_property="figure"),
#     [Input(component_id="left_team_dropdown", component_property="value")],
#     [State("left_country_dropdown", "value"),
#     State("left_league_dropdown", "value")],
# )
# def update_bool(value1, value2, value3):
#     mask1 = ( home["country_name"]==value1 )

#     df2 = home[mask1]
#     mask2 = ( df2["league_name"]==value2 )
#     df3 = df2[mask2]
#     mask3 =  (df3["team_long_name"]==value3 )
#     df_final = df3[mask3]

#     return star_chart(df_final, value1, value2, value3)