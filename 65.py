n = raw_input()
temvogal =0
for i in n:
	if i in "AEIOUaeiou":
		print i
		temvogal =1
		break
if temvogal==0:
	print "-"

