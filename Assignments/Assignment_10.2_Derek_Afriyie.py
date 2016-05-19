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

#Empty hours dictionary
hours = {}
for lines in fhand:
	lines = lines.lstrip()
	#Looking for string matching a specific criteria
	if lines.startswith('From '):
		#Takes ecah line beginning with 'From' 
	    #Removes all the white spaces and turns each line
	    #into a list of grouped characters 
		line = lines.split()
		#print line[5]
		#Stores the index location of the timesstamps found in every line
		time_stamp = line[5]
		#Stores all the timestamps without the colons 
		time_data=time_stamp.split(':')
		#Stores the empty dictionary with
		#the number of occurrences of each hour(index 0)
		#if it already has a count for a given hour 
		#get() returns that hour, else get returns 0
		#last increment each appearance by 1 
		hours[time_data[0]] = hours.get(time_data[0],0)+1
#Loops through hours dictionary & sort the keys & value by iterations
#key is set to lambda,anonymous function that reference the variables(k,v)
for key, value in sorted(hours.iteritems(), key=lambda (k,v): (v,k)):
    print'Hrs:  Counts: \n', "%s:\t %s" % (key, value)
		





	



