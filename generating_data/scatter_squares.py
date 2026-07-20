import matplotlib.pyplot as plt

x_values = range(1, 1000)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-darkgrid')

fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, color='turquoise', s=5)
# ax.scatter(x_values, y_values, color=(0.8, 0, 0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.rainbow, s=10)

ax.set_title('Squares', fontsize=30, fontweight='bold')
ax.set_xlabel('Value', fontsize=16)
ax.set_ylabel('Square of Value', fontsize=16)

ax.tick_params(labelsize=14)

# Set x and y limits
ax.set_xlim(0, 1100)
ax.set_ylim(0, 1_100_000)
# ax.axis([0, 1000, 0, 1_100_000]) #type: ignore

# Customize tick labels
ax.ticklabel_format(style='plain')

plt.show()