#Assigmnet 3.1
#Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above #40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use raw_input to read a string and float() to convert the string to a number. 


#Do not worry about error checking the user input - assume the user types numbers properly.

"Please begin writing the program with the code below:"
#hrs = raw_input("Enter Hours:")
#h = float(hrs)
#rate = raw_input("Enter pay rate:")
#r = float(rate)
#Determine total pay based on numbers of hours worked"

h= 45
r = 10.50
#Condition for noraml hours worked
if h <=  40:
	#Calculates total pay
	gPay = h * r 
	#Display total pay
	print 'Hey, I owe you', gPay
#Condition for overtime
elif h >= 40:
	gPay = 40 * r + (r * 1.5 *( h-40))
	#Display total pay for overtime
	print 'Hey, you worked overtime. I owe you $', gPay