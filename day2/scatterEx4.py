import pandas as pd
import matplotlib.pyplot as plt

diamonds = pd.read_csv('diamonds.csv')
#diamonds.info()
diamonds = diamonds.sample(frac=0.01, random_state=49)
diamonds.info()
cut_list = diamonds['cut'].unique()
print(cut_list) # ['Very Good' 'Good' 'Ideal' 'Premium' 'Fair']
print()

my_color = ['r', 'g', 'b', 'y', 'm']
cut_dict = {cut_list[idx]: my_color[idx] for idx in range(len(cut_list))}
print(cut_dict) # {'Very Good': 'r', 'Good': 'g', 'Ideal': 'b', 'Premium': 'y', 'Fair': 'm'}
diamonds['newcut'] = diamonds['cut'].map(cut_dict)
print(diamonds.head())
print()

def recode_table(table):
    if table >= 60:
        return 100
    elif table >= 58:
        return 30
    elif table >= 54:
        return 5
    else:
        return 1

diamonds['newtable'] = diamonds['table'].apply(recode_table)
#print(diamonds.head(10))

fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(111)
xdata = diamonds['price']
ydata = diamonds['depth']

ax1.scatter(xdata, ydata, s=diamonds['newtable'], c=diamonds['newcut'], alpha=0.7)
plt.xlabel('price')
plt.ylabel('depth')

import matplotlib.patches as patches
plt.legend(handles=[patches.Patch(color='r', label='Very Good'),
                    patches.Patch(color='g', label='Good'),
                    patches.Patch(color='b', label='Ideal'),
                    patches.Patch(color='y', label='Premium'),
                    patches.Patch(color='m', label='Fair')])
plt.show()