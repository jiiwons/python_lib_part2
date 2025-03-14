import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Malgun Gothic')

df = pd.read_csv('medical.csv')
df.info()
print()

print(df.describe()) # min에 -1값이 있음

# df = df.drop(df[df['Age']<0].index)
## 강사님 코드
df = df[df.Age>=0]
print(df.describe())
print()

df['No-show'] = df['No-show'].map({'No': 0, 'Yes':1})
# print(df['No-show'].unique())
# print(df['No-show'].value_counts())

# print(df[['ScheduledDay', 'AppointmentDay']])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
# df.info()

df['waiting_day'] = df['AppointmentDay'].dt.dayofyear - df['ScheduledDay'].dt.dayofyear
# df.info()
# print(df.head())
df = df[df.waiting_day>=0]
print(df.describe()['Age'])
import seaborn as sns

df = df[df.Age <=105]
# plt.figure(figsize=(14,2))
# sns.barplot(x=df.Age)
# plt.show()

# 당일 예약한 사람의 노쇼 비율
# today = df['ScheduledDay'].dt.day - df['AppointmentDay'].dt.day
# print(today.value_counts())
# print(df[today==0]['No-show'].value_counts())
## 강사님 코드
wtotal = df[df.waiting_day==0]['waiting_day'].value_counts()
ntotal = df[(df['waiting_day']==0) & (df['No-show']==1)]['waiting_day'].value_counts()
print(wtotal)
print(ntotal)
print()
print(ntotal/wtotal)

no_show = df[df['No-show']==1]
show = df[df['No-show']==0]
#
# no_show[no_show['waiting_day']<=10]['waiting_day'].hist(alpha=0.7, label='no_show')
# show[show['waiting_day']<=10]['waiting_day'].hist(alpha=0.3, label='no_show')
# plt.legend(loc='best')
# plt.show()

# no_show['ScheduledDay'].hist(alpha=0.7, label='no-show')
# show['ScheduledDay'].hist(alpha=0.7, label='show')
# plt.legend(loc='best')
# plt.show()

# x축은 수신 동의여부, y축은 waiting_day에 따른 No-show 빈도수
# sns.barplot(x='SMS_received', y='waiting_day', hue='No-show', data=df)
# plt.show()

# 성별에 따른 No-show
# sns.countplot(x='Gender', hue='No-show', data=df)
# plt.show()

woman_noshow = df[(df['Gender']=='F')&(df['No-show']==1)]['Gender'].value_counts()
man_noshow = df[(df['Gender']=='M')&(df['No-show']==1)]['Gender'].value_counts()
woman_total = df[df['Gender']=='F']['Gender'].value_counts()
man_total = df[df['Gender']=='M']['Gender'].value_counts()

print(f'노쇼 여성 비율:{woman_noshow/woman_total}')
print(f'노쇼 남성 비율:{man_noshow/man_total}')