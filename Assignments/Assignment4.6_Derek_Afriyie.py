#Assignment4.6

def computepay(h,r):
	grosspay = h * r
	return grosspay

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter PayRate: ")
r = float(rate)
	
print "Pay" , computepay

if h <= 40 :
    print grosspay
else:
     grosspay = r * 40 + (r * 1.5 * (h - 40))

     print grosspay