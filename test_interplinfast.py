# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 10:20:05 2022

@author: Gerrit Nowald
"""

import numpy as np
import matplotlib.pyplot as plt

import math_functions as mf

#--------------------------------------------------------------------------
# Variables

Nx  = 5
Nxi = 3

x = np.linspace(0,800,Nx)
# y = x**2
# y = x**3/1e3
y = np.column_stack(( x**2, x**3/1e3))

xi = np.linspace(-50,900,Nxi)

#--------------------------------------------------------------------------
# Interpolation

# yi = mf.interplinfast(x,y,xi)

m  = mf.calc_slope(x,y)
yi = mf.interplinfast(x,y,xi,m)






# Ntest = 1e4

# T = zeros(Ntest,2)
# for num=1:Ntest
#     tic
#     yi = interp1linfast(x,y,xi)
# #     yi = interp1linfast(x,y,xi,m)
#     T(num,1)=toc
    
#     tic
#     yi = interp1(x,y,xi,'linear','extrap')
#     T(num,2)=toc

# mean(T)/min(mean(T))

#--------------------------------------------------------------------------
# plot
plt.close('all')

plt.figure()
plt.plot(x,y,'--+')
plt.plot(xi,yi,'o')