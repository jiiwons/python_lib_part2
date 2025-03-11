import matplotlib.pyplot as plt
import numpy as np

dataA = np.random.randn(100,2)
dataA += np.array((-1,-1))

dataB = np.random.randn(100,2)
dataB += np.array((1,1))

plt.scatter(dataA[:, 0], dataA[:, 1], color='0.25')
plt.scatter(dataB[:, 0], dataB[:, 1], color='0.75', edgecolor='k')
plt.show()