#!/usr/bin/python
#
# Plots elevation against forest cover type.

import numpy as np
import matplotlib.pyplot as plt

GREEN = '#009900'

# Read the training data into a numpy array.
data = np.loadtxt('train.csv', delimiter=',', skiprows=1)

# Extract elevation and classes.
elevations = data[:,1]
classes = data[:,55]

# Plot.
plt.plot(elevations, classes, color=GREEN, linestyle='None', marker='o')
plt.axis([1500, 4000, 0, 8])
plt.xlabel('Elevation')
plt.ylabel('Forest Cover Type')

# Output.
# plt.savefig('elevation.png')
plt.show()
