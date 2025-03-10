import matplotlib.pyplot as plt
import numpy as np
# data = np.arange(0, 5, 0.2)
# plt.plot(data, data, 'b--',
#          data, 0.1*data**2, 'go:',
#          data, 0.2*data**3, 'rs-')
# plt.show()

plt.plot([10,20,30,40], [4,2,9,12],
         color='k', lw=5, ls='--', marker='o', ms=12, mec='blue', mew=5, mfc='yellow')

plt.plot([10,20,30,40], [22,6,15,2],
         color='red', lw=5, ls='--', marker='o', ms=12, mec='yellow', mew=5, mfc='blue')
plt.show()