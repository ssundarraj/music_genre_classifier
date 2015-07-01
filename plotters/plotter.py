import collections
import sys
import csv
import numpy
import matplotlib.pyplot as plt
from pandas import DataFrame
from pandas import Series


def get_data():
    data = numpy.genfromtxt('../clean_data.csv', delimiter=',')
    return data


def correlation_plot():
    data = get_data()
    # remove hardcoding of this \/
    cols = [
        'tempo', 'scale1', 'scale2', 'scale3',
        'scale4', 'scale5', 'mfcc1', 'mfcc2',
        'mfcc3', 'mfcc4', 'mfcc5', 'mfcc6',
        'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10',
        'mfcc11', 'mfcc12', 'mfcc13',  'genre']

    df = DataFrame(data, columns=cols)
    for col in cols[:-1]:
        df.plot(kind='scatter', x=col, y='genre')
    plt.show()


def data_distribution_chart():
    data = get_data()
    genres = ['Urban', 'Classical', 'Electronica', 'Jazz', 'Pop', 'Soundtrack', 'Alternative & Punk', 'Rock', 'Other']
    genre_dict = collections.defaultdict().fromkeys(genres, 0)
    for row in data:
        genre_dict[genres[int(row[-1])]] += 1
    print genre_dict
    data = numpy.array(genre_dict.values())
    series = Series(data, index=genres, name='genre_distribution')
    series.plot(kind='pie', figsize=(6, 6))
    plt.show()


if __name__ == '__main__':
    data_distribution_chart()
