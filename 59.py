meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]
n = map(float,raw_input().split())
m = map(float,raw_input().split())
for i in range(12):
	if n[i]-m[i]<0:
		print meses[i], n[i]-m[i] 
