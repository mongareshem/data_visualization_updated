from pathlib import Path
import json

import pandas as pd
import plotly.express as px

path = Path('../eq_data/past_month_eq_data.geojson')
content = path.read_text()
all_eq_data = json.loads(content)

path = Path('../eq_data/readable_past_month_eq_data.json')
readable_content = json.dumps(all_eq_data, indent=4)
path.write_text(readable_content)

print(type(all_eq_data)) # dictionary
# print(type(readable_content)) # string

lons, lats, mags, hover_names = [], [], [], [],
for feature in all_eq_data['features']:
    lons.append(feature['geometry']['coordinates'][0])
    lats.append(feature['geometry']['coordinates'][1])
    mags.append(feature['properties']['mag'])
    hover_names.append(feature['properties']['title'])

print(lons[:3])
print(lats[:3])
print(mags[:3])

data = pd.DataFrame({
    'longitudes':lons,
    'latitudes': lats,
    'magnitudes': mags,
    'hover_text': hover_names,
    'c': mags
})

fig = px.scatter_geo(data, lon='longitudes', lat='latitudes', size='magnitudes',
                     color='c',
                     color_continuous_scale='inferno_r', # _r at the end reverses
                     labels={'c':'magnitude', 'lon':'longitude'},
                     projection='natural earth',
                     hover_name='hover_text',
                    hover_data={'magnitudes':False, 'c':True}
                     )

fig.update_layout(title={
                         'text':all_eq_data['metadata']['title'],
                         'x':0.5,
                         'font':{
                             'family':'Serif',
                             'size': 23
                         }}, )

fig.show()