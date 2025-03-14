# 2.unemployment_rate.csv 파일을 이용하여 아래와 그림과 같이 선그래프를 그리시오(파일 로딩시 encoding='cp949' 사용)
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

df = pd.read_csv('unemployment_rate.csv', encoding='cp949', index_col='연도')
print(df)

data2001 = df.iloc[0]
data2002 = df.iloc[1]
data2003 = df.iloc[2]
data2004 = df.iloc[3]
data2005 = df.iloc[4]
print(data2001)
plt.figure(figsize=(12,8))
plt.plot(data2001, color='blue', marker='o', label='2001년')
plt.plot(data2002, color='orange', marker='o', label='2002년')
plt.plot(data2003, color='green', marker='o', label='2003년')
plt.plot(data2004, color='red', marker='o', label='2004년')
plt.plot(data2005, color='purple', marker='o', label='2005년')

plt.xlabel('연령대')
plt.ylabel('연도명')
plt.title('연령대별 연도명 꺾은 선')
plt.legend(loc=1)
plt.show()