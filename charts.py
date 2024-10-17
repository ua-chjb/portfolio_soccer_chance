import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

home = pd.read_csv("https://raw.githubusercontent.com/ua-chjb/soccer_chance/refs/heads/main/assets/data/home.csv")
away = pd.read_csv("https://raw.githubusercontent.com/ua-chjb/soccer_chance/refs/heads/main/assets/data/away.csv")

cols = ['buildUpPlaySpeed', 'buildUpPlayDribbling', 'buildUpPlayPassing', 
        'chanceCreationPassing', 'chanceCreationCrossing', 'chanceCreationShooting', 
        'defencePressure', 'defenceAggression', 'defenceTeamWidth']

home = home.sort_values(by=["buildUpPlaySpeed"], ascending=False)
away = away.sort_values(by=["buildUpPlaySpeed"], ascending=False)

############################# chart 1 ####################################
def star_chart(df, mask_team, color, cols=cols):

    df1 = df[mask_team]
    
    score_name = df1[cols].columns
    score_attr = df1[cols].values.flatten()

    return px.line_polar(r=score_attr, theta=score_name, line_close=True, markers=True, symbol_sequence=["diamond"], color_discrete_sequence=[color], range_r=[0, 80])


############################# chart 2 ####################################

import plotly.graph_objs as go

def score_output(df1, df2, mask1, mask2):

    x =["A"]
    
    y1 = home[mask1]["home_team_goal"].values
    y2 = away[mask2]["away_team_goal"].values

    name_home = str(home[mask1]["team_long_name"].values[0]) + "@ home"
    name_away = str(away[mask2]["team_long_name"].values[0]) + "@ away"

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
                                     "title": {"text": "goals, home v away", "x": 0.5},
                                     "legend": {"title": "legend", "orientation": "h",},
                                    }).update_xaxes({"zerolinewidth":5, "zerolinecolor": "lightgreen", "showticklabels": False
                                    }).update_yaxes({"showticklabels": False})
    return fig