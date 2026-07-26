from pathlib import Path
import json

import requests

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
