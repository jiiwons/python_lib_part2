import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

welfare = pd.read_csv('welfareClean.csv', encoding='cp949')
# welfare.info()
# print(welfare.tail())
# print()
#
# result = welfare.groupby('결혼유무')['결혼유무'].count()
# print(result)
#
# plt.bar(result.index, result.values)
# plt.show()

import seaborn as sns

# sns.countplot(data=welfare, x='결혼유무', order=['결혼','이혼','무응답'])
# sns.countplot(data=welfare, x='결혼유무', order=['결혼','이혼','무응답'], hue='종교유무')
# sns.countplot(data=welfare, x='결혼유무', order=['결혼','이혼','무응답'], hue='종교유무', palette='Paired')
# plt.title('count plot')
# plt.show()

# x = welfare['나이']
# # sns.distplot(x, hist=True, kde=False)
# sns.histplot(data=welfare, x='나이', bins=10)
# plt.show()

pdata = welfare.pivot_table(index='성별', columns='결혼유무', values='나이', aggfunc='mean')
# print(pdata)
# sns.heatmap(data=pdata, annot=True)
# plt.show()

# corr = welfare[['생일', '소득', '나이']].corr()
# print(corr)
# sns.heatmap(data=corr, annot=True, cmap='YlGnBu')
#
# plt.show()

# nwelfare = welfare.loc[:, ['생일','소득','나이']]
# sns.pairplot(data=nwelfare)
# plt.show()

# nwelfare = welfare.loc[:, ['생일','소득','나이','결혼유무']]
# sns.pairplot(data=nwelfare, hue='결혼유무')
# plt.show()

# sns.violinplot(x='성별', y='나이', data=welfare, hue='종교유무')
# plt.show()

# sns.lmplot(x='나이', y='소득', data=welfare, hue='결혼유무')
# sns.lmplot(x='나이', y='소득', data=welfare, hue='결혼유무', col='성별')
# sns.lmplot(x='나이', y='소득', data=welfare, hue='결혼유무', col='성별', row='연령대')
# plt.tight_layout()
# plt.show()

# sns.jointplot(x='나이', y='소득', data=welfare)
# plt.show()

sns.boxplot(x='성별', y='소득', data=welfare, hue='종교유무')
plt.show()