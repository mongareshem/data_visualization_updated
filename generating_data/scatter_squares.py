import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8-darkgrid')

fig, ax = plt.subplots()
#ax.scatter(2, 4, s=200)
ax.scatter(x_values, y_values, s=100)

ax.set_title('Squares', fontsize=30, fontweight='bold')
ax.set_xlabel('Value', fontsize=16)
ax.set_ylabel('Square of Value', fontsize=16)

ax.tick_params(labelsize=14)

plt.show()