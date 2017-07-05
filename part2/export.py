
# Export functions
from reports import *


def main():
    while True:
        try:
            file_name = input('Give the name of the file: ')
            export = open('export2.txt', 'w')
            report1 = get_most_played(file_name)
            export.write(str(report1)+'\n')
            report2 = sum_sold(file_name)
            export.write(str(report2)+'\n')
            report3 = get_selling_avg(file_name)
            export.write(str(report3)+'\n')
            report4 = count_longest_title(file_name)
            export.write(str(report4)+'\n')
            report5 = get_date_avg(file_name)
            export.write(str(report5)+'\n')
            title = input('What properties has a game? Give a title: ')
            while True:
                try:
                    report6 = get_game(file_name, title)
                    break
                except ValueError:
                    title = input('There is no game with this title. Try again: ')
            export.write(str(report6)+'\n')
            report7 = count_grouped_by_genre(file_name)
            export.write(str(report7)+'\n')
            report8 = get_date_ordered(file_name)
            export.write(str(report8)+'\n')
            export.close()
            print('Results are in the export2.txt file')
            break
        except FileNotFoundError:
            print('File not found')

main()
