# program to calculate the total number of games play in nba regular season
# each team plays a total of 82 games
# each team plays 4 games each againts the other 4 theams in their division (So, a total of 16 games)
# each team plays 3 or 4 games each againts the other 10 teams in their conference for a total of 36 games
# each team plays 2 games each each againts the other 15 teams of the non-conference for a total of 30 games.

#creat team names
def create_teams():
    teams = []
    for i in range(1, 31):
        convert = str(i)
        convert = "team" + convert
        teams.append(convert)
    return teams

