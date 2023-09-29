#!/usr/bin/python3
'''
 GitHub credentials (username and password(token as password)) and
 uses the GitHub API to display your id
'''
import requests
import sys


if __name__ == '__main__':
    if sys.argv == 2:
        username = sys.argv[1]
        paswd_token = sys.argv[2]
    #github API
    url = "https://api.github.com/user"

    #basic authentication
    auth = (username, passwd_token)

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        data = response.json()
        print(data['id'])
    else:
        print(None)
