import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.lines import lineStyles

plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('covid_data.csv', index_col='국가')
chartdata = data['4월06일']
print(chartdata)

def makeBarchart1(x, y, color, xlabel, ylabel, title):
    plt.figure(figsize=(8,6))
    plt.bar(x,y,color=colors, alpha=0.7)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title, fontsize=16)

    YTICK_INTERVAL = 50000 #  50,000 단위로 눈금 표시
    maxlim = (int(y.max()/ YTICK_INTERVAL) + 1) *YTICK_INTERVAL
    values = np.arange(0, maxlim+1, YTICK_INTERVAL)
    plt.yticks(values, ['%s'%format(val, ',') for val in values])

    ratio = 100 * y/y.sum()
    print(ratio)
    for idx in range(y.size):
        value = format(y[idx], ',') + '건'
        ratioval = f'{ratio[idx]:.1f}%'
        plt.text(x=idx, y=y[idx] + 2000, s=value, ha ='center', fontsize=9) # vertical horizontal 에 해당하는 걸 조정(5만 간격이니까 2천정도 조정해서 조금 위에 위치하도록)
        plt.text(x=idx, y=y[idx]/2, s=ratioval, ha ='center', fontsize=9) # 퍼센트는 막대 길이의 중앙에 위치

    meanval = y.mean()
    meantext=f'평균:{int(meanval)}건'
    plt.axhline(y=meanval, color='r', linewidth=1, linestyle='--')
    plt.text(x=y.size-1, y=meanval+3000, s=meantext, ha='center', fontsize=11)
    plt.show()

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
makeBarchart1(x=chartdata.index, y=chartdata, color=colors,
              xlabel='국가명', ylabel='발생 수', title='국가별 코로나 발생 수(4월 6일)')
