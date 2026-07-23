from pathlib import Path
import csv

path = Path('../eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for i, v in enumerate(header_row):
    print(i, v)
