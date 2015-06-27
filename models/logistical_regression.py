from sklearn import linear_model

import csv
import ingestor
import validator






training_data,training_target,test_data,test_target = ingestor.get_data('../clean_data.csv')

lr=linear_model.LogisticRegression()

lr.fit(training_data,training_target)


print validator.validate(lr,test_data,test_target)


