# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:21:30 2022

@author: Gerrit Nowald
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# trigonometry

def cos_sin(q):                       # q = np.array([x,y])
    return q/np.sqrt(np.sum(q**2))    # [cos, sin]

# -----------------------------------------------------------------------------
# linear 1D interpolation

def calc_slope(x,y):
    """
    slope of line segments for 1D linear inter- and extrapolation
    - x:  x-data vector [m], monotonically increasing
    - y:  y-data matrix [m x n], corresponding to x"""
    if y.ndim ==1:
        m  = np.diff(y)/np.diff(x)
    elif y.ndim ==2:
        m  = np.diff(y,axis=0)/np.diff(x)[:, np.newaxis]
    return m

def interplinfast(x,y,xi,m=None):
    """
    fast 1D linear inter- and extrapolation
    x:  x-data vector [m], monotonically increasing
    y:  y-data matrix [m x n], corresponding to x (interpolation for each column)
    xi: x-value vector [p] to be interpolated, in any order
    m:  slopes of line segments, can be computed in advance (optional)
    Loren Shure (The MathWorks) http://blogs.mathworks.com/loren/2008/08/25/piecewise-linear-interpolation/
    Jose M. Mier, https://de.mathworks.com/matlabcentral/fileexchange/43325-quicker-1d-linear-interpolation-interp1qr """
    if m.all()==None:
        m = calc_slope(x,y)             # slope of line segments
    ind = np.sum( xi > x[:, np.newaxis], axis=0) - 1    # find interval
    ind = np.maximum(ind, 0)            # avoid index smaller 0
    ind = np.minimum(ind, len(x)-2)     # avoid index larger than len(x)-2
    # inter- & extrapolation
    if y.ndim ==1:
        yi = m[ind]*(xi-x[ind]) + y[ind]
    elif y.ndim ==2:
        yi = m[ind,:]*(xi[:, np.newaxis]-x[ind, np.newaxis]) + y[ind,:]
    return yi   # interpolated values matrix [p x n], corresponding to xi

# -----------------------------------------------------------------------------
# curve fitting

def Vandermonde(x,N):
    # coefficient matrix for polynomial interpolation
    V = np.ones((len(x),N+1))
    for i in range(1, N+1):
        V[:,i] = x**i
    return V

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
# ODS

def state_space(M,D,C):
    # M,D,C: mass, damping and stiffness matrix
    Minv = np.linalg.inv(M)
    A = np.vstack((
        np.hstack(( np.zeros(np.shape(M)), np.eye(np.shape(M)[1]) )),
        np.hstack(( - Minv @ C, - Minv @ D )) ))
    return A, Minv  # state space matrix, inverse mass matrix (for force vector)

# -----------------------------------------------------------------------------
# plot

def plot_circ( R=1, C=(0,0), color='k', points=50 ):
    # plots a circle with radius R and center C
    angle = np.linspace(0, 2*np.pi, points)
    x = C[0] + R*np.cos(angle)
    y = C[1] + R*np.sin(angle)
    plt.plot(x,y, color=color )
    plt.axis('equal')