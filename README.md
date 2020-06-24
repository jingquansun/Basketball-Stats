# Basketball Team Stats Tool
In this project you will be writing a program that reads from the "constants" data (`PLAYERS` and `TEAMS`) in `constants.py`. This data will need to be translated into a new collection of your choosing and the fields need to be changed to something that makes more sense for Python to do its comparisons.

The number of players that should be on each team, a copy of the players and teams, a balanced team list, and an experienced and not experienced list are set as variables. 

In dunder main, there are the methods clean_data(), split_experience(), balance_teams(), and start_menu().

Helper methods include team_menu() and team_stats() which shows the options for the teams.

team_stats_format(team) provides the format that the team stats should be presented in. 

exp_of_players(team) finds the number of experienced and unexperienced players on the given team. 

avg_height(team) finds the average height of all the players on the given team. 

player_guardians(team) returns the guardians for the players for the given team, in a string. 

Finally, continue_stats() gives the option of whether the user wants to continue with the program.
