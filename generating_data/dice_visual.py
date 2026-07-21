import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

poss_results = range(2, die_1.num_sides + die_2.num_sides + 1)
frequencies = [results.count(i) for i in poss_results]

title = 'Results of rolling two D6 Dice 1,000 times'
labels = {'x': 'Result', 'y': 'Frequency of the result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(title={'x':0.5}, xaxis_dtick=1)
# fig.update_layout(xaxis_dtick=1) # labels all bars in the x axis
fig.show()