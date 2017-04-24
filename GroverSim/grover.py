import matplotlib.pyplot as plt
import numpy as np

N = 100
y = 20
iterations = 2500
vals = (1 / np.sqrt(N)) * np.ones(N)
y_amp = np.zeros(iterations)
xs = np.arange(0, iterations)
means = np.zeros(iterations)
zeros = np.zeros(iterations)

iters = []
count = 0
maxs = []

i = 0
while (i < iterations):
	vals[y - 1] = -vals[y - 1]
	mean = np.mean(vals)
	vals = mean * 2 - vals
	y_amp[i] = vals[y - 1]

	if (i > 3 and y_amp[i] < y_amp[i - 1] and y_amp[i - 1] > y_amp[i - 2]):
		iters.append(count)
		maxs.append(y_amp[i - 1])
		count += 1
		print(y_amp[i - 1])

	means[i] = mean
	
	i += 1

plt.plot(xs, y_amp)
plt.plot(xs, means)
plt.plot(xs, zeros)
plt.savefig('grover.png')

plt.close()
plt.plot(iters, maxs)
plt.savefig('tops.png')