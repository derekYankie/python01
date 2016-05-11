import re

#hand = open('mbox-short.txt')
#for line in hand:
	#remove all white spaces on the right
	#line = line.rstrip()
	#get me all lines starting with 'From'
	#if re.search('From', line):
		#print line

hand = open('mbox-short.txt')
for line in hand:
	#remove all white spaces on the right
	line = line.rstrip()
	#Looks to see if 'Jan' is in the string matching
	
	if re.search('Jan.+', line):
		print line