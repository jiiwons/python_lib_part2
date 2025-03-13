import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family='Malgun Gothic')

# x = np.random.randn(10000)
# plt.hist(x, bins=30, density=True) # density - 비율
# plt.show()

human = pd.read_csv('human_height.csv')
human.info()
man = human['man']
woman = human['woman']

plt.figure(figsize=(7,5))
plt.hist(man, bins=20, alpha=0.5, facecolor='darkblue', label='man', rwidth=0.95)
plt.hist(woman, bins=20, alpha=0.5, facecolor='pink', label='woman', rwidth=0.95)
plt.xlabel('height')
plt.ylabel('frequency')
plt.title('man height distribution')
plt.show()