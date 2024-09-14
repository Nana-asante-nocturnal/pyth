import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('scores.csv')

x = df['Name']
y = df["English Score"]

plt.xlabel('Name', fontsize=10)
plt.ylabel("Math Score", fontsize=16)
plt.bar(x, y)

plt.show()
