import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


np.random.seed(777)
frame = pd.DataFrame(np.random.rand(5,3),
                     index=['customer1', 'customer2', 'customer3', 'customer4', 'customer5'],
                     columns=['metric1', 'metric2', 'metric3'])
print(frame)

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(7,5))

frame.plot(kind='bar', ax=ax1, alpha=0.75, title='bar plot')
ax1.set_label('customer')
ax1.set_ylabel('value')
plt.setp(ax1.get_xticklabels(), rotation=45)

colors=dict(boxes='blue', whiskers='grey', medians='orange', caps='green')
frame.plot(kind='box', ax=ax2, title='box plot', color=colors)
ax2.set_xlabel('metrics')
ax2.set_ylabel('value2')
plt.tight_layout()
plt.show()