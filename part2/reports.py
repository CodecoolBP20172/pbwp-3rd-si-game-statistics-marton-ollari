
# Report functions
def open_file(file_name):
    with open(file_name) as f:
        game_list = f.read().splitlines()
        for i in range(len(game_list)):
            game_list[i] = game_list[i].split('\t')
        return game_list

def get_most_played(file_name):
    game_list = open_file(file_name)
    game_list = sorted(game_list, key=lambda game_list: float(game_list[1]))
    return game_list[-1][0]

def sum_sold(file_name):
    game_list = open_file(file_name)
    sum = 0
    for i in range(len(game_list)):
        sum += float(game_list[i][1])
    return sum

def get_selling_avg(file_name):
    game_list = open_file(file_name)
    sum = sum_sold(file_name)
    return sum/len(game_list)

def count_longest_title(file_name):
    game_list = open_file(file_name)
    long_title = 0
    for i in range(len(game_list)):
        x = len(game_list[i][0])
        if x > long_title:
            long_title = x
    return long_title

def get_date_avg(file_name):
    game_list = open_file(file_name)
    sum_date = 0
    for i in range(len(game_list)):
        sum_date += int(game_list[i][2])
    return round(sum_date/len(game_list))

def get_game(file_name, title):
    game_list = open_file(file_name)
    return_list = []
    for i in range(len(game_list)):
        if title == game_list[i][0]:
            return_list.extend([game_list[i][0],float(game_list[i][1]),
            int(game_list[i][2]),game_list[i][3],game_list[i][4]])
            return return_list
    raise ValueError

def count_grouped_by_genre(file_name):
    game_list = open_file(file_name)
    return_dict = {}
    for i in range(len(game_list)):
        if game_list[i][3] not in return_dict:
            return_dict[game_list[i][3]] = 1
        else:
            return_dict[game_list[i][3]] += 1
    return return_dict
def get_date_ordered(file_name):
    game_list = open_file(file_name)
    return_list = []
    game_list = sorted(game_list, key=lambda game_list: game_list[2])
    game_list.reverse()
    for a in range(len(game_list)):
        for i in range(len(game_list)-1):
            if game_list[i][2] == game_list[i+1][2]:
                if game_list[i][0] > game_list[i+1][0]:
                    temp = game_list[i]
                    game_list[i] = game_list[i+1]
                    game_list[i+1] = temp
    for i in range(len(game_list)):
        return_list.append(game_list[i][0])
    return return_list
