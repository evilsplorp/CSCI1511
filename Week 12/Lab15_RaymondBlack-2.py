"""
Program name: Plotting Cubic Numbers
Author: Raymond Black
Purpose: The purpose of the program is to visualize cubic numbers.
Resource: Starter code was obtained from Python Crash Course, 3rd Edition "scatter_squares.py" example.
Date: 2026-11-18
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.style.use("seaborn-v0_8")

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

x_values_5k = range(1, 5001)
y_values_5k = [x**3 for x in x_values_5k]

# begin set of manual values
fig1, ax_small = plt.subplots(figsize=(12, 8))


def plot_cubes(x_values, y_values, ax_small):
    ax_small.scatter(x_values, y_values, color="red", s=30)

    # Set chart title and label axes.
    ax_small.set_title("First Five Cubic Numbers", fontsize=24)
    ax_small.set_xlabel("Value", fontsize=14)
    ax_small.set_ylabel("Cube of Value", fontsize=14)

    # Set size of tick labels.
    ax_small.tick_params(labelsize=14)

    # Set the range for each axis. large values
    ax_small.axis([0, 6, 0, 150])
    ax_small.ticklabel_format(style="plain")


plot_cubes(x_values, y_values, ax_small)

# save to a file
plt.savefig("cubes_5.png", bbox_inches="tight")
plt.close(fig1)

# end set of manual values

# begin set of 5k range values

fig2, ax = plt.subplots(figsize=(12, 8))
ax.scatter(x_values_5k, y_values_5k, color="blue", s=10)

ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

ax.set_title("First 5000 Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis. large values
ax.axis([0, 5_100, 0, 130_000_000_000])


# save to a file
plt.savefig("cubes_5k.png", bbox_inches="tight")
plt.close(fig2)

# end set of 5k range values

# combined charts in a single image

fig3, (ax_small, ax) = plt.subplots(1, 2, figsize=(20, 8))

ax_small.scatter(x_values, y_values, color="red", s=30)
# Set chart title and label axes.
ax_small.set_title("First Five Cubic Numbers", fontsize=24)
ax_small.set_xlabel("Value", fontsize=14)
ax_small.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax_small.tick_params(labelsize=14)

# Set the range for each axis. large values
ax_small.axis([0, 6, 0, 150])

ax.scatter(x_values_5k, y_values_5k, color="blue", s=10)
# Format axes with commas
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

# Set chart title and label axes.
ax.set_title("First 5000 Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis. large values
ax.axis([0, 5_100, 0, 130_000_000_000])

plt.tight_layout()
plt.savefig("cubes_combined.png", bbox_inches="tight")

plt.close(fig3)
