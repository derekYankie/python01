"Exploring the HyperText Transport Protocol"
"You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers."
"http://www.pythonlearn.com/code/intro-short.txt"
"There are three ways that you might retrieve this web page and look at the response headers:"
"Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data."
"Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned."
"Use the telnet program as shown in lecture to retrieve the headers and content."
"Enter the header values in each of the fields below and press [submit]"




import urllib2

# Derive from Request class and override get_method to allow a HEAD request.
class HeadRequest(urllib2.Request):
    def get_method(self):
        return "HEAD"

myurl = "http://www.pythonlearn.com/code/intro-short.txt"
request = HeadRequest(myurl)

try:
    response = urllib2.urlopen(request)
    response_headers = response.info()


except urllib2.HTTPError, e:
    # Prints the HTTP Status code of the response but only if there was a 
    # problem.
    print ("Error code: %s" % e.code)
#HTTP request and response
print response_headers

'Dereks-MBP:Assignments derekafriyie$ python Assignment_12.py '
'Date: Thu, 19 May 2016 11:57:12 GMT'
'Server: Apache'
'Last-Modified: Mon, 12 Oct 2015 14:55:29 GMT'
'ETag: "20f7401b-1d3-521e9853a392b"'
'Accept-Ranges: bytes'
'Content-Length: 467'
'Cache-Control: max-age=604800, public'
'Access-Control-Allow-Origin: *'
'Access-Control-Allow-Headers: origin, x-requested-with, content-type'
'Access-Control-Allow-Methods: GET'
'Connection: close'
'Content-Type: text/plain'

#Last-Modified:
 
#ETag:
 
#Content-Length:
 
#Cache-Control:
 
#Content-Type:

