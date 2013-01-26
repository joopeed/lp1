# Date: Thu, 03 May 2012 22:47:09 +0000
# Question 176
# JOAO PEDRO FERREIRA DE MELO
# 21211940
def soma_matriz_interna(m, inicio, fim):
        soma =0
        for i in range(inicio[0],fim[0]+1):
                for j in range(inicio[1], fim[1]+1):
                        soma+= m[i][j]
        return soma
