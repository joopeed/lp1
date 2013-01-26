# Date: Wed, 11 Apr 2012 01:07:51 +0000
# Question 110
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940
def contazeros(numero):
        conta=0
        for i in numero:
                if i=="0":
                        conta+=1
                else: break
        return conta
def fat(num):
        fat=1
        for i in range(n,0,-1):
                fat*= i
        return str(fat)

n = int(raw_input())
n = fat(n)
print contazeros(n[::-1])

