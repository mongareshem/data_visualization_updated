import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8-darkgrid')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=2)

# Set chart title and label axes
ax.set_title('Square Numbers',
    fontdict={'family':'Serif', 'fontsize':24, 'fontweight':'bold', 'style':'italic'})
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()