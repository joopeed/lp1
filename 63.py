import math
n = raw_input()
m = raw_input()
conta = 0
for i in range(len(n)):
	if n[i]==m[i]:
		conta+=1
if conta > math.ceil(len(n)/2.0):
	print "sim"
else:
	print "nao"

