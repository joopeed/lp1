# Date: Wed, 11 Apr 2012 00:29:58 +0000
# Question 105
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

def conta_palavras(j, palavras):
        conta=0
        palavras = palavras.split(":")
        for i in palavras:
                if len(i)>=j:
                        conta+=1
        return conta

assert conta_palavras(5, "zero:um:dois:tres:quatro:cinco") ===
 2
