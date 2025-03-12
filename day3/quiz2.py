import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.lines import lineStyles

plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('covid_data.csv', index_col='국가')
usa_data = data.loc[['미국']].T # 데이터프레임 형식, data.loc['미국'] 과 비교해보기
print(usa_data)

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,6)) # 두 개의 axes 형태의 리스트 형태가 됨
usa_data.plot(kind='bar', ax=axes[0], rot=0, alpha=0.7)
usa_data.plot(kind='barh', ax=axes[1], color='m', alpha=0.7)

fig.suptitle('서브 플로팅', fontsize=16)
plt.show()
