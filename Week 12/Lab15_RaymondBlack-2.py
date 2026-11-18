"""
Program name: Plotting Cubic Numbers
Author: Raymond Black
Purpose: The purpose of the program is to visualize cubic numbers.
Resources: Starter code was obtained from Python Crash Course, 3rd Edition
           "scatter_squares.py" example.
           Google search to figure out how to add the comma separators
           on the x and y axes for the 5k cubes.
Date: 2026-11-18
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.style.use("seaborn-v0_8")

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

x_values_5k = range(1, 5001)
y_values_5k = [x**3 for x in x_values_5k]


def plot_cubes(x_values, y_values, ax, color, size, title, axis_limits):
    """
    Helper function to to handle generating the charts for all three versions:
    First five
    First five thousand
    Both in a single popup
    """
    ax.scatter(x_values, y_values, color=color, s=size)

    ax.set_title(title, fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cube of Value", fontsize=14)

    ax.tick_params(labelsize=14)

    ax.axis(axis_limits)

    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))


fig1, ax_small = plt.subplots(figsize=(12, 8))

plot_cubes(
    x_values,
    y_values,
    ax_small,
    color="red",
    size=30,
    title="First Five Cubic Numbers",
    axis_limits=[0, 6, 0, 150],
)

plt.savefig("cubes_5.png", bbox_inches="tight")
plt.close(fig1)

fig2, ax = plt.subplots(figsize=(12, 8))

plot_cubes(
    x_values_5k,
    y_values_5k,
    ax,
    color="blue",
    size=10,
    title="First 5000 Cubic Numbers",
    axis_limits=[0, 5_100, 0, 130_000_000_000],
)

plt.savefig("cubes_5k.png", bbox_inches="tight")
plt.close(fig2)

fig3, (ax_small, ax) = plt.subplots(1, 2, figsize=(20, 8))

plot_cubes(
    x_values,
    y_values,
    ax_small,
    color="red",
    size=30,
    title="First Five Cubic Numbers",
    axis_limits=[0, 6, 0, 150],
)

plot_cubes(
    x_values_5k,
    y_values_5k,
    ax,
    color="blue",
    size=10,
    title="First 5000 Cubic Numbers",
    axis_limits=[0, 5_100, 0, 130_000_000_000],
)

plt.tight_layout()
plt.savefig("cubes_combined.png", bbox_inches="tight")

plt.close(fig3)
