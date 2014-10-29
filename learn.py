#!/usr/bin/python
#
# Classification of the forest cover dataset.

from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler

from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier

names = ['Naive Bayes', '1-NN', '4-NN', '7-NN', 'AdaBoost']

classifiers = [
    GaussianNB(),
    KNeighborsClassifier(1),
    KNeighborsClassifier(4),
    KNeighborsClassifier(7),
    AdaBoostClassifier(),
    ]

# Load the training data, test data, and class labels.
print('Loading data...')
X_train = np.loadtxt('train.csv', delimiter=',', skiprows=1)
X_test = np.loadtxt('test.csv', delimiter=',', skiprows=1)
y = X_train[:,-1]

# Scale the data.
X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

# Remove id and class label columns.
X_train = np.delete(X_train, [0, 55], 1)
X_test = np.delete(X_test, 0, 1)

print('Classifying...')
for name, clf in zip(names, classifiers):
    clf.fit(X_train, y)
    print(name, 'accuracy on training data:', clf.score(X_train, y))
    Z = clf.predict(X_test)
    print(name + ' test data labels:', Z)

print('Done.')
