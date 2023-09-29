#!/usr/bin/python3
'''  sends a request to the URL and displays the value  '''
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    pas = requests.Request(url)

    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
