# Date: Mon, 09 Apr 2012 13:42:27 +0000
# Question 103
# coding: utf-# JOAO PEDRO FERREIRA DE MELO LEONCIO
# PROG1 - UFCG 2012.1
# 21211940
def acima_de(N,L):
        lista = []
        for i in range(len(L)):
                if L[i] >N:
                        lista.append(i)
        return lista
