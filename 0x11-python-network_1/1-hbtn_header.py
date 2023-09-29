#!/usr/bin/python3
'''  sends a request to the URL and displays the value  '''
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    pas = urllib.request.Request(url)

    with urllib.request.urlopen(pas) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
