#!/usr/bin/python3

"""script fetches 'https://alx-intranet.hbtn.io/status'
   using 'urllib'
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code < 400:
        print(r.content.decode('utf-8'))
    elif:
        print('Error code:', r.status_code)
