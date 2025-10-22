import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PARENT_DIR, "data", "task3")
RESULT_DIR = os.path.join(PARENT_DIR, "src_out", "task3")

def read_and_process_data(filepath):
    df = pd.read_csv(filepath, sep=';', header=None, names=['prep', 'group', 'mark'])
    df['group'] = df['group'].astype(str)
    return df
df = read_and_process_data(os.path.join(DATA_DIR, "students.csv")) # Указываем полный путь

prep_counts = df.groupby(['prep', 'mark']).size().unstack(fill_value=0)
group_counts = df.groupby(['group', 'mark']).size().unstack(fill_value=0)
MARKS = sorted(df['mark'].unique())

prep_counts = prep_counts[MARKS]
group_counts = group_counts[MARKS]

fig, axes = plt.subplots(2, 1, figsize=(12, 10))
colors = plt.cm.viridis(np.linspace(0, 1, len(MARKS)))
ax1 = axes[0]

x = prep_counts.index
width = 0.1
x_positions = np.arange(len(x))

for i, mark in enumerate(MARKS):
    ax1.bar(x_positions + (i * width) - (((len(MARKS) - 1) / 2) * width),
            prep_counts[mark],
            width=width,
            label=str(mark),
            color=colors[i])
    
ax1.set_title('Распределение оценок по преподавателям')
ax1.set_ylabel('Количество студентов')
ax1.set_xlabel('Преподаватель')
ax1.set_xticks(x_positions)
ax1.set_xticklabels(x)

ax1.legend(title='Оценка')
ax2 = axes[1]

x = group_counts.index
width = 0.1
x_positions = np.arange(len(x))

for i, mark in enumerate(MARKS):
    ax2.bar(x_positions + (i * width) - (((len(MARKS) - 1) / 2) * width),
            group_counts[mark],
            width=width,
            label=str(mark),
            color=colors[i])

ax2.set_title('Распределение оценок по группам')
ax2.set_ylabel('Количество студентов')
ax2.set_xlabel('Группа')
ax2.set_xticks(x_positions)
ax2.set_xticklabels(x)

ax2.legend(title='Оценка')

fig.tight_layout()
plt.savefig(os.path.join(RESULT_DIR, 'res.png'), dpi=300, bbox_inches='tight')
plt.show()
plt.close(fig)