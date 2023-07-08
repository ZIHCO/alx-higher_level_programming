#!/usr/bin/python3

"""script fetches 'https://alx-intranet.hbtn.io/status'
   using 'urllib'
"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    html = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(html) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(content)))
        print('\t- content: {_content}'.format(_content=content))
        print('\t- utf8 content: {_utf8}'.format(_utf8=utf8_content))
