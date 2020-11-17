import matplotlib.pyplot as plt
import numpy as np

def func(x, y):
    return 1 / (x + 1) - 5 / (y**2 + 1)

d = 2
dx = 0.001
N = (int)(d / dx)

x = np.zeros(N + 2)
y = np.zeros(N + 2)
f = np.zeros(N + 3)

x[0] = 1
y[0] = 1

f[0] = func(x[0], y[0])
y[1] = y[0] + dx * f[0]

f[1] = func(x[0] + dx, y[1])
y[2] = y[1] + dx * f[1]

f[2] = func(x[0] + 2*dx, y[2])
y[3] = y[2] + dx * f[2]

f[3] = func(x[0] + 3*dx, y[3])

for n in range(1, N):
    x[n] = x[0] + n * dx
    y[n + 1] = y[n] + (dx / 24) * (-f[n + 2] + 13 * f[n + 1] + 13 * f[n] - f[n - 1])
    y[n + 2] = y[n + 1] + dx * f[n + 1]
    f[n + 3] = func(x[0] + (n + 3)*dx, y[n + 2] + dx * f[n + 2])

plt.scatter(x[:N], y[:N], label='Result', color='r', marker='*', s=5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()