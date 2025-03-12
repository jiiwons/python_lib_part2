import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


plt.rc('font', family='Malgun Gothic')
# data = [5,25,50,20]
# plt.pie(data)
# plt.show()

data = pd.read_csv('covid_data.csv', index_col='국가')
chartdata = data.loc[['독일', '프랑스', '중국', '영국'],'4월06일']
# mylabel = chartdata.index
# mycolors = ['blue', '#6aff00', 'yellow', '#ff113c']
#
# plt.figure(figsize=(5,5))
# plt.pie(chartdata,
#         labels=mylabel,
#         startangle=90,
#         colors=mycolors,
#         autopct='%.2f%%',
#         counterclock=False,
#         explode=(0,0.1,0,0),
#         shadow=True)
# plt.legend(loc='best')
# plt.xlabel('국가명')
# plt.title('주요 국가 코로나 발생 비율(4월 6일)')
# plt.show()


fig, ax = plt.subplots(figsize=(8,4))
mylabel = chartdata.index
def getLabelFormat(pct, allvals):
    absolute = int(pct/100*np.sum(allvals))
    return f'{pct:.2f}%\n({absolute}명)'

wedges, texts, autotexts = ax.pie(chartdata,
                                  autopct = lambda pct:getLabelFormat(pct, chartdata),
                                  textprops=dict(color='w'),
                                  labels=mylabel)
plt.setp(autotexts, size=10, weight='bold')
plt.legend(title='국가명', loc='best')
plt.show()