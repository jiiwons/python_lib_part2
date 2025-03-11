import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Malgun Gothic')

covid_data = pd.read_csv('covid_data.csv', index_col='국가')
print(covid_data)

# chartdata = covid_data['4월06일']
# print(chartdata) # series
#
# YTICK_INTERVAL = 50000
# maxlim = (int(chartdata.max()/YTICK_INTERVAL) + 1 )*YTICK_INTERVAL # 계산값보다는 높게 1 더함
# #print(chartdata.max(), maxlim)
# values = np.arange(0, maxlim+1, YTICK_INTERVAL)
# #print(values)
# plt.plot(chartdata, color='b', ls='solid', marker='o') # 시리즈객체이기 때문에 국가가 x축에(..? 데이터프레임과의 차이를 찾아보기)
# plt.yticks(values, ['%s'%format(val, ',') for val in values])
# plt.grid(True)
# plt.xlabel('국가명')
# plt.ylabel('발생 수')
# plt.title('4월 6일 국가별 코로나 발생 수')
# plt.show()

COUNTRY = ['스페인', '프랑스', '독일', '중국', '영국', '이란']
chartdata = covid_data.loc[COUNTRY, '4월06일':'4월10일']
print(chartdata)
# 데이터프레임으로 그려야됨
print(chartdata.T)
chartdata.T.plot(title='일자 & 국가별 코로나 발생 수', figsize=(10,6), legend=True, marker='o')
plt.grid(True)
plt.show()