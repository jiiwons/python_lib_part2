# 1. 와인 품질 데이터셋을 이용한다.

import pandas as pd
#  a. 데이터 셋을 DataFrame으로 읽어온다.
wine = pd.read_csv('winequality-both.csv')
print(wine.head())

#  b. 위의 데이터프레임의 요약 통계를 표시한다.(최소, 최대, 사분위, 평균, 분산)
print(wine.describe())
print()
#  c. 와인 품질(quality)의 유일 값을 찾아 출력한다.
print(wine['quality'].unique())
print()
#  d. 와인 품질(quality)의 빈도를 계산하여 출력한다.
print(wine['quality'].value_counts())
print()
#  e. 와인 종류에 따라 기술 통계(최소, 최대, 사분위, 평균, 분산)를 출력한다.
print(wine.groupby(['type']).describe())
print()
#  f.  와인 종류에 따른 품질(quality)의 분포를 확인하기 위해 레드와인과 화이트 와인의 막대 그래프를 출력한다.
#     (이때 범례도 같이 출력한다. )
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(x='type', hue='quality', data=wine)
plt.show()
#  g. 와인 종류에 따라 품질의 차이를 검정(분산, 평균)하여 각 각을 출력한다.
print(wine.groupby('type')['quality'].var())
print(wine.groupby('type')['quality'].mean())