#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status '''
import urllib.request

if __name__ == '__main__':
    try:
        with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
            content = response.read()
            utf8_content = content.decode('utf-8')

            print("Body response:")
            print('    - type: ', type(content))
            print('    - content: ', content)
            print('    - utf8 content: ', utf8_content)
    except Exception as e:
        pass
