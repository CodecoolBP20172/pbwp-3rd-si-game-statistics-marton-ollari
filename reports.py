
# Report functions
def open_file(file_name):
    with open(file_name) as f:
        game_list = f.read().splitlines()
        for i in range(len(game_list)):
            game_list[i] = game_list[i].split('\t')
        return game_list

def count_games(file_name):
    game_list = open_file(file_name)
    return (len(game_list))

def decide(file_name, year):
    game_list = open_file(file_name)
    for i in range(len(game_list)):
        if str(year) in game_list[i][2]:
            return True
    return False

def get_latest(file_name):
    game_list = open_file(file_name)
    game_list = sorted(game_list, key=lambda game_list: game_list[2])
    for i in range(len(game_list)):
        if game_list[-1][2] in game_list[i]:
            return game_list[i][0]

def count_by_genre(file_name, genre):
    game_list = open_file(file_name)
    count = 0
    for i in range(len(game_list)):
        if game_list[i][3] == genre:
            count += 1
    return count

def get_line_number_by_title(file_name, title):
    game_list = open_file(file_name)
    for i in range(len(game_list)):
        if title == game_list[i][0]:
            return i+1
    raise ValueError

def sort_abc(file_name):
    game_list = open_file(file_name)
    names = []
    for i in range(len(game_list)):
        names.append(game_list[i][0])
    for i in range(len(names)):
        for i in range(len(names)-1):
            if names[i] > names[i+1]:
                temp = names[i+1]
                names[i+1] = names[i]
                names[i] = temp
    return names

def get_genres(file_name):
    game_list = open_file(file_name)
    genres = []
    for i in range(len(game_list)):
        genres.append(game_list[i][3])
    genres = list(set(genres))
    genres.sort()
    for a in range(len(genres)):
        for i in range(len(genres)-1):
            if genres[i][0] == genres[i+1][0]:
                if genres[i][1].lower() > genres[i+1][1].lower():
                    temp = genres[i+1]
                    genres[i+1] = genres[i]
                    genres[i] = temp
    return genres


def when_was_top_sold_fps(file_name):
    game_list = open_file(file_name)
    fps = []
    for i in range(len(game_list)):
        if game_list[i][3] == 'First-person shooter':
            fps.append(game_list[i])
    if fps == []:
        raise ValueError
    fps = sorted(fps, key=lambda fps: float(fps[1]))
    return int(fps[-1][2])