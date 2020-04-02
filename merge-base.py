import argparse
import json
from github import Github

def main(args):
    with open(args.event_path) as event_file:
        event = json.load(event_file)

    if not 'pull_request' in event['issue']:
        return

    g = Github(args.github_token)
    repo = g.get_repo(event['repository']['full_name'])
    pull = repo.get_pull(event['issue']['number'])

    # Merge base into head (opposite to "merging" pull request)
    repo.merge(pull.head.ref, pull.base.ref)

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--github_token", help="Token for GitHub API")
parser.add_argument("-e", "--event_path", help="JSON file path of GitHub event `POST` webhook payload")

args = parser.parse_args()

main(args)
