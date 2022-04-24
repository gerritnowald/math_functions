# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:21:30 2022

@author: Gerrit Nowald
"""

import numpy as np

# -----------------------------------------------------------------------------
# polynomial fitting

"""
polynomial fitting using least squares 
x: x-data vector, each value unique
y: y-data vector, corresponding to x
order: order of fitting polynomial
"""

def Vandermonde(x,order):
    # coefficient matrix for polynomial interpolation
    V = [x**(order-n) for n in range(order+1)]
    return np.transpose(np.array(V))

def polyfit(x,y,order):
    # calculation of polynomial coefficients (decreasing order)
    V = Vandermonde(x,order)
    B = np.transpose(V)
    return np.linalg.inv( B @ V ) @ ( B @ y )

def polyeval(x,coeff):
    # evaluate polynomial at vector x
    y = Vandermonde( x, len(coeff)-1 ) @ coeff
    return y

# -----------------------------------------------------------------------------
# linear 1D interpolation

def interpextraplin(x,y,xi):
    """
    1D linear inter- and extrapolation, multiple y-data possible
    x:  x-data vector [m], monotonically increasing
    y:  y-data matrix [m x n], corresponding to x (interpolation for each column)
    xi: x-value vector [p] to be interpolated, in any order
    Loren Shure (The MathWorks) http://blogs.mathworks.com/loren/2008/08/25/piecewise-linear-interpolation/
    Jose M. Mier, https://de.mathworks.com/matlabcentral/fileexchange/43325-quicker-1d-linear-interpolation-interp1qr """
    # slope of line segments
    if y.ndim ==1:
        m  = np.diff(y)/np.diff(x)
    elif y.ndim ==2:
        m  = np.diff(y,axis=0)/np.diff(x)[:, np.newaxis]
    ind = np.sum( xi > x[:, np.newaxis], axis=0) - 1    # find interval
    ind = np.maximum(ind, 0)            # avoid index smaller 0
    ind = np.minimum(ind, len(x)-2)     # avoid index larger than len(x)-2
    # inter- & extrapolation
    if y.ndim ==1:
        yi = m[ind]*(xi-x[ind]) + y[ind]
    elif y.ndim ==2:
        yi = m[ind,:]*(xi[:, np.newaxis]-x[ind, np.newaxis]) + y[ind,:]
    return yi   # interpolated values matrix [p x n], corresponding to xi