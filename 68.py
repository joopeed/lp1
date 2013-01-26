tudo = raw_input().split()
NC = map(int,list(tudo[0]))
DV = int(tudo[1])
soma=0
for i in range(len(NC)):
	soma+=NC[i]
dvrecebido = soma%11
if DV==dvrecebido:
	print "ok"
else:
	print "erro"

