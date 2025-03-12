import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('covid_data.csv', index_col='국가')
datachart = data.loc[['프랑스', '영국', '중국']]
print(datachart)
column_names = datachart.columns.tolist()
print(column_names)

chartdata = {}
for row in datachart.index:
    chartdata[row] = data.loc[row].values
print(chartdata)

labels = list(chartdata.keys())
data = np.array(list(chartdata.values()))
print(data)
print(data.shape)
# https://matplotlib.org/stable/users/explain/colors/colormaps.html
category_colors = plt.get_cmap('RdYlGn')(np.linspace(0.15, 0.85, data.shape[1]))
print(category_colors)

fig, ax = plt.subplots(figsize=(11,5))
ax.set_xlim(0, np.sum(data, axis=1).max())
ax.xaxis.set_visible(False)

data_sum = data.cumsum(axis=1)
print(data_sum)

for i, (columnname, color) in enumerate(zip(column_names, category_colors)):
    widths = data[:,i]
    start = data_sum[:,i]-widths
    ax.barh(labels, widths, left=start, height=0.5, label=columnname, color=color)

    r,g,b,_ = color
    text_color = 'white' if r*g*b < 0.5 else 'Darkgrey'
    xcenters = start + widths/2

    for y, (x, c) in enumerate(zip(xcenters, widths)):
        ax.text(x,y,str(int(c)), ha='center', color=text_color)

    #ax.legend(ncols=len(column_names), loc=(0,1))
    ax.legend(ncols=len(column_names), bbox_to_anchor=(0,1), loc=3) # 3은 좌측 하단이지만, bbox_to_anchor를 사용하면  0,1(좌측상단)을 기준으로 좌측하단부터 반시계 방향으로 1,2,3,4를 잡기 때문에 3을 잡으면 시작점이 박스 위에서부터 시작(loc=4 넣고 비교해보기)

plt.show()
