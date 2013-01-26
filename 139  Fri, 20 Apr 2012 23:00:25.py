# Date: Fri, 20 Apr 2012 23:00:25 +0000
# Question 139
# JOAO PEDRO LEONCIO - 21211940
## PROGRAMACAO I - UFCG 2012.1 - JORGE ABRANTES

n,m = map(int, raw_input().split())
matriz = []
for i in range(n):
        linha = map(int, raw_input().split())
        matriz.append(linha)
k = int(raw_input())
for i in range(len(matriz)):
        for j in range(len(matriz[0])):
                matriz[i][j]*=k
print matriz
