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

precipitations, dates = [], []
for row in reader:
    precipitations.append(float(row[5]))
    dates.append(datetime.strptime(row[2], '%Y-%m-%d'))

print(precipitations[:5])

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, precipitations)

plt.tight_layout()
plt.show()