header = ['STATION', 'NAME', 'LATITUDE', 'LONGITUDE', 'ELEVATION',
          'DATE', 'PRCP', 'SNWD', 'TMAX', 'TMIN', 'TOBS', 'WT01']
print(header.index('TMAX')) # First occurrence

nums = [12, 25, 12, 44, 33, 12, 56]
indices = [i for i, x in enumerate(nums) if x==12] # All instances
print(indices)

geometry =  {
    "type": "Point",
    "coordinates": [
        -75.3034,
        -12.1036,
        10
    ]
}
for i, v in enumerate(geometry):
    print(i, v)

print(geometry['coordinates'])