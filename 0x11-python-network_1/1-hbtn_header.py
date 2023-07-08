#!/usr/bin/python3
"""
   script takes in  url, sends request to the url and displays the value of
   the X-Request-Id variable found in the header of the response
"""

from sys import argv
from urllib.request import urlopen, Request

if __name__ == "__main__":
    get_url = argv[1]
    send_req = Request(get_url)
    with urlopen(send_req) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
