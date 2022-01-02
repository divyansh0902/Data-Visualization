import requests
import json

#make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json' #store URL of API call in url variable
headers = {'Accept' : 'application/vnd.github.v3+json'} #github currently in 3rd version of its API so we define headers for API call that ask to use this version
r = requests.get(url, headers=headers) #use requests to make call to API
print(f"Status code: {r.status_code}") #so we can make sure call went successfully

#store API response in a variable
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent= 4)