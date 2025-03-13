import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure(figsize=(6,4))
# grid = plt.GridSpec(nrows=2, ncols=2, width_ratios=[3,1], height_ratios=[1,3])
#
# ax1 = fig.add_subplot(grid[0])
# ax1.plot(np.random.rand(50))
#
# ax2 = fig.add_subplot(grid[1])
# ax2.plot(np.random.rand(50))
#
# ax3 = fig.add_subplot(grid[2])
# ax3.plot(np.random.rand(50))
#
# ax4 = fig.add_subplot(grid[3])
# ax4.plot(np.random.rand(50))
#
# plt.show()

data = np.linspace(-np.pi, np.pi, 1024)
grid_size = (4,2)

plt.subplot2grid(grid_size, (0,0), rowspan=3, colspan=1)
plt.plot(np.sin(2*data), np.cos(0.5*data), c='r')

plt.subplot2grid(grid_size, (0,1), rowspan=3, colspan=1)
plt.plot(np.sin(2*data), np.cos(0.5*data), c='b')

plt.subplot2grid(grid_size, (3,0), rowspan=1, colspan=2)
plt.plot(np.sin(5*data), np.cos(7*data), c='g')

plt.show()