import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc # 폰트 세팅을 위한 모듈 추가
font_path = "C:\Windows\Fonts\malgun.ttf" # 사용할 폰트명 경로 삽입
font = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)

data = pd.read_csv('tips.csv')
print(data)

# total_bill = data['total_bill']
# print(total_bill)
#
# tips = data['tip']
# print(tips)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.plot(total_bill, 'r-')
# ax1.set_ylabel('결제 금액')
#
# ax2.plot(tips, 'b-')
# ax2.set_ylabel('팁(tip)')
#
# plt.suptitle('결제 금액과 Tip(이중 축)')
# plt.show()

## 강사님 코드
xrange = range(len(data))
data_bill = data.loc[:, ['total_bill']]
data_tip = data.loc[:, ['tip']]

fig, ax1 = plt.subplots() # subplot과 subplots의 차이: subplots는 default로 1,1 이 매개변수로 들어가있음

ax1.set_title('결제 금액과 Tip(이중 축)')

color = 'tab:red'

ax1.set_ylabel('결제 금액', color=color)
ax1.plot(xrange, data_bill, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2=ax1.twinx()

color = 'tab:blue'

ax2.set_ylabel('팁(tip)', color=color, rotation=0)
ax2.plot(xrange, data_tip, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()