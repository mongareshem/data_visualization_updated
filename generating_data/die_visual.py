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
title = 'Results of Rolling a D6 1,000 Times'
labels = {'x':'Result', 'y':'Frequency of the Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.update_layout(title={'x':0.5}) # Center aligns the title

fig.show()