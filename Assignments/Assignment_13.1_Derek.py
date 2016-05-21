import urllib
from BeautifulSoup import *

import urllib
#open and read all the content in the website, read it, and look for span tags

tags = BeautifulSoup(urllib.urlopen('http://python-data.dr-chuck.net/comments_242237.html').read())('span')
#make an empty list
lst = []
#loop will fill the empty list with a list of all the numbers attached to span tags
for tag in tags:
	lst.append(int(tag.contents[0]))

print sum(lst)