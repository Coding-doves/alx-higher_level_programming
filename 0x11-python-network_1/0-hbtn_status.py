#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status '''
import urllib.request


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        utf8_content = data.decode('utf-8')

        print("Body response:")
        print("    - type:", type(data))
        print("    - content:", data)
        print("    - utf8 content:", utf8_content)
