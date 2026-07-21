import plotly.express as px

from generating_data.die import Die

die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll() + die_2.roll() for i in range(1000)]

poss_results = range(2, die_1.num_sides + die_2.num_sides + 1)
frequencies = [results.count(value) for value in poss_results]

print(list(poss_results))
print(frequencies)

title = 'Results of rolling Two D8 Dice'
labels = {'x': 'Value', 'y': 'Frequency of the Value'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(title={'x':0.5}, xaxis_dtick=1)
fig.show()