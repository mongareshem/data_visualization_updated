from pathlib import Path
import csv
from datetime import datetime

path = Path('../weather_data/san_francisco_2025_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for i, column_header in enumerate(header_row):
    print(i, column_header)

dates, t_maxs, t_mins, = [], [], [],
for row in reader:
    dates.append(datetime.strptime(row[5], '%Y-%m-%d'))
    try:
        t_maxs.append(int(row[8]))
        t_mins.append(int(row[9]))
    except ValueError:
        print(f'Missing data for {row[5]}')
