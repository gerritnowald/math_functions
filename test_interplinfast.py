# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 10:20:05 2022

@author: Gerrit Nowald
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------

# def interp1linfast(x,y,xi,m):
# fast 1D linear inter- and extrapolation (no input checking)
#
# Outputs:
# - yi: interpolated values, matrix [p x n], corresponding to xi
#       interpolation is performed for each column
#
# Inputs:
# - x:  x-data, column vector [m x 1], monotonically increasing
# - y:  y-data, matrix [m x n], corresponding to x
# - xi: x-values to be interpolated, column vector [p x 1], in any order
# - m:  slopes of line segments, can be computed in advance (optional)
#
# uses the approach given by Loren Shure (The MathWorks) in http://blogs.mathworks.com/loren/2008/08/25/piecewise-linear-interpolation/
# Acknowledgement: Jose M. Mier, https://de.mathworks.com/matlabcentral/fileexchange/43325-quicker-1d-linear-interpolation-interp1qr
#
# =========================================================================


# return yi








#--------------------------------------------------------------------------
# Variables

Nx  = 5
Nxi = 3

x = np.linspace(0,800,Nx)
y = x**2
# y = x**3/1e3
# y = np.column_stack(( x**2, x**3/1e3))

xi = np.linspace(-50,900,Nxi)

#--------------------------------------------------------------------------
# Interpolation


# slope of line segments
m  = np.diff(y)/np.diff(x)

# find interval
A = xi > x[:, np.newaxis]
ind = np.sum(A, axis=0) - 1

# avoid index smaller 0 or larger than len(x)-2
ind = np.maximum(ind, 0)
ind = np.minimum(ind, len(x)-2)

# inter- & extrapolation
yi = m[ind]*(xi-x[ind]) + y[ind]






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