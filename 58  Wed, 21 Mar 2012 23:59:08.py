# Date: Wed, 21 Mar 2012 23:59:08 +0000
# Question 58
# JOAO PEDRO FERREIRA 21211940

meses = ["jan","fev","mar","abr",=
"mai","jun","jul","ago","set&q=
uot;,"out","nov","dez"]
for i in range(12):
	n,m = map(float,raw_input().split())
	lucro = n-m
        if lucro <0:
		print meses[i],"%.1f" % lucro
