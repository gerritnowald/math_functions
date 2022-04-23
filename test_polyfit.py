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

from curves import polyfit

# -----------------------------------------------------------------------------
# input

N_data = 30     # number of data points
    
N = 2           # polynomial order ( N << N_data )


def main():
    
    # -----------------------------------------------------------------------------
    # test data 
    
    data_x = np.linspace(-2,2,N_data)
    data_y = np.cos(data_x)
    data_y += 0.2*(np.random.rand(np.shape(data_x)[0])-0.5)   # adding noise
    
    # -----------------------------------------------------------------------------
    # calculation
    
    # my implementation
    p1 = polyfit(data_x, data_y, N)   
    
    # numpy
    coeff_np  = np.polyfit(data_x, data_y, N)
    
    # comparison
    print(f'max. difference coefficients: {max(abs(p1.coeff-coeff_np))}')
    
    # -----------------------------------------------------------------------------
    # plot
    
    plot_x = np.linspace(-2,2,100)
    plot_y = p1(plot_x)
    
    plt.close('all')
    
    plt.figure()
    plt.style.use('dark_background')
    plt.plot(data_x, data_y, '.', label='data')
    plt.plot(plot_x, plot_y, label='fitted polynomial', color='gold')
    plt.legend()
    plt.title('polynomial fit with least squares')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.tight_layout()
    
    plt.show()
    # plt.savefig('fitted polynomial.png', transparent=True)


if __name__ == "__main__":
    main()