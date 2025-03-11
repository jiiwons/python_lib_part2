import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import lineStyles

plt.rc('font', family='Malgun Gothic')
kbo = pd.read_csv('kbo.csv', encoding='cp949')
print(kbo)

xdata =  kbo.loc[:, 'AVG']
ydata =  kbo.loc[:, 'HR']
plt.figure(figsize=(8,4))
plt.plot(xdata, ydata, marker='o', linestyle= 'none')
plt.xlabel('타율')
plt.ylabel('홈런')
plt.title('산점도 그래프')
plt.grid(True, color='w', lw=1)
plt.gca().patch.set_facecolor('0.9')
plt.show()