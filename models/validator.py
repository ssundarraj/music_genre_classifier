def validate(clf, test_data, test_target):
    cnt = 0

    for i in range(len(test_data)):
        for x in range(len(test_data[i])):
            test_data[i][x] = float(test_data[i][x])

        if(clf.predict(test_data[i]) != test_target[i]):
            cnt += 1

    return 100 * (float(cnt) / float(len(test_data)))
