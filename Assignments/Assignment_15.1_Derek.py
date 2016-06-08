#Calling a JSON API
#In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
#API End Points
#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
#http://python-data.dr-chuck.net/geojson


#This API uses the same parameters (sensor and address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
#To call the API, you need to provide a sensor=false parameter and the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.pythonlearn.com/code/geojson.py
#Just for fun, you can also test your program with the real Google API:
#http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=University+of+Michigan


#Singe Google's data is always changing, the data returned from the Google API could easily be different than from my local copy API. And the Google API has rate limits. But your code should work with the Google API with no modifications other than the base URL.
#Test Data / Sample Execution
#You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".
#$ python solution.py
#Enter location: South Federal University 
#Retrieving http://...
#Retrieved 2101 characters
#Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok 


#Turn In
#Please run your program to find the place_id for "University of Connecticut" and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJGbL ..."
import urllib

import json

myserviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input('Enter location: ')
	if len(address)< 1 : break
#creating url encoded string and concatonate it the url
	url = myserviceurl + urllib.urlencode({'sensor':'false','address':address})

	print 'Retrieving', url
	urlhandle = urllib.urlopen(url)
	data = urlhandle.read()
	print 'Retrieved', len(data), 'characters'
#deCearalizing library of list of dictionaries
	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print 'Faliure to Retrieve'
		print data
		continue
#pulling the first result in dictionary and the first place_id in the dictionary
	place = js["results"][0]["place_id"]

	print 'Place ID: ', place

