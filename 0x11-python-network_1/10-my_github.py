#!/usr/bin/python3
'''
GitHub credentials (username and password(token as password)) and
uses the GitHub API to display your id
'''
import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    paswd_token = sys.argv[2]

    # github API
    url = "https://api.github.com/user"

    # basic authentication
    auth = (username, paswd_token)

    response = requests.get(url, auth=auth)

    data = response.json()
    data_id = data.get('id')

    if data_id:
        print(data_id)
    else:
        print("None")
