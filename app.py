
import copy
from constants import PLAYERS, TEAMS

NUM_PLAYERS_TEAM = len(PLAYERS) / len(TEAMS)
players_copy = copy.deepcopy(PLAYERS)
teams_copy = copy.deepcopy(TEAMS)
balanced_teams = {key: [] for key in TEAMS}
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
    
def split_experience():
  for player in players_copy:
    if player.get('experience') == True:
      exp.append(player)
    else:
      no_exp.append(player)

def balance_teams():
  i = 0
  while len(balanced_teams.get('Panthers')) < NUM_PLAYERS_TEAM:
    for key, values in balanced_teams.items():
      player_exp = exp[i]
      player_no_exp = no_exp[i]
      items = {key:values.append(player_exp)}
      items = {key:values.append(player_no_exp)}
      i += 1
  for keys, values in balanced_teams.items():
    if len(values) > NUM_PLAYERS_TEAM:
      items = {key:values.pop()}
    
def start_menu():
  print("BASKETBALL TEAM STATS TOOL")
  print("---MENU--- \n\nHere are your choices:\n1) Display Team Stats\n2) Quit")
  option = input("Enter an option (1 or 2):  ")
  while True:
    if option == "1":
      team_menu()
      break
    if option == "2":
      print("Thank you, goodbye!")
      break
    else:
      option = input("This is not a valid option, please pick 1 or 2:  ")

def team_menu():
  print("\nThe teams are:\n1) Panthers\n2) Bandits\n3) Warriors")
  option = input("Enter an option (1, 2, or 3):   ")
  while True:
    if option == "1":
      team_stats(1)
      break
    if option == "2":
      team_stats(2)
      break
    if option == "3":
      team_stats(3)
      break
    else:
      option = input("This is not a valid option, please pick 1, 2, or 3:  ")

def team_stats(option):
  if option == 1:
    team_stats_format("Panthers")
  if option == 2:
    team_stats_format("Bandits")
  if option == 3:
    team_stats_format("Warriors")
  
def team_stats_format(team):
  print("Team: {} Stats".format(team))
  print("-" * 10)
  print("Total players: " + str(NUM_PLAYERS_TEAM))
  print("Players on team:")
  player_list = []
  for player in balanced_teams.get(team):
    player_list.append(player.get('name'))
  print(", ".join(player_list))
  
  exp_of_players(team)
  avg_height(team)
  player_guardians(team)
  
  option = input("\n\n Would you like to continue? (Y/N):  ")
  while True:
    if option.lower() == "y":
      start_menu()
      break
    if option.lower() == "n":
      print("Thank you! Goodbye.")
      break
    else:
      option = input("Sorry, please choose Y/N:   ")
      
def exp_of_players(team):
  experienced = 0
  not_experienced = 0
  for player in balanced_teams.get(team):
    if player.get('experience') == True:
      experienced += 1
    else:
      not_experienced += 1
  print("There are {} experienced players and {} not experienced players.\n".format(experienced, not_experienced))
  
def avg_height(team):
  total_height = 0
  for player in balanced_teams.get(team):
    total_height += player.get('height')
  avg_height = total_height / NUM_PLAYERS_TEAM
  print("The average height on this team is {} inches\n".format(round(float(avg_height))))

def player_guardians(team):
  guardians = []
  for player in balanced_teams.get(team):
    guardians += player.get('guardians')
  all_guardians = ", ".join(guardians)
  print("The guardians on this team are: {}.".format(all_guardians))

if __name__ == "__main__":
  clean_data()
  split_experience()
  balance_teams()
  start_menu()
  
  