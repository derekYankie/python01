#Assignment10.4

"Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. "
"You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon."

"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

"Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."


"Begin to write the program with the following code below:"
name = raw_input("Enter file:")
if len(name) < 1 :
	name = "mbox-short.txt"
	fhand = open(name)

timeList = list()
for lines in fhand:
	lines = lines.lstrip()
	#Looking for string matching a specific criteria
	if lines.startswith('From '):
		#Splits all the lines that begin with From into a list
		line = lines.split()
		print line[5]
		#Stores the index location of the times in the every list
		timeData = line[5]
		for numbers in line:
			line = lines.split()
			timeList.append(line[5])
print timeList


	



