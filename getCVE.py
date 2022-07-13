import sys
from urllib import request
from urllib.error import HTTPError
from urllib.request import urlopen, Request
import re
import os, ssl


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


pattern = "CVE-\d\d\d\d-\d{3,}"

url = sys.argv[1]
try:
    req = request.Request(url, headers={'User-Agent' : "Magic Browser"})
    page = urlopen(req)
except HTTPError:
    print(HTTPError)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

cves = re.findall(pattern, html, re.IGNORECASE)

cves = list(set(cves))

print(*cves, sep=', ')
