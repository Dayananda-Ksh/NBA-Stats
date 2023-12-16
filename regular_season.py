# program to calculate the total number of games play in nba regular season
# each team plays a total of 82 games
# each team plays 4 games each againts the other 4 theams in their division (So, a total of 16 games)
# each team plays 3 or 4 games each againts the other 10 teams in their conference for a total of 36 games
# each team plays 2 games each each againts the other 15 teams of the non-conference for a total of 30 games.

#creat team names
play = (" ", " ")
play_game = 0
all_teams = []
for n in range(1, 31):
    convert = str(n)
    convert = "team" + convert
    all_teams.append(convert)
print(all_teams)

div_games = 16
div_games_each = 4
division = all_teams[0:5]
count = 0
for x in range(5):
    for team in division:
        current_team = division[x]
        if play_game < div_games_each and team != division[x]:
            play = (current_team, team)
            print(play)
            count +=1
            print(count)