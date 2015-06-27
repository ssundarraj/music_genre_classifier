import csv
import numpy as np
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


def absHelper(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = abs(data[i][j])
    return data    




def get_data(file_name):
    with open(file_name, 'rb') as csvfile:
        data = []
        target = []
        datareader = csv.reader(csvfile, delimiter=',',)
        for row in datareader:
            row = [abs(float(i)) for i in row]
            data.append(row[:-1])
            target.append(row[-1])


   
    data = np.array(data) 
    data = preprocessing.scale(data)  

    data = absHelper(data)



    data = SelectKBest(chi2, k=15).fit_transform(data,target)
   
    



    data_length = len(data)

    split_factor = int(0.75*data_length)
    training_data = data[:split_factor]



    test_data = data[split_factor+1:]

    training_target = target[:split_factor]
    test_target = target[split_factor + 1:]




    return (training_data,training_target,test_data,test_target)     

