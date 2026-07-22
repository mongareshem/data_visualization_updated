from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('../weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

precipitations, dates, places = [], [], []
for row in reader:
    precipitations.append(float(row[5]))
    dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
    places.append(row[1])

print(precipitations[:5])
print(places[0])


plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, color='blue', alpha=0.7)

ax.set_title(f'DAILY RAINFALL IN {places[0]}',
             fontdict={'family':'serif', 'fontsize':17, 'fontweight':'bold'})
ax.set_xlabel('Dates', fontsize=14)
ax.set_ylabel('Precipitation', fontsize=16)
ax.tick_params(labelsize=10)
fig.autofmt_xdate()

plt.tight_layout() # Adjusts space automatically
plt.show()