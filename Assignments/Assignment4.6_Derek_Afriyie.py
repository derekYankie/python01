#Assignment4.6


hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter PayRate: ")
r = float(rate)

#compute function
def computepay(h,r):
	grosspay = h * r
	return grosspay


	
#print "Pay" , grosspay

#Regular Pay
if h <= 40 :
    print computepay(h,r)
#Overtime
else:
     grosspay = r * 40 + (r * 1.5 * (h - 40))

     print "Gross Pay:" , computepay(h,r)