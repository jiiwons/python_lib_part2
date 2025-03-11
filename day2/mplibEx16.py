import matplotlib.pyplot as plt

ax1 = plt.gca()
ax2 = ax1.twinx() # ax1와 ax2가 다른 객체 -> legend를 하면 레이블2개가 안 나옴

ln1 = ax1.plot([10, 5, 3, 12, 7], 'r--', label='y1')
ax1.set_ylabel('y1')

ln2 = ax2.plot([100, 200, 220, 170, 120], 'b:', label='y2')
ax2.set_ylabel('y2')

lns = ln1 + ln2
labels = [l.get_label() for l in lns]
print(labels)

plt.legend(lns, labels, loc=0)
plt.show()