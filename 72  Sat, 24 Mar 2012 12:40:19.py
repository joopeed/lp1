# Date: Sat, 24 Mar 2012 12:40:19 +0000
# Question 72
# JOAO PEDRO FERREIRA
# 21211940
n = int(raw_input())
lista = []
maior = 0
indice = 0
for i in range(n):
        num1, num2 = map(int, raw_input().split())
        lista.append(num2 - num1)
for i in range(len(lista)):
        if lista[i] >= maior:
                maior = lista[i]
                indice = i
print "carregamento", indice+1
