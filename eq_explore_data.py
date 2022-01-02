import json

#explore structure of data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) #load and store data in all_eq_data. json.load() converts data into format python can work with

readable_file = 'data/readable_eq_data.json' #we create a file to write this same data into more readable format
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) #indent=4 tells dump() to format the data using indentation that matches data's structure

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))


#extracting magnitude,longitude,latitude
mags, lons, lats = [],[],[] #empty list
for eq_dict in all_eq_dicts: #loop through dictionary all_eq_dict
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0] #eq_dict['geometry'] accesses geometry element of earthquake.['coordinates'] pulls list of values associated with coordinates.[0] index asks for 1st value in list of coordinates ie- longitude
    lat = eq_dict['geometry']['coordinates'][1] #eq_dict['geometry'] accesses geometry element of earthquake.['coordinates'] pulls list of values associated with coordinates.[1] index asks for 1st value in list of coordinates ie- latitude

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)




print(mags[:10])
print(lons[:5])
print(lats[:5])








































