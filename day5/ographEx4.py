import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df = px.data.tips()
print(df.head())

# fig = px.parallel_categories(df)
# fig.show()

fig = px.parallel_categories(df, dimensions=['sex', 'smoker', 'day'],
                             color='size',
                             labels={'sex':'payer_sex','smoker':'smoker at the table', 'day':'day of week'})