from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt
from numpy.ma.extras import average

path = Path('../weather_data/san_francisco_2025_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for i, column_header in enumerate(header_row):
    print(i, column_header)

dates, t_maxs, t_mins, place = [], [], [], ''
for row in reader:
    dates.append(datetime.strptime(row[5], '%Y-%m-%d'))
    place = row[1]
    try:
        t_maxs.append(int(row[8]))
        t_mins.append(int(row[9]))
    except ValueError:
        print(f'Missing data for {row[5]}')
        t_maxs.append(round(average(t_maxs)))
        t_mins.append(round(average(t_mins)))

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, t_maxs, color='gold')
ax.plot(dates, t_mins, color='darkmagenta')
ax.fill_between(dates, t_maxs, t_mins, color='midnightblue', alpha=0.5)

ax.set_title(f'2025 Temperature Readings for \n {place}',
             fontdict={'family':'Serif', 'size':18,})
ax.set_ylabel('Temperature (F)', fontdict={'family':'Serif', 'fontsize':18})
ax.tick_params(labelsize=12)

plt.tight_layout()

plt.savefig('san_francisco_temperatures_2025.png', dpi=300,) # transparent=True
plt.show()