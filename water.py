#!/usr/bin/python
#
# Plots vertical and horizontal distance to water against forest cover type.

import numpy as np
import matplotlib.pyplot as plt

BLUE = '#000099'

# Read the training data into a numpy array.
data = np.loadtxt('train.csv', delimiter=',', skiprows=1)

# Extract elevation and classes.
horiz = data[:,4]
vert = data[:,5]
classes = data[:,55]

# Plot.
plt.subplot(211)
plt.plot(horiz, classes, color=BLUE, linestyle='None', marker='o')
plt.axis([-100, 1400, 0, 8])
plt.xlabel(r'Horizontal Distance to $\mathrm{H_2O}$')
plt.ylabel('Forest Cover Type')

plt.subplot(212)
plt.plot(vert, classes, color=BLUE, linestyle='None', marker='o')
plt.axis([-200, 600, 0, 8])
plt.xlabel(r'Vertical Distance to $\mathrm{H_2O}$')
plt.ylabel('Forest Cover Type')

# Output.
plt.tight_layout()
# plt.savefig('water.png')
plt.show()
