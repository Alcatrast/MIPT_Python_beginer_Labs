import pandas as pd

data = pd.read_csv("transactions.csv", delimiter=',')
print("Task1.1:")
print(data[data["STATUS"] == "OK"].nlargest(3, "SUM"))

print('=============')
target = data[data["CONTRACTOR"] == "Umbrella, Inc"]
target = target[target["STATUS"] == "OK"]
print(f'Task1.2\nTotal sum of "Umbreall, Inc": {target["SUM"].sum()}')