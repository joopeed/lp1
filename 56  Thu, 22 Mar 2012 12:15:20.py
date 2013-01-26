# Date: Thu, 22 Mar 2012 12:15:20 +0000
# Question 56
# JOAO PEDRO FERREIRA
# 21211940
for i in range(12):
	n,m = map(float,raw_input().split())
	lucro = n-m
	if lucro>=0:
		print " %.1f" % lucro
	else:
		print "%.1f" % lucro
