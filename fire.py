#!/usr/bin/python
#
# Plots horizontal distance to fire points against forest cover type.

import numpy as np
import matplotlib.pyplot as plt

RED = '#990000'

# Read the training data into a numpy array.
data = np.loadtxt('train.csv', delimiter=',', skiprows=1)

# Extract fire point distance and classes.
fire = data[:,10]
classes = data[:,55]

# Plot.
plt.plot(fire, classes, color=RED, linestyle='None', marker='o')
plt.axis([-500, 7500, 0, 8])
plt.xlabel('Horizontal Distance to Fire Points')
plt.ylabel('Forest Cover Type')

# Output.
# plt.savefig('fire.png')
plt.show()
