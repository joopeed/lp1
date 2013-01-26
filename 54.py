# JOAO PEDRO FERREIRA
# coding: utf-8
n =0 
x =0
soma =0
while n>=0:
	soma+=n
	n = float(raw_input("valor? "))
	x+=1
print "---"
print "Quantidade de valores:", x-1
print "Soma dos valores: %.1f" %soma 
print "Média: %.1f"%(soma/(x-1))
