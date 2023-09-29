#!/usr/bin/python3
'''
sends a request to the URL and displays the body of the response
'''
import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    paswd_token = sys.argv[2]
    #github API
    url = "https://api.github.com/user"

    #basic authentication
    auth = (username, passwd_token)

    response = requests.get(url, auth=auth)

    #if response.status_code == 200:
    data = response.json()
    print(data)
