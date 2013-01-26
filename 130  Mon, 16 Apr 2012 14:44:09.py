# Date: Mon, 16 Apr 2012 14:44:09 +0000
# Question 130
# JOAO PEDRO FERREIRA
# 21211940
# JORGE ABRANTES - Programacao 1 - 2012.1
def soma_mats(m1,m2):
        matriz = []
        for i in range(len(m1)):
                linha =[]
                for j in range(len(m1[i])):
                        linha.append(m2[i][j]+m1[i][j])
                matriz.append(linha)
        return matriz
