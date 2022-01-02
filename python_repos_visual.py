'''import requests

from plotly.graph_objs import Bar
from plotly import offline

#make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' #store URL of API call in url variable
headers = {'Accept' : 'application/vnd.github.v3+json'} #github currently in 3rd version of its API so we define headers for API call that ask to use this version
r = requests.get(url, headers=headers) #use requests to make call to API
print(f"Status code: {r.status_code}") #so we can make sure call went successfully

#process results
response_dict = r.json()
repo_dicts = response_dict['items'] 
repo_names, stars, labels  = [], [], [] #create 3 empty lists to store data we wil include in initial chart
for repo_dict in repo_dicts: #in loop we append name of each project and number of stars it has to these lists
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    #add in loop owner and description for each project
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}" #plotly allows to use a line break between project owner's username and description
    labels.append(label)

#make visualization
data = [{
    'type':'bar',
    'x': repo_names,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}] #define the data list, defines type of plot and x and y axis. Set custom blue color for bars and specify bar will be outlined with grey line that's 1.5 pixels wide. Also set opacity of bar to 0.6

my_layout = {
    'title':'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
        'yaxis' : {'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
} #define layout using dictionary with specific specifications like chart titile and label for each axis

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python_repos.html')
'''





#adding clickable links to graph
import requests

from plotly.graph_objs import Bar
from plotly import offline

#make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' 
headers = {'Accept' : 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#process results
response_dict = r.json()
repo_dicts = response_dict['items'] 
repo_links, stars, labels  = [], [], [] 
for repo_dict in repo_dicts:
    repo_name =repo_dict['name']
    repo_url = repo_dict['html_url'] # pull rrl for project from repo_dict and assign to temporary variable repo_url
    repo_link = f"<a href= '{repo_url}'>{repo_name}</a>" #we generate a link to project. we use HTML anchor tag
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    #add in loop owner and description for each project
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}" 
    labels.append(label)

#make visualization
data = [{
    'type':'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}] 

my_layout = {
    'title':'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
        'yaxis' : {'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
} 
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python_repos.html')










