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


def star_chart(df, value1, value2, value3, color="darkblue", cols=cols):

    country_mask = ( home["country_name"] == value1 ) 
    league_mask = ( home["league_name"] == value2 )
    team_mask = ( home["team_long_name"] == value3 ) 

    df1 = df[country_mask & league_mask & team_mask]
    
    score_name = df1[cols].columns
    score_attr = df1[cols].values.flatten()

    return px.line_polar(r=score_attr, theta=score_name, line_close=True, markers=True, symbol_sequence=["diamond"], color_discrete_sequence=[color], range_r=[0, 80])

# star_chart(home, value1, value2, value3, "darkblue", cols)


def score_output(team1):

    mask1 = ( home["team_long_name"]==team1 )
    mask2 = ( away["team_long_name"]==team1 )

    x =["A"]
    y1 = home[mask1]["home_team_goal"]
    y2 = away[mask2]["away_team_goal"]

    customdata1 = np.array([[h*1] for h in [y1]])
    customdata2 = np.array([[h*1] for h in [y2]])
    
    trace1 = go.Bar(y=x, 
                    x=-y1, 
                    orientation="h", 
                    name="home", 
                    marker={"color": ["teal"]},
                    customdata=customdata1,
                    hovertemplate=
                    "%{customdata1} goals"
                   )
    trace2 = go.Bar(y=x, 
                    x=y2, 
                    orientation="h", 
                    name="away", 
                    marker={"color": ["darkblue"]},
                    customdata=customdata2,
                    hovertemplate=
                    "%{customdata2}"
                   )
    
    traces = [trace1, trace2]
    
    fig = go.Figure(traces).update_layout({"barmode": "relative", 
                                     "xaxis": {"range": [((np.array([y1, y2]).max()*-1)-2), np.array([y1, y2]).max()+2]},
                                     "title": {"text": "goals, home v away", "x": 0.5},
                                     "legend": {"title": "legend", "orientation": "h",},
                                    }).update_xaxes({"zerolinewidth":5, "zerolinecolor": "lightgreen", "showticklabels": False
                                    }).update_yaxes({"showticklabels": False})
    return fig


def scattersimple(soccer_h):
    return px.scatter(soccer_h, x=cols[-1], y=cols[-3]) 