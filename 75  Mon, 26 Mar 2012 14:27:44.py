# Date: Mon, 26 Mar 2012 14:27:44 +0000
# Question 75
# JOAO PEDRO FERREIRA
# 21211940
vezes =0
soma=0
while True:
        n = raw_input()
        if n == "fim":
                break
        soma +=len(n)
        vezes +=1
if vezes!=0:
        print "%.1f" % ( soma/float(vezes))
else:
        print "0.0"
