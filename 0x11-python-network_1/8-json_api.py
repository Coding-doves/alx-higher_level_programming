#!/usr/bin/python3
'''
ends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
'''
import requests
import sys


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    data = {'q': q}
    response = requests.post(url, data=data)

    try:
        j_data = response.json()
        if j_data:
            print("[{}] {}".format(j_data['id'], j_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
