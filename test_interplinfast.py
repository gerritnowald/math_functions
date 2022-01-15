# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 10:20:05 2022

@author: Gerrit Nowald
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------

def calc_slope(x,y):
    """
    slope of line segments for 1D linear inter- and extrapolation
    - x:  x-data vector [m], monotonically increasing
    - y:  y-data matrix [m x n], corresponding to x
          interpolation is performed for each column
    """
    if y.ndim ==1:
        m  = np.diff(y)/np.diff(x)
    elif y.ndim ==2:
        m  = np.diff(y,axis=0)/np.diff(x)[:, np.newaxis]
    return m

def interplinfast(x,y,xi,m=None):
    """
    fast 1D linear inter- and extrapolation
    - x:  x-data vector [m], monotonically increasing
    - y:  y-data matrix [m x n], corresponding to x
          interpolation is performed for each column
    - xi: x-value vector [p] to be interpolated, , in any order
    - m:  slopes of line segments, can be computed in advance (optional)
    uses the approach given by Loren Shure (The MathWorks) in http://blogs.mathworks.com/loren/2008/08/25/piecewise-linear-interpolation/
    Acknowledgement: Jose M. Mier, https://de.mathworks.com/matlabcentral/fileexchange/43325-quicker-1d-linear-interpolation-interp1qr
    """
    if m.all()==None:
        m = calc_slope(x,y)     # slope of line segments
    
    ind = np.sum( xi > x[:, np.newaxis], axis=0) - 1    # find interval
    ind = np.maximum(ind, 0)            # avoid index smaller 0
    ind = np.minimum(ind, len(x)-2)     # avoid index larger than len(x)-2
    
    # inter- & extrapolation
    if y.ndim ==1:
        yi = m[ind]*(xi-x[ind]) + y[ind]
    elif y.ndim ==2:
        yi = m[ind,:]*(xi[:, np.newaxis]-x[ind, np.newaxis]) + y[ind,:]
    return yi   # interpolated values matrix [p x n], corresponding to xi

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

# yi = interplinfast(x,y,xi)

m = calc_slope(x,y)
yi = interplinfast(x,y,xi,m)






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