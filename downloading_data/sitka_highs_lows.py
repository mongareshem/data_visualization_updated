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
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

print(highs)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')

# Format the plot.
ax.set_title('Daily High and Low Temperatures, 2021', fontsize=20)
ax.set_xlabel('', fontsize=11)
fig.autofmt_xdate() # fig. not ax.
ax.set_ylabel('Temperature (F)', fontsize=11)
ax.tick_params(labelsize=11)

plt.show()