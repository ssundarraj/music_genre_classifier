import collections
import csv
import sys


def clean_data(file_name, op_file_name):
    genres = []
    with open(sys.argv[1], 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',',)
        for row in datareader:
            genres.append(row[-1])

    ignored_genres = ['Classical', 'Jazz', 'Traditional', 'Soundtrack', 'Other']
    for i in ignored_genres:
        genres.remove(i)
    genres = list(set(genres))
    print genres
    genre_dict = collections.defaultdict().fromkeys(genres, 0)

    with open(file_name, 'rb') as csvfile, open(op_file_name, 'wb') as cleancsvfile:
        datareader = csv.reader(csvfile, delimiter=',',)
        datawriter = csv.writer(cleancsvfile, delimiter=',')
        for row in datareader:


            if 'nan' in row or row[-1] in ignored_genres:
                continue
            genre_dict[row[-1]] += 1
            row[-1] = genres.index(row[-1]) + 1
            # print row

            row = [abs(float(i)) for i in row]
            datawriter.writerow(row)

    print genre_dict


if __name__ == '__main__':
    clean_data(sys.argv[1], 'clean_data.csv')
