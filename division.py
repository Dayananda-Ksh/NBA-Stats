# This is only for 1 division

from regular_season import create_teams

nba_teams = create_teams()
print("All 30 teams are represented by : \n", nba_teams)


def division(teams):
    division = teams[0:5]
    play = (" ", " ")
    loop = 0
    div_game_played = []
    for x in range(4, 0, -1):
        stages = []
        count = loop + 1
        for y in range(x):
            play = (division[loop], division[count])
            stages.append(play)
            print(play)
            if count < 5:
                count += 1
        loop += 1
        div_game_played.append(stages)
    return div_game_played


def div_num(game_played):
    total = 0
    for stage in game_played:
        total += len(stage) * 4
    return total


div_game_played = division(nba_teams)
div_total = div_num(div_game_played)

print("\nThe game played are: ", div_game_played)

print("\nThe total number of game played in division is ", div_total)