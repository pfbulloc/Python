import matplotlib.pyplot as plt
import numpy as np

# Define time steps (arbitrary for demonstration)
time = np.linspace(0, 100, 10)

# Random 5-bit values for a and b (max 31 for 5 bits)
a_values = [3, 7, 15, 23, 27, 28, 30, 31, 17, 10]  # Example 5-bit values for a
b_values = [1, 5, 10, 20, 25, 24, 28, 30, 15, 5]   # Example 5-bit values for b

# Calculate y = 1 if a > b, else 0
y_values = [1 if a > b else 0 for a, b in zip(a_values, b_values)]  # a > b logic

# Create the plot
fig, axs = plt.subplots(3, 1, figsize=(10, 6), sharex=True)

# Plot the 5-bit values of a
axs[0].step(time, a_values, where='post', label='a[4:0]', color='blue')
axs[0].set_ylabel('a[4:0]')
axs[0].set_ylim(0, 32)
axs[0].grid(True)

# Plot the 5-bit values of b
axs[1].step(time, b_values, where='post', label='b[4:0]', color='green')
axs[1].set_ylabel('b[4:0]')
axs[1].set_ylim(0, 32)
axs[1].grid(True)

# Plot the output y = a > b
axs[2].step(time, y_values, where='post', label='y = a > b', color='red')
axs[2].set_ylabel('y = a > b')
axs[2].set_xlabel('Time')
axs[2].set_ylim(-0.1, 1.1)
axs[2].grid(True)

# Show the plot
plt.tight_layout()
plt.show()
