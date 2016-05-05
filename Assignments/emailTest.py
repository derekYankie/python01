#Searching for X-DSPAM-Confidence:
data = 'From: stephen.marquard@uct.ac.za'
startpos = data.find('@')
print startpos
endpos = data.find('',startpos)
print endpos
host = data[startpos+1 : endpos]
print host