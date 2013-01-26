# Date: Wed, 21 Mar 2012 22:48:51 +0000
# Question 54
# coding: utf-n=0
x=0
soma =0
while n>=0:
        soma+=n
        n = float(raw_input("valor? "))
        x+=1
print "---"
print "Quantidade de valores:", x-1
print "Soma dos valores: %.1f" %soma
print "M=E9dia: %.1f"%(soma/(x-1))
