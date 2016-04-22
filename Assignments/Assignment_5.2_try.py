#Assignment 5.2

"Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. "
"Once 'done' is entered, print out the largest and smallest of the numbers."
"If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number."



#A functionn to determine smallest
def sNum(num):
	
Validating User Input
numList =[]
while True:
    try:
        Get user inpur
        userNum = raw_input("Please enter interger numbers ")
        uNum = int(userNum)
        numList.append(uNum)
    except ValueError:
        print "Sorry, I didn't understand that."
        #better try again... Return to the start of the loop
        continue
        smallest = uNum
        #value = []
         print 'Before'
        	for numList in [] :
        		if smallest is uNum :
        			smallest = numList
        		elif numList < smallest :
        			smallest =numList 
        	    #return smallest
        		print smallest, numList
        		print 'Afrter', smallest
        print 'Samllest: ', sNum(int)
        print'done to end program'

        #uNum = 'done'
    if uNum == str('done') : break
        print numList


        #interger was successfully parsed!
        #we're ready to exit the loop.

        
        
        
        if uNum == str('done') : break
         #Begin writing the program with the code below:
#largest = None
    
    

#smallest = None
#while True:
    #num = raw_input("Enter a number: ")
    #if num = '':
    #break
    #num.append(num)
    #if num == "done" : break
    #print num


#print "Maximum", largest

#A function to determine largest
#largest = None
#print 'Before'
#for value in [3,6,9,2,18] :
#	if largest is None :
#		largest = value
	#elif value > largest :
		#largest = value 
	#print largest, value
#print 'Afrter', largest








