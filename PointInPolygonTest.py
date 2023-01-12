import numpy as np
import matplotlib.pyplot as plt

from polygon_math import polygon

import time

# ----------------------------------------------------------------------
# inputs

Vertices = [
    [0, 0],
    [1.75, 4],
    [1.5, 6],
    [1, 7],
    [0.25, 6],
    [0, 5],
    [-0.25, 6],
    [-1, 7],
    [-1.5, 6],
    [-1.75, 4],
    ]
    
N = 10000

# ----------------------------------------------------------------------
# plot

heart = polygon(Vertices)

points = np.hstack(( np.random.rand(N,1)*6 - 3, np.random.rand(N,1)*10 - 2 ))


fig, ax = plt.subplots()

start_time = time.time()
for point in points:
    if heart(point):
        style = "yo"
    else:
        style = "bo"
    plt.plot(*point, style)
print(f"elapsed time: {time.time() - start_time} s")

ax.set_axis_off()
plt.show()