import numpy as np
import matplotlib.pyplot as plt

# shape = plt.Circle((0,0), radius=1, color='#00ff00')
# plt.gca().add_patch(shape) # getcurrentaxis : 현재의 axes 객체를 구할 수 있음
# # plt.xlim(-1,1)
# # plt.ylim(-1,1)
# plt.axis('scaled') # plt의 객체를 보고서 자동으로 스케일을 조정
# plt.show()

import matplotlib.patches as patches

# shape = patches.Circle((0,0), radius=1, color='0.2')
# plt.gca().add_patch(shape)
#
# shape2 = patches.Rectangle((2.5, -0.5), 2, 1, color='0.5')
# plt.gca().add_patch(shape2)
#
# shape3 = patches.Ellipse((0,-2), 2, 1,angle=45, color='0.8')
# plt.gca().add_patch(shape3)
#
# plt.axis('scaled')
# plt.grid(True)
# plt.show()

# N = 16
# for i in range(N):
#     plt.gca().add_line(plt.Line2D((0,i), (N-i,0), color='r'))
# plt.axis('scaled')
# plt.grid(True)
# plt.show()

point=np.array([[1,1],[3,0],[8,3],[5,5],[1,1]])
shape = patches.Polygon(point, lw=3, edgecolor='k', ls='dashed', facecolor='r')
plt.gca().add_patch(shape)
plt.axis('scaled')
plt.grid(True)
plt.show()
