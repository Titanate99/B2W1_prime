
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import h5py as h5
import matplotlib.pyplot as plt
from itertools import product, combinations

from mpl_toolkits.mplot3d import Axes3D

a = np.load("test.npy")


# open file in read mode
h5_file = h5.File("particle.h5", 'r')

print(h5_file.keys())



r = h5_file['r'][()]



print(r)


h5_file.close()

ax = plt.gcf().add_subplot(111, projection='3d')

ax.plot(r[:,0],r[:,1],r[:,2])





