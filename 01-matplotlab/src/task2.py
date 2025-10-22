import numpy as np
import matplotlib.pyplot as plt
import os

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PARENT_DIR, "data", "task2")
RESULT_DIR = os.path.join(PARENT_DIR, "src_out", "task2")

def read_frames_data(filename):
    filepath = os.path.join(DATA_DIR, filename)
    all_x_data = []
    all_y_data = []

    try:
        with open(filepath, 'r') as f:
            line_count = 0
            for line in f:
                line = line.strip()
                if line:
                    coords = np.array(list(map(float, line.split())))
                    if line_count % 2 == 0:
                        all_x_data.append(coords)
                    else:
                        all_y_data.append(coords)
                    line_count += 1
        return all_x_data, all_y_data
    except Exception:
        print(f"Ошибка при чтении файла")
        raise Exception

all_x_data, all_y_data = read_frames_data("frames.dat")

N_FRAMES = len(all_x_data)
all_x_values = np.concatenate(all_x_data)
all_y_values = np.concatenate(all_y_data)
x_min, x_max = np.min(all_x_values) - 1, np.max(all_x_values) + 1
y_min, y_max = np.min(all_y_values) - 1, np.max(all_y_values) + 1

nrows = int(np.ceil(np.sqrt(N_FRAMES)))
ncols = int(np.ceil(N_FRAMES / nrows))

fig, axes = plt.subplots(nrows, ncols, figsize=(5 * ncols, 4 * nrows))

if nrows * ncols > 1:
    axes_flat = axes.flatten()
else:
    axes_flat = [axes]

for i in range(N_FRAMES):
    ax = axes_flat[i]
    x_coords = all_x_data[i]
    y_coords = all_y_data[i]
    ax.plot(x_coords, y_coords, marker='o', linestyle='-', markersize=3)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.grid(True, linestyle=':', alpha=0.8)
    ax.set_title(f"Frame {i}")

fig.text(0.5, 0.04, 'X', ha='center')
fig.text(0.04, 0.5, 'Y', va='center', rotation='vertical')

plt.tight_layout(rect=[0.05, 0.05, 1, 0.96])

output_filepath = os.path.join(RESULT_DIR, "res.png")
plt.savefig(output_filepath, dpi=300, bbox_inches='tight')

plt.show()
plt.close(fig)