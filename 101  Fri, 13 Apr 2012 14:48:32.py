# Date: Fri, 13 Apr 2012 14:48:32 +0000
# Question 101
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

n = int(raw_input())
soma =0
for i in range(n):
        chegada,saida = map(int, raw_input().split())
        if i==0:
                inicio = chegada
        elif i==n-1:
                fim = saida
        soma+= saida-chegada
print (fim-inicio)-soma
