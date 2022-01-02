from operator import itemgetter

import requests
from requests.models import Response

#make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json' 
r = requests.get(url)
print(f"Status code: {r.status_code}")


#process info about each submission
submission_ids = r.json() #convert response object to a python list which we store in submission_ids
submission_dicts = []
for submission_id in submission_ids[:30]:
    #make a seperate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json" #make a new API call for each submission by generating a URL that includes current value of submission_id
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}") #print status of each request along with its ID
    response_dict = r.json()

    #build a dict for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True) #we want to sort list of dicts by number of comments to do this we use a func called itemgetter()

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments:{submission_dict['comments']}")