import numpy as np
import matplotlib.pyplot as plt

file_path = r"signals\signal"
for i in range(1, 4):
    with open(f"{file_path}0{i}.dat") as f:
        data = np.array([float(line) for line in f])
        filtered = np.zeros_like(data)
        for j in range(data.size):
            if j < 10:
                filtered[j] = data[:j + 1].mean()
            else:
                filtered[j] = data[j - 9:j + 1].mean()
        fig, axs = plt.subplots(nrows=1, ncols=2)
        t = np.array(range(1, data.size+1))
        axs[0].plot(t, data)
        axs[0].grid(True)
        axs[0].set_title("Без фильтрации")
        axs[1].plot(t, filtered)
        axs[1].set_title("С фильтрацией")
        axs[1].grid(True)
        plt.tight_layout()
        plt.show()
