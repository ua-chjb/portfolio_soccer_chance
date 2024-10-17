from dash import Input, Output, State
from charts import home, away, star_chart, score_output

def callbacks_baby(app):
################# left ##################    
    # left dropdowns to polar    
    @app.callback(
        Output(component_id="left_lg_dd", component_property="options"),
        Input(component_id="left_ct_dd", component_property="value"),
    )
    def left_dropdown_country_to_league(country_value):
        mask_country = ( home["country_name"]==country_value )
        home1 = home[mask_country].copy()
        return [j for j in home1["league_name"].unique()]

    @app.callback(
        Output(component_id="left_tm_dd", component_property="options"),
        Input(component_id="left_lg_dd", component_property="value"),
    )
    def left_dropdown_league_to_team(league_value):
        mask_league = ( home["league_name"]==league_value )
        home2 = home[mask_league].copy()
        return [{"label": j, "value": j} for j in home2["team_long_name"].unique()]
    @app.callback(
        Output(component_id="leftpolar", component_property="figure"),
        Input(component_id="left_tm_dd", component_property="value"),
    )
    def polarline_left(team_name):
        mask_team = ( home["team_long_name"]==team_name )
        home3 = home[mask_team].copy()
        return star_chart(home3, mask_team)
        
################# right ##################
    # right dropdowns to polar    
    @app.callback(
        Output(component_id="right_lg_dd", component_property="options"),
        Input(component_id="right_ct_dd", component_property="value"),
    )
    def right_dropdown_country_to_league(country_value):
        mask_country = ( away["country_name"]==country_value )
        away1 = away[mask_country].copy()
        return [j for j in away1["league_name"].unique()]

    @app.callback(
        Output(component_id="right_tm_dd", component_property="options"),
        Input(component_id="right_lg_dd", component_property="value"),
    )
    def right_dropdown_league_to_team(league_value):
        mask_league = ( away["league_name"]==league_value )
        away2 = away[mask_league].copy()
        return [j for j in away2["team_long_name"].unique()]
    
    @app.callback(
        Output(component_id="rightpolar", component_property="figure"),
        Input(component_id="right_tm_dd", component_property="value"),
    )
    def polarline_right(team_name):
        mask_team = ( away["team_long_name"]==team_name )
        away3 = away[mask_team].copy()
        return star_chart(away3, mask_team)
        
################# bottom graph ###############       
    @app.callback(
        Output(component_id="win_lose", component_property="figure"),
        Input(component_id="left_tm_dd", component_property="value1"),
        Input(component_id="right_tm_dd", component_property="value2")
        )
    def home_or_away(value1, value2):
        mask_home = ( home["team_long_name"]==value1 )
        mask_away = ( away["team_long_name"]==value2 )
        return score_output(home, away, mask_home, mask_away)










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