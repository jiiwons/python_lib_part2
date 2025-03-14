import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

np.random.seed(777)

plt_data1 = np.random.randn(50).cumsum()
plt_data2 = np.random.randn(50).cumsum()
plt_data3 = np.random.randn(50).cumsum()
plt_data4 = np.random.randn(50).cumsum()
print(plt_data4)
# x = np.linspace(0, 50, 50)

# plt.plot(x, plt_data1,
#          "bo-", label='Blue Solid')
# plt.plot(x, plt_data2,
#          "r*--", label='Red Dashed')
# plt.plot(x, plt_data3,
#          "g*-.", label='Green Dash Dot')
# plt.plot(x, plt_data4,
#          "yd:", label='Orange Dotted')

# 강사님 코드
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.plot( plt_data1, marker='o', color='blue', linestyle='-', label='Blue Solid')
plt.plot(plt_data2,marker='+', color='red', linestyle='--', label='Red Dashed')
plt.plot(plt_data3,marker='*', color='green', linestyle='-.',label='Green Dash Dot')
plt.plot(plt_data4, marker='s', color='orange', linestyle=':', label='Orange Dotted')

# ax1.xaxis.set_ticks_position('top')
# ax1.yaxis.set_ticks_position('right')

ax1.set_title('Line Plots: Markers, Colors, and LineStyles', fontsize=16)
plt.xlabel('Draw')
plt.ylabel('Random Number')
plt.legend(loc=1)

# plt.savefig('line_plot_quiz.png', dpi=400, bbox_inches='tight')
# plt.show()