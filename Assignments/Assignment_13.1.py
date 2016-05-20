#Assignment13.1



import urllib
from BeautifulSoup import *

import urllib

fhand = urllib.urlopen('http://python-data.dr-chuck.net/comments_242237.html').read()
soup = BeautifulSoup(fhand)

data = soup.findAll("span", { "class":"comments" })
numbers = [int(d.text) for d in data]


#print numbers
print 'Sum', sum(numbers), '\nCount', len(data)

#if len(filename) < 1 :
#	filename = open("http://python-data.dr-chuck.net/comments_242237.html").read()



#soup = BeautifulSoup(filename)

#tags = soup.findall('span')
#print tags

#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
#Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.
#...
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
   # Look at the parts of a tag
   #print 'TAG:',tag
   #print 'URL:',tag.get('href', None)
   #print 'Contents:',tag.contents[0]
   #rint 'Attrs:',tag.attrs


#"You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.
#Sample Execution
#$ python solution.py 
#Enter - http://python-data.dr-chuck.net/comments_42.html
#Count 50
#Sum 2482


#Turning in the Assignment
#Enter the sum from the actual data and your Python code below:
#Sum:  (ends with 67) 