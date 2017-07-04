
# Export functions
from reports import *

#def main():
try:
    file_name = input('Give the name of the file: ')
    export = open('export.txt', 'w')
    report1 = count_games(file_name)
    export.write(str(report1)+'\n')
    year = input('Give a year: ') 
    report2 = decide(file_name, '1999')
    export.write(str(report2)+'\n')
    report3 = get_latest(file_name)
    export.write(str(report3)+'\n')
    genre = input('Give a genre: ')
    report4 = count_by_genre(file_name, genre)
    export.write(str(report4)+'\n')
    title = input('Give a title: ')
    report5 = get_line_number_by_title(file_name, title)
    export.write(str(report5)+'\n')
    report6 = sort_abc(file_name)
    export.write(str(report6)+'\n')
    report7 = get_genres(file_name)
    export.write(str(report7)+'\n')
    report8 = when_was_top_sold_fps(file_name)
    export.write(str(report8)+'\n')
    export.close()
except ValueError:
    pass

