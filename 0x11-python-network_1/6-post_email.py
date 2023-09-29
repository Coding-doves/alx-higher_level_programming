#!/usr/bin/python3
'''  sends a request to the URL and displays the value  '''
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    pas = requests.get(url)

    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
