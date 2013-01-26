# Date: Fri, 13 Apr 2012 22:25:47 +0000
# Question 122
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

def quantos_comeram(n,fila):
        soma=0
        ok=True
        for i in fila:
                if i <=n and ok:
                        n-=i
                else:
                        soma+=i
                        ok=False
        soma = sum(fila)-soma
        return soma
