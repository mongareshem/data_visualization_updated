from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates and high temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
    high = int(row[header_row.index('TMAX')])
    low = int(row[header_row.index('TMIN')])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.7)
ax.plot(dates, lows, color='blue', alpha=0.7)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot.
ax.set_title('Daily High and Low Temperatures, 2021', fontsize=20)
ax.set_xlabel('', fontsize=11)
fig.autofmt_xdate() # fig. not ax.
ax.set_ylabel('Temperature (F)', fontsize=11)
ax.tick_params(labelsize=11)

# ax.set_ylim(0, 130) # Same as death valley, for comparison

plt.show()