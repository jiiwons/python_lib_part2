import matplotlib.pyplot as plt
import numpy as np

def plot_slope(x,y):
    xs = x[1:] - x[:-1]
    ys = y[1:] - y[:-1]
    plt.plot(x[1:], ys/xs)

x = np.linspace(-3, 3, 100)
y = np.exp(-x**2)

plt.plot(x,y)
plot_slope(x,y)
plt.show()