# Date: Fri, 13 Apr 2012 21:47:05 +0000
# Question 123
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940
def lanchemaispedido(pedidos):
        listaprods = []
        quants =[]
        for i in pedidos:
                ok=0
                for j in listaprods:
                        if j==i:
                                ok =1
                if ok==0:
                        listaprods.append(i)
                        quants.append(0)
        for i in range(len(listaprods)):
                for j in pedidos:
                        if listaprods[i] ==j:
                                quants[i]+=1
        ele = None
        for i in range(len(quants)):
                if quants[i] > (len(pedidos)/2):
                        ele = listaprods[i]
        return ele
