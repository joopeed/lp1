# Date: Tue, 01 May 2012 16:27:16 +0000
# Question 165
# Joao Pedro Ferreira de Melo
# 21211940=20
def colunas_com_zero(m):
        colunas = {}
        for i in range(len(m)):
                for j in range(len(m[0])):
                        if m[i][j]==0:
                                colunas[j]=1
        return sorted(colunas.keys())
