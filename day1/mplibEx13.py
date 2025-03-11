import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('fine_dust.xlsx', index_col='area')
print(data)

data2016=data[2016]
data2017=data[2017]
data2018=data[2018]
data2019=data[2019]

plt.figure(figsize=(15,4))
# plt.plot(data2016, color='b', marker='o', label='2016')
# plt.plot(data2017, color='orange', marker='o', label='2017')
# plt.plot(data2018, color='green', marker='o', label='2018')
# plt.plot(data2019, color='red', marker='o', label='2019')
for year in range(2016, 2020):
    chartdata = data[year]
    plt.plot(chartdata, marker='s', label=year)

plt.xlabel('area')
plt.ylabel('micrometer')
plt.title('2018 Fine dust line graph')
plt.grid(True)
plt.legend(loc=1)
plt.show()