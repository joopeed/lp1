# Date: Thu, 22 Mar 2012 12:15:55 +0000
# Question 57
# JOAO PEDRO FERREIRA
# 21211940
meses = ["jan","fev","mar","abr",=
"mai","jun","jul","ago","set&q=
uot;,"out","nov","dez"]
for i in range(12):
	n,m = map(float,raw_input().split())
	lucro = n-m
	if lucro >=0:
		print meses[i]," %.1f" % lucro
	else:=09
		print meses[i],"%.1f" % lucro
