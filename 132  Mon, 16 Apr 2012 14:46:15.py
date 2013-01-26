# Date: Mon, 16 Apr 2012 14:46:15 +0000
# Question 132
# JOAO PEDRO FERREIRA
# 21211940
# JORGE ABRANTES - Programacao 1 - 2012.1
def diag_secundaria(m):
        lista =[]
        conta=0
        for i in range(len(m))[::-1]:
                lista.append(m[i][conta])
                conta+=1
        return lista[::-1]
