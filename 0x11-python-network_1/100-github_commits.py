#!/usr/bin/python3
"""takes two args, repos_name and owner_name
   list 10 commits of this repos
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/' + 'repos/' + argv[2] + '/' + argv[1]
    response = requests.get(url).json()
    commit_url = response['commits_url'][:-6]

    commits_response = requests.get(commit_url).json()
    for i in range(10):
        print(f"{commits_response[i]['sha']}: "
              f"{commits_response[i]['commit']['author']['name']}")
