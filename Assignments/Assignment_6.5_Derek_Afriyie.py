#Assignment6.5

"Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below."
"Convert the extracted value to a floating point number and print it out."

#Please use the line below:

text = "X-DSPAM-Confidence:    0.8475"

#Finds the decimal point and prints its location
locationDec = text.find('.')
print "Decimal index:", locationDec

#Splices the given text to output everything from the decimal & everything after
print "Decmial number found in text:",text[24:28]
capture = float(text[24:28])
#Start splice at the decimal
#and show/grab everything after it
capture = float(text[locationDec:])

print "Conversion of string-decimal to real decimal:",capture



