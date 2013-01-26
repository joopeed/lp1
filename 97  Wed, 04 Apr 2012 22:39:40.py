# Date: Wed, 04 Apr 2012 22:39:40 +0000
# Question 97
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

num = int(raw_input())
lista = map(int, raw_input().split())
indice=-1
conta=0

for i in range(len(lista)):
        if lista[i]==num:
                conta+=1
                if conta>1:
                        indice=i
print indice

