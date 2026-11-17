"""
Program name: Plotting Cubic Numbers
Author: Raymond Black
Purpose: The purpose of the program is to visualize cubic numbers.
Resource: Starter code was obtained from Python Crash Course, 3rd Edition "scatter_squares.py" example.
Date: 2026-11-17
"""

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(x_values, y_values, color="red", s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

ax.ticklabel_format(style="plain")

plt.show()

# save to a file
# plt.savefig('squares_plot.png', bbox_inches='tight')
