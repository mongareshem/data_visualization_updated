import requests

url = ("https://api.github.com/search/repositories"
       "?q=language:javascript+sort:stars+stars:>10000")
r = requests.get(url)
print(f'Status Code: {r.status_code}')

