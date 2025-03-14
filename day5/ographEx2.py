from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots(figsize=(10,4))

# gender = ['male', 'male', 'male', 'female', 'female', 'female']
# pet = ['cat', 'dog', 'dog', 'cat', 'dog', 'cat']
# t_col=[2,3,4,5,6,7]
# data = pd.DataFrame({'gender':gender,
#                      'pet':pet,
#                      'tvalue':t_col})
# # print(data)
# props = lambda key : {'color':'lightblue' if 'cat' in key else 'red'}
# mosaic(data, ['pet', 'gender'], title='mosaic graph', ax=ax, properties=props, gap=0.06, horizontal=False)
# plt.show()

plt.rc('font', family='Malgun Gothic')

url = 'https://raw.github.com/mattdelhey/kaggle-titanic/master/Data/train.csv'
titanic = pd.read_csv(url)
# titanic.info()
titanic = titanic[['survived', 'pclass', 'sex']]
# print(titanic.head(10))

titanic['survive'] = titanic.survived.map({0:'사망', 1:'생존'})
titanic['class'] = titanic.pclass.map({1:'1등급', 2:'2등급', 3:'3등급'})
titanic['gender'] = titanic.sex.map({'male':'남성', 'female':'여성'})
print(titanic.head())
props = lambda key : {'color':'orange' if '생존' in key else 'grey'}
mosaic(titanic.sort_values('class'), ['survive', 'class'], properties=props, gap=0.04, ax =ax)
plt.title('객실 등급 비율에 따른 사망 비율', fontsize=14)
plt.show()