#Assignment 8.4

"Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. "
"The program should build a list of words. "
"For each word on each line check to see if the word is already in the list and if not append it to the list. "
"When the program completes, sort and print the resulting words in alphabetical order."

"You can download the sample data at http://www.pythonlearn.com/code/romeo.txt"


#Opens file romeo.txt
fh = open('romeo.txt')
#Creates an empty list
lst = list()
for line in fh:
	#strips line of whitespaces and splits the words
	#stores words in wordBank (list of words)
	#to create random list of words
	wordBank = line.strip().split()
	print wordBank
#condition for the words inthe wordBank
for words in wordBank:
	#Condition: check to see if the word is already in the list 
	#and if not append it to the list.
	#words.lower()
	if words not in lst:
		lst.append(words.lower())
#use the sorted method 
#to list the words in alphabetical order
print max(lst)
print '\n',sorted(lst)

