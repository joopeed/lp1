# Date: Thu, 08 Mar 2012 12:16:43 +0000
# Question 16
import mata= float(raw_input())
b = float(raw_input())
c= float(raw_input())
delta = b**2 -(4*a*c)
if delta >0:
	x1 = (-b +math.sqrt(delta))/(2*a)
	x2 = (-b -math.sqrt(delta))/(2*a)
	print "x1 = %.2f" %x1
	print "x2 = %.2f" %x2
elif delta ==0:
	x = (-b)/(2*a)
	print "x = %.2f" %x
else:
	print "sem raizes reais"
