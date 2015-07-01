from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import svm
import csv
import ingestor
import validator
from sklearn.cluster import KMeans


training_data, training_target, test_data, test_target = ingestor.get_data(
    '../clean_data.csv')


clf = KNeighborsClassifier()

clf.fit(training_data, training_target)

print validator.validate(clf, test_data, test_target)
