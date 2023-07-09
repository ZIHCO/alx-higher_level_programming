#!/usr/bin/python3
"""
   script takes your Github credentials (username and password) and
   uses the github api to display your id
"""
import requests
from sys import argv
if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    r = r.json()
    print(r.get('id'))
