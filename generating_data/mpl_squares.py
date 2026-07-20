import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

# Set chart title and label axes
ax.set_title('Square Numbers',
    fontdict={'family':'Serif', 'fontsize':24, 'fontweight':'bold', 'style':'italic'})
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()