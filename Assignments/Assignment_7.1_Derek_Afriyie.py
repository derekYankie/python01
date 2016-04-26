"Hello Fellows!"

"Write a program that prompts for a file name, then opens that file and reads through the file, "
"and print the contents of the file in upper case. "

"The link: http://www.pythonlearn.com/code/words.txt, contains the following words:"
"WRITING PROGRAMS OR PROGRAMMING IS A VERY CREATIVE"
"AND REWARDING ACTIVITY  YOU CAN WRITE PROGRAMS FOR"
"MANY REASONS RANGING FROM MAKING YOUR LIVING TO SOLVING"
"A DIFFICULT DATA ANALYSIS PROBLEM TO HAVING FUN TO HELPING"
"SOMEONE ELSE SOLVE A PROBLEM  THIS BOOK ASSUMES THAT"
"{\EM EVERYONE} NEEDS TO KNOW HOW TO PROGRAM AND THAT ONCE"
"YOU KNOW HOW TO PROGRAM, YOU WILL FIGURE OUT WHAT YOU WANT"
"TO DO WITH YOUR NEWFOUND SKILLS"

"WE ARE SURROUNDED IN OUR DAILY LIVES WITH COMPUTERS RANGING"
"FROM LAPTOPS TO CELL PHONES  WE CAN THINK OF THESE COMPUTERS"
"AS OUR PERSONAL ASSISTANTS WHO CAN TAKE CARE OF MANY THINGS"
"ON OUR BEHALF  THE HARDWARE IN OUR CURRENT-DAY COMPUTERS"
"IS ESSENTIALLY BUILT TO CONTINUOUSLY AS US THE QUESTION"
"WHAT WOULD YOU LIKE ME TO DO NEXT"

"OUR COMPUTERS ARE FAST AND HAVE VASTS AMOUNTS OF MEMORY AND"
"COULD BE VERY HELPFUL TO US IF WE ONLY KNEW THE LANGUAGE TO"
"SPEAK TO EXPLAIN TO THE COMPUTER WHAT WE WOULD LIKE IT TO"
"DO NEXT IF WE KNEW THIS LANGUAGE WE COULD TELL THE"
"COMPUTER TO DO TASKS ON OUR BEHALF THAT WERE REPTITIVE"
"INTERESTINGLY, THE KINDS OF THINGS COMPUTERS CAN DO BEST"
"ARE OFTEN THE KINDS OF THINGS THAT WE HUMANS FIND BORING"
"AND MIND-NUMBING"


#Instructions:

"Use the file words.txt to produce the output above."""

"You can download the sample data at http://www.pythonlearn.com/code/words.txt"

"Begin to write the program with the following code below:"

# Use words.txt as the file name

#Recieve the name of user file
fname = raw_input("Enter file name: ")

#Use the open method to open the file
try:
	fhand = open(fname)
	#Prints contents of the file
	print fhand
#Custom error
except:
	print "Nope, there isn't a file with that name"

#Prints contents of selected file in uppercase letters
for line in fhand:
	#Prints the contents of the file in upper case
	#And puts the original text size on the preceeding line
	print line.upper(),line.rstrip()
	




