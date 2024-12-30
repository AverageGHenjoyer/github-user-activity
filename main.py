import requests
from sys import argv

data = []
try:
    r = requests.get(f"https://api.github.com/users/{argv[1]}/events")
    r.raise_for_status()
    for item in r.json():
        if item['type'] == "PushEvent":
            commits = item['payload'].get('commits', [])
            repo = item['repo'].get('name', [])
            time = item['created_at']
            size = item['payload'].get('size', [])
            data.append(f"- Pushed {size} commit" + f"{"s" if size > 1 else ''}"+f" to {repo} at {time}")

        elif item['type'] == "CreateEvent":
            issue_repo = item['repo'].get('name', [])
            thing = item['payload'].get('ref_type')
            time = item['created_at']
            data.append(f"- Created a new {thing} {issue_repo} at {time}")

        elif item['type'] == "DeleteEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('ref_type', [])
            time = item['created_at']
            data.append(f"- Deleted a {thing} in {repo} at {time}")

        elif item['type'] == "CommitCommentEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('action', [])
            time = item['created_at']
            comment = item['payload'].get('comment', [])
            data.append(f"- Commit comment {thing} in {repo} '{comment}' at {time}")

        elif item['type'] == "ForkEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('forkee', [])
            time = item['created_at']
            data.append(f"- Forked a {thing} in {repo} at {time}")

        elif item['type'] == "GollumEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('pages', []).get('action', [])
            time = item['created_at']
            data.append(f"- Wiki page has been {thing} in {repo} at {time}")

        elif item['type'] == "IssueCommentEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('action', [])
            time = item['created_at']
            changes = item['payload'].get('changes', [])
            data.append(f"- Issue comment has been {thing} in {repo} at {time}, changes: {changes}")

        elif item['type'] == "IssuesEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('action', [])
            time = item['created_at']
            issue = item['payload'].get('issue', [])
            data.append(f"- Issue has been {thing} in {repo} at {time} for {issue}")

        elif item['type'] == "MemberEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('action', [])
            member = item['payload'].get('member', [])
            time = item['created_at']
            data.append(f"- Member {member} has been {thing} in {repo} at {time}")

        elif item['type'] == "PublicEvent":
            repo = item['repo'].get('name', [])
            time = item['created_at']
            data.append(f"- Repository {repo} is now public at {time}")

        elif item['type'] == "PullRequestEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('action', [])
            time = item['created_at']
            number = item['payload'].get('number', [])
            data.append(f"- A pull request number {number} has been {thing} in {repo} at {time}")

        elif item['type'] == "PullRequestReviewEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('action', [])
            time = item['created_at']
            data.append(f"- A pull request review has been {thing} in {repo} at {time}")

        elif item['type'] == "PullRequestReviewCommentEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('action', [])
            time = item['created_at']
            data.append(f"- A pull request review comment has been {thing} in {repo} at {time}")

        elif item['type'] == "PullRequestReviewThreadEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('action', [])
            time = item['created_at']
            thread = item['payload'].get('thread', [])
            data.append(f"- A pull request review marked as {thing} in thread {thread} in {repo} at {time} ")

        elif item['type'] == "ReleaseEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('action', [])
            time = item['created_at']
            data.append(f"- A new release has been {thing} in {repo} at {time} ")

        elif item['type'] == "SponsorshipEvent":
            repo = item['repo'].get('name', [])
            thing = item['payload'].get('action', [])
            time = item['created_at']
            data.append(f"- A new sponsorship {thing} in {repo} at {time} ")

    for item in data:
        print(item)

except IndexError:
    print("Usage: gh-activity <username>")




