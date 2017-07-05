
# Printing functions


def open_file(file_name):
    with open(file_name) as f:
        game_list = f.read().splitlines()
        for i in range(len(game_list)):
            game_list[i] = game_list[i].split('\t')
        return game_list


def count_games(file_name):
    game_list = open_file(file_name)
    print(len(game_list))


def decide(file_name, year):
    game_list = open_file(file_name)
    for i in range(len(game_list)):
        if str(year) in game_list[i][2]:
            print(True)
            return
    print(False)


def get_latest(file_name):
    game_list = open_file(file_name)
    game_list = sorted(game_list, key=lambda game_list: game_list[2])
    for i in range(len(game_list)):
        if game_list[-1][2] in game_list[i]:
            print(game_list[i][0])


def count_by_genre(file_name, genre):
    game_list = open_file(file_name)
    count = 0
    for i in range(len(game_list)):
        if game_list[i][3] == genre:
            count += 1
    print(count)


def get_line_number_by_title(file_name, title):
    game_list = open_file(file_name)
    for i in range(len(game_list)):
        if title == game_list[i][0]:
            print(i+1)
            return
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
    print(names)


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
    print(genres)


def when_was_top_sold_fps(file_name):
    game_list = open_file(file_name)
    fps = []
    for i in range(len(game_list)):
        if game_list[i][3] == 'First-person shooter':
            fps.append(game_list[i])
    if fps == []:
        raise ValueError
    fps = sorted(fps, key=lambda fps: float(fps[1]))
    print(int(fps[-1][2]))


def main():
    file_name = 'game_stat.txt'
    count_games(file_name)
    decide(file_name, 2012)
    get_latest(file_name)
    count_by_genre(file_name, 'RPG')
    get_line_number_by_title(file_name, 'Diablo III')
    sort_abc(file_name)
    get_genres(file_name)
    when_was_top_sold_fps(file_name)

main()
