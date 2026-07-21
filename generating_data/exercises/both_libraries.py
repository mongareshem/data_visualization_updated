import matplotlib.pyplot as plt

from generating_data.die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll() + die_2.roll() + die_3.roll() for i in range(100_000)]

poss_results = range(3, die_1.num_sides + die_2.num_sides + die_3.num_sides + 1)
frequencies = [results.count(value) for value in poss_results]

fig, ax = plt.subplots()
ax.scatter(poss_results, frequencies)

ax.set_title('Plot of the results of rolling dice using pyplot')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency of the value')

plt.show()
