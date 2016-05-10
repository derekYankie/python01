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

for lines in fhand:
	lines = lines.lstrip()
	#Looking for string matching a specific criteria
	if line.startswith('From '):
		continue
	#print lines
		pos= line.find(':')

	print 'time:', lines.split(',')

	



