

string = " * FROM game WHERE (team_name_home = 'Boston Celtics' AND team_name_away = 'Miami Heat') OR (team_name_home = 'Miami Heat' AND team_name_away = 'Boston Celtics') AND game_date BETWEEN '2003-01-01' AND '2005-12-31'\n"

print(string.split("\n"))