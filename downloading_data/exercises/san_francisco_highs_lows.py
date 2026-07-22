from pathlib import Path
import csv

path = Path('../weather_data/san_francisco_2025_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for i, column_header in enumerate(header_row):
    print(i, column_header)