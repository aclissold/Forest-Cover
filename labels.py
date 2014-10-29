#!/usr/bin/env python
#
# Prints labels and their indices.

import numpy as np

labels = np.genfromtxt('train.csv', delimiter=',', dtype='str')[0]

for i in range(labels.size):
    print('{0}: {1}'.format(str(i), labels[i]))
