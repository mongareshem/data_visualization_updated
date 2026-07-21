import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die(10)

results = [die_1.roll() + die_2.roll() for i in range(50_000)]

poss_results = range(2, die_1.num_sides + die_2.num_sides + 1)
frequencies = [results.count(result) for result in poss_results]

title = 'Result of rolling a D6 and a D10 50,000 times'
labels = {'x': 'Result', 'y': 'Frequency of the Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(title={'x':0.5}, xaxis_dtick=1)
# fig.show()
fig.write_html('d6_d10_visual.html')