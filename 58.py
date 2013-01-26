meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]
for i in range(12):
	n,m = map(float,raw_input().split())
	lucro = n-m
        if lucro <0:
		print meses[i],"%.1f" % lucro
