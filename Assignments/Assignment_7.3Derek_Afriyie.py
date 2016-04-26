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
stext = "X-DSPAM-Confidence: 0"
#Get decimals

#sets the count for "of"
count = 0
#sets the count of lines to 0
lines = 0
#Prints contents of selected file in uppercase letters
for line in fhand:
	#Prints the contents of the file in upper case
	#And remove all white spaces after each line
	#print line.upper()#,line.rstrip()
	#Find how many times a charater appears in a file
	if line.find(stext) != -1:
		line = line.strip() 
		#finds "0" cahracter in file
		locate = line.find('0')
		#stext = line.find('0')
		zero = 0
		captureNUm = float(stext[locate:])
		#slice all characters from the 0 onwards
    	stext = line[0:]
    	#converts captured string number into a number
    	#number = float(stext)
		#locateP = stext.find("")
	count = count + 1
		
		

	#Counts the total number of lines in the text file
	lines =lines + 1
print 'Number of Lines in file', lines
#print "Location(index) of word:", found
#print "Decimal index:", locateP
print "Number times word appers:", count
print "Size of word:", len(stext)
print "Decimal number found in text:", stext[0:]
print "Conversion of string-decimal to real decimal:",captureNUm
#closes flie so information isn' tampered with
fhand.close()





