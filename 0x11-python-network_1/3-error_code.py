#!/usr/bin/python3
"""
   script takes in a url sends a request to the url and displays the body of
   the response (decoded in utf-8)
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import URLError
from sys import argv

if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except URLError as e:
        if hasattr(e, 'code'):
            print('Error code: ', e.code)
