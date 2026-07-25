import requests

# Make an API call and check the responses
url = "https://api.github.com/search/repositories?q=language:python+sort:stars"
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