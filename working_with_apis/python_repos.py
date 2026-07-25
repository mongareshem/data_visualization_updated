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

repo_dict = repo_dicts[0]
print(f'\nKeys: {len(repo_dict)}')
for key in sorted(list(repo_dict.keys())): # For a list omit the for loop
    print(key)

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print(f'Name: {repo_dict['full_name']}')
    print(f'Owner: {repo_dict['owner']['login']}')
    print(f'Stars: {repo_dict['stargazers_count']}')
    print(f'Repository: {repo_dict['html_url']}')
    print(f'Created: {repo_dict['created_at']}')
    print(f'Updated: {repo_dict['updated_at']}')
    print(f'Description: {repo_dict['description']}\n')