# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:21:30 2022

@author: Gerrit Nowald
"""

import numpy as np
import matplotlib.pyplot as plt
import warnings

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
        # input checking
        if len(xdata) != len(ydata):
            raise ValueError('data must have same length')
        xdata = np.array(xdata)
        ydata = np.array(ydata)
        
        N_data = len(xdata)
        if order > N_data - 1:
            order = N_data - 1
            warnings.warn(f'polynomial order set to {order}, only {N_data} data points', stacklevel=2)
        self.order = order
        
        # create polynomial from least squares fit
        self.coeff = self.__calc_coeff(xdata,ydata)
        # print polynomial formula
        print(self)
    
    def __call__(self,x):
        # evaluate polynomial at vector x
        x = np.array(x)
        y = self.__Vandermonde(x) @ self.coeff
        return y
    
    def __str__(self):
        # polynomial as string
        def fcoeff(i):
            return f' {"{0:+.3g}".format(self.coeff[i])}' # plus sign & rounding
        polstr = ''
        for i in range(self.order-1):
            polstr += fcoeff(i) + f'*x**{self.order-i}'
        if self.order > 0:
            polstr += fcoeff(-2) + '*x'
        polstr += fcoeff(-1)
        return 'polynomial: f(x) =' + polstr

    def __calc_coeff(self,x,y):
        # calculation of polynomial coefficients (decreasing order)
        V = self.__Vandermonde(x)
        B = np.transpose(V)
        return np.linalg.inv( B @ V ) @ ( B @ y )  
    
    def __Vandermonde(self,x):
        # coefficient matrix for polynomial interpolation
        V = [ x**(self.order-n) for n in range(self.order+1) ]
        return np.transpose(np.array(V))

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
# cos and sin of the location vector of a given point

def cos_sin(q):                       # q = np.array([x,y])
    return q/np.sqrt(np.sum(q**2))    # [cos, sin]

# -----------------------------------------------------------------------------
# plot of circle

def plot_circ( R=1, C=(0,0), color='k', points=50 ):
    # plots a circle with radius R and center C
    angle = np.linspace(0, 2*np.pi, points)
    x = C[0] + R*np.cos(angle)
    y = C[1] + R*np.sin(angle)
    plt.plot(x,y, color=color )
    plt.axis('equal')