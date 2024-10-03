player_data = open('first_tour.txt', 'r')
string_player = []
second_player = []
for index in player_data:
    string = index.rstrip()
    string_player.append(string)
players = string_player[1:]
for player in players:
    player_search = player.split()
    for index_player in player_search:
        if index_player.isdigit():
            if index_player > string_player[0]:
                second_player.append(player_search)
player_data.close()

second_round = open('second_tour.txt', 'w')
number_player = second_round.write(str(len(second_player)))
for index in second_player:
    slash = second_round.write('\n')
    name = index[1][0] + '.', index[0], index[2]
    past_player = ' '.join(name)
    next_plater = second_round.write(past_player)
second_round.close()
