#Processing an API response

import requests

#make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' #store URL of API call in url variable
headers = {'Accept' : 'application/vnd.github.v3+json'} #github currently in 3rd version of its API so we define headers for API call that ask to use this version
r = requests.get(url, headers=headers) #use requests to make call to API
#print(f"Status code: {r.status_code}") #so we can make sure call went successfully

#store API response in a variable
response_dict = r.json() #APIreturns info in json format so we use json() method to convert it into python dict
#print(f"Total repositories: {response_dict['total_count']}") #print value associated with 'total_count'

#explore info about repositories
repo_dicts = response_dict['items'] #store list of dictionaries 
#print(f"Repositories returned: {len(repo_dicts)}")#print length  of repo_dicts to see number of repositories

#examine first repository
repo_dict = repo_dicts[0] #pull out 1st item from repo_dicts and store in repo_dict
#print(f"\nKeys: {len(repo_dict)}") #print number of keys in dict
#for key in sorted(repo_dict.keys()): #print all dict's keys tosee what kind of info is included
#    print(key)

#print("\nSelected info about 1st repo:")
#print(f"Name: {repo_dict['name']}")
#print(f"Owner: {repo_dict['owner']['login']}")
#print(f"Stars: {repo_dict['stargazers_count']}")
#print(f"Repository: {repo_dict['html_url']}")
#print(f"Created: {repo_dict['created_at']}")
#print(f"Updated: {repo_dict['updated_at']}")
#print(f"Description: {repo_dict['description']}")

print("\nSelected info about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")


#process results
#print(response_dict.keys())