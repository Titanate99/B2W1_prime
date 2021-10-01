#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 16:21:06 2021

@author: nate_mac
"""

#data_array = your fake data from Exercise #1
#time_array = the time array for your fake data

#create a new data file object in write/overwrite mode
hdf_file = h5py.File("myfilename.h5", 'w')

#create a dataset object to hold our fake data
# we can make space as in the tutorial
fake_data = hdf_file.create_dataset("data", data_array.shape, dtype='f')
# and then fill the data object with our data
fake_data[:] = data_array
# it needs to be done using a strategy like this when you are creating datasets that get added to later.

# we could do the same for the time array, but let's take a shortcut
# if your data is all in memory already, you can just write it in one step
t = hdf_file.create_dataset("time", data=time_array)

#the great thing about HDF is that different types of data can be stored together.
description = hdf_file.create_dataset("log_entry", data="Description of relevant stuff.  If it's attached to the data itself, it should probably be included as an attribute (see tutorial)")

#close the file
hdf_file.close()