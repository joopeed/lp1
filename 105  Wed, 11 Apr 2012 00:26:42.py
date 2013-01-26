# Date: Wed, 11 Apr 2012 00:26:42 +0000
# Question 105
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

def maior_palavra(lista):
        maior = lista[0]
        for i in lista:
                if len(i) >= len(maior):
                        maior = i
        return maior;
lista1 = ["palavra", "exemplo", "computador&quot=
;, "mouse"]

lista2 = ["outra", "palavra", "como", &quot=
;exemplo", "mouse"]

assert maior_palavra(lista1) == "computador"

assert maior_palavra(lista2) in ["palavra", "exemplo"]<=
/div>
