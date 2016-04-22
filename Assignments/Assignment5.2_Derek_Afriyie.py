#Assignment 5.2

#Create a blank list
numList =[]
while True:
        #Get user input
    userNum = raw_input("Please enter interger numbers ")
    try:
    	#Convert number into a decimal
    	userNum = float(userNum)

    	#Custom message when user doesn't input an intereger
    except:
    	print "Sorry, please try to input a number this time."
    	#Condition to end while loop
    	if userNum == 'done': 
    		#Exits/breaks out of the while loop
    		break
    		#Will jump back to the top of the loop
    		#To force the user to input a number
    		#In order for the program to proceed
    	else:
    		continue
    numList.append(userNum)
if numList == []:
	print "your set set is empty"
else:
	print 'Greatest number is: ',max(numList)
	print 'Smallest number is: ', min(numList)
