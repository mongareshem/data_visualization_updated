# import plotly.express as px
import matplotlib.pyplot as plt

numbers = range(1, 5000)
cubes = [x**3 for x in numbers]

# fig = px.bar(x=numbers, y=cubes)
# fig.show()

plt.style.use('dark_background')
fig, ax = plt.subplots()

#ax.plot(numbers, cubes, linewidth=2, color='teal')
ax.scatter(numbers, cubes, c=cubes, cmap=plt.cm.autumn, s=6)
ax.set_title('Cubes')
ax.set_xlabel('Numbers')
ax.set_ylabel('Cubes of Numbers')
ax.ticklabel_format(style='sci') # plain

#plt.show()
plt.savefig('cubes.png', bbox_inches='tight')