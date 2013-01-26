# Date: Mon, 26 Mar 2012 13:16:58 +0000
# Question 73
# JOAO PEDRO FERREIRA
# 21211940
n = raw_input()
soma = 0
while n!="***":
        if not(n[0] in "AEIOUaeiou"):
                soma+=1
        n = raw_input()
print "Palavras:", soma
