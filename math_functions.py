# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:21:30 2022

@author: Gerrit Nowald
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# cos and sin of the location vector of a given point

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
# polynomial fitting

class polynomial:
    """
    polynomial fitting using least squares
    initialise: instance = polynomial(xdata,ydata,order=2)
        - xdata: list of x-data, each value unique
        - ydata: list of y-data, corresponding to x
        - order: order of fitting polynomial (default=2)
    attributes:
        - instance.order: order of fitting polynomial
        - instance.coeff: polynomial coeffcients (decreasing order)
    methods:
        - instance(x): evaluates polynomial at points x (list) 
    """
    
    def __init__(self,xdata,ydata,order=2):
        xdata = np.array(xdata)
        ydata = np.array(ydata)
        self.order = order
        # calculation of polynomial coefficients (only once)
        # coefficient matrix
        V = self.__Vandermonde(xdata)
        B = np.transpose(V)
        # polynomial coeffcients (decreasing order)
        self.coeff = np.linalg.inv( B @ V ) @ ( B @ ydata )        
    
    def __str__(self):
        # polynomial as string
        def fcoeff(i):
            # plus sign & rounding
            return f' {"{0:+.03f}".format(self.coeff[i])}'
        polstr = ''
        for i in range(self.order-1):
            polstr += fcoeff(i) + f'*x**{self.order-i}'
        if self.order > 0:
            polstr += fcoeff(-2) + '*x'
        polstr += fcoeff(-1)
        return 'polynomial: ' + polstr

    def __Vandermonde(self,x):
        # coefficient matrix for polynomial interpolation
        V = [ x**(self.order-n) for n in range(self.order+1) ]
        return np.transpose(np.array(V))
    
    def __call__(self,x):
        x = np.array(x)
        # evaluate polygon at vector x
        y = self.__Vandermonde(x) @ self.coeff
        return y

# -----------------------------------------------------------------------------
# plot of circle

def plot_circ( R=1, C=(0,0), color='k', points=50 ):
    # plots a circle with radius R and center C
    angle = np.linspace(0, 2*np.pi, points)
    x = C[0] + R*np.cos(angle)
    y = C[1] + R*np.sin(angle)
    plt.plot(x,y, color=color )
    plt.axis('equal')
