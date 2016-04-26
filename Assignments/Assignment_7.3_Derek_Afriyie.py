#Assignment7.3

"Write a program that prompts for a file name, then opens that file and reads through the file, looking" 
"for lines of the form:"
"X-DSPAM-Confidence:    0.8475"

"Count these lines and extract the floating point values from each of the lines and compute "
"the average of those values and produce an output as shown below. "
"Do not use the sum() function or a variable named sum in your solution."

"You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt "
"when you are testing below enter mbox-short.txt as the file name."

#Recieve the name of user file
fname = raw_input("Enter file name: ")

#Use the open method to open the file
try:
	fhand = open(fname, "r")
	#Prints contents of the file
	#print fhand
	#prints the first 5 characters of the file
	#print fhand.read(5)
#Custom error
except:
	print "Nope, there isn't a file with that name"
#Searching for X-DSPAM-Confidence:
stext = "X-DSPAM-Confidence: "
#sets the count of lines to 0
count = 0
#sets the count lines to 0
lines = 0
arry = []
#Prints contents of selected file in uppercase letters
for line in fhand:
	line = line.rstrip().lstrip()
	#Prints the contents of the file in upper case
	#And remove all white spaces after each line
	#print line.upper()#,line.rstrip()
	#Find how many times a charater appears in a file
	if line.find(stext) != -1:
		#it finds . in the line that we detected 
		locateP = line.find('.')
		#takes every float
		number = float(line[locateP:])
		#add to list
		arry.append(number)
		#counts amount times stext appaers
		count = count + 1
		
		
		

	#Counts the total number of lines in the text file
	lines =lines + 1
print "Different values assigned to X-DSPAM-Confidence:",arry
print 'Number of Lines in file', lines
print "Decimal index:", locateP
print "Number times word appers:", count
print "Size of word:", len(stext)
#closes flie so information isn' tampered with
fhand.close()





