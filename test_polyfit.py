# -*- coding: utf-8 -*-
"""
test for my oop implementation of a polynomial fit using least squares.
data is genarated as a cosine + noise.
the fitted polynomial with the data are plotted.
polynomial coefficients and evalauted values are compared with NumPy.

Created on Thu Jan 13 10:57:37 2022

@author: Gerrit Nowald
"""

import numpy as np
import matplotlib.pyplot as plt

from math_functions import polyfit

# -----------------------------------------------------------------------------
# input

N_data = 30     # number of data points
    
N = 2           # polynomial order ( N << N_data, N <= N_data - 1 )


def main():
    
    # -----------------------------------------------------------------------------
    # test data 
    
    data_x = np.linspace(-2,2,N_data)
    data_y = np.cos(data_x)
    data_y += 0.2*(np.random.rand(np.shape(data_x)[0])-0.5)   # adding noise
    
    # -----------------------------------------------------------------------------
    # calculation
    
    plot_x = np.linspace(-2,2,100)
    
    # my implementation
    polynomial = polyfit(data_x, data_y, N)
    plot_y = polynomial.eval(plot_x)
    
    # numpy
    pnp = np.polyfit(data_x, data_y, N)
    plot_ynp = np.polyval(pnp, plot_x)
    
    # comparison
    print(f'max. difference coefficients {max(abs(polynomial.coeff-pnp[::-1]))}')
    print(f'max. difference evaluated polynom {max(abs(plot_y-plot_ynp))}')
    
    # -----------------------------------------------------------------------------
    # plot
    
    plt.close('all')
    
    plt.figure()
    plt.plot(data_x, data_y, '.', label='data')
    plt.plot(plot_x, plot_y, 'k', label='fitted polynomial')
    plt.show()


if __name__ == "__main__":
    main()