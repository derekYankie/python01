#Assignment8.5

"Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:"
"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

"You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person "
"who sent the message). Then print out a count at the end."
"Hint: make sure not to include the lines that start with 'From:'."

"You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt"



#Recieve the name of user file
fname = raw_input("\nEnter file name:  ")

#Use the open method to open the file
try:
	fhand = open(fname,'r')
#Custom error
except:
	print "Nope, there isn't a file with that name"
#Sets the count of emails in the file to 0
count =0
#Loop the lines in the opened file:
for lines in fhand:
	#If theres a string that starts 'From:' print the entire line
	if lines.startswith('From:'):
		#Remove comment block to 
		#output all lines in the text file that begin with 'From:'
		#print lines
		#Remove comment block to 
		#Show where email in the file comes
		#but wont display the word 'From'
		removeFrom= lines.split('From:')
		print removeFrom[1].strip()
		#Outputs all emails in the text into a individual [list]  
		#print removeFrom
	#Keeps a ruunig total of all the emails in the file
	count =count +1
#print "\n Number of emails:", count
		
print "There are", count, "pepole who sent messages"
#-----------------------------------------#
#Same thing just less lines of code & comments below:

fname = raw_input("\nEnter file name:  ")

try:
	fhand = open(fname,'r')
#Custom error
except:
	print "Nope, there isn't a file with that name"
count =0
#Loop the lines in the opened file:
for lines in fhand:
	#If theres a string that starts 'From:' print the entire line
	lines = lines.strip()
	if  not lines.startswith('From:'): continue
	removeFrom= lines.split('From:')
	print removeFrom[1].strip()
	count = count + 1
print "Above are the myraid email adresses used to send messages.\nHow many are there? \n", count 
	#emails = removeFrom[1].strip()
	#print emails
	#words = lines.split('From')?
	#print words



