#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 16:24:28 2021

@author: nate_mac
"""

import numpy as np

import matplotlib.pyplot as plt

import random as r

time = np.arange(0,0.25,.001)

amp = np.sin(time *  120 * np.pi)

for i in range(len(amp)):
    rand = r.randint(1,5)
    if rand == 5:
        noise = np.random.normal(loc = 0, scale = .7, size = (1))
        amp[i] = noise
        



#   print(amp)

plt.plot(time,amp)
np.save('test', (time,amp))

a = np.load("test.npy")
print(a)