from pathlib import Path
import csv

path = Path('../weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

precipitation = []
for row in reader:
    precipitation.append(row[5])

print(precipitation[:5])