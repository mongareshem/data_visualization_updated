from pathlib import Path

import requests
import json

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# Explore the structure of the data
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)

# Storing the string in a readable format json file
path = Path('./hacker_news.json')
readable_string = json.dumps(response_dict, indent=4)
path.write_text(readable_string)
