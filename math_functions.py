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

# -----------------------------------------------------------------------------
# curve fitting

class polyfit:
    """
    polynomial fitting using least squares
    input:
        - xdata: list of x-data, each value unique
        - ydata: list of y-data, corresponding to x
        - order: order of fitting polynomial (default=2)
    attributes:
        - order: order of fitting polynomial
        - coeff: polynomial coeffcients (increasing order)
    methods:
        - eval(x): evaluates polynomial at points x (list) 
    """
    
    def __init__(self,xdata,ydata,order=2):
        # calculation of polynomial coefficients (only once)
        xdata = np.array(xdata)
        ydata = np.array(ydata)
        # order of polynomial
        self.order = order
        # coefficient matrix
        V = self.__Vandermonde(xdata)
        B = np.transpose(V)
        # polynomial coeffcients (increasing order)
        self.coeff = np.linalg.inv( B @ V ) @ ( B @ ydata )
        
    def __str__(self):
        return f'polynomial of order {str(self.order)}'

    def __Vandermonde(self,x):
        # coefficient matrix for polynomial interpolation
        V = [ x**n for n in range(self.order+1) ]
        return np.transpose(np.array(V))
    
    def evaluate(self,x):
        x = np.array(x)
        # evaluate polygon at vector x
        y = self.__Vandermonde(x) @ self.coeff
        return y

# -----------------------------------------------------------------------------
# plot

def plot_circ( R=1, C=(0,0), color='k', points=50 ):
    # plots a circle with radius R and center C
    angle = np.linspace(0, 2*np.pi, points)
    x = C[0] + R*np.cos(angle)
    y = C[1] + R*np.sin(angle)
    plt.plot(x,y, color=color )
    plt.axis('equal')
