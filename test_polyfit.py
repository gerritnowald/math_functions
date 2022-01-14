# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:57:37 2022

@author: Gerrit Nowald
"""

import numpy as np
import matplotlib.pyplot as plt

import math_functions as mf
    

N = 2   # polynomial order


# test data 
x = np.linspace(-2,2,100)
y = np.cos(x)
y += 0.2*(np.random.rand(np.shape(x)[0])-0.5)   # adding noise


# calculation
p, yf = mf.polyfit(x,y,N)


# plot
plt.close('all')

plt.figure()
plt.plot(x,y,'.')   # data
plt.plot(x,yf,'k')  # fitted polynomial