import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Malgun Gothic')

df = pd.read_csv('exam2.csv', encoding='cp949')
print(df)

fig, ax = plt.subplots(1,1,figsize=(9,9))

HUNDRED = 80
MIN_HEIGHT = 30
MAX_HEIGHT = HUNDRED + 5

ax.vlines(x=1, ymin=MIN_HEIGHT, ymax=MAX_HEIGHT, color='k', alpha=0.7, linewidth=1, ls='dotted')
ax.vlines(x=3, ymin=MIN_HEIGHT, ymax=MAX_HEIGHT, color='k', alpha=0.7, linewidth=1, ls='dotted')

ax.scatter(x=np.repeat(1, df.shape[0]),y=df['midexam'], s=10, color='k', alpha=0.7)
ax.scatter(x=np.repeat(3, df.shape[0]),y=df['finalexam'], s=10, color='k', alpha=0.7)

left_label = [f'{c}({y}점)' for c, y in zip(df.name, df['midexam'])]
right_label = [f'{c}({y}점)' for c, y in zip(df.name, df['finalexam'])]

import matplotlib.pyplot as lines

def newline(p1, p2):
    ax = plt.gca()
    lo = lines.Line2D([p1[0], p2[0]], [p1[1], p2[1]],
                      color='red' if p1[1] - p2[1] > 0 else 'green',
                      marker='o',
                      markersize=6)
    ax.add_line(lo)

for idx, (p1, p2) in enumerate(zip(df['midexam'], df['finalexam'])):
    newline([1, p1], [3,p2])
    ax.text(1-0.05, p1, left_label[idx], ha='right', fontsize=14)
    ax.text(3+ 0.05, p2, right_label[idx], ha='left', fontsize=14)
    
ax.set_title('시험 점수', fontsize=20)
ax.set(xlim=(0,4), ylim=(MIN_HEIGHT, MAX_HEIGHT), ylabel=('시험 점수'))
ax.set_xticks([1,3])
ax.set_xticklabels(['중간 고사', '기말 고사'])

plt.gca().spines['top'].set_alpha(0)
plt.gca().spines['bottom'].set_alpha(0)
plt.gca().spines['left'].set_alpha(0)
plt.gca().spines['right'].set_alpha(0)
plt.show()