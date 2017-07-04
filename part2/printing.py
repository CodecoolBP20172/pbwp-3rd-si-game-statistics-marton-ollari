
# Printing functions
def open_file(file_name):
    with open(file_name) as f:
        game_list = f.read().splitlines()
        for i in range(len(game_list)):
            game_list[i] = game_list[i].split('\t')
        return game_list

game_list = open_file('game_stat.txt')
name = 'Half-Life 2'
return_list = []
for i in range(len(game_list)):
    if name == game_list[i][0]:
        return_list.extend([game_list[i][0],float(game_list[i][1]),int(game_list[i][2]),
        game_list[i][3],game_list[i][4]])
        print(return_list)