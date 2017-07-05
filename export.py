
# Export functions
from reports import *

def main():
    while True:
        try:
            file_name = input('Give the name of the file: ')
            export = open('export.txt', 'w')
            report1 = count_games(file_name)
            export.write(str(report1)+'\n')
            year = input('Is there a game from a given year? Give a year: ')
            report2 = decide(file_name, year)
            export.write(str(report2)+'\n')
            report3 = get_latest(file_name)
            export.write(str(report3)+'\n')
            genre = input('How many games do we have by genre? Give a genre: ')
            report4 = count_by_genre(file_name, genre)
            export.write(str(report4)+'\n')
            title = input('What is the line number of the given game? Give a title: ')
            while True:
                try:
                    report5 = get_line_number_by_title(file_name, title)
                    break
                except ValueError:
                    title = input('There is no game with this title. Try again: ')
            export.write(str(report5)+'\n')
            report6 = sort_abc(file_name)
            export.write(str(report6)+'\n')
            report7 = get_genres(file_name)
            export.write(str(report7)+'\n')
            try:
                report8 = when_was_top_sold_fps(file_name)
                export.write(str(report8)+'\n')
            except ValueError:
                print('There is no First-person shooter game in the list')
            export.close()
            print('Results are in the export.txt file')
            break
        except FileNotFoundError:
            print('File not found')

main()
