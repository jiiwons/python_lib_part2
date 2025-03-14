# 3.final_exam.csv 파일을 이용하여 아래와 같이 막대그래프를 그리시오(파일 로딩시 encodingf='cp949' 사용)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('final_exam.csv', encoding='cp949', index_col='names')
korean = data['korean']

# sns.barplot(x='names', y='korean', data=data, palette = ['tab:blue', 'tab:orange', 'tab:red', 'tab:green', 'tab:purple'])
#
# plt.xlabel('학생 이름')
# plt.ylabel('점수')
# plt.title('국어 점수')
# plt.show()
def makeBarchart1(x, y, color, xlabel, ylabel, title):
    plt.figure(figsize=(8,6))
    plt.bar(x,y,color=colors, alpha=0.7)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title, fontsize=16)

    for idx in range(y.size):
        value = f'{y[idx]}점'
        plt.text(x=idx, y=y[idx], s=value, ha ='center', fontsize=9)

    meanval = y.mean()
    meantext=f'평균:{int(meanval)}점'
    plt.axhline(y=meanval, color='r', linewidth=1, linestyle='--')
    plt.text(x=0, y=meanval, s=meantext, ha='center', fontsize=11)
    plt.yticks(np.arange(0, 110, 10))
    plt.show()

colors = ['b', 'g', 'r', 'c', 'm']
makeBarchart1(x=korean.index, y=korean, color=colors,
              xlabel='학생 이름', ylabel='점수', title='국어 점수')