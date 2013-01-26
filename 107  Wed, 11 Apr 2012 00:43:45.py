# Date: Wed, 11 Apr 2012 00:43:45 +0000
# Question 107
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

def divisor(num, lista):
        result = -1
        for i in range(len(lista)):
                if lista[i]%num==0:
                        result= i
                        break
        return result

lista1 = [100,10,40,50]

lista2 = [3,15,50,23,5]


assert divisor(10, lista1) == 0

assert divisor(5, lista2) == 1
