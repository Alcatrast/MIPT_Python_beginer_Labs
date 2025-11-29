import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

with open("task2.txt", 'r') as f:
    N = int(f.readline())
    A = np.zeros((N, N))
    for i in range(N):
        a_i = np.array(list(map(float, f.readline().split())))
        A[i] = a_i
    b = np.array(list(map(float, f.readline().split())))
x = linalg.solve(A, b)

bars = plt.bar(range(1, N + 1), x)
plt.grid(True)
plt.tight_layout()
plt.show()