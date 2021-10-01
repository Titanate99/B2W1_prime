#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 16:21:06 2021

@author: nate_mac
"""
import h5py as h5

# open file in read mode
h5_file = h5.File("particle.h5", 'r')

#look at structure inside:
print(h5_file.keys())

# use dictionary keys to access data
# we can plot/print directly
plt.plot(h5_file['time'][()],h5_file['data'][()])
# the '[()]' operator returns the values inside the data object
print(h5_file['log_entry'][()]

# or we can assign the data to a local variable
t = h5_file['time'][()]
x = h5_file['data'][()]

# close the file
h5_file.close()

# with the local variables, we can keep the data in memory after the file is closed.
plt.plot(t,x,'--')