import matplotlib.pyplot as plt
import pandas as pd

# 데이터프레임을 통해서 그래프 그리기
# 한 포인트가 한 행
# my_score = [(50,90,95), (60,75,100), (75,85,90), (85,75,90), (95,80,85), (90,85,80), (95,80,75)]
# df = pd.DataFrame(my_score, columns=['kor', 'math', 'eng'])
# print(df)
# df.plot(kind='line')
# plt.show()

import numpy as np

x=np.linspace(-np.pi, np.pi, 256)
y1, y2=np.cos(x), np.sin(x)
plt.plot(x,y1,ls='--', label='cosine')
plt.plot(x,y2,ls=':', label='sine')
plt.xlabel('x axis')
plt.ylabel('result')
plt.legend(loc='best', fontsize=14) # loc -  0:best위치, 1:upper right, ..
plt.show()