import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Tools.scripts.make_ctype import values

plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('covid_data.csv', index_col='국가')
datachart = data.loc[['프랑스', '중국', '영국', '이란'],'4월06일':'4월08일']
print(datachart)

def makeBarChart2(chartdata, rotation, title, ylim = None, stacked=False, yticks_interval=10000):
    plt.figure(figsize=(8,6))
    chartdata.plot(kind='bar', rot=rotation, title=title, legend=True, stacked=stacked)

    if stacked==False:
        maxlim = (int(max(chartdata.max())/yticks_interval) +1) * yticks_interval
    else:
        maxlim = (int(max(chartdata.sum(axis=1))/yticks_interval)+1)*yticks_interval

    values = np.arange(0, maxlim+1, yticks_interval)
    plt.yticks(values, ['%s'%format(val, ',') for val in values])

    if ylim != None:
        plt.ylim(ylim)
    plt.show()

#makeBarChart2(datachart, rotation=0, title='국가별 일별 발생 수')
makeBarChart2(datachart, rotation=0, stacked=True, title='국가별 일별 발생 수', yticks_interval=50000)