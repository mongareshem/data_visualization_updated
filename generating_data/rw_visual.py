import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(14,8)) # figsize=(14,8), dpi=128 # default dpi=100

    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, color='maroon', linewidth=2)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0, 0, color='green', edgecolors='none', s=200)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=200)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break