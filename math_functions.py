# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:21:30 2022

@author: Gerrit Nowald
"""

import numpy as np

# -----------------------------------------------------------------------------
# polynomial fitting

def Vandermonde(x,N):
    # coefficient matrix for polynomial interpolation
    return np.transpose( np.array([x**i for i in range(N+1)]) )

def polyfit(x,y,N):
    """
    polynomial fitting using least squares 
    x: x-data vector, each value unique
    y: y-data vector, corresponding to x
    N: order of fitting polynomial """
    V = Vandermonde(x,N)    # coefficient matrix
    B = np.transpose(V)
    p = np.linalg.inv( B @ V ) @ ( B @ y )
    return p    # polynomial coeffcients in increasing order

def polyeval(x,p):
    # evaluate polygon with coefficients p at vector x
    return Vandermonde( x, len(p)-1 ) @ p   # y vector corresponding to x

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