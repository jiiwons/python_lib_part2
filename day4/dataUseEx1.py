import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

welfare = pd.read_csv('welfare_python.csv', encoding='utf-8')
welfare.info()
print(welfare.head())

welfare.loc[welfare['gender']== 1, ['gender']]='남성'
welfare.loc[welfare['gender']== 2, ['gender']]='여성'

thisyear=2000
welfare['age'] = thisyear - welfare['birth']

# welfare['marriage'] = welfare['marriage'].map({1:" 결혼", 3:"이혼"})
# welfare['marriage'] = welfare['marriage'].fillna('무응답')
# print(welfare['marriage'].value_counts())
## 강사님 코드
def setMarriage(x):
    if x==1:
        return '결혼'
    elif x==3:
        return '이혼'
    else:
        return '무응답'

welfare['marriage'] = welfare['marriage'].map(setMarriage)

welfare.loc[welfare['income'].isnull(), 'income'] = welfare['income'].mean()

print(welfare.head())

jobFrame = pd.read_csv('welfare_job.csv', encoding='cp949')
print(jobFrame.head())
print()

welfare = pd.merge(welfare, jobFrame, on='code_job')
#print(welfare.head())
def setReligion(x):
    if x==1:
        return '있음'
    else:
        return '없음'

welfare['religion'] = welfare['religion'].map(setReligion)
print(welfare.iloc[4])
print()

def setCR(x):
    if int(x)==1:
        return '서울'
    elif int(x) == 2:
        return '수도권'
    elif int(x) == 3:
        return '부산/경남/울산'
    elif int(x) == 4:
        return '대구/경북'
    elif int(x) == 5:
        return '대전/충남'
    elif int(x) == 6:
        return '강원도/충북'
    elif int(x) == 7:
        return '광주/전남/전북/제주도'

welfare['code_religion'] = welfare['code_religion'].map(setCR)
print(welfare.iloc[4])
print()

def newAge(x):
    if x < 30:
        return '청년'
    elif x >= 30 and x < 60:
        return '중년'
    else:
        return '노년'

welfare['ageg'] = welfare['age'].map(newAge)
print(welfare.iloc[4])
print()

welfare = welfare.rename(columns={'gender':'성별', 'birth':'생일', 'marriage':'결혼유무', 'religion':'종교유무',
                        'code_job':'직업코드', 'income':'소득', 'code_religion':'지역구',
                        'age':'나이', 'job':'직업', 'ageg':'연령대'})
print(welfare.columns)

welfare.to_csv('welfareClean.csv', index=False, encoding='cp949')