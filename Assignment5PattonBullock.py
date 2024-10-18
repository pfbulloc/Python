import numpy as np
import matplotlib.pyplot as plt

# Load the data from the provided CSV file
file_path = 'assignment5_data(1).csv'
data = np.loadtxt(file_path, delimiter=',')

# Extracts time and voltage columns
time_data = data[:, 0]
voltage_data = data[:, 1]

# Step II: Compute y(t) = cos(4πt)
y_t = np.cos(4 * np.pi * time_data)

# Step III: Plot both curves using all data points
plt.figure(figsize=(10, 6))
plt.plot(time_data, y_t, label="Exact", linestyle='-', color='blue')  # continuous line for the exact function
plt.scatter(time_data, voltage_data, label="Noisy", color='red')  # dots for the noisy data

# Labels the plot
plt.xlabel('Time, s')
plt.ylabel('Voltage, V')
plt.legend()
plt.title('Plot of Exact Function and Noisy Data (All Points)')
plt.grid(True)

# Displays the plot for all data points
plt.show()

# Step V: Plot both curves using only the first 25 data points
plt.figure(figsize=(10, 6))
plt.plot(time_data[:25], y_t[:25], label="Exact", linestyle='-', color='blue')  # continuous line for the exact function
plt.scatter(time_data[:25], voltage_data[:25], label="Noisy", color='red')  # dots for the noisy data

# Labels the plot
plt.xlabel('Time, s')
plt.ylabel('Voltage, V')
plt.legend()
plt.title('Plot of Exact Function and Noisy Data (First 25 Points)')
plt.grid(True)

# Displays the plot for the first 25 data points
plt.show()
