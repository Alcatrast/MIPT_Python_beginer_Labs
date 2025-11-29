from sympy import symbols, Function, Eq, dsolve
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = symbols('x')
y = Function('y')

equation = Eq(y(x).diff(x), -2 * y(x))
print(equation)

solution1 = dsolve(equation, ics={y(0): np.sqrt(2)})
print(solution1)


def model(y, x):
    dydx = -2 * y
    return dydx


y0 = np.sqrt(2)
xdata = np.linspace(0, 10, 100)
solution2 = odeint(model, y0, xdata)
print("=======")
print(solution2)

ydata = solution2[:, 0]

y_array = np.zeros_like(xdata)
for i, x_val in enumerate(xdata):
    y_val = solution1.rhs.subs(x, x_val)
    y_array[i] = float(y_val)
y_dif = abs(y_array - ydata)
fig, axs = plt.subplots(nrows=1, ncols=3)
axs[0].plot(xdata, y_array)
axs[1].plot(xdata, ydata)
axs[2].plot(xdata, y_dif)
axs[0].set_title("SymPy")
axs[1].set_title("SciPy")
axs[2].set_title("Difference")
for i in range(3):
    axs[i].grid(True)
plt.show()