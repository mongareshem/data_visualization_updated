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
for submission_id in submission_ids[:2]:
    # Make a new API call for each submission
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f'Status Code: {r.status_code}')
    response_dict = r.json() # dictionary
    print(response_dict)

    # Build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': response_dict['url'],
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

print(submission_dicts)