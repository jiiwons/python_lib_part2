import matplotlib.pyplot as plt
import numpy as np


plt.subplot(2,2,1)
plt.title('axes1')
plt.plot(np.random.randn(50))

plt.subplot(2,2,2)
plt.title('axes2')
plt.plot(np.random.randn(50))

plt.subplot(223)
plt.title('axes3')
plt.plot(np.random.randn(50))

plt.subplot(224)
plt.title('axes4')
plt.plot(np.random.randn(50))

plt.suptitle('multi view', fontsize=16)
plt.tight_layout()
plt.show()