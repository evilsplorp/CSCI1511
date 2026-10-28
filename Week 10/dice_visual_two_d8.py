"""
Rolling dice
Raymond Black
A basic hard-code die roller that creates a histogram of the results (two D8)
Resources: Chapter 15
2026-10-28
"""

import plotly.express as px

from die import Die

# 2d8
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    # result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)

# poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.

fig = px.bar(x=poss_results, y=frequencies)

fig.update_layout(
    title_text="Results of Rolling Two D8 Die 50,000 Times",
    xaxis_title_text="Result",
    yaxis_title_text="Frequency of Result",
    xaxis_dtick = 1
)

fig.show()

print(frequencies)
# fig.write_html('dice_visual_d8d20.html')