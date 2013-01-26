# Date: Wed, 21 Mar 2012 23:58:41 +0000
# Question 59
# JOAO PEDRO FERREIRA 21211940

meses = ["jan","fev","mar","abr",=
"mai","jun","jul","ago","set&q=
uot;,"out","nov","dez"]
n = map(float,raw_input().split())
m = map(float,raw_input().split())
for i in range(12):
	if n[i]-m[i]<0:
		print meses[i], n[i]-m[i] 
