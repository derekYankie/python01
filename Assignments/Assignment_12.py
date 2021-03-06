"Exploring the HyperText Transport Protocol"
"You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers."
"http://www.pythonlearn.com/code/intro-short.txt"
"There are three ways that you might retrieve this web page and look at the response headers:"
"Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data."
"Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned."
"Use the telnet program as shown in lecture to retrieve the headers and content."
"Enter the header values in each of the fields below and press [submit]"




import urllib2
#telnet http://www.pythonlearn.com 80
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

print response_headers


#Last-Modified:
 
#ETag:
 
#Content-Length:
 
#Cache-Control:
 
#Content-Type:
