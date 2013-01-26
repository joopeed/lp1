# Date: Thu, 12 Apr 2012 11:56:57 +0000
# Question 111
# PROG 1 - UFCG 2012.1
# JOAO PEDRO FERREIRA
# 21211940
def divisores_proprios(num):
        lista =[]
        for i in range(1,num):
                if num%i==0:
                        lista.append(i)
        return lista
