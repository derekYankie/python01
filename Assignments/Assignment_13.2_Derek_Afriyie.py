import urllib
from BeautifulSoup import *


url = "http://python-data.dr-chuck.net/known_by_Ross.html"


count = 7
while count > 0:
	website = urllib.urlopen(url).read()
	parsed_website = BeautifulSoup(website)

	tags = parsed_website('a')

	link_lst = []

	for tag in tags:
		link = tag.get('href', None)
		link_lst.append(link)

	url = link_lst[17]

	count -= 1

print url