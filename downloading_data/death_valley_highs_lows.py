from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.6)
ax.plot(dates, lows, color='blue', alpha=0.6)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = 'Daily High and Low Temperatures, 2021 \n Death Valley, CA'
ax.set_title(title, fontsize=16, family='Serif')
ax.set_xlabel('', fontsize=11)
ax.set_ylabel('Temperatures(F)', fontsize=11)
fig.autofmt_xdate()
ax.tick_params(labelsize=11)

ax.set_ylim(0, 130) # same as sitka, for comparison

plt.show()