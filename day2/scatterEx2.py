import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family='Malgun Gothic')

mpg = pd.read_csv('mpg.csv', encoding='utf-8')
# print(mpg)
#
# xdata = mpg.loc[:, ['displ']]
# ydata = mpg.loc[:, ['hwy']]
#
# plt.plot(xdata, ydata, marker='o', linestyle='None')
# plt.title('산점도 그래프', fontsize=15)
# plt.xlabel('엔진 크기')
# plt.ylabel('고속도로 주행 마일 수')
# plt.show()
#
# print(mpg.loc[:, ['displ', 'hwy']].corr())

mpg.info()
print(mpg.drv.unique())

mycolor=['r','g','b']
label_dict = {'f':'전륜 구동', '4':'4륜 구동', 'r':'후륜 구동'}

for idx, finditem in enumerate(mpg.drv.unique()):
    xdata = mpg.loc[mpg['drv'] == finditem, 'displ']
    ydata = mpg.loc[mpg['drv'] == finditem, 'hwy']
    plt.plot(xdata, ydata, color=mycolor[idx], marker='o', linestyle='None', label=label_dict[finditem])
    
plt.legend(loc='best')
plt.xlabel('엔진 크기')
plt.ylabel('고속도로 주행 마일 수')
plt.show()