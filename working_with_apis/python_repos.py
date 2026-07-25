import requests

# Make an API call and check the responses
url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
headers = {
    "Accept": "application/json",              # JSON response
    "X-GitHub-Api-Version": "2026-03-10"      # Explicit API version
    }

r = requests.get(url, headers=headers)
print(f'Status Code: {r.status_code}')

# Convert the response to a dictionary
response_dict = r.json()

# Process Results
print(response_dict.keys())

print(f'Total Repositories: {response_dict['total_count']}')
print(f'Complete Results: {not response_dict['incomplete_results']}')

repo_dicts = response_dict['items']
print(f'Repositories Returned: {len(repo_dicts)}')

repo_dict_1 = repo_dicts[0]
print(f'\nKeys: {len(repo_dict_1)}')
for key in repo_dict_1.keys():
    print(key)

print('\nSelected information about the first directory:')
print(f'Name: {repo_dict_1['full_name']}')
print(f'Owner: {repo_dict_1['owner']['login']}')
print(f'Stars: {repo_dict_1['stargazers_count']}')
print(f'Repository: {repo_dict_1['html_url']}')
print(f'Created: {repo_dict_1['created_at']}')
print(f'Updated: {repo_dict_1['updated_at']}')
print(f'Description: {repo_dict_1['description']}')