import matplotlib.pyplot as plt
import numpy as np

time = np.linspace(0, 100, 10)
a_values = [3, 7, 15, 23, 27, 28, 30, 31, 17, 10]
b_values = [1, 5, 10, 20, 25, 24, 28, 30, 15, 5]
y_values = [1 if a > b else 0 for a, b in zip(a_values, b_values)]

fig, axs = plt.subplots(3, 1, figsize=(10, 6), sharex=True)
axs[0].step(time, a_values, where='post', label='a[4:0]', color='blue')
axs[1].step(time, b_values, where='post', label='b[4:0]', color='green')
axs[2].step(time, y_values, where='post', label='y = a > b', color='red')
plt.tight_layout()
plt.show()


