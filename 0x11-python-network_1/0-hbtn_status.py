#!/usr/bin/python3
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
response = urllib.request.Request(url)
with urllib.request.urlopen(response) as data:
    content = data.read
print(content)
