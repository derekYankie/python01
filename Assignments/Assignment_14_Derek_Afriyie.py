#Assignmnet14
import urllib
from xml.etree.ElementTree as ET 

while True:
	url = raw_input("Enter url:")
	if len(url) <1: break

	html = urllib.urlopen(url).read()
	#gives me xml object
	xml = ET.fromstring(data)

	#get me all the comments
	comments = xml.findall('comments/comment')

	total = 0
	#go from comments to comments to find individual comments
	#than find the counts
	for comment in comments:
		comment = int(find('count').txt)

		total += number

	print total


