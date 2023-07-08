#!/usr/bin/python3
"""
   Script takes in a url and an email, sends a POST request to the URL with
   the email as param. and displays the body of the response in utf-8
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    data = urlencode({
                        'email': argv[2]
                    }).encode('ascii')
    req = Request(argv[1], data)

    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
