import numpy as np
import matplotlib.pyplot as plt
import os

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PARENT_DIR, "data","task1", "dead_moroz")
RESULT_DIR = os.path.join(PARENT_DIR, "src_out","task1")
N_FILES = 5

def read_data_from_file(filename):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'r') as f:
        N_points = int(f.readline())
        points = []
        for _ in range(N_points):
            line = f.readline().strip()
            x, y = map(float, line.split())
            points.append((x, y))
        return np.array(points)

for i in range(1, N_FILES + 1):
    filename = f'00{i}.dat'
    points = read_data_from_file(filename)
    x_coords = points[:, 0]
    y_coords = points[:, 1]

    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, s=50, marker='.', edgecolors='red', linewidths=0.5)

    plt.title(f"Эпизод 1 - Data from {filename}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True, linestyle='--', alpha=0.7)

    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)

    x_range = x_max - x_min
    y_range = y_max - y_min
    padding_x = x_range * 0.1
    padding_y = y_range * 0.1

    plt.xlim(x_min - padding_x, x_max + padding_x)
    plt.ylim(y_min - padding_y, y_max + padding_y)

    plt.gca().set_aspect('equal', adjustable='box')

    plt.savefig((os.path.join(RESULT_DIR, f"00{i}.png")), dpi=600, bbox_inches='tight')
    plt.show() 
    plt.close()