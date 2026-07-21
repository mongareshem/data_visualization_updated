import plotly.express as px

from generating_data.random_walk import RandomWalk

rw = RandomWalk(100)
rw.fill_walk()

results = rw.x_values
print(rw.x_values)

poss_results = range(int(min(rw.x_values)), int(max(rw.x_values))+1)
print(list(poss_results))

frequencies = [results.count(value) for value in poss_results]
print(frequencies)

fig = px.bar(x=poss_results, y=frequencies)

fig.show()