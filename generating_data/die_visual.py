from die import Die

# Create a D6
die = Die()

# Make some rolls and store the results in a list
results = [die.roll() for i in range(100)]

print(results)
