import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

ax.set_title('Squares', fontsize=30, fontweight='bold')
ax.set_xlabel('Value', fontsize=16)
ax.set_ylabel('Square of Value', fontsize=16)

ax.tick_params(labelsize=14)

plt.show()