import numpy as np
from matplotlib import pyplot as plt

dataSet = {'Traditional': 1, 'Urban': 136, 'Alternative & Punk': 169, 'Classical': 4, 'Rock': 88, 'Electronica': 59, 'Jazz': 4, 'Other': 33, 'Soundtrack': 7, 'Pop': 135}
fig = plt.figure()

width = 0.75
ind = np.arange(len(dataSet.values()))
plt.bar(ind, dataSet.values())
plt.xticks(ind + width / 2, dataSet.keys())

fig.autofmt_xdate()

plt.savefig("figure.jpg")