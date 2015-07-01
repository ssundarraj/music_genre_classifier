import matplotlib.pyplot as plt
from pandas import DataFrame
import sys
import csv
import numpy


def get_data():
    data = numpy.genfromtxt('../clean_data.csv', delimiter=',')
    return data


def plot():
    data = get_data()
    # remove hardcoding of this \/
    cols = [
        'tempo', 'scale1', 'scale2', 'scale3',
        'scale4', 'scale5', 'mfcc1', 'mfcc2',
        'mfcc3', 'mfcc4', 'mfcc5', 'mfcc6',
        'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10',
        'mfcc11', 'mfcc12', 'mfcc13',  'genre']

    df = DataFrame(data, columns=cols)
    for a in cols[:-1]:
        df.plot(kind='scatter', x=a, y='genre')
    plt.show()

if __name__ == '__main__':
    plot()
