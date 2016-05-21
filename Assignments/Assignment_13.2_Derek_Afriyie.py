import urllib
from BeautifulSoup import *


url = "http://python-data.dr-chuck.net/known_by_Ross.html"

#Run through the links 7 times
count = 7
while count > 0:
    #Open and read file with BSoup
	parsed_website = BeautifulSoup(urllib.urlopen(url).read())
	#look for anchor tag a.k.a. links 
	tags = parsed_website('a')
	#empty list
	link_lst = []

	for tag in tags:
		#make a list of links
		link_lst.append(tag.get('href', None))
		#look for the 18th link
	url = link_lst[17]
	#countdown by 1
	count -= 1

print url
