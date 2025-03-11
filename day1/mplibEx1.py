import matplotlib.pyplot as plt

# plt.title('pltEx1')
# plt.plot([1, 4, 19, 15,])
# plt.show()

## list 객체
# plt.title('pltEx1')
# plt.plot([10,20,30,40,50], [1, 4, 19, 15,17])
# plt.show()

## range 객체
# x = range(100)
# y = [x**2 for x in x]
# plt.plot(x, y)
# plt.show()


import numpy as np
# x = np.linspace(0, 2*np.pi, 100) # 0부터 2*np.pi까지 100개의 구간으로
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()

# plt.plot([10,20,30,40], [1, 3, 12, 17], "rs--") # r: red, s:square, --:dash(선 스타일)
# plt.show()

plt.plot([10,20,30,40], [1, 3, 12, 17], "b*-.")
plt.show()