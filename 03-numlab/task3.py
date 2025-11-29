import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open("task3.txt", "r") as f:
    u1 = np.array([float(line.strip()) for line in f])

N = u1.size
A = np.zeros((N, N))
np.fill_diagonal(A, 1)
np.fill_diagonal(A[1:], -1)
A[0, -1] = -1
t = np.linspace(0, 50, 50)
u_n = u1.copy()
all_states = np.zeros((256, N))
all_states[0] = u1.copy()

for n in range(255):
    u_next = u_n - 0.5 * (A @ u_n)
    all_states[n + 1] = u_next.copy()
    u_n = u_next

fig, ax = plt.subplots()
line, = ax.plot(t, all_states[0])
ax.grid(True)
ax.set_ylim(all_states.min(), all_states.max())

def animate(frame):
    line.set_ydata(all_states[frame])
    return line,

anim = animation.FuncAnimation(
    fig,
    animate,
    frames=256,
    interval=50,
    blit=False,
    repeat=True
)

plt.tight_layout()
plt.show()