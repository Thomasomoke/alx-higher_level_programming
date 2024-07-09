#!/usr/bin/python3
#to install requests use python -mpip install requests
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = urllib.request.Request(url, headers=header)
with urllib.request.urlopen(response) as data:
    content = data.read
    head = data.headers
print(head)
value = head.get('X-Request-Id')
print(value)
