
import copy
from constants import PLAYERS, TEAMS

NUM_PLAYERS_TEAM = len(PLAYERS) / len(TEAMS)
players_copy = copy.deepcopy(PLAYERS)
teams_copy = copy.deepcopy(TEAMS)
exp = []
no_exp = []

def clean_data():
  for player in players_copy:
    if player.get('experience') == 'NO':
      player['experience'] = False
    else:
      player['experience'] = True
    player['height'] = int(player['height'][:2])
    player['guardians'] = player['guardians'].split(" and ")

def balance_teams():
  balanced_teams = {key: [] for key in TEAMS}
  i = 0
  while len(balanced_teams.get('Panthers')) < NUM_PLAYERS_TEAM:
    player_exp = exp[i]
    player_no_exp = no_exp[i]
    for key, values in balanced_teams.items():
      items = {key:list.append(player_exp)}
      items = {key:list.append(player_no_exp)}
      i += 1
  return balanced_teams

def split_experience():
  clean_data()
  for player in players_copy:
    if player.get('experience') == True:
      exp.append(player)
    else:
      no_exp.append(player)
          
balance_teams()


#if __name__ == "__main__":
 
  
  