# Date: Fri, 30 Mar 2012 15:44:55 +0000
# Question 89
# JOAO PEDRO FERREIRA
# 21211940
menor = 1000000000000000000000000000000000
maior = 0
while True:
        num = int(raw_input())
        if num ==-1: break
        if num > maior:
                maior =num
        if num < menor:
                menor =num
print "maior:" ,maior
print "menor:", menor
