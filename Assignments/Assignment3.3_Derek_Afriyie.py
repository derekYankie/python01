#Assignment 3.3
#Write a program to prompt for a score between 0.0 and 1.0. 
#If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade #using the following table:

"Score Grade"
">= 0.9 A"
">= 0.8 B"
">= 0.7 C"
">= 0.6 D"
"< 0.6 F"

#If the user enters a value out of range, print a suitable error message and exit. For the test
#enter a score of 0.85.

#Please begin writing the program with the code below:

score = float(raw_input("Enter Score: "))

s = score

#s = 0.85 #score
#Check to see if user entered a number between 0.0 and 1.0
try:
    s >= 0.0 and s <=1.0
    print 'Your score is:',score
except:
    #Display error message
    print 'Invalid number. Enter a number between 0.0-1.0'


if s>= 0.9:
	#Prints A
	print 'A'

elif s>= 0.8:
	#Prints B
	print 'B'
elif s>= 0.7:
	#Prints C
	print 'C'
elif s>= 0.6:
	#Prints D
	print 'D'
elif s< 0.6:
	#Prints F
	print 'F'
else:
    print "Theres no score to give."
