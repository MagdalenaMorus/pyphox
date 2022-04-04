import pandas as pd
import matplotlib.pyplot as plt


ACC_PATH = 'data/Raw Data.csv'
df = pd.read_csv(ACC_PATH)
df = df[df.columns[1]]
print(df)
df.plot()
plt.title('acceleration x in time')
plt.grid(True)
plt.show()