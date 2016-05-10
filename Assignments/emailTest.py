#Searching for X-DSPAM-Confidence:
data = 'From: stephen.marquard@uct.ac.za'
startpos = data.find('@')
print startpos
endpos = data.find('',startpos)
print endpos
host = data[startpos+1 : endpos]
print host

----------8.5 update------------
#Assignment9.4

"Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. "
"The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. "
"The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. "
"After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."

#Recieve the name of user file
fname = raw_input("\nEnter file name:  ")

#Use the open method to open the file
try:
	fhand = open(fname,'r')
#Custom error
except:
	print "Nope, there isn't a file with that name"
#Sets the count of emails in the file to 0
#count =0
senderlst = []
#emails = {}
#Loop the lines in the opened file:
for lines in fhand:
	#If theres a string that starts 'From:' print the entire line
	if  not lines.startswith('From:'): continue
		#Remove comment block to 
		#output all lines in the text file that begin with 'From:'
		#print lines
		#Remove comment block to 
		#Show where email in the file comes
		#but wont display the word 'From'
		#removeFrom= lines.split('From:')
		#print removeFrom[1].strip()
		#emails = removeFrom[1].strip()
		#print emails
	words = lines.split()
		#print words
	#theemail = words[1]
	#print theemail
#content= senderlst.append(theemail)
#print content
		#email = dict([p.removeFrom, p.appearance]) for p in removeFrom])

-----------------9.5 late night coding---------------------
#Assignment9.4

"Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. "
"The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. "
"The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. "
"After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."

#Recieve the name of user file
fname = raw_input("\nEnter file name:  ")

#Use the open method to open the file
try:
	fhand = open(fname,'r')
#Custom error
except:
	print "Nope, there isn't a file with that name"
#Sets the count of emails in the file to 0
#count =0
eNames = dict()
#emails = {}
#Loop the lines in the opened file:
for lines in fhand:
	#If theres a string that starts 'From:' print the entire line
	if  not lines.startswith('From:'): continue


		#Remove comment block to 
		#output all lines in the text file that begin with 'From:'
		#print lines
		#Remove comment block to 
		#Show where email in the file comes
		#but wont display the word 'From'
		#removeFrom= lines.split('From:')
		#print removeFrom[1].strip()
		#emails = removeFrom[1].strip()
		#print emails
	#removes the '\n'character added after every email
	lines.split('\n')
	#locates the index of the colon
	colon = lines.find(':') + 1
	#makes a list of just emails found in the file
	email =  lines[lines.find(' ')+1:]
	#Dictionary rule: 
	#Entries need to be made into the dictionary(eNames)
	if email not in eNames:
		#When a new email is found a new key & value is made
		eNames[email] = 1
	else:
		#If an email is seen multiple times we add to the count
		eNames[email] = eNames.get(email, 0) + 1
	#print 'colon index:', colon
	#print lines
	#print "email:", email
	print 'Email Dictionaryc :', eNames
	#words =lines.split()
	#print words
	#print words.index(1)
	#theemail = words[1]
	#print theemail
	
#content= senderlst.append(theemail)
#print content
		#email = dict([p.removeFrom, p.appearance]) for p in removeFrom])
---------------------9.5 modified--------------------
name = raw_input("Enter text here")
#If the user input isn"t correct 
#than asign user input to the correct file name
if name < 1:
	name = "mbox-short.txt"
handle = open(name)
eName = dict()



