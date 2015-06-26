import csv
import numpy as np


def get_data(file_name):
    with open(file_name, 'rb') as csvfile:
        data = []
        target = []
        datareader = csv.reader(csvfile, delimiter=',',)
        for row in datareader:
            data.append(row[:-1])

            target.append(row[-1])

    data_length = len(data)

    split_factor = int(0.9 * data_length)
    training_data = data[:split_factor]
    test_data = data[split_factor + 1:]
    training_target = target[:split_factor]
    test_target = target[split_factor + 1:]

    return (training_data, training_target, test_data, test_target)
