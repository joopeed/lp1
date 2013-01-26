# Date: Tue, 27 Mar 2012 22:41:24 +0000
# Question 79
# JOAO PEDRO FERREIRA
# 21211940
soma =0
n = int(raw_input())
conta = 0
while n !=9999:
        soma+= n
        conta+=1
        n = int(raw_input())
print "%.1f" %(soma/float(conta))
