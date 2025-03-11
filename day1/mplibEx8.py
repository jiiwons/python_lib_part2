import matplotlib.pyplot as plt
import numpy as np

# plt.figure(figsize=(10,2))
# plt.title('figure size = (10, 2)', fontsize=14)
# plt.plot(np.random.randn(200))
# plt.show()

x = np.linspace(0, 3, 50)
y1 = np.cos(3 * np.pi * x) * np.exp(-2*x)
y2 = np.cos(3 * np.pi * x)

plt.subplot(2,1,1)
plt.plot(x, y1, 'yo-')
plt.title('multi graph')
plt.xlabel('x1')
plt.ylabel('result1')

plt.subplot(2,1,2)
plt.plot(x,y2,'r-.')
plt.xlabel('time')
plt.ylabel('result2')
#plt.tight_layout()
plt.subplots_adjust(hspace=0.7) # tight_layout 써도됨, wspace 옵션도 있음

plt.show()