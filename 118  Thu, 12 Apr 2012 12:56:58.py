# Date: Thu, 12 Apr 2012 12:56:58 +0000
# Question 118
# coding: utf-# PROG 1 - UFCG 2012.1
# JOAO PEDRO FERREIRA
# 21211940
def filtra_lista(num, lista):
        retorno =[]
        for i in range(len(lista)):
                if i%num==0:
                        retorno.append(lista[i])
        return retorno
lista1 = [0,1,2,3,4,5,6]

lista2 = [2,3,5,7,11,13,17]

assert filtra_lista(2, lista1) == [0,2,4,6]

assert filtra_lista(3, lista1) == [0,3,6]

assert filtra_lista(4, lista2) == [2,11]

assert filtra_lista(40, lista2) == [2]

