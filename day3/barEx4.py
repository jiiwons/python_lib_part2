import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('covid_data.csv', index_col='국가')
datachart = data.loc[['스페인', '프랑스', '중국', '영국', '이란'], '4월06일':'4월10일']
print(datachart)

rows = [x for x in datachart.columns]
columns = [x for x in datachart.columns]
print(rows)
print(columns)

LEFT_MARGIN = 0.3
bar_width = 1 - 2*LEFT_MARGIN
index = np.arange(len(columns)) + LEFT_MARGIN
y_offset = np.zeros(len(columns))

plt.figure(figsize=(8,8))
cell_text = []

for row in datachart.index:
    chartdata = datachart.loc[row].tolist()
    plt.bar(index, chartdata, bar_width, bottom=y_offset, label=row)
    y_offset += chartdata
    cell_text.append([format(x, ',') for x in chartdata])

plt.legend(loc='best')
cell_text.reverse()
rows = [rows[idx] for idx in range(len(rows)-1, -1, -1)]

plt.table(cellText=cell_text, rowLabels = rows, colLabels=columns)
plt.xticks([])
plt.tight_layout()
plt.title('테이블 데이터 & 막대 그래프')
plt.show()