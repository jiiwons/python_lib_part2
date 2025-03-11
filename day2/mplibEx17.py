import matplotlib.pyplot as plt
import pandas as pd

# df = pd.DataFrame({'day1':[7,1,5,6,3,0,5,8],
#                    'day2':[1,2,8,4,6,5,3,1]})
# plt.plot(df)
# lg = plt.legend(['day1', 'day2'], loc=1, title='t_legend', title_fontsize=14)
# lg._legend_box.sep = 20 # 간격 조절
# plt.show()



# plt.plot([2,3,5,9], label='values')
# plt.legend(loc=(0.2,0.5))
# plt.show()



plt.plot([2,3,5,7], label='value1')
plt.plot([0,1,7,3], label='value2')
plt.plot([5,6,9,5], label='value3')
plt.plot([7,5,8,3], label='value4')
plt.legend(loc=2, ncol=3)
plt.show()
