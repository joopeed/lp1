# Date: Fri, 27 Apr 2012 22:33:07 +0000
# Question 164
# JOAO PEDRO FERREIRA DE MELO
# 21211940
def constroi_matriz(m,n,valores):
        matriz = []
        for i in range(m):
                linha =[]
                for j in range(n*i,n*i+n):
                        print j, n*i, n*i+n, m
                        linha.append(valores[j])
                matriz.append(linha)
        return matriz
