from pathlib import Path
import json

import requests
import plotly.express as px

url = ("https://api.github.com/search/repositories"
       "?q=language:javascript+sort:stars+stars:>10000")
r = requests.get(url)
print(f'Status Code: {r.status_code}')

response_dict = r.json() # Dictionary
path = Path('./javascript_repos.json')
contents = json.dumps(response_dict, indent=4)
path.write_text(contents)

for key in response_dict.keys():
       print(key)

print(f'\nTotal Count: {response_dict['total_count']}')
print(f'Complete Results: {not response_dict['incomplete_results']}')
print(f'Number of Repos: {len(response_dict['items'])}')

items = response_dict['items']

names, stars = [], []
for item in items:
       names.append(item['name'])
       stars.append(item['stargazers_count'])

       print(f'\nName: {item['name']}')
       print(f'Stars: {item['stargazers_count']}')
       print(f'URL: {item['owner']['url']}')
       print(f'Created at: {item['created_at']}')
       print(f'Updated at: {item['updated_at']}')
       print(f'Description: {item['description']}')

labels = {'x':'Repo', 'y': 'stars'}
fig = px.bar(x=names, y=stars, labels=labels)

fig.update_layout(title={
       'text': 'Most Starred JavaScript Repositories in GitHub',
       'x': 0.5,
       'font':{
              'family': 'Serif',
              'size': 32,
              'style': 'italic',
              'weight': 'bold',
              'color': 'black',
       }
})

fig.update_layout(xaxis_title={
       'text': 'Repositories',
       'font':{
              'family':'Serif',
              'color': 'blue',
              'size': 25
       },
}, yaxis_title={
       'text': 'Number of Stars',
       'font':{
              'family':'Serif',
              'color': 'blue',
              'size': 25,
       }})

fig.update_traces(marker_color='red', marker_opacity=0.8)

fig.show()