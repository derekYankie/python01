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
fname = raw_input("\nEnter file name: ")

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
#creates any empty list
arry = []
#sets the sum of all decimals to 0
listAvg = 0
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
		#number converts every string decimal
		#into a float
		number = float(line[locateP:])
		#makes a list of every string decimal 
		#converted into a float 
		arry.append(number)
		#counts amount times stext appaers
		count = count + 1
		#getting the sum of all decimals
		listAvg = listAvg + number
		
		
		

	#Counts the total number of lines in the text file
	lines =lines + 1
#Divde the sum of all the dceimals by total count of all the decimals;Average 
avg = listAvg/count
print '\nDifferent values assigned to X-DSPAM-Confidence: \n',arry
print '\nNumber of Lines in file:', lines
print 'Number of values assigned to X-DSPAM-Confidence(apperances):', count
#print "Size of word:", len(stext)
print 'Avergae of all the deciamal values:', avg
#closes flie so information isn't tampered with
fhand.close()





