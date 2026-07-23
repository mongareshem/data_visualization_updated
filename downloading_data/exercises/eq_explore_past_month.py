from pathlib import Path
import json

path = Path('../eq_data/past_month_eq_data.geojson')
content = path.read_text()
all_eq_data = json.loads(content)

path = Path('../eq_data/readable_past_month_eq_data.json')
readable_content = json.dumps(all_eq_data, indent=4)
path.write_text(readable_content)

print(type(all_eq_data)) # dictionary
# print(type(readable_content)) # string

lons, lats, elevs, mags, = [], [], [], []
for feature in all_eq_data['features']:
    lons.append(feature['geometry']['coordinates'][0])
    lats.append(feature['geometry']['coordinates'][1])
    elevs.append(feature['geometry']['coordinates'][2])
    mags.append(feature['properties']['mag'])

print(lons[:3])
print(lats[:3])
print(elevs[:3])
print(mags[:3])