from pathlib import Path
import csv

import pandas as pd
import plotly.express as px

path = Path('../eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for i, v in enumerate(header_row):
    print(i, v)

lons, lats, brightness, = [], [], []
for column_header in reader:
    lons.append(column_header[1])
    lats.append(column_header[0])
    brightness.append(float(column_header[2]))

print(lons[:3])
print(lats[:3])
print(brightness[:3])

data = pd.DataFrame({
    'longitudes':lons,
    'latitudes':lats,
    'size':brightness,
    'color':brightness
})

title = 'World Fires'
fig = px.scatter_geo(data, lon='longitudes', lat='latitudes', size='size',
                     color='color',
                     color_continuous_scale='icefire',
                     labels={'size':'brightness'},
                     projection='natural earth',
                     hover_data={'color':False})

fig.update_layout(title={'text':title,
                         'x':0.5,
                         'font':{
                             'family':'Serif',
                             'size': 44
                         }})

fig.show()
