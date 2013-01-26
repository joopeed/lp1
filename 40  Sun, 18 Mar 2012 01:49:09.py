# Date: Sun, 18 Mar 2012 01:49:09 +0000
# Question 40
# coding: utf-aprov =[]
reprov = []
soma=0
soma2=0
for i in range(int(raw_input())):
	lido = float(raw_input())
	if lido>=7:
		aprov.append(lido)
	else:
		reprov.append(lido)
print "Reprovados:",len(reprov)
if len(reprov)>0:
	for i in reprov:
		soma = soma + i
	print "M=E9dia: %.1f"%( soma/len(reprov))
print "\nAprovados:", len(aprov)
if len(aprov)>0:
	for i in aprov:
		soma2 = soma2 + i
	print "M=E9dia: %.1f"%( soma2/len(aprov))


