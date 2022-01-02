import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


#explore structure of data
#filename = 'data/eq_data_1_day_m1.json'
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) #load and store data in all_eq_data. json.load() converts data into format python can work with

readable_file = 'data/readable_eq_data.json' #we create a file to write this same data into more readable format
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) #indent=4 tells dump() to format the data using indentation that matches data's structure

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))


#extracting magnitude,longitude,latitude
mags, lons, lats, hover_texts = [],[],[],[] #empty list
for eq_dict in all_eq_dicts: #loop through dictionary all_eq_dict
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0] #eq_dict['geometry'] accesses geometry element of earthquake.['coordinates'] pulls list of values associated with coordinates.[0] index asks for 1st value in list of coordinates ie- longitude
    lat = eq_dict['geometry']['coordinates'][1] #eq_dict['geometry'] accesses geometry element of earthquake.['coordinates'] pulls list of values associated with coordinates.[1] index asks for 1st value in list of coordinates ie- latitude
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

#map the earthquakes
#data = [Scattergeo(lon=lons, lat=lats)] #scattergeo chart type allow you to overlay a scatter plot of geographic data on a map
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat':lats,
    'text': hover_texts,
    'marker':{
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}] #a better way to give data #using key 'marker' to specify marker's size. we use a nested dict as value associated with 'marker' because we can specify a number of settings for all the mrkers in a series
##we want size to correspond to magnitude of each earthquake. hence we used list comprehension.
my_layout = Layout(title= 'Global Earthquakes')

fig = {'data': data, 'layout': my_layout} #creates a dictionary fig that contains data and layout
#offline.plot(fig, filename= 'global_earthquakes.html')
#offline.plot(fig, filename= 'global_earthquakes_30.html')
offline.plot(fig, filename= 'global_earthquakes_30_modified.html')