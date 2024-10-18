import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y1, label='Sine function')
plt.title("Sine Function")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.legend()
plt.savefig("sine_plot.png", dpi=300)
plt.show()

x = np.linspace(-5, 5, 100)
y2 = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

plt.figure(figsize=(6, 4))
plt.plot(x, y2, color='r', label='Gaussian Distribution')
plt.title("Standard Normal Distribution")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.grid(True)
plt.legend()
plt.savefig("gaussian_plot.png", dpi=300)
plt.show()


x = np.linspace(0, 5, 100)
y3 = np.exp(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y3, color='g', label='Exponential Function')
plt.title("Exponential Function")
plt.xlabel("x")
plt.ylabel("exp(x)")
plt.grid(True)
plt.legend()
plt.savefig("exponential_plot.png", dpi=300)
plt.show()
