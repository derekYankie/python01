#Assignment 15.2

#The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.
#ample Execution
#$ python solution.py 
#Enter location: http://python-data.dr-chuck.net/comments_42.json
#Retrieving http://python-data.dr-chuck.net/comments_42.json
#Retrieved 2733 characters
#Count: 50
#Sum: 2482


#Turning in the Assignment
#Enter the sum from the actual data and your Python code below:
#Sum:  (ends with 77)
import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_242238.json'
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

result = json.loads(data)

#Gets info about individual commnets
print result['comments'][0]
print result['comments'][1]

count = 0
for comm in result['comments']['count']:
  count = count + comm

print comm

#Gets the sum
total = sum(comm['count'] for comm in result['comments'])
print 'Sum:' , total






