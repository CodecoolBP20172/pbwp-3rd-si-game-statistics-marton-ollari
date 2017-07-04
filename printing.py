
# Printing functions
def open_file(file_name):
    with open('game_stat.txt') as f:
        game_list = f.read().splitlines()
        for i in range(len(game_list)):
            game_list[i] = game_list[i].split('\t')
        return game_list

game_list = open_file('game_stat.txt')
fps = []
for i in range(len(game_list)):
    if game_list[i][3] == 'First-person shooter':
        fps.append(game_list[i])
print(fps)
fps = sorted(fps, key=lambda fps: float(fps[1]))
print(fps)
print(fps[-1][2])