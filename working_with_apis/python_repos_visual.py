import requests
import plotly.express as px

# Make an API call and check the responses
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {
    "Accept": "application/json",              # JSON response
    "X-GitHub-Api-Version": "2026-03-10"      # Explicit API version
    }

r = requests.get(url, headers=headers)
print(f'Status Code: {r.status_code}')

# Process overall results
response_dict = r.json()
print(f'Complete Results: {not response_dict['incomplete_results']}')

# Process repository information
repo_dicts = response_dict['items']
repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f'{owner}<br />{description}' # <br /> is a line break
    hover_texts.append(hover_text)


print(repo_names[:5])
print(stars[:5])

# Make visualization
title = 'Most Starred Python Projects on GitHub '
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_names, y=stars, title=title,
             labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.show()