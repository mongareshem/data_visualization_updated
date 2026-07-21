from die import Die

# Create a D6
die = Die()

# Make some rolls and store the results in a list
results = [die.roll() for i in range(1000)]

# Analyze the results
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

print(frequencies)
