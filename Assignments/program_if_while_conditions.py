#I can count to 10

#Begins the count at 0
count = 0

#As long as the condition, the value of count is less than 10 
#It will print  "Hello, I am an if statement and count is", count
if count <= 10:
    print "Hello, I am an if statement and count is", count
    
 #This loop will run as the condition set is meet
while count <= 9:
    print "Hello, I am a while and count is", count
    #This will increment the value of count 
    #And prevent an infinit loop
    #Can also be written as: count = count + 1
    count += 1

#I can square numbers

#Begins doubling numbers from 1
num = 1

#The loop will keep dubling until it stops at 10
while num < 11:  # Fill in the condition
     print num**2 # Print num squared(**5 python exponents)
     num = num + 1 # Increment num (make sure to do this!)