import numpy as np

n_ref = np.array([-8.339837e-01 , -1.609418e-01 , -5.277962e-01])

A = np.array([-1.671070e-01 , -4.356568e+00 , 2.524810e+00])
B = np.array([-1.114400e-01 , -4.300000e+00 , 2.419600e+00])
C = np.array([-1.196820e-01 , -4.380000e+00 , 2.457018e+00])

n = np.cross(B - A , C - A)
n = n / np.linalg.norm(n)

print(n)
print((n - n_ref) / n_ref * 100)