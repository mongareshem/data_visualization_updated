import plotly.express as px

from generating_data.die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll() * die_2.roll() * die_3.roll() for i in range(1000)]

poss_results = range(3, die_1.num_sides * die_2.num_sides * die_3.num_sides + 1)
frequencies = [results.count(value) for value in poss_results]

title = 'Results of the Frequencies of Multiplying Three D6 Dice'
labels = {'x': 'Value', 'y': 'Frequency of the Value'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(title={'x': 0.5})
fig.show()