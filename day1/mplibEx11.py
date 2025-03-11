import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(-4, 4, 1024)
# y = 0.25 * (x*4) * (x+1) * (x-2)
#
# plt.annotate('annotate text!!!!!!',
#              ha='left', va='bottom',
#              xytext=(-1.5, 20),
#              xy=(1.75, -2.8),
#              arrowprops={'facecolor':'r', 'shrink':0.5}) # shrink값이 클수록 짧아지는
# plt.plot(x,y,c='k')
# plt.show()

# align_list = ['center', 'left', 'right']
#
# ax1 = plt.gca()
# ax1.axes.get_xaxis().set_visible(False)
# ax1.axes.get_yaxis().set_visible(False)
#
# for i, align in enumerate(align_list):
#     plt.text(0,i,f'align={align}', ha=align, fontsize=14)
#
# plt.plot([0,0], [-1, len(align_list)], c='#808080', ls='--')
# plt.scatter([0]*len(align_list), range(len(align_list)))
# plt.show()

arrow_style_list = ['<->', '<-','->', 'wedge', 'fancy', 'simple']
plt.scatter([0] * len(arrow_style_list), range(len(arrow_style_list)), c='k')

for i, arrow_style in enumerate(arrow_style_list):
    plt.annotate('arrowstyle=%s'%arrow_style,
                 ha='left', va='center',
                 xytext=(0.75, i+0.5),
                 xy=(0.025, i),
                 arrowprops={'arrowstyle':arrow_style, 'facecolor':'k'})
plt.xlim(-0.5, 2)
plt.ylim(-0.5, 6.5)
plt.show()