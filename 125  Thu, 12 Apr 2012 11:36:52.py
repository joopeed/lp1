# Date: Thu, 12 Apr 2012 11:36:52 +0000
# Question 125
# PROG 1 - UFCG 2012.1
# JOAO PEDRO FERREIRA
# 21211940
def remove_menores(N, lista):
        conta = 0
        lista_remover =[]
        for i in lista:
                if i < N:
                        lista_remover.append(i)
                        conta+=1
        for i in lista_remover:
                lista.remove(i)
        return conta

