import csv
import sys


def clean_data(file_name, op_file_name):
    genres = []
    with open(sys.argv[1], 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',',)
        for row in datareader:
            genres.append(row[-1])

    genres = list(set(genres))
    print genres

    with open(file_name, 'rb') as csvfile, open(op_file_name, 'wb') as cleancsvfile:
        datareader = csv.reader(csvfile, delimiter=',',)
        datawriter = csv.writer(cleancsvfile, delimiter=',')
        for row in datareader:
            row[-1] = genres.index(row[-1]) + 1
            print row
            datawriter.writerow(row)

if __name__ == '__main__':
    clean_data(sys.argv[1], 'clean_data.csv')
