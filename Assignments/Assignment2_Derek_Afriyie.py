#Magic Dates program
#Derek Afriyie 03/30/2016
#Write a program that checks to see if the month & day 
#of the user's birthday results in the year they were born

#Ask user for their month of birth and store in the variable month
year = int(raw_input("What year were you born?"))
"Ask user for their month of birth and store in the variable month"
month = int(raw_input("What month were you born?"))
day = int(raw_input("What day were you born?"))

#Checks
if (month * day) == year:
	print "Your birthday is magical!"
else:
	print "Theres nothing magical about your birthday"
