import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

############################# chart 1 ####################################
def star_chart(df, mask_team, color, cols):

    df1 = df[mask_team]
    
    score_name = df1[cols].columns
    score_attr = df1[cols].values.flatten()

    return px.line_polar(r=score_attr, theta=score_name, line_close=True, markers=True, symbol_sequence=["diamond"], color_discrete_sequence=[color], range_r=[0, 80])


############################# chart 2 ####################################

import plotly.graph_objs as go

def score_output(df1, df2, value1, value2, title, shlg):

    mask_home = ( df1["team_long_name"]==value1 )
    mask_away = ( df2["team_long_name"]==value2 )
    x =["A"]

    y1 = df1[mask_home]["home_team_goal"].values
    y2 = df2[mask_away]["away_team_goal"].values
    
    name_home = str(df1[mask_home]["team_long_name"].values[0]) + " @home"
    name_away = str(df2[mask_away]["team_long_name"].values[0]) + " @away"

    customdata1 = np.array([[h*1] for h in [y1]])
    customdata2 = np.array([[h*1] for h in [y2]])

    trace1 = go.Bar(y=x, 
                    x=-1 * y1, 
                    orientation="h", 
                    name=name_home,
                    marker={"color": ["teal"]},
                    customdata=customdata1,
                    hovertemplate=
                    "Goals: %{customdata}"
                   )
    trace2 = go.Bar(y=x, 
                    x=y2, 
                    orientation="h", 
                    name=name_away,
                    marker={"color": ["darkblue"]},
                    customdata=customdata2,
                    hovertemplate=
                    "Goals: %{customdata}"
                   )
    
    traces = [trace1, 
              trace2
             ]
    
    fig = go.Figure(traces).update_layout({"barmode": "relative", 
                                     "xaxis": {"range": [-5, 5]},
                                     "title": {"text": title, "x": 0.5},
                                     "legend": {"title": "legend", "orientation": "h", "visible":shlg},
                                    }).update_xaxes({"zerolinewidth":5, "zerolinecolor": "lightgreen", "showticklabels": False
                                    }).update_yaxes({"showticklabels": False})
    return [fig]