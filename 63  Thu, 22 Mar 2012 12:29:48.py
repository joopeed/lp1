# Date: Thu, 22 Mar 2012 12:29:48 +0000
# Question 63
# JOAO PEDRO FERREIRA
# 21211940
import math
n = raw_input()
m = raw_input()
conta = 0
for i in range(len(n)):
	if n[i]==m[i]:
		conta+=1
if conta > len(n)/2:
	print "sim"
else:
	print "nao"

