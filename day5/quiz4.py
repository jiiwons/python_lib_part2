# 4. drinks.csv 파일을 이용하여 아래의 조건에 맞게 출력하시오(아래 그래프 이미지 참조)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('drinks.csv')

#  ㄱ. 파일을 읽어 데이터 프레임으로 구성한 뒤 앞의 10개 행을 출력
print(data.head(10))
print()
#  ㄴ.'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol'들의 상관계수를 계산하여 출력하고
#      heatmap를 이용하여 이를 그래프로 출력
print(data[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']].corr())
df1 = data[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']]

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df1.corr(), annot=True)
plt.show()
#  ㄷ. 'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol'들의 상관 관계를 보기 위해 각 특성들의
#      산점도를 그래프로 출력
sns.pairplot(df1, height=1.5)
plt.show()

#  ㄹ. 'continent'의 결측데이터에는 'OT'를 삽입
print(data['continent'].value_counts())
data['continent'] = data['continent'].fillna('OT')
print()
print(data['continent'].value_counts())

#  ㅁ. 대륙별('continent')의 데이터 수의 비율을 파이 그래프를 이용하여 출력
df_continent = pd.DataFrame(data['continent'].value_counts())
print(df_continent)
chartdata = df_continent['count']
mylabel = chartdata.index
plt.rc('font', family='Malgun Gothic')

plt.figure(figsize=(5,5))
plt.pie(chartdata,
        labels=mylabel,
        startangle=0,
        autopct='%1.0f%%',
        counterclock=True,
        explode=(0,0,0,0.1,0,0),
        shadow=True,
        wedgeprops = {'linewidth' : 1, 'edgecolor' : 'white' })
plt.show()

#  ㅂ. 'total_litres_of_pure_alcohol' 전체 평균 보다 많은 알코올을 섭취하는 대륙을 구하여 출력
total_mean = data['total_litres_of_pure_alcohol'].mean()
# print(total_mean)
# print(data[data['total_litres_of_pure_alcohol'] > total_mean]['continent'].value_counts())
## 강사님 코드
continent_mean = data.groupby('continent')['total_litres_of_pure_alcohol'].mean()
continent_over_mean = continent_mean[continent_mean >= total_mean]
print(continent_over_mean)

#  ㅅ. 대륙별 spirit_servings의 평균, 최소, 최대, 합계를 막대 그래프로 출력
# cont_mean = data.groupby('continent')['spirit_servings'].mean()
# cont_min = data.groupby('continent')['spirit_servings'].min()
# cont_max = data.groupby('continent')['spirit_servings'].max()
# cont_sum = data.groupby('continent')['spirit_servings'].sum()

# cont = data.groupby("continent")["spirit_servings"].agg(["mean","min","max","sum"]).reset_index()
#
# fig, ax = plt.subplots(figsize=(12,6))
#
# index = np.arange(len(cont['continent']))
# bar_width = 0.25
# ax.bar(index, cont['mean'], bar_width, label='Mean', color='red')
# ax.bar(index + bar_width, cont['min'], bar_width, label='Min', color='green')
# ax.bar(index + 2 * bar_width, cont['max'], bar_width, label='Max', color='blue')
# ax.bar(index + 3 * bar_width, cont['sum'], bar_width, label='Sum', color='gold')
#
# ax.set_xticks(index + 1.5 * bar_width)
# ax.set_xticklabels(cont['continent'])
# ax.grid(True)
# ax.legend()
#
# plt.show()

## 강사님 코드
result = data.groupby('continent').spirit_servings.agg(['mean', 'min', 'max', 'sum'])
n_groups = len(result.index)
print(result)

result.plot(kind='bar')
plt.show()
#  ㅇ. 대륙별 total_litres_of_pure_alcohol를 막대 그래프로 출력
# cont_alchol = data.groupby('continent')['total_litres_of_pure_alcohol'].mean().reset_index()
#
# mean = data['total_litres_of_pure_alcohol'].mean()
#
# fig, ax = plt.subplots(figsize=(12, 6))
#
# ax.bar(cont_alchol['continent'], cont_alchol['total_litres_of_pure_alcohol'], color='skyblue', alpha=0.7, label='Continent')
# ax.bar('mean', mean, color='red', alpha=0.7, label='Mean')
# ax.axhline(mean, color='black', linestyle='--')
#
# ax.set_xlabel('Continent')
# ax.set_ylabel('total_litres_of_pure_alcohol')
# ax.set_title('total_litres_of_pure_alcohol by Continent')
# ax.grid(True)
# ax.legend()
#
# plt.show()

## 강사님 코드
continents = continent_mean.index.tolist()
continents.append('mean')
x_pos = np.arange(len(continents))
alchol = continent_mean.to_list()
alchol.append(total_mean)

bar_list = plt.bar(x_pos, alchol, align='center', alpha=0.5)
# print(bar_list) # bar_list 7개
bar_list[len(continents) - 1].set_color('r') # 맨 마지막 것만 붉은색이 되게
plt.plot([0,6],[total_mean, total_mean], 'k--')
plt.xticks(x_pos, continents)
plt.ylabel('total_liters_of_pure_alchol')
plt.title('total_litres_of_pure_alcohol by Continent')
plt.grid(True)
plt.show()