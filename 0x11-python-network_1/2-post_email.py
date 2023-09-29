#!/usr/bin/python3
''' sends a POST request to the passed URL with the email as a parameter'''
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    eml = urllib.parse.urlencode({'email': email}).encode('utf-8')
    pas = urllib.request.Request(url, data=eml, method='POST')

    with urllib.request.urlopen(pas) as response:
        data = response.read().decode('utf-8')
        print(data)
