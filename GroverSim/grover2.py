import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

N = 1000
a = 500
x = np.repeat(1/np.sqrt(N), N)
indices = np.arange(N)

fig, ax = plt.subplots()
ax.set_xlim(0, N)
ax.set_ylim(-1.2, 1.2)
line, = ax.plot(indices, x)

def animate(i):
    global x
    x[a] = -x[a]
    x = 2*np.mean(x) - x
    line.set_ydata(x)
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1,100), interval=100)
plt.show()
