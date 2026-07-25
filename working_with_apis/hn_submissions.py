from operator import itemgetter

import requests

# Make an API call and check the response
url =  "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f'Status Code: {r.status_code}')

# Process information about each submission
submission_ids = r.json() # Returns a list
# print(submission_ids)

submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f'Status Code: {r.status_code}')
    response_dict = r.json() # dictionary
    # print(response_dict)