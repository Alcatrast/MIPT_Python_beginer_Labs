import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("flights.csv", delimiter=',')
data = data.rename(columns={"Unnamed: 0": "id"})
total = data.groupby("CARGO")["id"].count().reset_index(name='flights_count')
total_sum = data.groupby("CARGO")["PRICE"].sum().reset_index(name='total_sum')
total_weight = data.groupby("CARGO")["WEIGHT"].sum().reset_index(name='total_weight')
total = pd.merge(total, total_sum, on="CARGO")
total = pd.merge(total, total_weight, on="CARGO")
print(total)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

ax1.bar(total['CARGO'], total['flights_count'], color='skyblue')
ax1.set_title('Total flights')
ax1.tick_params(axis='x', rotation=0)

ax2.bar(total['CARGO'], total['total_sum'], color='lightgreen')
ax2.set_title('Total sum')
ax2.tick_params(axis='x', rotation=0)

ax3.bar(total['CARGO'], total['total_weight'], color='lightcoral')
ax3.set_title('Total weight')
ax3.tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()