import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# x = np.linspace(-15, 15, 1024)
# y = np.sinc(x)
#
# # ticker를 사용하려면 현재 axis 객체를 가져와야함
# #ax = plt.gca() #이렇게 사용해도 되지만 아래 방법을 더 권장
# ax = plt.axes()
# ax.xaxis.set_major_locator(ticker.MultipleLocator(5)) # major단위를 5단위로
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(1)) # 눈금 1단위로
# plt.plot(x, y, c='k')
# plt.show()



# ax = plt.gca()
#
# def make_label(value, pos):
#     return f'{100*value:.1f}%'
# ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))
#
# x = np.linspace(0, 1, 256)
# plt.plot(x, np.exp(-10*x), c='k')
# plt.show()



import datetime
start_time = datetime.datetime(2025,1,1)

ax = plt.gca()

def make_label(value, pos):
    time = start_time + datetime.timedelta(days=365*value)
    return time.strftime('%b %y ')

ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))

x = np.linspace(0, 1, 256)
plt.plot(x, np.exp(-10*x), c='k')
x_labels = ax.get_xticklabels()
plt.setp(x_labels, rotation=30, fontsize=12)
plt.show()

