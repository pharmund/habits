import calmap
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('src/habits.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

yoga = pd.Series(df.Yoga)
plt.figure(figsize=(14, 6))
calmap.yearplot(data=yoga, year=2024)
plt.suptitle('Yoga 2024', y=.65, fontsize=15)
plt.show(block=True)

skates = pd.Series(df.Skates)
plt.figure(figsize=(14, 6))
calmap.yearplot(data=skates, year=2024)
plt.suptitle('Skates 2024', y=.65, fontsize=15)
plt.show(block=True)
