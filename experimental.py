header = ['STATION', 'NAME', 'LATITUDE', 'LONGITUDE', 'ELEVATION',
          'DATE', 'PRCP', 'SNWD', 'TMAX', 'TMIN', 'TOBS', 'WT01']
print(header.index('TMAX')) # First occurrence

nums = [12, 25, 12, 44, 33, 12, 56]
indices = [i for i, x in enumerate(nums) if x==12] # All instances
print(indices)