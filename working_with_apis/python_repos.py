import requests

url = "https://api.github.com/search/repositories?q=language:python+sort:stars"
headers = {
    "Accept": "application/json",              # JSON response
    "X-GitHub-Api-Version": "2026-03-10"      # Explicit API version
    }

r = requests.get(url, headers=headers)
print(f'Status Code: {r.status_code}')

response_dict = r.json()
print(response_dict.keys())