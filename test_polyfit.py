# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:57:37 2022

@author: Gerrit Nowald
"""

import numpy as np
import matplotlib.pyplot as plt

from math_functions import polyfit, polyeval

# -----------------------------------------------------------------------------
# input

N_data = 30     # number of data points
    
N = 2           # polynomial order ( N << N_data )

# -----------------------------------------------------------------------------
# test data 

data_x = np.linspace(-2,2,N_data)
data_y = np.cos(data_x)
data_y += 0.2*(np.random.rand(np.shape(data_x)[0])-0.5)   # adding noise

# -----------------------------------------------------------------------------
# calculation

coeff = polyfit(data_x, data_y, N)   # polynomial coeffcients in decreasing order

coeff_np = np.polyfit(data_x, data_y, N)

print(f'max. difference coefficients {max(abs(coeff-coeff_np))}')

# -----------------------------------------------------------------------------
# plot

plot_x = np.linspace(-2,2,100)
plot_y = polyeval(plot_x, coeff)

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