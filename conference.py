# This is only for 1 division 
from regular_season import create_teams


nba_teams = create_teams()


def conference(teams):
    conference = teams[0:15]
    play = (" ", " ")
    loop = 0
    conf_game_played = []
    myList = [10, 10, 10, 10, 10]
    for x in myList:
        stages = []
        count = 5
        for y in range(x):
            play = (conference[loop], conference[count])
            stages.append(play)
            print(play)
            if count < 15:
                count += 1
        loop += 1
        conf_game_played.append(stages)
    return conf_game_played


def conf_num(game_played):
    total = 0
    for stage in game_played:
        total += len(stage) * 3
    return total

game_played = conference(nba_teams)
conf_total = conf_num(game_played)
print("The games played are: ", game_played)

print("\n The total number of games are : ", conf_total)


