#!/usr/bin/python3

"""script fetches 'https://alx-intranet.hbtn.io/status'
   using 'urllib'
"""

import requests
from sys import argv

if __name__ == "__main__":
    payload = dict(email=argv[2])
    r = requests.post(argv[1], payload)
    print(r.context.decode('utf-8'))
