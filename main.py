import requests
from sys import argv
try:

    r = requests.get(f"https://api.github.com/users/{argv[1]}/events")
    r.raise_for_status()
    commits_count = 0
    for item in r.json():
        if item['type'] == "PushEvent":
            commits = item['payload'].get('commits', [])
            repo = item['repo'].get('name', [])
            print(f"- Pushed {len(commits)} commit" + f"{"s" if len(commits) > 1 else ''}"+f" to {repo}")
        elif item['type'] == "Created":
            issue_repo = item['repo'].get('name', [])
            print(f"Opened a new issue in {issue_repo}")

except IndexError:
    print("Usage: gh-activity <username>")

