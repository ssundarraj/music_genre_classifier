from sklearn import svm
from sklearn.ensemble import ExtraTreesClassifier
import csv
import ingestor
import validator

training_data,training_target,test_data,test_target = ingestor.get_data('../clean_data.csv')




clf = svm.SVC()
clf.fit(training_data,training_target)

print validator.validate(clf,test_data,test_target)




