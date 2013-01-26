# Date: Wed, 26 Sep 2012 22:56:58 +0000
# Question 186
#JOAO PEDRO LEONCIO -  21211940
# 2012.1 - JORGE ABRANTES
n = int(raw_input())
inicio = 0
fim = 0
maior = 0
pegando = 0
for i in range(n):
        c,f = map(int, raw_input().split())
        if i == 0:
                inicio = c
        if i == n-1:
                fim = f
        pegando+=f-c
        if f-c>maior:
                maior = f-c
print maior,"horas durou a maior pegada"
print fim-inicio-pegando,"horas sem pegar ninguem"
