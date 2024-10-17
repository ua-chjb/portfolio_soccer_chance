from dash import Input, Output, State, exceptions
from charts import star_chart, score_output
from read_data import home, away, cols

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
        return [j for j in home2["team_long_name"].unique()]
    @app.callback(
        Output(component_id="leftpolar", component_property="figure"),
        Input(component_id="left_tm_dd", component_property="value"),
    )
    def polarline_left(team_name):
        if team_name==None:
            raise exceptions.PreventUpdate
        mask_team = ( home["team_long_name"]==team_name )
        home3 = home[mask_team].copy()
        return star_chart(home3, mask_team, "teal", cols)
        
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
        if team_name==None:
            raise exceptions.PreventUpdate
        else:
            mask_team = ( away["team_long_name"]==team_name )
            away3 = away[mask_team].copy()
            return star_chart(away3, mask_team, "darkblue", cols)
        
################# bottom graph ###############       
    @app.callback(
        [Output(component_id="win_lose", component_property="figure")],
        [Input(component_id="thebutton", component_property="n_clicks")],
        [State(component_id="left_tm_dd", component_property="value"),
        State(component_id="right_tm_dd", component_property="value")]

        )
    def home_or_away(n_clicks, value1, value2):
        if n_clicks==0:
            return score_output(home, away, "Liverpool", "Leicester City")
        else:
            print(n_clicks)
            return score_output(home, away, value1, value2)
