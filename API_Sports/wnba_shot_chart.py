# Uses the nba_shot_chart as a template
# Queries wnba shot data using pyball wnba_shots

# Imporing all modules from nba_shot_chart
from nba_api.stats.endpoints import shotchartdetail
import json
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# nba_api
from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import PlayerCareerStats

# wnba specific 
from py_ball import wnba_shots #what else is here?
from py_ball import wnba_salaries
from py_ball import wnba_shots

# Can I first get all of this data in json format, that way I can manipulate in the same way
# Use API call to get data and save to my github
# Replicate this 
## teams = json.loads(requests.get('https://raw.githubusercontent.com/bttmly/nba/master/data/teams.json').text) ## I have this on my github 
teams = json.loads(requests.get('https://raw.githubusercontent.com/websteralycia/wnba/main/get_wnba_teams.json').text)
## players = json.loads(requests.get('https://raw.githubusercontent.com/bttmly/nba/master/data/players.json').text) ## need all players 

print(type(teams)) # it's a dictionary right now, needs to be a list if I want to use it in the same way 


