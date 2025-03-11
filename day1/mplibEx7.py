import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('sample.txt')
print(data)
print(type(data))# ndarray
print()

#plt.plot(data[:, 0], data[:, 1])
# plt.plot(data)
# plt.show()

for column in data.T:
    plt.plot(data[:, 0], column)
plt.show()