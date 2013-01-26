vezes =0
soma=0
while True:
	n = raw_input()
	if n == "fim":
		break
	soma +=len(n)
	vezes +=1
if vezes!=0:
	print soma/float(vezes)
else: 
	print "0.0"
