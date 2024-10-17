import pandas as pd

home = pd.read_csv("https://raw.githubusercontent.com/ua-chjb/soccer_chance/refs/heads/main/assets/data/home.csv")
away = pd.read_csv("https://raw.githubusercontent.com/ua-chjb/soccer_chance/refs/heads/main/assets/data/away.csv")

cols = ['buildUpPlaySpeed', 'buildUpPlayDribbling', 'buildUpPlayPassing', 
        'chanceCreationPassing', 'chanceCreationCrossing', 'chanceCreationShooting', 
        'defencePressure', 'defenceAggression', 'defenceTeamWidth']

home = home.sort_values(by=["buildUpPlaySpeed"], ascending=False)
away = away.sort_values(by=["buildUpPlaySpeed"], ascending=False)
