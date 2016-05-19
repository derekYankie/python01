import urllib 
from BeautifulSoup import *

url = raw_input('Enter - ')

openurl = urllib.urlopen(url).read()

soup = BeautifulSoup(openurl)

tags = soup.find('script')

print tags

import httplib
>>> conn = httplib.HTTPConnection("www.google.com")
>>> conn.request("HEAD", "/index.html")
>>> res = conn.getresponse()
>>> print res.status, res.reason
200 OK
>>> print res.getheaders()
[('content-length', '0'), ('expires', '-1'), ('server', 'gws'), ('cache-control', 'private,