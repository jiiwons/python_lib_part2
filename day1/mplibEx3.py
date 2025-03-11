import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 256)
y = np.cos(x)
plt.plot(x, y)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           ['-pi', '-pi/2', '0', 'pi/2', 'pi'])
plt.yticks([-1, 0, 1],
           ['low', 0, 'high'])
plt.grid()
plt.show()