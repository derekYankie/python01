import urllib 
from BeautifulSoup import *

url = raw_input('Enter - ')

openurl = urllib.urlopen(url).read()

soup = BeautifulSoup(openurl)

tags = soup.find('script')

print tags