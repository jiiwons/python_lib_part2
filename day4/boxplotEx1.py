import matplotlib.pyplot as plt
import numpy as np


# data = np.random.randn(1000)
# plt.boxplot(data)
# plt.show()

N = 500
normal1 = np.random.normal(loc=100, scale=15, size=N)
normal2 = np.random.normal(loc=88, scale=30, size=N)

fig = plt.figure(figsize=(7,5))
ax1 = fig.add_subplot(111)
ax1.boxplot([normal1, normal2], tick_labels=['normal1', 'normal2'], vert=False, showmeans=True) # showmeans-삼각형 형태의 평균값 보여줌
plt.show()
