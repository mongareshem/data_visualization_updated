import plotly.express as px

from die import Die

# Create a D6
die = Die()

# Make some rolls and store the results in a list
results = [die.roll() for i in range(1000)]

# Analyze the results
poss_results = range(1, die.num_sides + 1)
frequencies = [results.count(value) for value in poss_results]

print(frequencies)

# Visualize the results
fig = px.bar(x=poss_results, y=frequencies) # try: line, scatter
fig.show()
