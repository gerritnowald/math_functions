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
# curve fitting

def Vandermonde(x,N):
    # coefficient matrix for polynomial interpolation
    V = np.ones((len(x),N+1))
    for i in range(1, N+1):
        V[:,i] = x**i
    return V

def polyfit(x,y,N):
    # polynomial fitting using least squares 
    # x: x-data vector, each value unique
    # y: y-data vector, corresponding to x
    # N: order of fitting polynomial 
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