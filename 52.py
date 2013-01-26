n = int(raw_input("n? "))
b =1

for i in range(1,3*(n/2),3):
	b = b * i
	print i
	print b
if n%2!=0:
	print i+3
